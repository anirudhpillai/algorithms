import string


class ConceptMap(object):
    """
    Using Aho–Corasick - this allows the searching to revert back to
    earlier state (i.e. dump the prefix) once a state failed

    Attributes:
        trie: describe the trie's function here
    """

    def __init__(self, concepts):
        """Initialise trie from list of concepts"""
        concepts = [concept.lower() for concept in concepts]

        self.trie = [{
            "value": "",
            "next_states": [],
            "fail_state": 0,
            "outputs": []
        }]
        self._add_concepts(concepts)
        self._set_transitions()

    # private methods should start with underscore
    def _check_next_state(self, current_state, next_value):
        """search if next_value is in next_states"""
        for item in self.trie[current_state]["next_states"]:
            if self.trie[item]["value"] == next_value:
                return item

        return None  # you actually don't need this line but think its easier to understand with it

    def _add_concepts(self, concepts):
        for concept in concepts:
            current_state = 0
            index = 0  # I think index makes it easier to understand
            next_state = self._check_next_state(current_state, concept[index])

            # find the longest prefix
            while next_state:
                current_state = next_state
                index += 1
                if index < len(concept):
                    next_state = self._check_next_state(
                        current_state, concept[index]
                    )
                else:
                    break

            # add new states
            for c in concept[index:]:
                # add new state for the character
                self.trie.append({
                    "value": c,
                    "next_states": [],
                    "fail_state": 0,
                    "outputs": []
                })
                self.trie[current_state]["next_states"].append(
                    len(self.trie) - 1
                )  # point current to next
                current_state = len(self.trie) - 1

            self.trie[current_state]["outputs"].append(concept)

    def _set_transitions(self):
        """set fail_state : point to longest suffix of current_state"""
        queue = []

        for state in self.trie[0]["next_states"]:
            queue.append(state)
            self.trie[state]["fail_state"] = 0

        while queue:
            root = queue.pop(0)

            for state in self.trie[root]["next_states"]:
                queue.append(state)
                fail_state = self.trie[root]["fail_state"]

                while (
                    fail_state != 0 and
                    not self._check_next_state(
                            fail_state,
                            self.trie[state]["value"]
                    )
                ):
                    fail_state = self.trie[fail_state]["fail_state"]

                temp_fail_state = self._check_next_state(
                    fail_state,
                    self.trie[state]["value"]
                )

                if not temp_fail_state:
                    self.trie[state]["fail_state"] = 0
                else:
                    self.trie[state]["fail_state"] = temp_fail_state

                self.trie[state]["outputs"].extend(
                    self.trie[self.trie[state]["fail_state"]]["outputs"]
                )

    def get_concepts(self, utterance):
        """
        Finds all concepts in the utterance

        Args:
            :utterance describe utterance here
        Returns:
            list of dicts containing concept and the index at which it occurs
        """
        # Removing punctuation
        utterance = utterance.lower().replace(string.punctuation, "")
        current_state = 0
        concepts = []

        for idx, char in enumerate(utterance):
            while (
                current_state != 0 and
                not self._check_next_state(current_state, char)
            ):
                current_state = self.trie[current_state]["fail_state"]

            temp_current_state = self._check_next_state(current_state, char)

            if not temp_current_state:
                current_state = 0
            else:
                current_state = temp_current_state
                for item in self.trie[current_state]["outputs"]:
                    concepts.append({
                        "index": idx - len(item) + 1,
                        "word": item
                    })

        return concepts
