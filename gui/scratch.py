import pandas as pd
from jamdict import Jamdict
from fugashi import Tagger
import jaconv

jmd = Jamdict(memory_mode=True)
tagger = Tagger()

# %%
with open("kona.txt", "r") as file:
    text = file.read()

# %%
allow_pos = ["名詞", "動詞", "形容詞", "形状詞"]

# %%
words = []
tokens = []

for token in tagger(text):
    if token.feature.pos1 in allow_pos:
        word = token.feature.lemma
        if word is not None and word not in words:
            words.append(word)
            tokens.append(token)

print(*words, sep="\n")

# %%
entries = []
for word, token in zip(words, tokens):
    try:
        entry = jmd.lookup(word).entries[0]
        sense = entry.senses[0]
        defn = str.join("; ", [gloss.text for gloss in sense.gloss])
        info = str.join(" ", sense.info)
        kana = jaconv.kata2hira(token.feature.kanaBase)
        accent = token.feature.aType
        pos = token.feature.pos1
        entries.append([token.feature.orthBase, kana, defn, pos, accent, info])
    except IndexError:
        print(f"{word} not found.")

entries = pd.DataFrame(entries, columns=["word", "kana", "definition", "pos", "accent", "info"])

# entries.loc[entries["word"] == entries["kana"], "word"] = ""

entries.to_csv("entries.csv", index=False)

# %%
with open("output.tex", "w") as file:
    for _, entry in entries.iterrows():
        word = entry["word"]
        kana = entry["kana"]
        pitch_info = int(entry["accent"].split(",")[0])

        if pitch_info == 0:
            pitch = str.join(",", [f"{k}/{int(p != 0)}" for p, k in enumerate(kana)])
            pitch += ",/1"
        else:
            pitch = str.join(",", [f"{k}/{int(p <= pitch_info and (pitch_info == 1 or p != 1))}"
                                   for p, k in enumerate(kana, 1)])
            pitch += ",/0"

        kana = rf"\pitch{{{pitch}}}"
        defn = entry["definition"]
        pos = entry["pos"]
        print(rf"\dictentryadv{{{word} \strut}}{{{kana}}}{{\item {defn}}}{{{pos}}}", file=file)
