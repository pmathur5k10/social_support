import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

train = pd.read_csv('./training data/labeled_training_set.csv')

Emotional_disclosure=train.loc[train['Emotional_disclosure'] == 1]
print("Emotional_disclosure", len(Emotional_disclosure))

Information_disclosure=train.loc[train['Information_disclosure'] == 1]
print("Information_disclosure", len(Information_disclosure))

Support=train.loc[train['Support'] == 1]
print("Support", len(Support))

General_support=train.loc[train['General_support'] == 1]
print("General_support", len(General_support))

Info_support=train.loc[train['Info_support'] == 1]
print("Info_support", len(Info_support))

Emo_support=train.loc[train['Emo_support'] == 1]
print("Emo_support", len(Emo_support))

wordcount=train['wordcount'].tolist()



# bins = np.linspace(math.ceil(min(wordcount)), 
#                    math.floor(max(wordcount)),
#                    10) # fixed number of bins

# plt.xlim([min(wordcount)-5, max(wordcount)+5])

# plt.hist(wordcount, bins=bins, alpha=0.5)

path = list(set(wordcount)) ## gets the unique values in the list

histo = []

for i in path:
    histo.append(wordcount.count(i)) ## add the number of occurances to the histo list

plt.bar(path, histo)
plt.title('Word Count Frequency')
plt.xlabel('wordcount')
plt.ylabel('Frequency')

plt.show()