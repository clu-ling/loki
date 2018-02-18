import re

class LokiPattern(object):
    """
    Houses a sequence of pattern fragments
    """
    def __init__(self, fragments):
        self.fragments = fragments

    def match(self, sentence, start_indices):
        num_fragments = len(self.fragments)
        indices = start_indices
        for i, frag in enumerate(self.fragments):
            passed = frag.match(sentence, indices)
            # if this isn't the final pattern fragment, we need to advance one token iff the next frag is also a TokenPattern
            # ex. "<dobj [lemma="make"] [] >dep", but not "<dobj [lemma="make"] >dep"
            if isinstance(frag, TokenPattern) and i + 1 < num_fragments and isinstance(self.fragments[i + 1], TokenPattern):
                indices = [idx + 1 for idx in passed if idx + 1 < len(sentence.words)]
            # this covers both TraversalPatterns as well as fragment-final TokenPatterns
            else:
                indices = list(passed)
            if not indices:
                return []
        return indices

class TraversalPattern(object):
    """
    Base class for graph-based traversal patterns
    """
    def __init__(self, is_regex=False, pattern=None):
        self.is_regex = is_regex
        self.pattern = pattern

    def compile(self):
        """
        compiles a traversal pattern
        """
        if self.is_regex and not isinstance(self.pattern, re._pattern_type):
            self.pattern = re.compile(self.pattern)

    def match_token(self, candidate):
        """
        Checks token against regex or literal pattern
        """
        # re.search isn't anchored (cf re.match)
        return self.pattern.search(candidate) != None if self.is_regex else self.pattern == candidate


class IncomingTraversal(TraversalPattern):
    """
    """
    def __init__(self, is_regex=False, pattern=None):
        super(IncomingTraversal, self).__init__(is_regex, pattern)

    def match(self, sentence, start_indices):
        # check if compiled
        self.compile()
        destinations = set()
        for start in start_indices:
            for (dest, rel) in sentence.dependencies.incoming[start]:
                if self.match_token(rel):
                    destinations.add(dest)
        return destinations


class OutgoingTraversal(TraversalPattern):
    """
    """
    def __init__(self, is_regex=False, pattern=None):
        super(OutgoingTraversal, self).__init__(is_regex, pattern)

    def match(self, sentence, start_indices):
        # check if compiled
        self.compile()
        destinations = set()
        for start in start_indices:
            for (dest, rel) in sentence.dependencies.outgoing[start]:
                if self.match_token(rel):
                    destinations.add(dest)
        return destinations


class IncomingWildcard(TraversalPattern):
    """
    """
    def __init__(self):
        super().__init__()

    def match(self, sentence, start_indices):
        destinations = set()
        for start in start_indices:
            for (dest, _) in sentence.dependencies.incoming[start]:
                destinations.add(dest)
        return destinations


class OutgoingWildcard(TraversalPattern):
    """
    """
    def __init__(self):
        super().__init__()

    def match(self, sentence, start_indices):
        destinations = set()
        for start in start_indices:
            for (dest, _) in sentence.dependencies.outgoing[start]:
                destinations.add(dest)
        return destinations

##############################
# Token patterns
##############################

class TokenPattern(object):
    """
    """
    def match(self, sentence, start_indices):
        pass

class TokenWildcard(TokenPattern):
    """
    """
    def __init__(self):
        super().__init__()

    def match(self, sentence, start_indices):
        return [i for i in start_indices if 0 <= i < len(sentence.words)]


class TokenConstraint(TokenPattern):
    """
    """
    def __init__(self):
        super().__init__()
        # ex. lemma=cat
        self.attribute_constraints = []
    # TODO: test me
    def match(self, sentence, start_indices):
        indices = start_indices
        for ac in self.attribute_constraints:
            indices = ac.match(sentence, indices)
            if not indices:
                return []
        return indices

class AttributeConstraint(object):
    """
    """
    def __init__(self, token_attribute=None, negated=False, is_regex=False, pattern=None):
        self.token_attribute = token_attribute
        self.negated = negated
        self.is_regex = is_regex
        self.pattern = pattern

    def to_loki_pattern(self):
        self.compile()
        neg_repr = "" if not self.negated else "!"
        # pattern.pattern assumes re.compile()
        pattern_repr = "/{}/".format(self.pattern.pattern) \
        if self.is_regex and isinstance(self.pattern, re._pattern_type) else self.pattern
        return "{neg}{tok_attr}={patt}".format(
                neg=neg_repr,
                tok_attr=self.token_attribute,
                patt=pattern_repr
        )

    def compile(self):
        """
        compiles Attribute Constraint
        """
        if self.is_regex and not isinstance(self.pattern, re._pattern_type):
            self.pattern = re.compile(self.pattern)

    def match(self, sentence, start_indices):

        self.compile()

        def match_token(candidate):
            """
            Checks token against regex or literal pattern
            """
            # NOTE: re.search isn't anchored (cf re.match)
            matched = self.pattern.search(candidate) != None if self.is_regex else self.pattern == candidate
            #print("matched '{}'? {}".format(candidate, matched))
            # ex. negated == False and match == True  +> False != True -> True
            # ex. negated == True and match == True  +> True != True -> False
            return self.negated != matched

        def match_tokens(tokens):
            """
            """
            return [i for i in start_indices if i < len(tokens) and match_token(tokens[i])]

        def match_deps(deps):
            """
            """
            indices = []
            for i in start_indices:
                for (_, rel) in deps[i]:
                    if match_token(rel):
                        indices.append(i)
            return indices

        if self.token_attribute == "word":
            toks = sentence.words
            return match_tokens(toks)
        if self.token_attribute == "tag":
            toks = sentence.tags
            return match_tokens(toks)
        if self.token_attribute == "lemma":
            toks = sentence.lemmas
            return match_tokens(toks)
        if self.token_attribute == "chunk":
            toks = sentence.chunks
            return match_tokens(toks)
        if self.token_attribute == "incoming":
            deps = sentence.dependencies.incoming
            return match_deps(deps)
        if self.token_attribute == "outgoing":
            deps = sentence.dependencies.outgoing
            return match_deps(deps)
