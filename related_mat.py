from rake_nltk import Rake


def process_words():
    with open('transcript.txt', 'r') as file:
        line = file.readline()
        line_content = line.replace('\n', ' ').replace(':', '').lower()
        r = Rake()
        r.extract_keywords_from_text(line_content)
        return r.get_ranked_phrases()[0:10]
