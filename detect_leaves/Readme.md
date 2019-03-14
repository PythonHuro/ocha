detect_leaves
====

### ※19/3/15現在、メインのソースの名前が、detect_leaf_areaになっていますので、リポジトリ名と違います。

### 🐍やったこと
- お茶畑の画像から、色での絞り込みによりおちゃっぱの部分のみを抜き出すことに成功
- とりあえず結果画像見てください  
![result](https://github.com/PythonHuro/ocha/blob/master/detect_leaves/Output.png)
- こちらがソース画像です
![result](https://github.com/PythonHuro/ocha/blob/master/detect_leaves/resource/chabatake/P1100295.JPG)

### 🐍これからできそうなこと
- 二値画像に拡大・縮小処理を行うことで、葉にできた小さい影による検出漏れを防ぐ→虫食いみたいになってるところの改善
- 輪郭検出をして、葉一枚を抜き出すことができるか検証
- 葉を数枚検出してみて、元画像と比較してみて、この手法の有用性を確認
- 閾値を自動決定してほしい
