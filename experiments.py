import sys

from sentence_transformers import CrossEncoder

# cross encoders are more accurate but slower than sentence encoders
model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


# string subclass which holds the document name for each passage
# we can think of this as a simple document store then add as many attributes as we want so that
# we can relate each package to as many modules as possible
# this way users can get the most relevant information from the document
class Passage(str):

    def __new__(cls, *args, document=None, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance.document = document
        return instance

    def __init__(self, text: str, document=None):
        self.text = text
        self.document = document

    def __str__(self):
        return self.text


def main():
    # query = "How many people live in Berlin?"
    query = input("query: ")
    passages = [
        Passage("Berlin had a population of 3,520,031 registered inhabitants in an area of 891.82 square kilometers.",
                document="Berlin Population"),
        Passage("Berlin is well known for its museums.", document="Museums"),
        Passage("In 2014, the city state Berlin had 37,368 live births (+6.6%), a record number since 1991.",
                document="Berlin Births"),
        Passage(
            "The urban area of Berlin comprised about 4.1 million people in 2014, making it the seventh most populous urban area in the European Union.",
            document="EU"),
        Passage(
            "The city of Paris had a population of 2,165,423 people within its administrative city limits as of January 1, 2019",
            document="Paris"),
        Passage(
            "An estimated 300,000-420,000 Muslims reside in Berlin, making up about 8-11 percent of the population.",
            document="Berlin Muslims"),
        Passage("Berlin is subdivided into 12 boroughs or districts (Bezirke).", document="Berlin Boroughs"),
        Passage("In 2015, the total labour force in Berlin was 1.85 million.", document="Berlin Labour Force"),
        Passage(
            "In 2013 around 600,000 Berliners were registered in one of the more than 2,300 sport and fitness clubs.",
            document="Berlin Sports"),
        Passage(
            "Berlin has a yearly total of about 135 million day visitors, which puts it in third place among the most-visited city destinations in the European Union.",
            document="Berlin Visitors"),
    ]
    ranks = model.rank(query, passages)
    print(f"{ranks = }")
    print("Query:", query)
    for rank in ranks:
        passage = passages[rank['corpus_id']]
        print(f"{rank['score']:.2f}\t{passage.document}\t{passage}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
