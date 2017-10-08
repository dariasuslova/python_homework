
def poly_hash(s, x=31, p=997):
    h = 0
    for j in range(len(s)-1, -1, -1):
        h = (h * x + ord(s[j]) + p) % p
    return h

def search_rabin_multi(text, patterns):
    indices = []
    for pattern in patterns:
        pos=[]
        pattern_hash = poly_hash(pattern)
        for i in range(len(text) - len(pattern)):
            substr_hash = poly_hash(text[i: i + len(pattern)])
            if substr_hash == pattern_hash:
                if text[i: i + len(pattern)] == pattern:
                    pos.append(i)
        indices.append(pos)
    return indices

# ###### Асимтоматическая оценка сложности алгоритма
# сложность функции poly_hash равняется O(n), так как в ней всего один цикл => сложность функции search_rabin_multi будет включать в себя сложность функции poly_hash => сложность фунции O(n^3)

from unittest import *

class SearchNaiveTest(TestCase):
    def setUp(self):
        self.search = search_rabin_multi
    def test_empty(self):
        text = ''
        patterns = ['w', 't']
        self.assertEqual(len(self.search(text, patterns)[0]), 0)
        self.assertEqual(len(self.search(text, patterns)[1]), 0)
        
    def test_empty_pattern(self):
        text = 'cat'
        patterns = []
        self.assertEqual(len(self.search(text, patterns)), 0)
        
    def test_big_pattern(self):
        text = 'dog'
        patterns = ['dogdogdog']
        self.assertEqual(len(self.search(text, patterns)[0]), 0)
        
    def test_count(self):
        text = 'Betty Botter bought some butter,             But, she said, the butter’s bitter.             If I put it in my batter,             It will make my batter bitter.'
        patterns = ['tt', 'll', 'ke', 'i']
        indices = [[2, 8, 27, 66, 75, 113, 149, 156], [136], [141], [56, 74, 102, 105, 135, 155]]
        self.assertListEqual(self.search(text, patterns), indices)
        
case = SearchNaiveTest()
suite = TestLoader().loadTestsFromModule(case)
TextTestRunner().run(suite)

