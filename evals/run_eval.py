#!/usr/bin/env python3
"""Trigger-accuracy eval cho skill `fiinquant`.

Kiểm tra: với mỗi câu hỏi (query), hệ thống có route ĐÚNG sang file
`references/<...>.md` mong đợi hay không.

Schema mỗi case (trigger_accuracy.jsonl):
  id                 : định danh
  query              : câu hỏi của người dùng
  expected_group     : nhóm mong đợi ("7.3", "9", hoặc "ASK")
  expected_reference : file reference CHÍNH cần mở, hoặc "ASK" nếu phải hỏi lại
  accept (optional)  : list reference KHÁC cũng được chấp nhận (case đa nhóm,
                       hoặc "ASK" nếu vừa được route mặc định vừa được hỏi lại)
  type (optional)    : route | clarify | abbrev | multi | trap
  noise (optional)   : true nếu là case nhiễu (không nằm trong failure-mode gốc)
  was_f1_zero        : true nếu thuộc nhóm từng F1=0 trong trigger test gốc

Một dự đoán `pred` là ĐÚNG khi: pred == expected_reference HOẶC pred ∈ accept.

Hai chế độ:
  1) validate (mặc định): kiểm tra toàn vẹn bộ test.
        python3 evals/run_eval.py
  2) score: chấm điểm predictions.json {"<id>": "<pred.md|ASK>"}.
        python3 evals/run_eval.py --pred evals/predictions.json
     Báo cáo accuracy tổng + theo type + nhóm-F1=0 + subset noise + case sai.
"""
import argparse, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "evals" / "trigger_accuracy.jsonl"
REFDIR = ROOT / "plugins" / "fiinquant" / "skills" / "fiinquant" / "references"


def load_cases():
    return [json.loads(l) for l in DATA.read_text().splitlines() if l.strip()]


def accepted(case):
    """Tập đáp án được chấp nhận cho 1 case."""
    return {case["expected_reference"], *case.get("accept", [])}


def is_valid_target(t):
    return t == "ASK" or (REFDIR / t).exists()


def validate(cases):
    ok = True
    # 1) mọi target (expected + accept) hợp lệ
    bad = []
    for c in cases:
        for t in accepted(c):
            if not is_valid_target(t):
                bad.append((c["id"], t))
    if bad:
        ok = False
        print(f"✗ {len(bad)} target không tồn tại: {bad}")
    # 2) phủ đủ 10/10 nhóm (bỏ qua case clarify thuần 'ASK')
    groups = {c["expected_group"].split(".")[0] for c in cases if c["expected_group"] != "ASK"}
    miss = sorted({str(i) for i in range(10)} - groups, key=int)
    if miss:
        ok = False
        print(f"✗ Thiếu nhóm: {miss}")
    else:
        print("✓ Phủ đủ 10/10 nhóm (0..9)")
    # 3) id duy nhất
    ids = [c["id"] for c in cases]
    if len(ids) != len(set(ids)):
        ok = False
        dup = sorted({i for i in ids if ids.count(i) > 1})
        print(f"✗ id trùng: {dup}")
    n_noise = sum(c.get("noise", False) for c in cases)
    n_hard = sum(c.get("was_f1_zero", False) for c in cases)
    n_ask = sum(c["expected_reference"] == "ASK" for c in cases)
    print(f"✓ {len(cases)} case | {n_hard} nhóm-F1=0 | {n_noise} noise | {n_ask} clarify(ASK)")
    print("OK" if ok else "FAILED")
    return ok


def _rate(c, t):
    return f"{c}/{t} = {c/t:.1%}" if t else "n/a"


def score(cases, pred_path):
    pred = json.loads(pathlib.Path(pred_path).read_text())
    missing = [c["id"] for c in cases if c["id"] not in pred]
    if missing:
        print(f"⚠ Thiếu prediction cho {len(missing)} case: {missing[:8]}{'...' if len(missing)>8 else ''}")

    by_type, hard = {}, [0, 0]
    noise = [0, 0]
    total = correct = 0
    wrong = []
    for c in cases:
        p = pred.get(c["id"], "<missing>")
        hit = p in accepted(c)
        total += 1
        correct += hit
        t = c.get("type", "route")
        bt = by_type.setdefault(t, [0, 0])
        bt[0] += hit; bt[1] += 1
        if c.get("was_f1_zero"):
            hard[0] += hit; hard[1] += 1
        if c.get("noise"):
            noise[0] += hit; noise[1] += 1
        if not hit:
            wrong.append((c["id"], sorted(accepted(c)), p))

    print(f"Accuracy tổng:      {_rate(correct, total)}")
    print(f"  nhóm từng-F1=0:   {_rate(*hard)}")
    print(f"  subset noise:     {_rate(*noise)}")
    print("  theo type:")
    for t in sorted(by_type):
        print(f"    - {t:8s} {_rate(*by_type[t])}")
    if wrong:
        print("\nCase route sai:")
        for cid, exp, got in wrong:
            print(f"  - {cid}: expected ∈ {exp}, got {got!r}")
    return not wrong


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--pred", help="JSON {id: predicted_reference.md|ASK} để chấm điểm")
    args = ap.parse_args()
    cases = load_cases()
    ok = score(cases, args.pred) if args.pred else validate(cases)
    sys.exit(0 if ok else 1)
