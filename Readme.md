
# Decision Tree Classification in Python
This is a project is using decision tree algorithm, which is one of the many Machine Learning algorithms.

Classification: given input data, it is class A or class B?
In this project we will visualize a decision tree using the Python module pydotplus and the module graphviz.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
 - Docker
 
 ### Installing
 
 1. Copy the project to your machine
 
     ```
     git clone https://github.com/ayoubabozer/Python-Decision-Tree-Classification.git
     ```
 
 2. Get into the Dir 
     ```
     cd Python-Decision-Tree-Classification
     ```
    
 3. Build Docker
 
    ```
     docker build -t <tag_name> .
    ```
    
    don't forget the dot.
 
 4. Create container from the docker image
 
     ```
        docker create <tag_name>
     ```
     
 5. List containers 
    ```
    docker ps
    ``` 
  
 6. Run the app in the container
 
      ```
      docker exec -it <container_ID> python app.py
      ```
     
     -it : to make sure that it runs in interactive mode with the terminal attached.

     - The program will ask you some question, and will predict if you are a Man or a Woman.     
     - The will output tree.png file in the docker container.
 
 6. Copy tree algorithm image from container to your host
    
    ```
    docker cp <CONTAINER_ID>:/app/tree.png .
    ```
    
    don't forget the dot again.

# ENJOY!.
