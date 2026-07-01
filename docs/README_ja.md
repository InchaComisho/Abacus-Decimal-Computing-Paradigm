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

---

## 著者

マスター / inchacomusho / InchaComisho

日本の独立構想者、観測者、提案者、AI調律者、人工叡智の定義者。  
自然補完科学の学問体系の構築・提唱者。  
クーリングクレジット・フレームワークの定義者、自然冷却価値評価プロトコルの創設者・原著作者。  
温暖化因果構造と完全解決策の定義者・体系化者。

マスターは、地球温暖化を単なるCO₂濃度の問題ではなく、森林喪失、土壌劣化、水循環断絶、水の相転移の弱体化、大気循環・海洋循環・食の循環／有機物循環の弱体化、蒸散・雲形成・降雨循環の弱体化、自然冷却フィードバックの停止として統合的に捉え、その解決策を排出削減、炭素固定源回復、物理的冷却、自然冷却機能の再起動、MRV、クーリングクレジット、文明OSへ接続する公開フレームワークとして提示している。

自然法則思想、地球循環再生、AIとの共創を中心に、NOTE・GitHub・各種公開媒体を通じて公開活動を行う。

## ライセンス

CC BY 4.0

本記事は、Creative Commons Attribution 4.0 International License（CC BY 4.0）で公開する。  
著者表示を行う限り、共有、転載、翻訳、改変、再利用を許可する。