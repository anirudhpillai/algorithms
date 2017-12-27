from ConceptMap import ConceptMap

import random
import string


def generate_word(word_len):
    return ''.join(random.choice(string.ascii_letters) for _ in range(word_len))


def create_concepts_list(no_of_concepts):
    concepts = []
    for _ in range(no_of_concepts):
        concepts.append(generate_word(random.randint(4, 9)))
    return concepts


def generate_utterance(concepts):
    correct_answer = 0

    utterance = ""
    for _ in range(10):
        chance = random.randint(1, 100)
        if chance <= 50:
            utterance += random.choice(concepts)
            correct_answer += 1
        else:
            utterance += generate_word(random.randint(0, 3))

    return utterance, correct_answer


concepts = create_concepts_list(10)
cmap = ConceptMap(concepts)

print(concepts)

for _ in range(10):
    utterance, correct_answer = generate_utterance(concepts)
    matches = cmap.get_concepts(utterance)
    print(utterance, correct_answer, len(matches))
    assert len(matches) == correct_answer
