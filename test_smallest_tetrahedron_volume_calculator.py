import unittest
from smallest_tetrahedron_volume_calculator import read_points_from_file, find_smallest_tetrahedron

class TestTetrahedronVolumeCalculator(unittest.TestCase):

    def test_read_points_from_file(self):
        points = read_points_from_file('data/test_case_1.txt')
        expected_points = [
            (1.0, 1.0, 1.0, 25),
            (2.0, 2.0, 2.0, 25),
            (3.0, 3.0, 3.0, 25),
            (4.0, 4.0, 4.0, 25),
            (5.0, 5.0, 5.0, 5),
            (6.0, 6.0, 6.0, 5),
            (7.0, 7.0, 7.0, 5),
            (8.0, 8.0, 8.0, 5)
        ]
        self.assertEqual(points, expected_points)

    def test_find_smallest_tetrahedron(self):
        points = [
            (1.0, 1.0, 1.0, 25),
            (2.0, 2.0, 2.0, 25),
            (3.0, 3.0, 3.0, 25),
            (4.0, 4.0, 4.0, 25),
            (5.0, 5.0, 5.0, 5),
            (6.0, 6.0, 6.0, 5),
            (7.0, 7.0, 7.0, 5),
            (8.0, 8.0, 8.0, 5)
        ]
        result, volume = find_smallest_tetrahedron(points)
        expected_result = (0, 1, 2, 3)  # The indices of the points forming the smallest valid tetrahedron
        self.assertEqual(result, expected_result)
        self.assertTrue(volume >= 0)

if __name__ == '__main__':
    unittest.main()
