from perceptron import perceptronnw
from adaline import adaline
from sgd import adalineSGD
perceptronnw()
adaline()
adalineSGD()
import sys
import os.path
import csv
import numpy as np
import pandas as pd



def main():
    # Check for appropriate number of arguements
    if len(sys.argv) != 3:
        print("\nnumber of arguements are not right\n")
        print("Program Usage:\n\tpython main.py <classifier> <dataset>\n")
        exit()

    classifier = str(sys.argv[1])
    datafile = str(sys.argv[2])

    # Check to see if datafile exists
    if not os.path.isfile(datafile):
        print("\nProvided data file does not exist.\n")
        print("Program Usage:\n\tpython main.py <classifier> <dataset>\n")
        exit()

    # Process dataset into dataframe
    df = pd.read_csv(datafile, header=None)
    y = df.iloc[0:, 2].values
    X = df.iloc[0:, [0, 1]].values

    # Check to see if one of four classifiers is requested, then executes respective classifier
    if classifier == "perceptron":
        print("\nPerceptron", datafile + ".\n")
        # Perceptron()

        # ppn = Perceptron(eta=0.001, n_iter=10)
        ppn = perceptronnw(eta=0.0001, n_iter=1000)
        ppn.fit(X, y)
        # ppn.plot()

    elif classifier == "adaline":
        print("\nUsing Adaline classifier  with dataset at", datafile + ".\n")
        # Adaline()

        # ada = Adaline(eta=0.0004, n_iter=100)
        ada = adaline(eta=0.00001, n_iter=10000)
        ada.fit(X, y)
        # ada.plot()


    elif classifier == "sgd":
        print("\nSGD at", datafile + ".\n")
        # SVG()

        # sgd = SGD(eta=0.001, n_iter=100)
        sgd = adalineSGD(eta=0.0001, n_iter=1000)
        sgd.fit(X, y)
        # sgd.plot()

# Statement to invoke main method at program's execution
if __name__ == "__main__": main()