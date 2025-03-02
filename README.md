# SimpleSampleApplicationFromGrok3
## これは何か？  
Grok3にプロンプトから生成してもらった簡単なゲームっぽいアプリケーションのコードです。  
関連リポジトリ： [SimpleSampleApplicationFromLLMs](https://github.com/CakeNNN/SimpleSampleApplicationFromLLMs)   
[元ツイート](https://x.com/CakeTwt/status/1895846186042736864)  

## 実行するには？  
①python(3.8で確認)の使える環境にてpygameをインストールします。 
<pre>
  pip install pygame
</pre>
②あとは個々のファイルを実行するだけです。  
(例)
<pre>
python testgame00_00.py  
</pre>

  
## 詳細
### testgame00_00.py
以下のプロンプトで生成してもらったコードです。
<pre>
次のような簡単なゲームを作成したいと思います。pythonでコードを書いてください。
・「プレイヤー」はカーソルキーで上下左右に移動。
・画面周辺から「敵」がランダムで出現
・「敵」はプレイヤー方向に移動
・「プレイヤー」が「敵」に接触したらゲーム終了。
</pre>  

### testgame00_01.py  
出力されたコードでは以下のエラーが発生しました。  
<pre>
direction = http://self.player.rect.center - http://self.rect.center
TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
</pre>
これを以下のプロンプトにて修正してもらったコードです。  
<pre>
提案していただいたコードは71行目に置いて実行時に以下のエラーが発生します。修正をお願いできますか？
direction = self.player.rect.center - self.rect.center
TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
</pre>

### testgame00_02.py  
以下のプロンプトによって仕様変更を行い生成されたコードです。  
<pre>
「敵」の仕様を次のように変更します。コードを修正してください。
・「敵」は出現から一定時間はプレイヤー方向に移動
・一定時間経過後はそのまま直進
・画面外に出そうになったら消滅  
</pre>
