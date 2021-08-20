#######################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows users to analyse monthly visitors data analysis in Europe
#Name: Kai Wee
#Group Name: Blob
#Class: PN2004Y
#Date: 12 August 2021
#Version:<....>
#######################################################################

#######################################################################
#IMPORT Pandas Library for Data Analysis
#######################################################################
#import pandas for data analysis
import pandas as pd
#######################################################################
#IMPORT Pandas Library for Data Analysis
#######################################################################
#import pie chart
import matplotlib.pyplot as mat
#######################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#######################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthlyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):

  #print number of rows in dataframe
  print("There are " + str(len(df)) + " data rows read. \n")

  #display dataframe (rows and columns)
  print("The following dataframe are read as follows: \n")
  print(df)


  #display a specific country (United Kingdom,Germany,France,Italy,Netherlands,Greece,Belgium and Luxembourg,Switzerland,Scandinavia,CIS and Eastern Europe) in column #20,21,22,23,24,25,26,27,28,29 and 30
  #Display Europe countries
  Europe = df.columns[20] + "," + df.columns[21] + "," + df.columns[22] + "," + df.columns[23] + "," + df.columns[24] + "," + df.columns[25] + "," + df.columns[26] + "," + df.columns[27] + "," + df.columns[28] + "," + df.columns[29] + "," + df.columns[30]

  print(Europe + "were selected")

  #reading columns
  Europe = df.columns[20] + df.columns[21] + df.columns[22] + df.columns[23] + df.columns[24] + df.columns[25] + df.columns[26] + df.columns[27] + df.columns[28] + df.columns[29] + df.columns[30]
 


  #reading columns 
  df.columns
  
  
  #sorting dataframe (rows and columns)
  print("\nThe following dataframe are read as follows: \n")
  SortedDF = (df[['Year','Month',' United Kingdom ',' Germany ',' France ',' Italy ',' Netherlands ',' Greece ',' Belgium & Luxembourg ',' Switzerland ',' Austria ',' Scandinavia ',' CIS & Eastern Europe ']][350:480])
  #Printing The data
  print(SortedDF)



  # This will convert dtypes from object to int
  SortedDF[' United Kingdom '] = SortedDF[' United Kingdom '].astype(int)
  SortedDF[' Germany '] = SortedDF[' Germany '].astype(int)
  SortedDF[' France '] = SortedDF[' France '].astype(int)
  SortedDF[' Italy '] = SortedDF[' Italy '].astype(int)
  SortedDF[' Netherlands '] = SortedDF[' Netherlands '].astype(int)
  SortedDF[' Greece '] = SortedDF[' Greece '].astype(int)
  SortedDF[' Belgium & Luxembourg '] = SortedDF[' Belgium & Luxembourg '].astype(int)
  SortedDF[' Switzerland '] = SortedDF[' Switzerland '].astype(int)
  SortedDF[' Austria '] = SortedDF[' Austria '].astype(int)
  SortedDF[' Scandinavia '] = SortedDF[' Scandinavia '].astype(int)
  SortedDF[' CIS & Eastern Europe '] = SortedDF[' CIS & Eastern Europe '].astype(int)

  
  


  #Removing unwanted Columns
  New = SortedDF.drop(['Year','Month'], axis=1)
  # Add up the total amount of visitors
  total = New.sum()

    #Sorting on descending order
  Sortedvalue = total.sort_values(ascending=False)

  #Sorting toward top 3 countries
  print("The Top 5 countries from Europe to Singapore in the span of 10 years are: ")
  print("################################")
  print("Period: 2007-2017 ")
  print("Region: Europe ")
  print(Sortedvalue.head(n=5))
  #pie chart 
  activities = ['United Kingdom','Germany', 'CIS & Eastern Europe', 'France', 'Scandinavia']
  slices = [5162602, 2649558, 1626192, 1568727, 1128958]
  colours = ['r', 'g', 'm', 'o', 'i']

  mat.pie(slices,
        labels=activities,
        startangle=90,
        shadow=True,
        explode=(0.2, 0.1, 0.1, 0.1, 0),
        autopct='%1.2f%%')

  mat.legend()

  mat.show()
  
  



  return
#######################################################################
#FUNCTION Branch: End of Code
#######################################################################

#######################################################################
#Main Branch
#######################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()


#######################################################################
#Main Branch: End of Code
#######################################################################



