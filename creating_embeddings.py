import pathlib
import sys

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

document_root = pathlib.Path("~/Downloads/docs").expanduser()


def main():
    markdown_files = document_root.glob("*.md")

    i = 0
    for md_file in markdown_files:
        if i > 0:
            break
        with open(md_file) as f:
            print(f"{md_file = }")
            print(f"{f = }")
            # we remove the last two items as they are junk
            text = [line.strip() for line in f.read().split("\n") if len(line) > 0][:-2]
            # print(text)
            embeddings = model.encode(text)
            # print(embeddings)
            text_and_embeddings = list(zip(text, embeddings))
            # print(text_and_embeddings)
        i += 1

    for text, embeddings in text_and_embeddings:
        print(f"{text}\t{embeddings.tolist()}")
    print(f"no of files: {i}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
