# -\*- coding: utf-8 -\*-

r"""
sample_nmr_spectra.py - This file is part of pygmca.
The pygmca package aims at performing non-negative matrix factorization.
This module provides synthetic NMR spectra.
Copyright 2014 CEA
Contributor : Jérémy Rapin (jeremy.rapin.math@gmail.com)
Created on December 13, 2014, last modified on December 14, 2014

This software is governed by the CeCILL  license under French law and
abiding by the rules of distribution of free software.  You can  use,
modify and/ or redistribute the software under the terms of the CeCILL
license as circulated by CEA, CNRS and INRIA at the following URL
"http://www.cecill.info".

As a counterpart to the access to the source code and  rights to copy,
modify and redistribute granted by the license, users are provided only
with a limited warranty  and the software's author,  the holder of the
economic rights,  and the successive licensors  have only  limited
liability.

In this respect, the user's attention is drawn to the risks associated
with loading,  using,  modifying and/or developing or reproducing the
software by the user in light of its specific status of free software,
that may mean  that it is complicated to manipulate,  and  that  also
therefore means  that it is reserved for developers  and  experienced
professionals having in-depth computer knowledge. Users are therefore
encouraged to load and test the software's suitability as regards their
requirements in conditions enabling the security of their systems and/or
data to be ensured and,  more generally, to use and operate it in the
same conditions as regards security.

The fact that you are presently reading this means that you have had
knowledge of the CeCILL license and that you accept its terms.
"""

__version__ = "1.0"
__author__ = "Jeremy Rapin"
__url__ = "http://www.cosmostat.org/GMCALab.html"
__copyright__ = "(c) 2014 CEA"
__license__ = "CeCill"

import numpy as np

peak_list = {}
# arrays are num_peaks x (ppm, amplitude)

peak_list["quinine"] = np.array([[8.430, 174],
                                 [8.418, 182],
                                 [7.881, 168],
                                 [7.858, 182],
                                 [7.449, 149],
                                 [7.437, 146],
                                 [7.269, 97],
                                 [7.262, 124],
                                 [7.246, 71],
                                 [7.239, 141],
                                 [7.229, 185],
                                 [7.222, 124],
                                 [5.755, 35],
                                 [5.735, 39],
                                 [5.729, 43],
                                 [5.711, 64],
                                 [5.693, 46],
                                 [5.686, 47],
                                 [5.667, 43],
                                 [5.489, 86],
                                 [5.482, 89],
                                 [5.379, 71],
                                 [4.959, 103],
                                 [4.916, 99],
                                 [4.913, 86],
                                 [4.910, 97],
                                 [4.907, 109],
                                 [4.881, 95],
                                 [3.878, 1000],
                                 [3.461, 35],
                                 [3.460, 35],
                                 [3.455, 38],
                                 [3.449, 37],
                                 [3.449, 37],
                                 [3.067, 85],
                                 [3.042, 68],
                                 [3.033, 69],
                                 [3.007, 60],
                                 [2.641, 53],
                                 [2.630, 66],
                                 [2.624, 56],
                                 [2.607, 74],
                                 [2.601, 72],
                                 [2.600, 72],
                                 [2.597, 71],
                                 [2.235, 42],
                                 [2.235, 42],
                                 [2.234, 42],
                                 [2.233, 42],
                                 [1.786, 71],
                                 [1.781, 79],
                                 [1.773, 66],
                                 [1.767, 58],
                                 [1.745, 59],
                                 [1.732, 71],
                                 [1.714, 80],
                                 [1.689, 31],
                                 [1.688, 31],
                                 [1.504, 38],
                                 [1.503, 38],
                                 [1.497, 43],
                                 [1.473, 76],
                                 [1.459, 50],
                                 [1.455, 53],
                                 [1.454, 53],
                                 [1.449, 47],
                                 [1.448, 47]])

