__author__ = 'thanakorn'

from question import Question

class QuestionExtractor(object):

    def __init__(self):
        self._questions = ['what', 'when', 'which', 'how much', 'how many', 'i want', 'i would like']
        self._verbs = ['is', 'am', 'are', 'use', 'know', 'have', 'recommend', 'expire', 'pay']
        self._adjectives = ['current', 'now', 'calling and internet', 'internet', 'calling']
        self._informations = ['package', 'bill', 'account', 'balance', 'money']

    def extract(self, question):

        # Convert user's question to standard format
        # Find question word
        qw = None
        for q in self._questions:
            if q in question:
                qw = q

        # Find verb
        verb = None
        for v in self._verbs:
            if v in question:
                verb = v

        # Find related information
        info = None
        for inf in self._informations:
            if inf in question:
                info = inf

        # Find adjective
        adj = None
        for a in self._adjectives:
            if a in question:
                adj = a
                break

        return Question(qw, verb, adj, info)
