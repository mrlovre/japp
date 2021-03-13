_stop_words = """
車　くるま
上　うえ
下　した
入る　はいる
火　ひ
外　そと
出る　でる
出す　だす
大きい　おおきい
大きな　おおきな
山　やま
中　なか
何　なに
時　とき
見る　みる
今　いま
前　まえ
話す　はなす

一　いち
二　に
三　さん
四　よん
五　ご
六　ろく
七　しち
八　はち
九　きゅう
十　じゅう
百　ひゃく
千　せん
万　まん
"""

_delim_entry = "\n"
_delim_col = "　"

stop_words = [tuple(row.split(_delim_col)) for row in _stop_words.strip().split(_delim_entry) if row]