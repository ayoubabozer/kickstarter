from sklearn import tree
import pandas as pd

# DataSet from dataset.csv

data_feature_names = [ 'Height', 'Weight', 'Hair Length']

dataset = pd.read_csv("dataset.csv")

# X is the dataset without the Class column
X = dataset.drop('Class', axis=1)

# Y is the Class column
Y = dataset['Class']

# classifier - DecisionTreeClassifier
clf = tree.DecisionTreeClassifier();

# learn from data
clf = clf.fit(X,Y);

import pydotplus
import collections

dot_data = tree.export_graphviz(clf,
                                feature_names=data_feature_names,
                                out_file=None,
                                filled=True,
                                rounded=True)

graph = pydotplus.graph_from_dot_data(dot_data)

colors = ('turquoise', 'orange')

edges = collections.defaultdict(list)

for edge in graph.get_edge_list():
    edges[edge.get_source()].append(int(edge.get_destination()))

for edge in edges:
    edges[edge].sort()
    for i in range(2):
        dest = graph.get_node(str(edges[edge][i]))[0]
        dest.set_fillcolor(colors[i])

graph.write_png('tree/tree.png')

print ("The Machine will predict if you are a Man or a Woman :)")

height = input("What is your Height? ")
weight = input("What is your Weight? ")
hair_length = input("What is your Hair Length [0-100]? ")


#test_data
test_data =[ [height, weight, hair_length] ];

#prediction
prediction_tree = clf.predict(test_data);

print("Prediction of DecisionTreeClassifier:",prediction_tree);