peak_list["mannitol"] = np.array([[4.432, 965],
                                  [4.418, 1000],
                                  [4.362, 382],
                                  [4.347, 917],
                                  [4.333, 409],
                                  [4.163, 772],
                                  [4.145, 819],
                                  [3.637, 164],
                                  [3.629, 191],
                                  [3.623, 172],
                                  [3.614, 225],
                                  [3.610, 236],
                                  [3.602, 224],
                                  [3.596, 215],
                                  [3.587, 217],
                                  [3.562, 236],
                                  [3.543, 470],
                                  [3.524, 357],
                                  [3.485, 104],
                                  [3.476, 112],
                                  [3.470, 212],
                                  [3.462, 212],
                                  [3.456, 198],
                                  [3.449, 217],
                                  [3.441, 128],
                                  [3.435, 110],
                                  [3.427, 101],
                                  [3.408, 263],
                                  [3.394, 343],
                                  [3.381, 275],
                                  [3.366, 299],
                                  [3.352, 148]])

peak_list["menthone"] = np.array([[2.375, 84],
                                  [2.370, 91],
                                  [2.366, 102],
                                  [2.360, 99],
                                  [2.343, 108],
                                  [2.338, 102],
                                  [2.333, 125],
                                  [2.328, 127],
                                  [2.170, 41],
                                  [2.166, 57],
                                  [2.153, 85],
                                  [2.149, 79],
                                  [2.139, 70],
                                  [2.136, 111],
                                  [2.132, 66],
                                  [2.119, 90],
                                  [2.115, 70],
                                  [2.107, 36],
                                  [2.106, 37],
                                  [2.102, 50],
                                  [2.097, 34],
                                  [2.095, 37],
                                  [2.089, 58],
                                  [2.085, 56],
                                  [2.081, 99],
                                  [2.075, 89],
                                  [2.067, 183],
                                  [2.057, 172],
                                  [2.054, 176],
                                  [2.053, 166],
                                  [2.048, 130],
                                  [2.045, 114],
                                  [2.040, 59],
                                  [2.035, 94],
                                  [2.031, 109],
                                  [2.024, 127],
                                  [2.021, 132],
                                  [2.015, 43],
                                  [1.993, 190],
                                  [1.990, 190],
                                  [1.961, 157],
                                  [1.958, 147],
                                  [1.942, 30],
                                  [1.936, 36],
                                  [1.935, 37],
                                  [1.931, 53],
                                  [1.926, 65],
                                  [1.922, 87],
                                  [1.920, 82],
                                  [1.917, 84],
                                  [1.914, 81],
                                  [1.908, 72],
                                  [1.902, 53],
                                  [1.899, 68],
                                  [1.893, 98],
                                  [1.885, 80],
                                  [1.879, 64],
                                  [1.876, 47],
                                  [1.870, 67],
                                  [1.864, 44],
                                  [1.859, 56],
                                  [1.854, 56],
                                  [1.849, 42],
                                  [1.844, 52],
                                  [1.839, 45],
                                  [1.833, 33],
                                  [1.828, 38],
                                  [1.409, 59],
                                  [1.406, 47],
                                  [1.402, 73],
                                  [1.390, 33],
                                  [1.381, 101],
                                  [1.378, 151],
                                  [1.376, 169],
                                  [1.370, 116],
                                  [1.365, 83],
                                  [1.363, 79],
                                  [1.358, 124],
                                  [1.354, 92],
                                  [1.351, 93],
                                  [1.342, 40],
                                  [1.340, 37],
                                  [1.338, 44],
                                  [1.333, 60],
                                  [1.331, 59],
                                  [1.326, 33],
                                  [1.022, 882],
                                  [1.006, 968],
                                  [0.992, 41],
                                  [0.933, 57],
                                  [0.923, 985],
                                  [0.906, 986],
                                  [0.893, 37],
                                  [0.884, 32],
                                  [0.882, 32],
                                  [0.863, 981],
                                  [0.846, 1000]])

peak_list["caffein"] = np.array([[7.512, 96],
                                 [7.510, 95],
                                 [3.997, 523],
                                 [3.996, 507],
                                 [3.583, 1000],
                                 [3.406, 998]])

