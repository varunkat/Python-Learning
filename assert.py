import unittest
lis = [1,2,3,4]


def mul(lis):
    x = 1
    for i in lis:
        x = x*i
    return x
3
#assert mul(lis) == 12, "Should be 24"
print(mul(lis))

class testsum(unittest.TestCase):
    def test_mul(self):
        self.assertEqual(mul(lis), 24, "should be 24")

if __name__ == '__main__':
    unittest.main()
