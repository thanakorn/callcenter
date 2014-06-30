__author__ = 'thanakorn'

from src.question import Question

class QuestionExtractor(object):

    def __init__(self):
        self._questions = ['what', 'when', 'which', 'how much', 'how many', 'i want', 'i would like']
        self._verbs = ['is', 'am', 'are', 'use', 'know', 'have', 'recommend', 'expire']
        self._adjective = ['current', 'now', 'calling and internet', 'internet', 'calling']
        self._information = ['package', 'bill', 'account', 'balance', 'money']

    def extract(self, question):

        words = question.split() # Split question into list of single words

        # Convert user's question to standard format
        verb = None
        qw = None
        info = None
        adj = None
        for word in words:
            # Find verb
            if word in self._verbs:
                verb = word
            # Find question word
            elif word in self._questions:
                qw = word
            # Find related information
            elif word in self._information:
                info = word
            # Find adjective
            elif word in self._adjective:
                adj = word

        return Question(qw, verb, adj, info)
