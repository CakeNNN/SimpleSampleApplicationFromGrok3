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
direction = self.player.rect.center - self.rect.center
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

### testgame00_02_fix_suggestion.py  
testgame00_02.pyでは敵が全く出現しなくなってしまいました。  
原因を確認したうえでその理由は告げずに修正をお願いし、提案されたコードです。  
コードは修正箇所のみの提案となっており、このコード単体では動作しません。また、testgame00_02.pyにそのまま貼り付けると仕様変更が巻き戻ってしまうため必要な箇所のみの手動マージが必要となります。  

### testgame00_03.py  
前述の修正コードをマージして仕様通り動作するようになったコードです。

