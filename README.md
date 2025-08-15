# LNA-ES v0.1 — グラフ × 演算子で LLM を“あなたの方言”に

**LNA-ES は、テキストを Neo4j グラフにし、演算子で整えて LLM に渡すための最小セット。**
そして一番大事なポイントは…… **「方言（Dialect）」で“あなた好み”に育てられる** こと。

- 状態: Draft v0.1（試用歓迎）
- 目的: ベンダー非依存の 小さなコア + 好みを載せる 方言

## 2分クイックスタート

```bash
# 1) 開発ツール（整形・Lint）を入れる
make setup

# 2) 付属の例を眺める（まずは読むだけでOK）
ls examples/
#  - operators.sample.xml  ← 方言のタネ
#  - recipe.lna.yaml       ← 小さなレシピ
#  - graph.sample.json     ← グラフの例

# 3) （CLIが入っていれば）方言をコンパイルして試す
#    ※ まだ入っていなければ、このステップはスキップでOK
python3 -m lna_es.cli ops validate examples/operators.sample.xml || true
python3 -m lna_es.cli ops compile  examples/operators.sample.xml -o runs/dialect.json || true
```

> うまく動いたら `runs/dialect.json` ができます。
> まだ CLI 実装が整っていない場合でも、方言の発想は `examples/operators.sample.xml` を読むだけで掴めます。

## 一番大事：方言（Dialect）で好みに育てる

LNA-ES では、コアは小さく安定、好みや文体は 方言 に寄せるという考え方です。

- コア（変えない部分）

  - 小さな演算子セット（EXTRACT / RESOLVE / WEIGHT / LOCK / STYLE / VERIFY / REWRITE）
  - 優先順位（LOCK → VERIFY → REWRITE → STYLE）

- 方言（変えて楽しむ部分）

  - 文体・語彙・編集方針・「魂の濃度」などを、XML や YAML で宣言的に記述
  - 例）`examples/operators.sample.xml` をコピーして、自分の方言 `my_dialect.xml` を作る

方言の始め方（3ステップ）:

1. サンプルをコピー
   ```bash
   cp examples/operators.sample.xml my_dialect.xml
   ```
1. ルールを少し変える（語彙、重み、禁止・推奨など）
1. （CLIがあれば）構文チェックとコンパイル
   ```bash
   python3 -m lna_es.cli ops validate my_dialect.xml
   python3 -m lna_es.cli ops compile  my_dialect.xml -o runs/dialect.json
   ```

> ポイント: 方言＝“あなたの編集方針”。
> たとえば「三島度を上げる」「固有名は絶対保持」「台詞は短く」などを、方言として保存・共有できます。

______________________________________________________________________

## Python 3.12 venv（任意）

This repo is configured to use Python 3.12 via a local virtual environment `./.venv`.

- Create venv and install tools: `make setup`
- Run commands inside venv automatically via Make targets (they use `./.venv/bin/python`)
- If `python3.12` is not found on your system, install it (e.g., via `pyenv` or Homebrew) or override `PYTHON` when creating the venv:

```bash
make PYTHON=$(which python3.12) setup
# Or try: make install-python  # attempts pyenv/brew installation helpers
```

Run tests: `make test`

## CI (GitHub Actions)

This repo includes a basic CI workflow at `.github/workflows/ci.yml` that runs on every push and pull request:

- Set up Python 3.12
- Install dev tools (`pre-commit`, `black`, `ruff`, `mdformat`, `pytest`, `jsonschema`, `xmlschema`)
- Run `pre-commit` on all files (format + lint)
- Run `pytest`
- Run a quick CLI sanity check (`python -m lna_es.cli --help`)

How to use:

- Push your branch to GitHub; the workflow auto-runs
- Check the “Actions” tab for status and logs
- To speed up linting, the workflow caches pre-commit hooks

## 方言を自作したい人向けの最短ルート

1. `examples/operators.sample.xml` をコピーして拡張する
1. `lna ops validate your_operators.xml` で検証
1. `lna ops compile your_operators.xml -o your_dialect.json` でコンパイル
1. `lna generate ... --dialect your_dialect.json` で利用（adapter側でのマッピング想定）

## Repo layout

```
/spec
  LNA-ES-v0.1.md
  operator.schema.json
  operators.xsd
  RFC-Process.md
/tools
  cli-commands.md
/examples
  control.json
  control_A.json
  control_B.json
  recipe.lna.yaml
  graph.sample.json
  operators.sample.xml
  operator.sample.json
/CONTRIBUTING.md
/README.md (this file)
```

## License (suggested)

- Code: Apache-2.0
- Docs/Spec: CC-BY-4.0
