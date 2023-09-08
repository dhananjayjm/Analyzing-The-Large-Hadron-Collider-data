## 1. Goal of the project:

**Analyzing LHC data with the help of a docker container. The task is to measure the mass of the Z-Boson.**

At [this link](http://www.atlas.uni-wuppertal.de/~harenber/masses.txt), you will find a data file containing 1919 invariant masses (in GeV) of a two-electron system from a Z→ee decay.

This data needs to be filled into a histogram, see [Wikipedia - Histogram](http://en.wikipedia.org/wiki/Histogram) for a definition of histograms (see "mathematical definition").
The following steps are required for a successful measurement:
1. Download the file.
2. You now need to histogramize the data, create a histogram with 150 bins from 0 to 150 GeV.
3. Find the bin with the highest value. The x-value of that bin is your Z boson mass measurement.
4. As a comparison to that method, do a Gaussian fit of the distribution and find the maximum. How does this value differ from the previous value? What is the influence of the number of bins chosen for the histogram?
5. Try to visualize your data with some kind of graphical representation.
6. **Write out the results into a bind-mount volume.**
#
- **Author**: *Dhananjay Mandalkar*
- **Degree**: MSc Computer Simulation in Science

## 2. Please refer *Project Report Docker Virtualization 1.pdf*  for implementation of the project.

## 3. Documentation for *main.py*

## Project Documentation: 

### Introduction

This project aims to analyze LHC (Large Hadron Collider) data within a Docker container. The primary objective is to measure the mass of the Z-Boson, a fundamental particle in particle physics.

### Dependencies

This project utilizes several Python libraries for data analysis and visualization, including
- `matplotlib` for data visualization.
- `numpy` (aliased as `np`) for numerical computation and array manipulation.
- `scipy.optimize.curve_fit` for fitting a curve to data points.

### Methodology

### Histogram Generation

1. The project begins by reading data from a provided file, which contains 1919 invariant masses (in GeV) of a two-electron system from a Z→ee decay.

2. A histogram is generated from this data, with 150 bins spanning from 0 to 150 GeV.

3. The bin with the highest frequency in the histogram is identified, and its corresponding x-value represents the Z boson mass measurement using the histogram method.

4. ![](https://github.com/dhananjayjm/Analyzing-The-Large-Hadron-Collider-data/blob/main/histogram.png) 

### Gaussian Fitting

4. As a comparison, the project fits a Gaussian distribution to the data and identifies the maximum of this distribution. This value represents the Z boson mass measurement using the Gaussian fitting method.

### Visualization

5. The data is visualized using Matplotlib, with a histogram plot and a Gaussian fit overlay.

### Results

6. The results, including Z boson mass measurements from both methods, are saved to text files.

### Bin Size Variation

7. The project explores the influence of different bin sizes on the mass measurements by repeating the process with various bin sizes. The absolute difference between mass values obtained from the histogram and Gaussian fitting methods is calculated and plotted against different bin sizes.

### Usage

- To perform the analysis, simply run the provided code, specifying the desired bin sizes in the `bin_sizes` list.
- The project recommends using bin sizes up to 2000 for accurate measurements, as beyond this point, differences between histogram and Gaussian fitting results become significant.

### Conclusion

This project demonstrates a step-by-step process for analyzing LHC data to measure the mass of the Z-Boson. It provides insights into the impact of bin size choice on the accuracy of mass measurements.

For further details, refer to the code and comments within the provided script.

## Documentation of Dockerfile

1. **Base Image**: It starts with the `python:3.11` base image, which provides a Python 3.11 environment.

2. **Updating and Installing Dependencies**: It updates the package list and installs several dependencies:
   - `build-essential`: These are essential packages for building software.
   - `libfreetype6-dev` and `libxft-dev`: These are development libraries for rendering fonts and text.
   - `numpy`, `scipy`, `matplotlib`: These Python libraries are installed using `pip`.

3. **Setting the Working Directory**: It sets the working directory within the Docker container to `/usr/src/app`.

4. **Copying Application Files**: It copies the application files from the host machine to the container's working directory (`/usr/src/app`).

5. **Setting Matplotlib Backend**: It sets the Matplotlib backend to 'Agg' using Python code. This is commonly done when you want to use Matplotlib in a non-interactive environment (e.g., inside a Docker container) to save plots as image files.

6. **CMD Command**: The final `CMD` command specifies how the container should run. It runs the `main.py` script using Python 3 (`python3`).

The Dockerfile sets up a Python environment with the necessary dependencies for running a Python application (`main.py`) that likely involves data analysis and visualization using NumPy, SciPy, and Matplotlib. The 'Agg' backend for Matplotlib ensures that plots are generated as image files without requiring a graphical display.

---
