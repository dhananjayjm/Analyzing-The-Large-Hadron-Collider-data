'''
Analyzing LHC data with the help of a docker container:
The task is to measure the mass of the Z-Boson.
'''
'''
Dhananjay Mandalkar
MSc Computer Simulation in Science
Matri. No. 1942677
'''

# Importing matplotlib library for data visualization
import matplotlib

# Setting matplotlib backend to 'Agg' to use the non-interactive Agg backend for generating plots
matplotlib.use('Agg')
 
import matplotlib.pyplot as plt

# numpy library and aliasing it as 'np' for numerical computation and array manipulation
import numpy as np

# Importing the 'curve_fit' function from the 'optimize' module of the scipy library
# for fitting a curve to a given set of data points
from scipy.optimize import curve_fit

# Importing warnings module and ignoring UserWarning category of warnings
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# defining a function 'gaussian'
def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

# The function reads data from the given file, where each line of the file contains a single float value
def plot_histogram(file_name, bin_size):
    # Read data from file
    data = []
    with open(file_name, 'r') as f:
        for line in f:
            data.append(float(line.strip()))

    # Plot histogram
    hist, bins = np.histogram(data, bins=bin_size)
    bin_centers = (bins[:-1] + bins[1:]) / 2
    plt.hist(data, bins=bins)
    plt.xlabel('Mass of Z bosons in GeV')
    plt.ylabel('Frequency')
    plt.title('Histogram for a two electron system from a Z→ee decay')
    plt.savefig("histogram.png", bbox_inches='tight')
   
    
    # Find the bin value for the highest value
    max_index = np.argmax(hist)
    bin_value_histo = (bins[max_index] + bins[max_index+1]) / 2
    print("The bin value for the highest value from Histogram is:", bin_value_histo, "GeV.")    
    np.savetxt('MaxBinValueHistogram.txt', ["The highest value corresponds to the Z boson mass from Histogram is "+ '%.5f' % bin_value_histo + " GeV, when the bin size is" + '%4d' % bin_size + "."], fmt='%s')
    
    # Fit Gaussian distribution to the histogram    
    popt, _ = curve_fit(gaussian, bin_centers, hist)
    x = np.linspace(bins[0], bins[-1], 100)
    plt.plot(x, gaussian(x, *popt), 'k', linewidth=2)
    plt.show()
    plt.close()
    
    # Find the bin of the maximum value of the fitted Gaussian distribution    
    max_index = np.argmax(gaussian(bin_centers, *popt))
    bin_value_gauss = (bins[max_index] + bins[max_index+1]) / 2
    print("The bin value for the highest value from Gaussian Distribution is:", bin_value_gauss, "GeV.")
    print()
    np.savetxt('MaxBinValueGaussian.txt', ["The highest value corresponds to " + '%.5f' % bin_value_gauss + " GeV Z boson mass from Gaussian Distribution, when bin size is " + '%0.4i' % bin_size + "."], fmt='%s')

    return bin_value_histo, bin_value_gauss

# One can choose suitable bin size as per requirements.
# bin_sizes = [150, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3400, 3800, 4200, 4600]
# bin_sizes = [150, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
# bin_sizes = [150, 500, 1000, 1500, 2000, 2500, 3000, 3500]
bin_sizes = [150, 500, 2000, 3000, 3500]

# You may choose the following bin size for calculating mass values around bin size 150.
#bin_sizes = [149, 150]

# Create lists to store bin_size and difference values
bin_sizes_list = []
differences = []

for bin_size in bin_sizes:
    # print("Plotting histogram with bin size of", bin_size)
    print("The Z boson value in GeV for bin: ", bin_size)
    bin_value_histo, bin_value_gauss = plot_histogram("masses.txt", bin_size)
    bin_sizes_list.append(bin_size)
    differences.append(abs(bin_value_histo - bin_value_gauss))

# Plot the data
plt.plot(bin_sizes_list, differences)
plt.xlabel('Bin Sizes')
plt.ylabel('Absolute Diff between mass values: Histogram and Gaussian Distri.')
plt.title('Bin Size vs Absolute Diff among mass values')
plt.savefig("EffectOfBinSize.png", bbox_inches='tight')
print(" Till bin size 2000, we can observe very little difference among values for the Z-boson from the histogram and the gaussian distribution.")
print()
print("Beyond the 2000 bin sizeThere is a sharp rise among values for Z-boson from the histogram and the gaussian distribution.")
print()
print("It may not be recommended to choose a bin size beyond 2000.")

