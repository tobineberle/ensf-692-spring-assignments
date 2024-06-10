# calgary_dogs.py
# Author: Tobin Eberle
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 README file.

import pandas as pd

def topYears(data, dog_breed):
    '''
    Finds the years for which a dog breed was in the top breeds data set

    Params
        data: data set to analyze
        dog_breed: dog breed to find data for

    Returns
        A series containing unique years
    
    '''
    sorted = data.set_index("Breed").Year
    return sorted[dog_breed].unique()
        
def totalRegistration(data, dog_breed):
    '''
    Finds the total number of registrations for a dog breed over all years

    Params
        data: data set to analyze
        dog_breed: dog breed to find data for

    Returns
        The total registraion for a dog breed over all years
    
    '''
    return data.groupby(["Breed"]).sum().Total[dog_breed]

def yearlyPercentage(data, dog_breed, year):
    '''
    Finds the percentage of a dog out of all total breeds for a specific year

    Params
        data: data set to analyze
        dog_breed: dog breed to find data for
        year: year to analyze

    Returns
        The percentage of a specifc breed for specifc year
    '''

    #Setup multi indexing for Breed/Year, with the results being summed
    sorted = data.groupby(["Breed", "Year"]).sum()

    #Slice by all breeds, year and return the total of the sum
    total_year = sorted.loc[pd.IndexSlice[:, [year]], "Total"].sum()

    #Slice by specific breed, year and return the percentage
    total_breed = sorted.loc[pd.IndexSlice[[dog_breed], [year]],:].Total.sum()

    #return the only value in the dataframe
    return total_breed/total_year * 100
    
def totalPercentage(data, dog_breed):
    '''
    Finds the percentage of a dog out of all total breeds for all years

    Params
        data: data set to analyze
        dog_breed: dog breed to find data for

    Returns
        The percentage of a specifc breed for all years
    '''
    #Setup multi indexing for Breed/Year, with the results being summed
    sorted = data.groupby(["Breed", "Year"]).sum()

    #Slice by all breeds, all year and return the total of the sum
    total = sorted.loc[:, :].Total.sum()

    #Slice by specific breed, year and return the percentage
    total_breed = sorted.loc[dog_breed, :].Total.sum()  

    #return the only value in the dataframe
    return total_breed/total * 100

def popularMonths(data, dog_breed):
    '''
    Finds the months for which the dog was the most popular 

    Params
        data: data set to analyze
        dog_breed: dog breed to find data for

    Returns
        A list of months
    '''
    #Apply a mask to sort by dog breed and return the mode (most popular) of the month column
    return data[data.Breed == dog_breed].Month.mode()

def main():
    # Import data here
    # Import xlsx as dataframe
    dog_data = pd.read_excel("CalgaryDogBreeds.xlsx")

    # Create a list of all unique dog breeds/years
    dog_breed_list = dog_data.Breed.unique()
    
    print("ENSF 692 Dogs of Calgary")

    # User input stage
    while True:
        try:
            # Take user input and convert to uppercase
            user_input = input("Please enter a dog breed: ").upper()
            if user_input in dog_breed_list:
                break
            else:
                raise ValueError
            
        #Throw error if name not in dog set
        except ValueError:
            print("Dog breed not found, please try again")
        
    # Data anaylsis stage
    print(user_input + " was found in top breeds for years:", *topYears(dog_data, user_input))
    print("There have been {} {} dogs registered in total.".format(totalRegistration(dog_data, user_input), user_input))
    print("The " + user_input + " was {percent:.6f}% of all breeds for {year}.".format(percent = yearlyPercentage(dog_data, user_input, 2021), year = 2021))
    print("The " + user_input + " was {percent:.6f}% of all breeds for {year}.".format(percent = yearlyPercentage(dog_data, user_input, 2022), year = 2022))
    print("The " + user_input + " was {percent:.6f}% of all breeds for {year}.".format(percent = yearlyPercentage(dog_data, user_input, 2023), year = 2023))
    print("The " + user_input + " was {percent:.6f}% of all breeds across all years.".format(percent = totalPercentage(dog_data, user_input)))
    print("The most popular month(s) for " + user_input + " dogs: ", *popularMonths(dog_data, user_input))

if __name__ == '__main__':
   
    main()

