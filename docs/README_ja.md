---

# ナビゲーション

- [リポジトリトップ](../README_ja.md)
- [英語版 README](../README.md)
- [英語版ドキュメント索引](./README.md)
- [シミュレーション](../simulations/README_ja.md)

---

# ドキュメント索引

このディレクトリには、**Abacus Decimal Computing Paradigm** を研究・実装向けリポジトリとして強化するための技術文書を置く。

---

## 主要ドキュメント

- [仕様書](./SPEC_ja.md)  
  5ビットそろばん型10進セル、正規パターン、エンコード、デコード、演算、正規化、光学写像を定義する。

- [BCDとの比較](./COMPARISON_WITH_BCD_ja.md)  
  そろばん型10進セルとBCDの違いを整理する。重要な違いは、BCDが10進符号であるのに対し、そろばん型10進セルは10進・空間コンピューティング構造である点である。

- [検証計画](./VALIDATION_PLAN_ja.md)  
  ソフトウェアシミュレーション、FPGA、LED表示、画像認識、光セル、量子互換フォトニック写像までの段階的検証計画を定義する。

- [アーキテクチャ図解](./ARCHITECTURE_DIAGRAMS_ja.md)  
  セル構造、エンコード・デコード、電子から光への経路、多層検証、関連アーキテクチャとの関係をMermaid図で示す。

---

## 拡張ドキュメント

- [そろばん型10進互換レイヤー](./COMPATIBILITY_LAYER_ja.md)  
  5ビットそろばん型10進セルを、電子ビット、LEDセル、光セル、多値フォトニック状態、将来の量子互換光システムをつなぐハードウェア非依存の互換レイヤーとして定義する。

- [認知的そろばん拡張](./COGNITIVE_ABACUS_EXTENSION_ja.md)  
  そろばん概念を、計算とハードウェア設計だけでなく、人間の認知、教育、空間パターン認識、AI分類、複雑な計算システムの人間可読な解釈へ拡張する。

- [文明採用シミュレーション](./CIVILIZATION_ADOPTION_SIMULATION_ja.md)  
  分断型コンピュータ開発と、文明規模で共通そろばん型10進互換レイヤーを採用した場合を比較し、ソフトウェア連続性、OS統合、光CPU準備度、パーソナルコンピュータ採用速度を評価するシナリオモデル。

---

## English Documents

- [Specification](./SPEC.md)
- [Comparison with BCD](./COMPARISON_WITH_BCD.md)
- [Validation Plan](./VALIDATION_PLAN.md)
- [Architecture Diagrams](./ARCHITECTURE_DIAGRAMS.md)
- [Abacus Decimal Compatibility Layer](./COMPATIBILITY_LAYER.md)
- [Cognitive Abacus Extension](./COGNITIVE_ABACUS_EXTENSION.md)
- [Civilization Adoption Simulation](./CIVILIZATION_ADOPTION_SIMULATION.md)

---

## 推奨読書順

1. `SPEC_ja.md`  
2. `COMPARISON_WITH_BCD_ja.md`  
3. `VALIDATION_PLAN_ja.md`  
4. `COMPATIBILITY_LAYER_ja.md`  
5. `COGNITIVE_ABACUS_EXTENSION_ja.md`  
6. `CIVILIZATION_ADOPTION_SIMULATION_ja.md`  
7. `ARCHITECTURE_DIAGRAMS_ja.md`  
8. `../simulations/README_ja.md`  
9. `../simulations/abacus_decimal.py`  
10. `../simulations/civilization_adoption_sim.py`

---

## プロジェクト上の位置づけ

Abacus Decimal Computing Paradigm は、以下の階層として理解できる。

```text
電子側の10進・空間基盤
↓
LED可視コンピューティング
↓
電子・光ハイブリッドコンピューティング
↓
多値フォトニックコンピューティング
↓
量子互換フォトニックアーキテクチャ
```

これは完成済みの量子コンピュータとして提示するものではない。  
電子・光・将来の量子互換コンピューティングを、共通の10進・空間情報構造によって接続するための段階的アーキテクチャである。

互換レイヤー文書と認知拡張文書は、以下の2つの解釈を追加する。

```text
ハードウェア互換:
電子 → LED → 光 → フォトニック → 量子互換

認知互換:
数 → そろばんパターン → 空間認識 → AI/フォトニック分類
```

文明採用シミュレーションは、さらにエコシステム規模の問いを追加する。

```text
早期に共通互換レイヤーが存在した場合、
文明は分断を減らし、OS・ソフトウェア・光CPU・
パーソナルコンピュータ採用を加速できるか。
```