peak_list["saccharose"] = np.array([[5.423, 308],
                                    [5.414, 314],
                                    [4.232, 391],
                                    [4.210, 506],
                                    [4.076, 207],
                                    [4.055, 344],
                                    [4.034, 198],
                                    [3.918, 80],
                                    [3.909, 96],
                                    [3.903, 166],
                                    [3.897, 84],
                                    [3.893, 140],
                                    [3.888, 97],
                                    [3.882, 135],
                                    [3.873, 138],
                                    [3.861, 149],
                                    [3.854, 140],
                                    [3.848, 99],
                                    [3.847, 99],
                                    [3.845, 98],
                                    [3.830, 862],
                                    [3.823, 854],
                                    [3.815, 550],
                                    [3.799, 55],
                                    [3.789, 181],
                                    [3.764, 267],
                                    [3.741, 231],
                                    [3.680, 1000],
                                    [3.580, 235],
                                    [3.570, 228],
                                    [3.555, 183],
                                    [3.545, 187],
                                    [3.498, 200],
                                    [3.474, 279],
                                    [3.450, 136]])

peak_list["phenylalanine"] = np.array([[7.467, 187],
                                       [7.463, 334],
                                       [7.459, 165],
                                       [7.451, 239],
                                       [7.446, 880],
                                       [7.442, 612],
                                       [7.431, 406],
                                       [7.428, 950],
                                       [7.426, 672],
                                       [7.422, 207],
                                       [7.414, 50],
                                       [7.409, 214],
                                       [7.405, 475],
                                       [7.401, 365],
                                       [7.396, 67],
                                       [7.393, 143],
                                       [7.387, 514],
                                       [7.379, 148],
                                       [7.372, 141],
                                       [7.368, 231],
                                       [7.363, 823],
                                       [7.359, 1000],
                                       [7.353, 251],
                                       [7.347, 348],
                                       [7.343, 640],
                                       [4.019, 471],
                                       [4.006, 525],
                                       [3.999, 536],
                                       [3.992, 52],
                                       [3.986, 505],
                                       [3.339, 221],
                                       [3.326, 216],
                                       [3.302, 328],
                                       [3.289, 309],
                                       [3.154, 365],
                                       [3.133, 351],
                                       [3.117, 252],
                                       [3.097, 236]])

peak_list["lactose"] = np.array([[6.342, 670],
                                 [6.331, 662],
                                 [5.107, 510],
                                 [5.097, 510],
                                 [4.908, 407],
                                 [4.898, 618],
                                 [4.888, 420],
                                 [4.793, 354],
                                 [4.785, 361],
                                 [4.707, 45],
                                 [4.685, 345],
                                 [4.670, 565],
                                 [4.659, 606],
                                 [4.646, 292],
                                 [4.627, 43],
                                 [4.621, 55],
                                 [4.564, 41],
                                 [4.564, 41],
                                 [4.537, 460],
                                 [4.525, 468],
                                 [4.507, 79],
                                 [4.494, 262],
                                 [4.479, 562],
                                 [4.467, 1000],
                                 [4.205, 41],
                                 [4.204, 42],
                                 [4.203, 42],
                                 [4.202, 43],
                                 [4.185, 481],
                                 [4.166, 480],
                                 [4.154, 41],
                                 [4.148, 41],
                                 [3.725, 175],
                                 [3.716, 368],
                                 [3.708, 244],
                                 [3.700, 206],
                                 [3.691, 390],
                                 [3.684, 282],
                                 [3.674, 66],
                                 [3.670, 69],
                                 [3.647, 593],
                                 [3.634, 790],
                                 [3.625, 840],
                                 [3.594, 71],
                                 [3.589, 64],
                                 [3.578, 284],
                                 [3.567, 142],
                                 [3.555, 668],
                                 [3.541, 361],
                                 [3.531, 560],
                                 [3.516, 362],
                                 [3.498, 387],
                                 [3.485, 326],
                                 [3.471, 216],
                                 [3.459, 721],
                                 [3.445, 457],
                                 [3.429, 244],
                                 [3.413, 115],
                                 [3.406, 101],
                                 [3.402, 95],
                                 [3.400, 93],
                                 [3.397, 90],
                                 [3.393, 85],
                                 [3.392, 84],
                                 [3.391, 82],
                                 [3.389, 80],
                                 [3.387, 79],
                                 [3.383, 76],
                                 [3.380, 73],
                                 [3.377, 72],
                                 [3.376, 71],
                                 [3.374, 69],
                                 [3.374, 69],
                                 [3.373, 69],
                                 [3.372, 69],
                                 [3.370, 68],
                                 [3.369, 68],
                                 [3.368, 67],
                                 [3.367, 67],
                                 [3.366, 67],
                                 [3.364, 66],
                                 [3.363, 66],
                                 [3.362, 65],
                                 [3.361, 64],
                                 [3.354, 109],
                                 [3.343, 90],
                                 [3.330, 351],
                                 [3.313, 816],
                                 [3.285, 495],
                                 [3.263, 564],
                                 [3.239, 331],
                                 [3.194, 148],
                                 [3.180, 215],
                                 [3.171, 257],
                                 [3.162, 198],
                                 [3.148, 135]])

