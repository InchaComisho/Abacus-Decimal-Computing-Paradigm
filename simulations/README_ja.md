# シミュレーション

このディレクトリには、**Abacus Decimal Computing Paradigm** の参照シミュレーションを置く。

現在の実装は、意図的にシンプルで外部依存のないPythonコードとしている。  
目的は、FPGA、LED、光学、量子互換実験へ進む前に、最小技術層を検証し、さらにエコシステム規模の採用シナリオを探索することである。

---

## ファイル

- `abacus_decimal.py`  
  5ビットそろばん型10進セルの参照実装。

- `test_abacus_decimal.py`  
  そろばん型10進セル参照実装の基本ユニットテスト。

- `civilization_adoption_sim.py`  
  分断型コンピュータ開発と、共通そろばん型10進互換レイヤー採用型開発を比較するシナリオ・シミュレーション。

---

## セル規約

参照シミュレーションでは、以下の論理順序を使う。

```text
[H, L1, L2, L3, L4]
```

ここで、

- `H` は5を表す。
- `L1`, `L2`, `L3`, `L4` はそれぞれ1を表す。

正規の下4ビットパターンは以下である。

```text
0 -> 0000
1 -> 1000
2 -> 1100
3 -> 1110
4 -> 1111
```

物理的なLED配置は反転してもよい。重要なのは論理モデルである。

---

## そろばん型10進セルの使い方

リポジトリのルートから実行する。

```bash
python simulations/abacus_decimal.py table
```

正規パターン表を表示する。

```bash
python simulations/abacus_decimal.py encode 7
```

1桁をエンコードする。

```bash
python simulations/abacus_decimal.py decode 1 1 1 0 0
```

5ビットセルをデコードする。

```bash
python simulations/abacus_decimal.py add 1234 5678
```

桁ごとの10進加算を行う。

```bash
python simulations/abacus_decimal.py sub 9000 1234
```

桁ごとの10進減算を行う。

```bash
python simulations/abacus_decimal.py states
```

32通りの5ビット状態をすべて列挙し、正規状態か非正規状態かを分類する。

```bash
python simulations/abacus_decimal.py error --trials 10000 --flips 1
```

ランダムなビット反転によるエラー検出シミュレーションを行う。

```bash
python -m unittest simulations/test_abacus_decimal.py
```

ユニットテストを実行する。

---

## 文明採用シナリオの使い方

```bash
python simulations/civilization_adoption_sim.py
```

2026年から2060年までの標準シナリオ比較を実行する。

```bash
python simulations/civilization_adoption_sim.py --start-year 2026 --end-year 2070
```

より長いシナリオを実行する。

```bash
python simulations/civilization_adoption_sim.py --csv outputs/civilization_adoption.csv
```

年ごとの成熟度スコアをCSVへ出力する。

このシミュレーションは以下を比較する。

- `fragmented`: 各企業・研究機関が互換性のない電子・光ハイブリッド、または光コンピューティングアーキテクチャを開発する場合。
- `shared_layer`: 共通の5ビットそろばん型10進互換レイヤーを早期採用し、ソフトウェア再利用、標準化、ハードウェア移行効率を高める場合。

これは未来予測ではなく、シナリオ比較モデルである。

---

## このシミュレーションで検証すること

そろばん型10進セル参照実装では、以下を検証する。

- 10進数字のエンコード
- 10進数字のデコード
- 正規パターンの検査
- 非正規状態の検出
- 1桁加算
- 1桁減算
- 多桁加算
- 多桁減算
- ランダムビット反転の検出
- 正規状態から別の正規状態へ化けるサイレント変化率

文明採用シミュレーションでは、以下を探索する。

- ソフトウェアエコシステム形成
- OS統合速度
- 光CPU / フォトニックプロセッサ準備度
- パーソナルコンピュータ採用準備度
- 分断型開発と共通互換レイヤー採用型開発の違い
- シナリオ間の閾値到達年の差

---

## 重要な制限

正規状態チェックだけでは、すべてのエラーを検出できるわけではない。

ビット反転によって、有効な数字が別の有効な数字へ変化する場合がある。  
これをサイレント有効変化と呼ぶ。

安全性が重要な用途では、以下の追加機構を検討する必要がある。

- パリティ
- チェックサム
- 冗長セル
- 時系列一貫性
- 反復サンプリング
- 電子・光の相互検証

文明採用シミュレーションにも制限がある。単純化された変数を用いるため、特定年を予測するものとして読んではならない。

---

## 次のシミュレーション候補

今後追加するとよいもの：

- エラーシミュレーションのCSV出力
- 検出率グラフ
- BCD比較ベンチマーク
- LEDパターンPNG生成
- カメラ認識モックアップ
- FPGA / HDL相当テスト
- 文明採用パラメータの感度分析
- オープン標準、企業独自標準、国家主導標準の代替シナリオ
