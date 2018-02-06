
'''
The toy company "I Can't Believe It Works!" has hired you to help
develop educational toys. The current project is a word toy that
displays four letters at all times. Below each letter are two buttons
that cause the letter above to change to the previous or next letter
in alphabetical order. So, with one click of a button the letter 'c'
can be changed to a 'b' or a 'd'. The alphabet is circular, so for
example an 'a' can become a 'z' or a 'b' with one click. 

In order to test the toy, you would like to know if a word can be
reached from some starting word, given one or more constraints. A
constraint defines a set of forbidden words that can never be displayed
by the toy. Each constraint is formatted like "X X X X", where each X
is a string of lowercase letters. A word is defined by a constraint if
the ith letter of the word is contained in the ith X of the contraint.
For example, the constraint "lf a tc e" defines the words "late",
"fate", "lace" and "face". 

You will be given a String start, a String finish, and a String[]
forbid. Calculate and return the minimum number of button presses
required for the toy to show the word finish if the toy was originally
showing the word start. Remember, the toy must never show a forbidden
word. If it is impossible for the toy to ever show the desired word,
return -1.

Class:  SmartWordToy
Method: minPresses
Parameters: String, String, String[]
Returns:    int
Method signature:  public int minPresses(String start, String finish,
                                         String[] forbid)
'''

import collections

class Forbidden(object):
    def __init__(self, forbid):
        self.words = set(forbid)

    def forbid(self, w):
        self.words.add(w)

    def word(self, w):
        is_forbidden = False
        for _word in self.words:
            c1, c2, c3, c4 = _word.split(' ')
            forbidden = w[0] in c1 \
                      and w[1] in c2 \
                      and w[2] in c3 \
                      and w[3] in c4
            is_forbidden |= forbidden
        return is_forbidden

class History(object):
    def __init__(self):
        self.itinerary = set()

    def visit(self, word):
        self.itinerary.add(word)

    def is_visited(self, word):
        return word in self.itinerary

    def clear(self):
        self.itinerary = set()

class WordVertex(str):
    def __new__(cls, s, history, forbidden=None, end_word=None):
        return super(WordVertex, cls).__new__(cls, s)

    def __init__(self, s, history, forbidden=None, end_word=None):
        super(WordVertex, self).__init__(s)
        self.visited = None
        self.distance = 0
        self.history = history
        self.forbidden = forbidden
        self.end_word = end_word

    def set_end_word(self, end_word):
        self.end_word = end_word

    def visit(self, distance=0):
        self.history.visit(self)
        self.distance += distance

    def edges(self):
        l = len(self)
        if self.forbidden is not None:
            for i in range(l):
                o = ord(self[i]) - 97
                v1 = self[0:i] + chr(((o + 1) % 26) + 97) + self[i+1:l]
                v2 = self[0:i] + chr(((o - 1) % 26) + 97) + self[i+1:l]
                if not self.history.is_visited(v1) \
                   and not self.forbidden.word(v1):
                    yield WordVertex(v1, self.history, self.forbidden,
                        self.end_word)
                if not self.history.is_visited(v2) \
                   and not self.forbidden.word(v2):
                    yield WordVertex(v2, self.history, self.forbidden,
                        self.end_word)
            return
        for i in range(l):
            o = ord(self[i]) - 97
            v1 = self[0:i] + chr(((o + 1) % 26) + 97) + self[i+1:l]
            v2 = self[0:i] + chr(((o - 1) % 26) + 97) + self[i+1:l]
            if not self.history.is_visited(v1):
                yield WordVertex(v1, self.history, self.forbidden,
                    self.end_word)
            if not self.history.is_visited(v2):
                yield WordVertex(v2, self.history, self.forbidden,
                    self.end_word)

# NOTE: ignore the following (reference only)
#    def _score(self):
#        return sum([
#            ((ord(self[0]) - 97) * 26**3),
#            ((ord(self[1]) - 97) * 26**2),
#            ((ord(self[2]) - 97) * 26**1),
#            ((ord(self[3]) - 97) * 26**0),
#        ])
#
#    @property
#    def rank(self):
#        if self.end_word is None:
#            raise ValueError('end_word is None')
#        K_min = 0
#        K_max = 26**4
#        k_1 = self._score()
#        k_n = self.end_word._score()
#        delta_max = K_max/2
#        delta_max_pos = (self._score() + delta_max) % K_max
#        if k_1 <= k_n <= K_max:
#            return (True, k_n - k_1)
#        if k_1 <= k_n <= delta_max_pos:
#            return (True, k_n - k_1)
#        if K_min <= k_n <= delta_max_pos:
#            return (True, (K_max - k_1) + k_n)
#        if delta_max_pos <= k_n <= k_1:
#            return (False, k_1 - k_n)
#        if K_min <= k_n <= k_1:
#            return (False, k_1 - k_n)
#        if delta_max_pos <= k_n <= K_max:
#            return (False, (K_max - delta_max_pos) + k_1)

class SmartWordToy(object):
    def __init__(self, start_word, end_word, forbid):
        self.history = History()
        self.forbidden = Forbidden(forbid)
        self.end = WordVertex(end_word, self.history, self.forbidden)
        self.end.set_end_word(self.end)
        self.start = WordVertex(start_word, self.history, self.forbidden,
            self.end)

    def minPresses(self):
        if self.forbidden.word(self.start):
            return -1
        self.start.visit()
        proc_queue = collections.deque([self.start])
        total_distance = self.start.distance
        while proc_queue:
            current_word = proc_queue.popleft()
            total_distance = current_word.distance
            for word in current_word.edges():
                word.visit(current_word.distance + 1)
                proc_queue.append(word)
            if current_word == self.end:
                break
            if not proc_queue and current_word != self.end:
                total_distance = -1
        return total_distance

if __name__ == '__main__':
    import json
    cases = []
    with open('smartwordtoy_tests.txt') as f:
        for line in f.readlines():
            cases.append(json.loads('[%s]' % line))
    for i, case in enumerate(cases):
        toy = SmartWordToy(case[0], case[1], case[2])
        print "case %d PASS: %s" % (i, toy.minPresses() == int(case[3]))

