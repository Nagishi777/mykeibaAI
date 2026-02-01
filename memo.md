# memo
# Recent Day
すぐやらないと支障がでる

## Overall
- ~~特徴量とエンコーディングについては○○ファイルで保存&管理~~
  - ~~徴量はjsonから読みだしてそのままfeatureに代入できるように~~
- ~~クラスを使った関数整理~~
- 特徴量ルールを決める
  - 値が高い方が良い
  - 一桁整数に丸める
- スクレイピングデータは一年ずつ作っていき、使うときにconcatで良いのでは？

## scrape_race_result.ipynb
  - "https://db.netkeiba.com/race/2023H1121008/"などレースIDに文字が入っている海外レースを正しくスクレイピングできるように
  →海外レースは対象外に

## scrape_horse_result.ipynb
- テーブルの"race_id","horse_id"をstringにしておく
  - odds, popularity, weightがstring→to_numericで数字に
  - idはstring, その他数字
  - df_race["race_id"] = df_race["race_id"].astype(str).str.strip()
- 順位(rank)をラベル化したものや、1-3位を1にする列を作る
- ~~マージする際にNum_of_horsesの列も足して…~~

- 斤量は"weight"ではなく"weight_carried", 馬体重は"weight_horse"にする、差分はweight_diff

- encoding_course_condition()
  - "鞘"を追加、"鞘重"は逆にない？
- parse_margin()
  - marginの計算方法が色々違う、コメントアウトしているところを解除
- コーナー通過順位
  - 処理の関数を追加
  - 分割した際、レースごとに分割数（すなわち追加される列が変化する）
  - テーブルのマージの際に困る、最大4? 同じレース内で評価する必要有

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
