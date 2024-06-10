import itertools
import sys
import os

TARGET_SUM = 100
COMBINATION_POINTS = 4
DATA_FILE_PATH = "data"


def read_points_from_file(file_path):
    """Read points from a file and return them as a list of tuples."""
    points = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                x_coord, y_coord, z_coord, n_value = map(float, line.strip().replace('(', '').replace(')', '').split(','))
                points.append((x_coord, y_coord, z_coord, int(n_value)))
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return points


def calculate_tetrahedron_volume(p1, p2, p3, p4):
    try:
        # Vectors from p1 to p2, p3, and p4
        AB = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
        AC = (p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2])
        AD = (p4[0] - p1[0], p4[1] - p1[1], p4[2] - p1[2])

        # Direct calculation of the cross product components
        cross_product_x = AB[1] * AC[2] - AB[2] * AC[1]
        cross_product_y = AB[2] * AC[0] - AB[0] * AC[2]
        cross_product_z = AB[0] * AC[1] - AB[1] * AC[0]

        # Dot product of AD with the cross product of AB and AC
        scalar_triple_product = (
            AD[0] * cross_product_x +
            AD[1] * cross_product_y +
            AD[2] * cross_product_z
        )

        # The volume of the tetrahedron
        volume = abs(scalar_triple_product) / 6.0
        return volume
    except Exception as e:
            print(f"An unexpected error occurred while calculating volume: {e}")
            return float('inf')


def find_smallest_tetrahedron(points):
    min_volume = float('inf')
    min_tetrahedron = None
    try:
        # itertools.combinations will give the all possible combinations of 4 Points
        for combination in itertools.combinations(enumerate(points), COMBINATION_POINTS):
            indices, tetra_points = zip(*combination)
            n_sum = sum(point[3] for point in tetra_points)
            
            if n_sum == TARGET_SUM:
                # Calculate Volume of Tetrahedron
                volume = calculate_tetrahedron_volume(*tetra_points)
                if volume < min_volume:
                    min_volume = volume
                    min_tetrahedron = indices
        return min_tetrahedron, min_volume
    
    except Exception as e:
        print(f"An error occurred while finding the smallest tetrahedron: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python smallest_tetrahedron_volume_calculator.py <input_file>")
        sys.exit(1)
        
    file_path = os.path.join(DATA_FILE_PATH, sys.argv[1])
    # print(file_path)
    points = read_points_from_file(file_path)
    result, volume = find_smallest_tetrahedron(points)
    
    if result is not None:
        print(f"The indices of the points forming the smallest valid tetrahedron are: {result}")
        print(f"The volume of this tetrahedron is: {volume}")
    else:
        print("No valid tetrahedron found.")


if __name__ == "__main__":
    main()
