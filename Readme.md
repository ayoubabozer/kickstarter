
# Calculating companies stocks risk
This is a project calculating logarithmic rate of return and standard deviation (risk)  of two companies,
- PG - Procter & Gamble
- BEI.DE - Beiersdorf

we are using three of the must-have python packages for Data Science and Finance:
- NumPy : allowing us to work with multidimensional arrays, and a fast numeric array computations
- Pandas : allowing us to organize data in a tabular form, and quickly loading remote data or a .csv file.
- Matplotlib : a 2D plotting library specially designed for visualization of Numpy computations.


with this project we reinforce the fact that stocks with higher expected return, OFTEN embed MORE risks. 


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
 - Docker
 
 ### Installing
 
 1. Copy the project to your machine
 
     ```
     git clone https://github.com/ayoubabozer/calculating-stocks-risk.git
     ```
 
 2. Get into the Dir 
     ```
     cd calculating-stocks-risk
     ```
    
 3. Build Docker
 
    ```
     docker build -t <tag_name> .
     ```
    
     - don't forget the dot.
 
 4. Run docker
 
     ```
        docker run -it <tag_name>
     ```
     - -it : to make sure that it runs in interactive mode with the terminal attached.


# ENJOY!.
