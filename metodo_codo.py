#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 14:20:09 2018

@author: leonel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sn

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("dataFinal.csv")
data.head( 10 )

#print(data.columns)

X = data[['sexo', 'edad', 'escolaridad', 'pebl', 'dsmt', 'hare', 'ciep', 'cief',
       'ciec', 'ciem', 'ciex', 'cies', 'cie', 'rmsTr', 'pkLevel', 'crest',
       'rmsPk', 'minLevel', 'maxLevel', 'rmsLevel', 'tiempo', 'respuesta',
       'frecuencia', 'tipo']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform( X )
'''
cmap = sn.cubehelix_palette(as_cmap=True, rot=-.3, light=1)

sn.clustermap(X_scaled, cmap=cmap, linewidths=.5)

'''

cluster_range = range( 1, 20 )
cluster_errors = []

for num_clusters in cluster_range:
  clusters = KMeans( num_clusters )
  clusters.fit( X_scaled )
  cluster_errors.append( clusters.inertia_ )
  
clusters_df = pd.DataFrame( { "num_clusters":cluster_range, "cluster_errors": cluster_errors } )
clusters_df[0:10]

plt.figure(figsize=(12,6))
plt.plot( clusters_df.num_clusters, clusters_df.cluster_errors, marker = "o" )




