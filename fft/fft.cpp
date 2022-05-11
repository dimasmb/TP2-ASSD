#include "fft.h"


//////////////////////////
// Function Definitions //
//////////////////////////

void fft(std::vector<complex<double> >&  in, std::vector<complex<double> >&  out, size_t n) {
   
   vector<complex<double> > dataSetInTime(n);
   vector<complex<double> > dataSetFFT(n);

   for (size_t i = 0; i < n; i++)
      dataSetInTime[i] = in[i];

   dataSetFFT = cooleyTukeyAlgorithm(dataSetInTime);

   for (size_t i = 0; i < n; i++)
      out[i] = dataSetFFT[i];

}


std::vector<complex<double> > cooleyTukeyAlgorithm(std::vector<complex<double> >& sampleSignal) {
   
   int N = sampleSignal.size();

   if (N == 1){
      return sampleSignal;
   }

   else {

      int M = N/2;
      

      std::vector<complex<double> > even(M);
      std::vector<complex<double> > odd(M);

      for (int i = 0; i != M; i++) {
       
         even[i] = sampleSignal[2 * i];
         odd[i] = sampleSignal[2 * i + 1];
      
      }

      std::vector<complex<double> > Xeven(M);
      std::vector<complex<double> > Xodd(M);
      
      
      Xeven = cooleyTukeyAlgorithm(even);
      Xodd = cooleyTukeyAlgorithm(odd);

      std::vector<complex<double> > bins (N);
      
      for (int k = 0; k != N/2; k++) {

         complex<double> Wnk = polar(1.0,-2 * PI * k / N);
         complex<double> WnkTimesXodd = Wnk * Xodd[k];

         bins[k] = Xeven[k] + WnkTimesXodd;
         bins[k + N / 2] = Xeven[k] - WnkTimesXodd;
         
      }

      return bins;
    
    }
}
