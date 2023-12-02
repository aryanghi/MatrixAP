//
//  var.h
//  code
//
//  Created by macuser on 12/3/23.
//

#include <iostream>
#include <cmath>

double calculateVariance(const double* data, int size) {
    if (size <= 1) {
        std::cerr << "Variance calculation requires at least two data points." << std::endl;
        return 0.0; // or handle error appropriately
    }

    // Calculate the mean
    double mean = 0.0;
    for (int i = 0; i < size; ++i) {
        mean += data[i];
    }
    mean /= size;

    // Calculate the sum of squared differences from the mean
    double sumSquaredDiff = 0.0;
    for (int i = 0; i < size; ++i) {
        sumSquaredDiff += std::pow(data[i] - mean, 2);
    }

    // Divide by the number of elements - 1 to get the variance for sample data
    int divisor = size - 1;

    // Calculate the variance
    double variance = sumSquaredDiff / divisor;

    return variance;
}



double calculateStd(const double* data, int size) {
    if (size <= 0) {
        std::cerr << "Standard deviation calculation requires a non-empty array." << std::endl;
        return 0.0; // or handle error appropriately
    }

    // Calculate the mean
    double mean = 0.0;
    for (int i = 0; i < size; ++i) {
        mean += data[i];
    }
    mean /= size;

    // Calculate the sum of squared differences from the mean
    double sumSquaredDiff = 0.0;
    for (int i = 0; i < size; ++i) {
        sumSquaredDiff += std::pow(data[i] - mean, 2);
    }

    // Divide by the number of elements and take the square root
    double stdDeviation = std::sqrt(sumSquaredDiff / size);

    return stdDeviation;
}

