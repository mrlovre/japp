import pandas as pd

vocabulary = pd.read_csv("vocabulary-aiamukonpyuuta.tsv", sep="\t")
vocabulary = vocabulary.sort_values("readings")

def process(row: pd.DataFrame):
    word = row["word"]
    word = word.replace(";", r"$\cdot$")
    readings = row["readings"]
    readings = readings.replace(";", r"$\cdot$")
    meanings = row["meanings"].replace(";", "; ").split("\n")
    meanings = [r"\item " + meaning for meaning in meanings]
    meanings = str.join(" ", meanings)
    return rf"\entry{{{word}}}{{{readings}}}{{\begin{{itemize}}{meanings}\end{{itemize}}}}".strip()

with pd.option_context("display.max_colwidth", -1), open("output.txt", "w") as file:
    print(vocabulary.apply(process, axis="columns").to_string(index=False), file=file)
