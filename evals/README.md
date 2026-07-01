# Evals - Trigger Accuracy

Bộ test kiểm tra skill `fiinquant` route đúng câu hỏi sang file
`references/<...>.md` tương ứng, hoặc trả về `ASK` khi câu hỏi quá mơ hồ.

## Files

- `trigger_accuracy.jsonl`: 46 case, phủ đủ 10/10 nhóm (0-9).
- `run_eval.py`: validate toàn vẹn bộ test và chấm điểm predictions nếu có.

## Schema 1 Case

```jsonc
{
  "id": "...",
  "query": "...",
  "expected_group": "7.3",
  "expected_reference": "7.3-...md",
  "accept": ["...md", "ASK"],
  "type": "route|clarify|abbrev|multi|trap",
  "noise": true,
  "was_f1_zero": false
}
```

Dự đoán đúng khi `pred == expected_reference` hoặc `pred` nằm trong `accept`.

## Chạy Validate

```bash
python3 evals/run_eval.py
```

## Chấm Điểm Predictions

Nếu đã có file predictions dạng `{"<id>": "<pred.md|ASK>"}`, chạy:

```bash
python3 evals/run_eval.py --pred evals/predictions.json
```

## Kiểm Tra Chất Lượng

- `validate` phải pass đủ 10/10 nhóm.
- Mọi `expected_reference` và `accept` phải trỏ tới file hợp lệ hoặc `ASK`.
- Case ID không được trùng.
