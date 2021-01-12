#include <iostream>
#include <Eigen/Dense>

// I'm using the Eigen C++ library here, which has a lot of tools for matrix multiplication and
// accessing entries of matrices

#define PathLength 5
#define numVert 8

using namespace Eigen;
using namespace std;

// Matrix Intersection:
// pre: two matrices with integer entries are passes into the method
// post: returns a matrix where the only entries are those the two input matrices had in common

Matrix<int, numVert, numVert> matIntersect(Matrix<int, numVert, numVert> a, Matrix<int, numVert,
                                       numVert> b) {
    Matrix<int, numVert, numVert> product;
    for (size_t x = 0; x < numVert; ++x) {
        for (size_t y = 0; y < numVert; ++y) {
            if (a(x, y) == b(x, y)) {
                product(x, y) = a(x, y);
            }
            else {
                product(x, y) = 0;
            }
        }
    }
    return product;
}

// pathCounter
// pre: a matrix and a desired path length
// post: returns matrix which contains all of the paths (and only paths, not walks) of a certain
// length
// Notes: This is a recursive function based on the equation P_{n} = c(AP_{n-1} n P_{n-1}A),
// where c(A) clears the main diagonal of the matrix A and P_{2} = c(A^{2}). The recursive strategy
// is take the path matrix from the previous step, and apend an edge to the end of the path or
// append the path to an existing edge. If the result is truly a path, it should show up in both
// matrices, and so we keep it. Otherwise, that entry is sent to zero.

Matrix<int, numVert, numVert> pathCounter(Matrix<int, numVert, numVert> a, size_t length) {
    MatrixXi paths;
    if (length == 1) {                           // Base case for paths of length 1
        MatrixXi tmp1 = a;
        tmp1.diagonal().setZero();
        return tmp1;
    }
    if (length == 2) {                           // Base case for paths of length 2
        MatrixXi tmp2 = a * a;
        tmp2.diagonal().setZero();
        return tmp2;
    }
    else {
        MatrixXi prevStep = pathCounter(a, length - 1);
        MatrixXi rightMult = prevStep * a;
        MatrixXi leftMult = a * prevStep;
        paths = matIntersect(leftMult, rightMult);
        paths.diagonal().setZero();
        return paths;
    }
}

bool isValid(size_t newX, size_t newY) {
    return ((newX != newY) && (0 <= newX) && (newX < numVert) && (0 <= newY) && (newY < numVert));
}

void populate(Matrix<int, numVert, numVert> a, size_t curX, size_t curY) {
    if (isValid(curX, curY)) {
        a(curX, curY) = 1;
    }
    populate(a, curX + 1, curY);
    populate(a, curX + 1, curY + 1);
    populate(a, curX, curY + 1);
    populate(a, curX - 1, curY + 1);
    populate(a, curX - 1, curY);
    populate(a, curX - 1, curY - 1);
    populate(a, curX, curY - 1);
    populate(a, curX + 1, curY - 1);
}

// main function
// Implements the methods above
int main() {
    MatrixXi m(numVert, numVert);
    m.setZero();

    return 0;
}
