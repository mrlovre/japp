import pandas as pd
from jamdict import Jamdict
from fugashi import Tagger
import jaconv
import re

jmd = Jamdict(memory_mode=True)
tagger = Tagger()

# %%
with open("saigo.txt", "r") as file:
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
        lemma = token.feature.lemma
        kanji = str.join("、", [form.text for form in entry.kanji_forms])
        accent = token.feature.aType
        pos1 = token.feature.pos1
        pos2 = token.feature.pos2
        pos_ext = sense.pos
        defs = str.join("\n", [str.join("; ", [gloss.text for gloss in sense.gloss]) for sense in entry.senses])
        entries.append([token.feature.orthBase, kana, lemma, kanji, defn, pos1, pos2, pos_ext, accent, info, defs])
    except IndexError:
        print(f"{word} not found.")

entries = pd.DataFrame(entries, columns=["word", "kana", "lemma", "kanji_forms", "definition", "pos1", "pos2", "pos_ext", "accent", "info", "all_defs"])

# entries.loc[entries["word"] == entries["kana"], "word"] = ""

entries.to_csv("entries.csv", index=False)

# %%
with open("output.tex", "w") as file:
    for _, entry in entries.iterrows():
        word = entry["lemma"]
        kana = entry["kana"]
        pitch_info = int(entry["accent"].split(",")[0])

        if pitch_info == 0:
            pitch = str.join(",", [f"{k}/{int(p != 0)}" for p, k in enumerate(kana)])
            pitch += ",/1"
        else:
            pitch = str.join(",", [f"{k}/{int(p <= pitch_info and (pitch_info == 1 or p != 1))}"
                                   for p, k in enumerate(kana, 1)])
            pitch += ",/0"

        pitch = re.sub(r"/([01]),([ゃゅょャュョ])/[01]", r"\\m{\2}/\1", pitch)

        kana = rf"\pitch{{{pitch}}}"
        defn = entry["definition"]
        # defs = str.join(" ", [rf"\item {def_}" for def_ in entry["all_defs"].split("\n")])
        pos = entry["pos1"]

        if "intransitive verb" in entry["pos_ext"]:
            pos = "自" + pos
        elif "transitive verb" in entry["pos_ext"]:
            pos = "他" + pos

        print(rf"\dictentryadv{{{word} \strut}}{{{kana}}}{{\item {defn}}}{{{pos}}}", file=file)
        # print(rf"\dictentryadv{{{word} \strut}}{{{kana}}}{{{defs}}}{{{pos}}}", file=file)
