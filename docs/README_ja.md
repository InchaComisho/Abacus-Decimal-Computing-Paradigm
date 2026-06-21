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

## English Documents

- [Specification](./SPEC.md)
- [Comparison with BCD](./COMPARISON_WITH_BCD.md)
- [Validation Plan](./VALIDATION_PLAN.md)
- [Architecture Diagrams](./ARCHITECTURE_DIAGRAMS.md)

---

## 推奨読書順

1. `SPEC_ja.md`  
2. `COMPARISON_WITH_BCD_ja.md`  
3. `VALIDATION_PLAN_ja.md`  
4. `ARCHITECTURE_DIAGRAMS_ja.md`  
5. `../simulations/README_ja.md`  
6. `../simulations/abacus_decimal.py`

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
