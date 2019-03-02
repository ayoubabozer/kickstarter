
# Kickstarter Data Exploration & Predicting Projects Funding Success
[Kickstarter](https://www.kickstarter.com/) is a global crowdfunding platform, focused on creativity and merchandising.
The company's stated mission is to "help bring creative projects to life".

This project is making simple exploration and a look around to the
 crowdfunding data in Kickstarter.
  
Then our goal will be to evaluate and explore multiple supervised machine learning models, to predict if a project funding will be successfull before it is launched. 

I took the data from [Kaggle](https://www.kaggle.com/kemical/kickstarter-projects#ks-projects-201801.csv) website, it includes 378,661 Kickstarter projects.

each project has 15 features:

1. **ID** : project ID.
2. **name** : the name of the respective project.
3. **main_category** : the main category the project falls in.
4. **category** : a subgroup of main_category.
5. **currency** : the currency of the project.
6. **deadline** : the deadline for the project.
7. **goal** : goal amount in project currency.
8. **launched** : the launch date for the project.
9. **pledged** : pledged amount in the project currency.
10. **state** : state is a categorical status of the project.
11. **usd pledged** : pledged amount in USD (conversion made by KS).
12. **usd_pledged_real** : pledged amount in USD (conversion made by fixer.io).
13. **usd_goal_real** : amount of USD the project asked for initially.
14. **backers** : the number of supporters that actually invested in the project.
15. **country** : country of origin of the project.


we are using two of the must-have python packages for Data Science and Finance:
- NumPy : allowing us to work with multidimensional arrays, and a fast numeric array computations
- Pandas : allowing us to organize data in a tabular form, and quickly loading remote data or a .csv file.


I was able to answer three of the questions I had set out to answer.

The biggest factor in having a successful kickstarter project is the funding goal you set yourself. The median successful project had a funding goal nearly half of the median unsuccessful project.
The most successful categories are Music, Film & Video, Dance, Comics - many of the arts.
There were quite a few differences between successful and unsuccessful projects. Other than the ones mentioned above, the median fundraising duration of a successful project was 7 hours shorter than that of unsuccessful projects. Maybe there is a sense of urgency that convinces people to donate. Furthermore, median pledge in USD is about 65$ for successful projects and only $17 for unsuccessful ones, which shows that one would be wise to incentivize higher values of pledges.


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
    cd predict
     ``` 
 
 3. Pull & Run Docker Image
 
     ```
     git clone https://github.com/ayoubabozer/calculating-stocks-risk.git
     ```
     - -it : to make sure that it runs in interactive mode with the terminal attached.


# ENJOY!.
