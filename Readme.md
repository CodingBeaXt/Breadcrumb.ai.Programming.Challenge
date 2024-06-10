
# Find Valid Tetrahedron with the smallest possible Volume

This project identifies four points from a list of points on a 3D plane that form a 'valid' tetrahedron with the smallest possible volume. A 'valid' tetrahedron is defined as one where the sum of the associated integer values (`n_value`) of the points is equal to 100.

## Features

- Reads a list of points from a file.
- Calculates the volume of a tetrahedron formed by any four points.
- Identifies the indices of the four points that form the smallest valid tetrahedron.

## Prerequisites

- Python 3.8 or higher


## Setup

1. **Unzip the folder**

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  
    
    # On Windows use `venv\Scripts\activate`
    ```

3. **Prepare your input file**:

    - Place your input file (e.g., `points_small.txt`) in the `data` directory.
    - Each line in the file should contain a point in the format: `(x_cord, y_cord, z_cord, n_value)`
    - Example:
      ```
      (3.00, 4.00, 5.00, 22)
      (2.00, 3.00, 3.00, 3)
      (1.00, 2.00, 2.00, 4)
      (3.50, 4.50, 5.50, 14)
      (2.50, 3.50, 3.50, 24)
      (6.70, 32.20, 93.0, 5)
      (2.50, 3.00, 7.00, 40)
      ```

## Running Unit Tests

1. To run the unit tests, execute the following command:
    ```sh
    python -m unittest test_tetrahedron_volume_calculator.py
    ```

## Running the Program

1. **Run the script**:

    ```bash
    python smallest_tetrahedron_volume_calculator.py points_small.txt
    ```

    - The script will read the points from `data/points_small.txt` and calculate the smallest valid tetrahedron.
    - It will output the indices of the points forming the smallest valid tetrahedron and the volume of the tetrahedron.


## Notes

- Ensure that the `points_small.txt` file is properly formatted as specified above.
- The program sorts the points by their `n` values and uses a combination of points to find the smallest tetrahedron that satisfies the condition.
- The combination approach can be computationally intensive for a large number of points.

