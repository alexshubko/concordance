import sys
import spacy
nlp = spacy.load('en_core_web_sm')
from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)


def concordance(file_path, searched_term, window = 3):

	with open(file_path) as input_f:
		contents = input_f.read()

	doc = nlp(contents)

	searched_term = nlp(searched_term)

	matcher.add('searched_term', None, searched_term)

	matches = matcher(doc)

	matches_with_context = []

	for match_id, start, end in matches:
		surroundings = doc[start-window:end+window].text
		matches_with_context.append(surroundings)

	return "\n".join(matches_with_context)

if __name__ == "__main__":
	print(concordance(sys.argv[1],sys.argv[2],int(sys.argv[3])))	