peak_list["ascorbic acid"] = np.array([[8.309, 81],
                                       [4.857, 52],
                                       [4.786, 32],
                                       [4.785, 32],
                                       [4.783, 31],
                                       [4.781, 31],
                                       [4.723, 988],
                                       [4.720, 1000],
                                       [3.754, 133],
                                       [3.751, 134],
                                       [3.735, 321],
                                       [3.731, 222],
                                       [3.719, 167],
                                       [3.715, 169],
                                       [3.477, 66],
                                       [3.461, 103],
                                       [3.451, 561],
                                       [3.446, 533],
                                       [3.435, 432],
                                       [3.426, 429],
                                       [3.420, 118],
                                       [3.400, 77]])

peak_list["citric acid"] = np.array([[2.783, 570],
                                     [2.745, 1000],
                                     [2.677, 994],
                                     [2.638, 559]])

peak_list["sodium p-hydroxybenzoate"] = np.array([[7.808, 919],
                                                  [7.787, 1000],
                                                  [6.743, 991],
                                                  [6.722, 1000]])

peak_list["fruit alcohol"] = np.array([[12.420, 116],
                                       [4.286, 727],
                                       [4.275, 822],
                                       [4.267, 892],
                                       [4.255, 770],
                                       [2.648, 658],
                                       [2.636, 684],
                                       [2.609, 995],
                                       [2.597, 970],
                                       [2.481, 1000],
                                       [2.462, 970],
                                       [2.442, 660],
                                       [2.423, 661]])

peak_list["folic acid"] = np.array([[8.676, 1000],
                                    [8.186, 313],
                                    [8.167, 315],
                                    [7.690, 717],
                                    [7.668, 761],
                                    [6.975, 333],
                                    [6.680, 726],
                                    [6.658, 722],
                                    [4.522, 519],
                                    [4.508, 514],
                                    [4.377, 138],
                                    [4.369, 164],
                                    [4.366, 184],
                                    [4.358, 174],
                                    [4.354, 168],
                                    [4.353, 168],
                                    [4.346, 147],
                                    [2.365, 301],
                                    [2.347, 655],
                                    [2.328, 374],
                                    [2.084, 139],
                                    [2.065, 165],
                                    [1.937, 143]])

peak_list["taurine"] = np.array([[3.818, 1000],
                                 [3.619, 80],
                                 [3.602, 181],
                                 [3.585, 102],
                                 [3.352, 106],
                                 [3.336, 195],
                                 [3.319, 81]])

peak_list["cholesterol"] = np.array([[5.356, 88],
                                     [5.351, 67],
                                     [5.348, 65],
                                     [5.343, 81],
                                     [3.538, 31],
                                     [3.534, 45],
                                     [3.524, 54],
                                     [3.521, 55],
                                     [3.511, 45],
                                     [3.507, 35],
                                     [3.494, 30],
                                     [2.270, 79],
                                     [1.996, 99],
                                     [1.854, 154],
                                     [1.830, 157],
                                     [1.494, 183],
                                     [1.329, 124],
                                     [1.100, 168],
                                     [1.007, 1000],
                                     [0.923, 498],
                                     [0.907, 465],
                                     [0.876, 764],
                                     [0.871, 757],
                                     [0.859, 717],
                                     [0.855, 699],
                                     [0.692, 42],
                                     [0.678, 927]])

