# school_data.py
# Tobin Eberle
#
# A terminal-based application for computing and printing statistics based on given input.

import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

#Declare any global variables needed to store the data here:

#List of the arrays imported from given_data
given_data_list = [year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022]

#Dictionary of codes:schools
school_dict = {1224:"Centennial High School",
               1679:"Robert Thirsk School",
               9626:"Louise Dean School",
               9806:"Queen Elizabeth High School",
               9813:"Forest Lawn High School",
               9815:"Crescent Heights High School",
               9816:"Western Canada High School",
               9823:"Central Memorial High School",
               9825:"James Fowler High School",
               9826:"Ernest Manning High School",
               9829:"William Aberhart High School",
               9830:"National Sport School",
               9836:"Henry Wise Wood High School",
               9847:"Bowness High School",
               9850:"Lord Beaverbrook High School",
               9856:"Jack James High School",
               9857:"Sir Winston Churchill High School",
               9858:"Dr. E. P. Scarlett High School",
               9860:"John G Diefenbaker High School",
               9865:"Lester B. Pearson High School"
               }

#User defined functions and classes here:

def reshapeSchoolData(data_list):
    """Turns nans to 0 and reshapes the 1D school data into the folling 3D format:
    [year][school][enrollment] 

    Params:
        data_list: the given school data list
    
    Returns:
        a 3D np.array object 
    """

    #Reshape 1D array -> 2D
    list2D = [item.reshape(20,3) for item in data_list]
    #Return the 2D array as an array for 3D
    shape3D = np.array(list2D)
    #Mask to return nans to 0:
    shape3D[np.isnan(shape3D)] = 0

    return shape3D

def reshapeSchoolDataMeans(data_list):
    """Repalces nans with mean values for the specific grade/year and reshapes the 1D school data into the folling 3D format:
    [year][school][enrollment]

    Params:
        data_list: the given school data list
    
    Returns:
        a 3D np.array object 
    """

    #Reshape 1D array -> 2D
    list2D = [item.reshape(20,3) for item in data_list]

    #Check for nan values, if they exist use a mask to replace them with the mean
    for array2D in list2D:
        if np.isnan(array2D).any():
            #nanmean axis = 0, calculates the mean of the columns that include a nan and replace it with the mean value
            array2D[np.isnan(array2D)]  = np.nanmean(array2D, axis = 0)

    #Return the 2D array as an array for 3D
    shape3D = np.array(list2D)
    return shape3D

#Note: probably don't need to use a  class for SchoolStats or GeneralStats, it was just easier to store/reference the isntance variables for this project
class SchoolStats:
    """Class to access school data and perform analytics
       Data is sorted by [years][school][grade]

    Params:
        code: school code
        name: school name
        idx: position of the school data in the array
        array_3D: the 3D array to work on

    """

    def __init__(self, code, array_3D):
        self.code = code
        self.name = school_dict[code]
        self.idx = list(school_dict.keys()).index(code)
        self.array_3D = array_3D

    def meanEnrollment(self, grade = 0):
        """
        Calculates the mean enrollment for a specific grade over all years

        params:
            grade: the specified grade
            
        
        returns:
            float represeting mean enrollment fora grade
        """
        return self.array_3D[:,self.idx,(grade - 10)].mean()

    def highestEnrollment(self):
        '''
        Calculates highest enrollment over all years

        returns:
            float representing max enrollment
        '''
        return np.max(self.array_3D[:, self.idx, :])
    
    def lowestEnrollment(self):
        '''
        Calculates lowest enrollment over all years

        returns:
            float representing minimum enrollment
        '''
        return np.min(self.array_3D[:, self.idx, :])
        
    def totalEnrollment(self, year):
        '''
        Calculates total enrollment for specified year

        params:
            year: specified year

        returns:
            float representing sum of yearly enrollment
        '''
        year = year - 2013
        return np.sum(self.array_3D[year, self.idx, :])
    
    def medianTotalEnrollment(self):
        '''
        Calculates the median total enrollment over all years
        for enrollements of over 500 and prints. Otherwise prints error

        '''
        #Mask whether any data is > 500 and count the resulting true/false
        if np.count_nonzero(self.array_3D[:, self.idx, :] > 500) == 0:
            print("No enrollments over 500.")
        else:
            x = self.array_3D[:, self.idx, :]
            #Use a mask to print the median
            print("For all enrollments over 500, the median value was:", np.median(x[x > 500]).astype(int))

    def meanTotalEnrollment(self):
        '''
        Calculates the mean total enrollment over all years

        returns:
            float representing the mean value of enrollment over 10 years
        
        '''
        x = []
        #Self reference the totalEnrollment and add them to a list
        for year in range(2013,2023):
            x.append(self.totalEnrollment(year))
        #Return the mean of the array of list of enrollments
        return np.array(x).mean()

