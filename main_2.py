import fugashi
import jamdict

jmd = jamdict.Jamdict()

# text = "今日はいい天気ですね？"
text = "麩菓子は、麩を主材料とした日本の菓子。"
tagger = fugashi.Tagger()
words = tagger(text)
print(tagger(text))

