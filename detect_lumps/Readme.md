detect_lumps
====

detect_lumps.htmlで、とりあえずもこもこした部分を取り出そうとしていることがわかるはず。  
でもそこから、

- どうやってカタマリを認識するか
- どうやって分割するか  

で悩んだ。  
最終的に、Watershedアルゴリズムを使用してみたが、徒労に終わった。  
現段階でやるものではなかった。watershed.htmlに記載。　　
  
## 🎉ぼかす関数について🎉
- Blurする関数はいくつかあって、それぞれ特徴が違うため、最適なものを選ぶ必要がある。
- 今回のソースは[ここ](https://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html)

### 🐍Averaging(平均化・平滑化)
- 対象ピクセルを含める周囲9ピクセルの画素値の平均を取得し、その値を対象ピクセルの画素値とする。これを全画素に対し行う。
- 移動平均フィルタと呼ばれるもの。
- ノイズ除去になる。
- 局所的な大きなノイズがある画像(ゴマ塩ノイズ)への対応には向いていない。

### 🐍Gaussian Blurring(ガウシアンフィルタ)
- ガウス分布の関数を用いてレートを計算して、重みづけをした平均化を行う。
- 対象ピクセルに近いピクセルほど、画素値に重みづけをする。
- 移動平均フィルタよりも平滑化の出来はよいはず。

### 🐍Median Blurring
- 対象ピクセルを含める周囲9ピクセルの画素値の中央値を取得し、その値を対象ピクセルの画素値とする。これを全画素に対し行う。中央値である。
- 局所的で大きな外れ値に影響されることがないので、ゴマ塩ノイズのようなものに堅牢。

### 🐍Bilateral Filtering
- なんとエッジを残したまま平滑化することができる。
