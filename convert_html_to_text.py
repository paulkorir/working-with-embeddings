import pathlib
import sys
import re

import html2text

document_root = pathlib.Path("~/Downloads/docs").expanduser()
print(f"{document_root = }")


def remove_all_blank_rows(text: str) -> str:
    clean_text = ""
    for row in text.split("\n"):
        if re.match(r"^\s*$", row):
            continue
        clean_text += row + "\n"
    return clean_text

def main():
    h = html2text.HTML2Text()
    h.ignore_links = True
    html_files = document_root.glob("*.html")
    i = 0
    for html_file in html_files:
        # if i > 0:
        #     break
        with open(html_file) as f:
            print(f"{html_file = }")
            print(f"{f = }")
            html = f.read()
            text = remove_all_blank_rows(h.handle(html))
            print(text)
            with document_root.joinpath(html_file.stem + ".md").open("w") as f:
                f.write(text)
        i += 1
    print(f"no of files: {i}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
