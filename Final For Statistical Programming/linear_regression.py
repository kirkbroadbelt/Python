import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from math import nan
class SLR:
    def __init__(self, data):
        """ (SLR, Data) -> NoneType

        Create a new simple linear regression object from data,
        with data data, intercept beta0, and slope beta1.
        """
        self.data = data
        self.beta0 , self.beta1 = data.compute_least_squares_fit()
    
    def predict(self, x_new):
        """ (SLR, number) -> number

        Return predicted value at x_new.
        """
        return self.beta0 + self.beta1 * x_new 
        
    def compute_residuals(self):
        """ (SLR) -> list

        Return the residuals in a list of numbers.
        """
        residual_list = []
        for i in range(self.data.num_obs()):
            residual_list.append(self.data.y[i] - self.predict(self.data.x[i]))
        return residual_list

    def compute_SSResid(self):
        """ (SLR) -> number

        Return the sum of square residuals (SSResid).
        """
        SSResid = 0
        resids = self.compute_residuals()
        for i in range(len(resids)):
            SSResid = SSResid + (resids[i] ** 2)
        return SSResid
    
    def compute_residual_sd(self):
        """ (SLR) -> number

        Return the residual standard deviation.
        """
        return (self.compute_SSResid() / (self.data.num_obs() - 2) ) ** 0.5

    def compute_rsquared(self):
        """ (SLR) -> number

        Return the R-squared of the SLR fit.
        """
        #return (self.data.compute_SST() - self.compute_SSresid() ) / self.data.computeSST() 
        a = self.compute_SSResid()
        c = self.data.compute_SST()
        return((c-a)/(c))
    def __str__(self):
        """ (SLR) -> str

        Return a string representation of an SLR in this format:

        Least squares fit on 10 data points.
        Intercept = 45.584331
        Slope = 3.465523
        Residual standard deviation = 13.051139
        R-squared = 0.731364
        """
        #output_text =  'Least squares fit on {} data points.\n'.format(self.data.num_obs())
        #output_text += 'Intercept = {}\n'.format(self.beta0)
        #output_text += 'Slope = {}\n'.format(self.beta1)
        #output_text += 'Residual standard deviation = {}\n'.format(self.compute_residual_sd() )
        #output_text += 'R-squared = {}\n'.format(self.compute_rsquared())
        return 'Least squares fit on {} data points.\nIntercept = {:.6f}\nSlope = {:.6f}\nResidual standard deviation = {:.6f}\nR-squared = {:.6f}'.format(self.data.num_obs(),self.beta0,self.beta1,self.compute_residual_sd(),self.compute_rsquared())
        
    def plot(self):
        """ (SLR) -> None

        Produce a scatter plot of the data and
        the simple linear regression model.
        """
        plt.plot(self.data.x, self.data.y, marker = '^', color = 'b', linewidth = 0)
        xMax = max(self.data.x)
        xMin = min(self.data.x)
        xRange = np.arange(xMin, xMax, .1)
        plt.plot(xRange, self.beta0 + self.beta1 * xRange, color = 'k')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()


    def compute_test_statistic(self):
        """ (SLR) -> float

        Returns the t-statistic for the slope parameter.
        """
        try:
            x_sample_mean , y_sample_mean = self.data.compute_sample_means()
            Sxx = 0
            for i in range(len(self.data.x)):
                Sxx += (self.data.x[i] - x_sample_mean) ** 2
            return self.beta1 / (self.compute_residual_sd() / (Sxx ** 0.5))
        except    ZeroDivisionError:
            print('Standard error of the slope is zero.')
            return nan         
        

    def compute_p_value(self):
        """ (SLR) -> float

        Returns the p-value for the slope parameter.
        """
        return stats.t.cdf(self.compute_test_statistic(), self.data.numobs() - 2)
        

    def t_test_two_tailed(self, alpha):
        """ (SLR, float) -> str

        Performs a two-tailed t-test on the slope parameter.
        """
        p_value = self.compute_p_value()
        
        try: 
            if alpha > 0 and alpha < 1:
                pass
            else:
                raise ValueError('Inputed significance level is  not supported.')
            if p_value <= alpha:
                print('There is a statistically significant association at the alpha level of {}.'.format(alpha))
                return 'There is a statistically significant association at the alpha level of {}.'.format(alpha)
            else:
                print('There is not a statistically significant association at the alpha level of {}.'.format(alpha))
                return('There is not a statistically significant association at the alpha level of {}.'.format(alpha))
        except ZeroDivisionError:
            print('Standard error of the slope is zero.')
            print('Test statistic cannot be computed.')
            return('Test statistic cannot be computed.')
        except ValueError as excpt:
            print(excpt)
            return 'Inputed significance level is  not supported.'