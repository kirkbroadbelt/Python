class Data:
    def __init__(self, x, y):
        """ (Data, list, list) -> NoneType

        Create a new data object with two attributes: x and y.
        """
        self.x = x
        self.y = y

    def num_obs(self):
        """ (Data) -> int

        Return the number of observations in the data set.

        >>> data = Data([1, 2], [3, 4])
        >>> data.num_obs()
        2
        """
        return len(self.x)

    def __str__(self):
        """ (Data) -> str
        Return a string representation of this Data in this format:
        x	        y
        18.000          120.000
        20.000          110.000
        22.000          120.000
        25.000          135.000
        26.000          140.000
        29.000          115.000
        30.000          150.000
        33.000          165.000
        33.000          160.000
        35.000          180.000
        """
        output = ''
        output = output + 'x\t\ty\n'
        for i in range(len(self.x)):
            output = output + '{0:.3f\t\t{1:.3f}\n'.format(self.x[i], self.y[i])
        return output

    def compute_sample_means(self):
        """ (Data) -> number, number

        Return sample mean of x and sample mean of y.
        """
        
        meanx = sum(self.x)/(len(self.x))
        meany = sum(self.y)/(len(self.y))
        return (meanx, meany)

    def compute_least_squares_fit(self):
        """ (Data) -> number, number

        Return the intercept and slope of the simple linear regression fit
        of the data.
        """
    
        Sxx = 0
        Sxy = 0 
        meanx, meany = self.compute_sample_means()
        for i in range(len(self.x)):
            Sxx += (self.x[i] - meanx)**2
            Sxy += ((self.x[i] - meanx) * (self.y[i] - meany))
        
        beta1 =  Sxy / Sxx
        beta0 = meany -(beta1 * meanx)
        
        return(beta0, beta1)

    def compute_SST(self):
        """ (Data) -> number

        Return the sum of squares total (SST).
        """
        SST = 0
        meanx, meany = self.compute_sample_means()
        for i in range(len(self.x)):
            SST += (self.y[i] - meany) ** 2
        return SST