##ifndef ARMA_INCLUDE_H_
##define ARMA_INCLUDE_H_


#if defined __USE_R_INCLUDES__
#include "RcppArmadillo.h"
#define COUT = Rcpp::Rcout
#else
#include "Armadillo.h"
#define COUT = std::cout
#endif

##endif