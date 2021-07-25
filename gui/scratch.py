import pandas as pd
from jamdict import Jamdict
from fugashi import Tagger

jmd = Jamdict(memory_mode=True)
tagger = Tagger()

# %%
with open("kona.txt", "r") as file:
    text = file.read()

# %%
allow_pos = ["名詞", "動詞", "形容詞", "形状詞"]

# %%
words = []

for token in tagger(text):
    if token.feature.pos1 in allow_pos:
        word = token.feature.orthBase
        if word is not None and word not in words:
            words.append(token.feature.orthBase)

print(*words, sep="\n")

# %%
entries = []
for word in words:
    try:
        entry = jmd.lookup(word).entries[0]
        sense = entry.senses[0]
        defn = str.join("; ", [gloss.text for gloss in sense.gloss])
        info = str.join(" ", sense.info)
        kana = str.join("; ", [form.text for form in entry.kana_forms])
        entries.append([word, kana, defn, info])
    except IndexError:
        print(f"{word} not found.")

entries = pd.DataFrame(entries, columns=["word", "kana", "definition", "info"])
entries.to_csv("entries.csv", index=False)