class GeneralStats:
    """Class to generally access and perform analytics
       Data is sorted by [years][school][grade]

       params:
            array_3D: 3D data array to search
            array_3D_means: 3D data array with means instead of nans

    """

    def __init__(self, array_3D, array_3D_means):
        self.array_3D = array_3D
        self.array_3D_means = array_3D_means
        
    def meanEnrollment(self, year):
        """
        Calculates the mean enrollment for all grades for a 
        specific year

        params:
            year: the speicified year

        returns:
            float represeting mean enrollment 
        """
        year = year - 2013
        return self.array_3D_means[year,:,:].mean()
    
    def totalGraduating(self, year):
        """
        Calculates the total graduating from grade 12 for a certain year

        params:
            year: the speicified year

        returns:
            float representing graduated
        """
        year = year - 2013
        return np.sum(self.array_3D[year, :, 2])
    
    def highestEnrollment(self):
        """
        Calculates the highest enrollment from any grade
       
        returns:
            float representing highest enrollment
        """   
        return np.max(self.array_3D)

    def lowestEnrollment(self):
        """
        Calculates the lowest enrollment from any grade

        returns:
            float representing lowest enrollment
        """
        return np.min(self.array_3D)


def main():
    print("\nENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    array_3D = reshapeSchoolData(given_data_list)
    array_3D_means = reshapeSchoolDataMeans(given_data_list)
    print("Shape of full data array: ", array_3D.shape)
    print("Dimension of full data array: ", array_3D.ndim)

    # Prompt for user input
    while True:

        #Raises value error if the input is not within the school/code dictionary
        try:
            userInput = input("Please enter a highschool name or school code: ")
           
            if userInput in list(school_dict.values()):
                 #Change user input from string to code for future functionality
                 userInput = list(school_dict.keys())[list(school_dict.values()).index(userInput)]
                 break
            
            elif int(userInput) in school_dict.keys():
                break
            
            else:
                raise ValueError
        
        except ValueError:
            print("Please input a valid school name or school code!")

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")

    s = SchoolStats(int(userInput), array_3D)

    print("School Name:", s.name, "// School Code:", s.code)
    print("Mean enrollment for grade 10:", s.meanEnrollment(10).astype(int))
    print("Mean enrollment for grade 11:", s.meanEnrollment(11).astype(int))
    print("Mean enrollment for grade 12:", s.meanEnrollment(12).astype(int))
    print("Highest enrollment for a single grade:", s.highestEnrollment().astype(int))
    print("Lowest enrollment for a single grade:", s.lowestEnrollment().astype(int))

    #Compute the total enrollment for each year
    total = 0
    for year in range(2013,2023):
        print("Total enrollment for", (year), ":", s.totalEnrollment(year).astype(int))
        total += s.totalEnrollment(year).astype(int)

    print("Total ten year enrollment:", total)
    print("Mean total enrollment over 10 years:", s.meanTotalEnrollment().astype(int))
    s.medianTotalEnrollment()

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")

    g = GeneralStats(array_3D, array_3D_means)

    print("Mean enrollment in 2013:", g.meanEnrollment(2013).astype(int))
    print("Mean enrollment in 2022:", g.meanEnrollment(2022).astype(int))
    print("Total graduating class of 2022:", g.totalGraduating(2022).astype(int))
    print("Highest enrollment for a single grade:",g.highestEnrollment().astype(int))
    print("Lowest enrollment for a single grade", g.lowestEnrollment().astype(int))

if __name__ == '__main__':
   
    main()

