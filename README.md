## picture_aspect_resizer

jpg,png画像をリサイズして余白を追加することでアスペクト比と大きさを揃えます。

## ライセンス
[MITライセンス](https://github.com/YoutechA320U/picture_aspect_resizer/blob/master/LICENSE)となります。

## 概要
jpg,png画像をリサイズして余白を追加することでアスペクト比と大きさを揃えるPythonスクリプトです。

![SS](https://raw.githubusercontent.com/YoutechA320U/picture_aspect_resizer/main/42425276.png?raw=true "変換前") 
![SS](https://raw.githubusercontent.com/YoutechA320U/picture_aspect_resizer/main/16_9_42425276.png?raw=true "変換後") 

アスペクト比と解像度は1:1(1080x1080),4:3(1440x1080),16:9(1920x1080)に対応しています。

## 開発環境
    OS : Windows10_64bit_Build19043.1706
    Python : ver3.7.7

## 必要なライブラリ
    pillow, math, pathlib, sys,※CUI版のみ, PySimpleGUI※GUI版のみ

## 使い方

CUI版:
変換したい画像があるフォルダを引数で指定して実行するとファイル名の先頭にアスペクト比の値が追加された上で、同じフォルダに変換された画像が出力されます。

    Windowsの例 python.exe "C:/Users/YoutechA320U/jpg16_9resize.py" "C:/Users/YoutechA320U/Pictures/resize/"

    Debianの例　python /home/youtecha320u/png1_1resize.py /home/youtecha320u/Pictures/
GUI版:
exeファイルを実行し、GUIに従ってフォルダを選択します。

## 備考
画像の拡張子がjpg,png以外だと認識しません。
透過pngを変換すると、元の透過情報はそのままに不透明な余白が追加されます。

質問やバグの報告は[このリポジトリのIssue](https://github.com/YoutechA320U/picture_aspect_resizer/issues)か[作者のTwitter](https://twitter.com/YoutechA320U)へお願いします。

### 参考コード・資料
 * <https://coffee-blue-mountain.com/python-get-filename-0809/>  
 * <https://note.nkmk.me/python-pillow-add-margin-expand-canvas/>  
 * <https://note.nkmk.me/python-pillow-paste/>
 * <https://qiita.com/takanorimutoh/items/53bf44d6d5b37190e7d1/>


## 履歴
    [2022/06/17] - 初回リリース
