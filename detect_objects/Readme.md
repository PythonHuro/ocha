detect_objects
====

GoogleのVisionAPI使って、物体を認識してそれを矩形で囲って物体名も表示するっていうの書きました。  
ちょっとVisionAPI使うまでが面倒だけど、まぁ今後使うことはなさそうでしょう。  
  
## Demo
りんごの物体名が、なんかいろいろで重なってしまっていますね。  
こういう時、確信度の低いほうを削除する機能を追加したほうが見栄えはいいかもしれません。
![result](https://github.com/PythonHuro/ocha/blob/master/detect_objects/Output.jpg)

## Saveされたファイルの名前について(2019/3/4追記)
名前は「'object名' + '確信度' + '.png'」になっています。  
確信度を追加した理由は、例えばbottleが2つ写っていた場合、名前だけだと片方が上書きされて、結局1枚しか残らないからです。
  
## Description
わかりやすいhtmlファイル乗っけてあるので、ダウンロードして読んでください。
