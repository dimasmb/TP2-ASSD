#include <iostream>
#include <fstream>
#include <vector>
#include <complex>
using namespace std;

#define SAMPLE_SIZE 4096
#define PI 3.141592

///////////////////////////
// Function Prototypes   //
///////////////////////////

void fft(std::vector<complex<double> >&  in, std::vector<complex<double> >&  out, size_t n);
std::vector<complex<double> > cooleyTukeyAlgorithm(std::vector<complex<double> >& sampleSignal);


