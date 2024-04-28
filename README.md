# RNA Folding Algorithm

# Setup

## Prerequisites

-   g++
-   python (optional required only for running scripts and visualization)

## Installation

-   Clone the repository
-   [Optional] Run the following command to install python dependencies:
    ```python
      pip install -r requirements.txt
    ```
-   Run `doxygen` in the root directory to generate the documentation

## Running the project

-   Run the following command to compile the binary.

    ```bash
      g++ -Iinclude src/*.cpp main.cpp
    ```

-   The binary accepts a file as command line argument containing the RNA sequence.
    ```bash
      ./a.out <input_file>
      # Example
      ./a.out in.txt
    ```
-   Running the visualization script requires one to already have installed the dependencies. The script can be run as follows:
    ```bash
      cd scripts
      python visualize.py <input_file>
      # Example
      python visualize.py ../in.txt
    ```
