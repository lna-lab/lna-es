# CLI (reference)

- `lna preset list`
- `lna ops validate operators.xml`
- `lna ops compile operators.xml -o dialect.json`
- `lna generate -g graph.json -c control.json --dialect dialect.json -o out/`
- `lna verify   -i out/draft.txt -c control.json -o out/verify.json`
- `lna rewrite  -i out/draft.txt -v out/verify.json -o out/fixed.txt`
- `lna audit    -m out/metrics.json -v out/verify.json -o out/audit_card.md`
- `lna abtest -A control_A.json -B control_B.json -g graph.json -o out/ab/`
- `lna doctor`
