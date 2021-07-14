from tkinter import *
from tkinter import filedialog
# import re
# import ast
from tkinter import messagebox
# import final_code
from GUI import GUImain
from sklearn.cluster import SpectralClustering
from sklearn.metrics import pairwise_distances

from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import numpy as np

class spectralClustering:
    def __init__(self,inputFile,outputDirectory,k,eigenSolver,n_init,random_state,gamma,n_neighbor,assign_labels,degree,coef0,affinity):
        self.inputFile = inputFile
        self.outputDir = outputDirectory
        self.k = k
        self.eigenSolver = eigenSolver
        self.n_init = n_init
        self.gamma = gamma
        self.random_state = random_state
        self.n_neighbor = n_neighbor
        self.assign_labels = assign_labels
        self.degree = degree
        self.coef0 = coef0
        self.affinity = affinity
    def run(self):
        outputfile = self.outputDir + '/result_spectralClustering' + str(self.k) + '_' + str(self.eigenSolver) + '.csv'
        otc = self.outputDir + '/centers_spectralClustering' + str(self.k) + '_' + str(self.eigenSolver) + '.csv'

        if (self.inputFile == '' or self.outputDir == '' or self.k == '' or self.n_init==''):
            messagebox.showerror("Error", "Please fill the fields properly")
        else:
            if self.random_state == '':
                self.random_state = None


            of = open(outputfile, 'w')
            f = open(self.inputFile, 'r')
            oc = open(otc, 'w')
            data = []
            # data1=[]
            pts = []

            for i in f:
                j = i.strip('\n').split(' ')
                for r in range(1, len(j)):
                    j[r] = float(j[r])
                pts.append(j[0])
                data.append(j[1:])
            X = np.array(data)
            #X_precomputed = pairwise_distances(X, metric='manhattan')
            spectralClustering = SpectralClustering(n_clusters=int(self.k),eigen_solver=self.eigenSolver,random_state=self.random_state,
                                                    n_init=int(self.n_init),gamma=float(self.gamma),affinity=self.affinity,
                                                    n_neighbors=int(self.n_neighbor),assign_labels=self.assign_labels,degree=float(self.degree),
                                                    coef0=float(self.coef0)).fit(X)

            labels = spectralClustering.labels_

            for p in range(len(X)):
                # print(p)
                # wr=kmeans.predict(p)
                stri = pts[p] + ',' + str(labels[p]) + '\n'
                of.write(stri)
            of.close()
            print(spectralClustering.affinity_matrix_)


