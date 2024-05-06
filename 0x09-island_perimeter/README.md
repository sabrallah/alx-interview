# Island Perimeter Project

## Overview

This project, part of the ALX Africa Intranet curriculum, focuses on solving a geometric problem within a grid context. The goal is to calculate the perimeter of a single island in a 2D array of integers, where 0 represents water and 1 represents land. The project requires applying knowledge of algorithms, data structures (specifically matrices or 2D lists), and iterative or conditional logic.

## Project Details

- **Project Name:** 0x09. Island Perimeter
- **Author:** Alexa Orrico, Software Engineer at Holberton School
- **Start Date:** Mar 3, 2024 7:00 PM
- **End Date:** Mar 7, 2024 7:00 PM
- **Checker Release:** Mar 4, 2024 7:00 PM
- **Auto Review Deadline:** Mar 7, 2024
- **[Repository Link](https://github.com/sabrallah/alx-interview/tree/master/0x09-island_perimeter)**
- **[File Link](https://github.com/sabrallah/alx-interview/blob/master/0x09-island_perimeter/0-island_perimeter.py)**

## Project Requirements

- **Allowed Editors:** vi, vim, emacs
- **Interpreted/Compiled on:** Ubuntu 20.04 LTS using Python3 (version 3.4.3)
- **File Structure:** All files should end with a new line. The first line of all files should be `#!/usr/bin/python3`.
- **README.md:** A mandatory file at the root of the project folder.
- **PEP 8 Style:** Code should follow PEP 8 style guidelines (version 1.7).
- **Import Restrictions:** No external modules are allowed.
- **Documentation:** All modules and functions must be documented.
- **File Executability:** All files must be executable.

## Tasks

### Task 0: Island Perimeter

Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in the given grid. The grid is a list of lists of integers, where 0 represents water and 1 represents land. The cells are square with a side length of 1, connected horizontally/vertically (not diagonally). The grid is rectangular, with its width and height not exceeding 100. There is only one island (or nothing), and the island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island).

### Example

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

print(island_perimeter(grid))  # Output: 12
```

## Concepts Needed

- **2D Arrays (Matrices):**
  - Accessing and iterating over elements in a 2D array.
  - Understanding how to navigate through adjacent cells (horizontally and vertically).

- **Conditional Logic:**
  - Applying conditions to determine whether a cell contributes to the perimeter of the island.

- **Counting Techniques:**
  - Developing a method to count the edges that contribute to the island’s perimeter.

- **Problem-Solving Strategies:**
  - Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.

- **Python Programming:**
  - Nested loops for iterating over grid cells.
  - Conditional statements to check the status of adjacent cells.

## Resources

- **Python Official Documentation:**
  - [Nested Lists](https://docs.python.org/3/tutorial/introduction.html#lists)

- **GeeksforGeeks Articles:**
  - [Python Multi-dimensional Arrays](https://www.geeksforgeeks.org/python-multi-dimensional-arrays)

- **TutorialsPoint:**
  - [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)

- **YouTube Tutorials:**
  - [Python 2D arrays and lists](https://www.youtube.com/watch?v=hYzwCsKGRrg)

By understanding these concepts and utilizing the provided resources, you will be equipped to approach the problem methodically. The project not only tests your algorithmic thinking but also reinforces your ability to manipulate data structures and apply logical reasoning to solve problems.

## Additional Resources

- Mock Technical Interviews

## License

Copyright © 2024 ALX, All rights reserved.