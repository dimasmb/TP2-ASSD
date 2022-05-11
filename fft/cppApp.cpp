using namespace std;

#include <iostream>
#include <fstream>
#include <vector>
#include <complex>
#include "fft.h"


////////////
// Main   //
///////////

int main() {
  
   // File to Export Data

   std::ofstream fptr;
   fptr.open("dataSet.txt");
   std::ofstream outputDataSet;
   outputDataSet.open("outputDataSet.txt");

   // Definition of Sample Function in Time

   std::vector<complex<double> > out (SAMPLE_SIZE);
   std::vector<complex<double> > sampleSignal (SAMPLE_SIZE);

   // Number of sample points

   size_t N = SAMPLE_SIZE;

   // Signal Frequency and Amplitude for Sine

   //////////////////////////////////////////////////////////////////

   // MODIFY THIS IS IN ORDER TO GENERATE A DIFFERENT SIN FUNCTION //

   float signalF = 500;
   float amplitude = 1;

   //////////////////////////////////////////////////////////////////

   // Sample spacing

   float F = 800;
   float T = 1.0 / F;

   // Signal DataSet Creator for Sine Wave

   for (int i = 0; i < N; i++) {
      sampleSignal[i] = sin(500.0 * 2 * PI * T * i);;
      //sampleSignal[i] = sin( 50.0 * 2 * PI * T * i ) + 0.5*sin( 80 * 2 * PI * T * i ) + 0.25*sin( 160.0 * 2 * PI * T * i );;
		//sampleSignal[i] =  sin( 200.0 * 2 * PI * T * i ) + sin( 100 * 2 * PI * T * i )+sin( 50.0 * 2 * PI * T * i ) + sin( 25 * 2 * PI * T * i );;
	}
   

   //////////////
   // FFT Test //
   /////////////

   fft (sampleSignal, out, N);

   
   
   // Export data to be compared and plotted in Python in Time

   for(int loop = 0; loop < SAMPLE_SIZE; loop++){
      
      if (loop == 0) {
         fptr << F << "\n" ;
      }

      fptr << sampleSignal[loop].real();

      if (loop < SAMPLE_SIZE - 1) {
         fptr << ",";
      }
   }

   fptr.close();

   // Export data to be compared and plotted in Python in Freq

   for(int loop = 0; loop < SAMPLE_SIZE; loop++){
      
      outputDataSet << abs(out[loop]);

      if (loop < SAMPLE_SIZE - 1) {
         outputDataSet << ",";
      }
   }
   outputDataSet.close();
   return 0;
}

