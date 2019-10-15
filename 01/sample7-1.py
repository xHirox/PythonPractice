#エスケープシーケンス
# 例えば複数行にわたる文字列を定義したい場合、
# 文字列の中に改行を表す文字を入力する必要があります。
# このような特殊な文字を表すのに使用するのがエスケープシーケンスです。
# windows:エンマーク その他:バックスラッシュ
# ¥n	文字列を途中で改行する
# ¥¥	バックスラッシュ (¥)
# ¥'	一重引用符 (')
# ¥"	二重引用符 (")
# ¥a	ASCII 端末ベル (BEL)
# ¥b	ASCII バックスペース (BS)
# ¥f	ASCII フォームフィード (FF)
# ¥n	ASCII 行送り (LF)
# ¥r	ASCII 復帰 (CR)
# ¥t	ASCII 水平タブ (TAB)
# ¥v	ASCII 垂直タブ (VT)
# ¥ooo	8進数oooを持つASCII文字
# ¥xhh	16進数hhを持つASCII文字
# ¥N{name}	Unicode データベース中で名前 name を持つ文字
# ¥uxxxx	16ビットの16進数値xxxxを持つUnicode文字
# ¥Uxxxxxxxx	32ビットの16進数値xxxxxxxxを持つUnicode文字
print ("こんにちは。\nお元気ですか？\nそれではまた。")
print ('Tom\'s toy')
print ("I will go to the amusement park with \
my children tomorrow")