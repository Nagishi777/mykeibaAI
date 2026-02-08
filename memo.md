# memo
# Recent Day
すぐやらないと支障がでる

## Overall
- 特徴量ルールを決める
  - 値が高い方が良い
  - 一桁整数に丸める
- スクレイピングデータは一年ずつ作っていき、使うときにconcatで良いのでは？

## scrape_race_result.ipynb
  - "https://db.netkeiba.com/race/2023H1121008/"などレースIDに文字が入っている海外レースを正しくスクレイピングできるように
  →海外レースは対象外に

## scrape_horse_result.ipynb

## predict_rank.ipynb
- 閾値判定は0.5だが本当にこれでよいの？
  - 確率の分布を確認してみて適切な分布を決める（総当たりで的中率が高くなる値を探す？）

# Some day
いつかやろうは馬鹿野郎

## コード修正
- G1やG2などのレース分類
- 一件だけtrainer_idでTypeNoneが出現(race_id=202301010408)
- Floatで34.400002といった誤差が発生

## 特徴量
- 血統、騎手データ
- 1位に近い順位の処理
- 物理量ベースの指数化
- 脚質
- GroupKFold
- 学習時のオッズを確定前のものにする
- 人気順ごとの基準オッズ：https://keibaanalysis.com/archives/383
- 外枠内枠の有利不利: https://note.com/kirari394/n/nd7aca876715a

## 学習
- ランキング学習を試す
  - https://qiita.com/tech_tech_pingu/items/2e74165be8564aa18e77

## 回収率計算
- 期待値計算
  - 投資金額の最適化(ケリー基準の導入：https://qiita.com/tikeda123/items/3f4dd42c8f57333deeaf )
