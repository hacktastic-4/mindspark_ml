import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import queue

dataset = pd.read_csv("Solar.csv")
x = dataset.iloc[:,2:]
kmeans = KMeans(n_clusters = 3)
kmeans.fit(x)
ymeans = kmeans.predict(x)

def optimize(userid):
    user_id = int(userid)-1
    pre = x.iloc[user_id,:].values
    req_clus = kmeans.predict([pre])
    bool_list = ymeans == req_clus
    bool_list
    clus_list = []
    for i in range(len(bool_list)):
        if bool_list[i]:
            clus_list.append(i)

    priority_queue = queue.PriorityQueue()
    i=0
    while i<len(clus_list):
        priority_queue.put([-x.iloc[clus_list[i],-1],clus_list[i]])
        i+=1
    i = 0
    recommend_list = []
    for i in range(5):
        if not priority_queue.empty():
            t = priority_queue.get()
            recommend_list.append(t[1]+1)
    return recommend_list
