
# Kickstarter Data Exploration & Predicting Projects Funding Success
[Kickstarter](https://www.kickstarter.com/) is a global crowdfunding platform, focused on creativity and merchandising.
The company's stated mission is to "help bring creative projects to life".

This project is making simple exploration and a look around to the
 crowdfunding data in Kickstarter.
  
Then our goal will be to evaluate and explore multiple supervised machine learning models, to predict if a project funding will be successful or failed before it is launched. 

I took the data from [Kaggle](https://www.kaggle.com/kemical/kickstarter-projects#ks-projects-201801.csv) website, it includes 378,661 Kickstarter projects.

each project has 15 features:

1. **ID** : project ID.
2. **name** : the name of the project.
3. **main_category** : the main category the project.
4. **category** : a subgroup of main_category.
5. **currency** : the currency of the project.
6. **deadline** : the deadline of the project.
7. **goal** : goal amount in project currency.
8. **launched** : the launch date for the project.
9. **pledged** : pledged amount in the project currency.
10. **state** : state is a categorical status of the project.
11. **usd pledged** : pledged amount in USD (conversion made by KS).
12. **usd_pledged_real** : pledged amount in USD (conversion made by fixer.io).
13. **usd_goal_real** : amount of USD the project asked for initially.
14. **backers** : the number of supporters that actually invested in the project.
15. **country** : country of origin of the project.


in this project, we can find out :

- what is the most common category of kickstarter projects.
- what is the average amount of pledged(USD), goal and backers.
- what is the accuracy score of the prediction model.
- what is the most important factor in having successful project.

i will use the must-have python packages for Data Science and Finance:
- NumPy : Allowing us to work with multidimensional arrays, and a fast numeric array computations
- Pandas : Allowing us to organize data in a tabular form, and quickly loading remote data or a .csv file.
- Sklearn : Machine Learning in Python, Simple and efficient tools for data mining and data analysis.
- Matplotlib : is a Python 2D plotting library.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
 - Docker
 
 ### Installing
 
 1. Copy the project to your machine
 
     ```
     git clone https://github.com/ayoubabozer/kickstarter.git
     ```
 
 2. Get into the Dir
    
    ```
    cd kickstarter
     ``` 
 
 3. Pull & Run Docker Image
 
     ```
     docker run -d --rm --name jupyter -p 8888:8888 -v $PWD:/opt playniuniu/jupyter-pandas
     ```
 4. Open the app in : [http://localhost:8888](http://localhost:8888)


# ENJOY!.
