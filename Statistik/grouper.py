import unittest
from parameterized import parameterized


def group(values):
    group_dict = {}
    for num in values:
        group_dict[num] = group_dict.get(num, 0) + 1
        
    return group_dict

def group_2(values):
    return {num: values.count(num) for num in values}

    
def lin_buckets(values, num):
    if num == 0:
        raise ValueError("Cant divide by 0!")
    if not num:
        return []
    min_num = min(values)
    max_num = max(values)
    bucket_width = (max_num - min_num) / num

    buckets = [[] for _ in range(num)]
    caps = []

    #borders = [min_num + i * bucket_width for i in range(num + 1)]
    #caps = [(lower, upper) for lower, upper in zip(borders, borders[1:])]

    for i in range(num):
        lower_bound = min_num + i * bucket_width
        upper_bound = min_num + (i + 1) * bucket_width
        caps.append((lower_bound, upper_bound))
    
    for value in values:
        for i, (lower_bound, upper_bound) in enumerate(caps):
            if lower_bound <= value < upper_bound:
                buckets[i].append(value)
        if value == max_num:
            buckets[-1].append(value)
    return buckets

class TestGrupierer(unittest.TestCase):
    
    @parameterized.expand([
        [['mo', 'di', 'mo'], {'mo': 2, 'di': 1}],
        [['mo', 'di', 'mo', 'do', 'di', 'mo'], {'mo': 3, 'di': 2, 'do':1}],
        [["fr"], {"fr": 1}],
        [[], {}]
        ])
    def test_group(self, values, expected):
        self.assertEqual(group(values), expected)
        
    @parameterized.expand([
        [([14.5, 96.8, 15, 22, 10, 100], 3), [[14.5, 15, 22, 10], [], [96.8, 100]]],
        [([5.0, 21, 29, 52.4, 77.3, 85], 4), [[5.0, 21], [29], [52.4], [77.3, 85]]],
        [([10], 1), [[10]]],
        [([0], 1), [[0]]],
        [([5.0, 21, 29, 52.4, 77.3, 85], 4), [[5.0, 21], [29], [52.4], [77.3, 85]]],
        [([5.0, 21, 29, 52.4, 77.3, 85.9], 4), [[5.0, 21], [29], [52.4], [77.3, 85.9]]],
        [([10, 40, 50, 70], 2), [[10], [40, 50, 70]]]
    ])
    
    def test_lin_buckets(self, params, expected):
        values, num = params
        self.assertEqual(lin_buckets(values, num), expected)
        
    def test_raise_value_error(self):
        with self.assertRaises(ValueError) as context:
            lin_buckets([], 0)
        self.assertEqual(str(context.exception), "Cant divide by 0!")


if __name__ == '__main__':
    unittest.main()