peak_list["adenosine"] = np.array([[8.382, 942],
                                   [8.182, 38],
                                   [8.181, 39],
                                   [8.168, 1000],
                                   [7.409, 448],
                                   [5.915, 431],
                                   [5.900, 439],
                                   [5.510, 388],
                                   [5.495, 475],
                                   [5.483, 194],
                                   [5.472, 134],
                                   [5.250, 333],
                                   [5.239, 330],
                                   [4.663, 103],
                                   [4.648, 221],
                                   [4.635, 222],
                                   [4.620, 101],
                                   [4.187, 111],
                                   [4.176, 215],
                                   [4.169, 218],
                                   [4.157, 109],
                                   [4.006, 119],
                                   [3.998, 304],
                                   [3.990, 296],
                                   [3.982, 118],
                                   [3.724, 67],
                                   [3.714, 113],
                                   [3.705, 80],
                                   [3.693, 120],
                                   [3.690, 110],
                                   [3.684, 178],
                                   [3.675, 101],
                                   [3.607, 96],
                                   [3.598, 114],
                                   [3.589, 115],
                                   [3.589, 115],
                                   [3.579, 128],
                                   [3.568, 79],
                                   [3.559, 77],
                                   [3.550, 63]])

peak_list["myo-inositol"] = np.array([[4.073, 326],
                                      [4.066, 661],
                                      [4.058, 401],
                                      [3.654, 465],
                                      [3.629, 1000],
                                      [3.615, 43],
                                      [3.605, 919],
                                      [3.574, 22],
                                      [3.571, 23],
                                      [3.568, 25],
                                      [3.567, 25],
                                      [3.555, 926],
                                      [3.548, 938],
                                      [3.530, 507],
                                      [3.523, 554],
                                      [3.305, 414],
                                      [3.282, 641],
                                      [3.259, 306]])

peak_list["oleic acid"] = np.array([[5.361, 102],
                                    [5.359, 81],
                                    [5.352, 131],
                                    [5.347, 237],
                                    [5.345, 243],
                                    [5.339, 138],
                                    [5.338, 138],
                                    [5.333, 81],
                                    [5.330, 109],
                                    [2.365, 171],
                                    [2.346, 306],
                                    [2.327, 202],
                                    [2.019, 261],
                                    [2.005, 246],
                                    [1.990, 111],
                                    [1.650, 101],
                                    [1.633, 150],
                                    [1.614, 127],
                                    [1.599, 61],
                                    [1.596, 62],
                                    [1.311, 812],
                                    [1.289, 540],
                                    [1.268, 1000],
                                    [0.898, 250],
                                    [0.881, 774],
                                    [0.863, 303]])

peak_list["glycerol"] = np.array([[4.485, 411],
                                  [3.480, 72],
                                  [3.466, 238],
                                  [3.453, 453],
                                  [3.439, 346],
                                  [3.426, 203],
                                  [3.405, 624],
                                  [3.392, 316],
                                  [3.378, 1000],
                                  [3.365, 712],
                                  [3.340, 34],
                                  [3.327, 993],
                                  [3.312, 744],
                                  [3.300, 574],
                                  [3.285, 435]])


def get_nmr_spectrum(peak_list, ppm_range,
                     num_samples=2048, peak_width=4):
    r"""
    Creates a synthetic NMR spectrum from a list of peaks.
    
    Inputs
    ------
    - peak_list: numpy array
        list of peaks under array form, with first column the location in ppm,
        and second column the intensity.
    - ppm_range: tuple
        Range of ppm for the location of the peaks (typically (0, 10)).
    - num_samples (default: 2048): int
        number of samples of the spectrum.
    - peak_width (default: 4): float
        width of the Laplacian kernel used to convolve with the peaks.
    """
    ppm = np.array(range(0, num_samples), dtype=np.float64)
    ppm *= float(max(ppm_range) - min(ppm_range)) / (num_samples - 1)
    ppm +=  min(ppm_range)
    spectrum = 0 * ppm
    # add peaks
    for npeak in range(0, peak_list.shape[0]):
        ind = np.where(abs(ppm - peak_list[npeak, 0]) ==
                      min(abs(ppm - peak_list[npeak, 0])));
        spectrum[ind[0]] += peak_list[npeak, 1];
    # convolve
    half = int(num_samples / 2);
    kern = np.array(range(0, num_samples)).astype(np.float64) - half
    mu = 0.5 * peak_width / np.log(2);
    kern = np.exp(-abs(kern) / mu);
    spectrum = np.convolve(spectrum, kern, mode='same')
    return (spectrum, ppm)
