# HPI-Prediction
Housing Price Index (HPI) measures the price changes of residential housing. It is a broad
measure of the movement of single-family house prices in the United States. Apart from
serving as an indicator of house price trends, the House Price Index provides an analytical
tool for estimating changes in the rates of mortgage defaults, prepayments, and housing
affordability. The HPI is a weighted, repeat-sales index, which means that it measures average
price changes in repeat sales or refinancing on the same properties. A comprehensive HPI
report is published every quarter
## Features
In the project, the given variables were:
1. The Federal Funds Rate:
The federal funds rate is the interest rate at which depository institutions (banks and credit
unions) lend reserve balances to other depository institutions overnight, on an uncollateralized
basis.
2. Total Expenditure:
The total expenditure by the country. Defined as cost of goods times the quantity of goods.
3. Labor Force Price:
The cost of labor is the sum of all wages paid to employees, as well as the cost of employee
benefits and payroll taxes paid by an employer. The cost of labor is broken into direct and
indirect (overhead) costs.
4. Producer Price Index:
The Producer Price Index (PPI) is a weighted index of prices measured at the wholesale, or
producer level. A monthly release from the Bureau of Labor Statistics (BLS), the PPI shows
trends within the wholesale markets (the PPI was once called the Wholesale Price Index),
manufacturing industries and commodities markets.
5. Gross Domestic Product:
Gross Domestic Product (GDP) is a monetary measure of the market value of all the final
goods and services produced in a period of time, often annually or quarterly. Nominal GDP
estimates are commonly used to determine the economic performance of a whole country or
region, and to make international comparisons.
6. S&P 500 Index:
The Standard & Poor's 500, often abbreviated as the S&P 500, or just the S&P, is an
American stock market index based on the market capitalizations of 500 large companies
having common stock listed on the NYSE or NASDAQ. The S&P 500 index components and
their weightings are determined by S&P Dow Jones Indices.
7. Consumer Price Index:
A consumer price index (CPI) measures changes in the price level of market basket of
consumer goods and services purchased by households. It is one of several price indices
calculated by most national statistical agencies. The annual percentage change in a CPI is
used as a measure of inflation.
8. Long Interest Rate:
Long-term interest rates refer to government bonds maturing in ten years. Rates are mainly
determined by the price charged by the lender, the risk from the borrower and the fall in the
capital value. Long-term interest rates are generally averages of daily rates, measured as a
percentage.
Unemployment Factors:
9. Total Unemployed:
Total number of unemployed citizens
10. More than 15 weeks:
Number of citizens unemployed for over 15 weeks.
11. Not in Labor – Searched for Work
Number of citizens who are unemployed while still searching for work.
12. Multiple Jobs:
Number of citizens who have multiple jobs, or are offered multiple jobs.
13. Leavers:
A job leaver is a person who has voluntarily quit one job and is actively seeking employment
elsewhere.
14. Losers:
A job loser is an unemployed person who has been involuntarily terminated or laid off from a
job. More specifically, a job loser is either a person who has been permanently terminated
from a job and is actively seeking employment or a person who has been temporarily laid off
from a job and is not actively seeking employment due to expectations being called back to
work within six months.
<br />

## Implementation Flow 

![flow diagram](images/flow.png?raw=true) <br />

## Accuracy Score Check
We used two metrics to check the accuracy score of the trained model. <br />
a) Mean Absolute Error:
The Mean Absolute Error is a measure of difference between two continuous variables.
MAE=∑ ( | y i – x i | ) / n
The MAE for Linear Regression was the least as compared to the other algorithms. <br />
b) Explained Variance Score:
Explained variation measures the proportion to which a mathematical model accounts for the
variation (dispersion) of a given data set. Often, variation is quantified as variance; then, the
more specific term explained variance can be used.
The Explained Variance Score was the best for Linear Regression.
16So the given problem was best explained by Linear Regression. Hence, finalized linear
regression as the model for the problem.
As the performance metrics were satisfactory, we went to the next step.

## RFE
Recursive Feature Elimination (RFE) as its title suggests recursively removes features, builds
a model using the remaining attributes and calculates model accuracy. RFE is able to work
out the combination of attributes that contribute to the prediction on the target variable (or
class).<br />
![rfe diagram](images/rfe.png?raw=true) <br/>
After following the process, the best results were obtained by keeping 7 features out of the 14
initially. These were:
1. Total Expenditure
2. Producer Price Index
3. S&P 500 Index
4. Consumer Price Index
5. Long Interest Rate
6. Multi Jobs
7. Losers


