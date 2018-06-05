import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import os

def makingGraph(analyzeResult):
    labels = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
    N = len(analyzeResult) - 1

    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
     
    ax = plt.subplot(111, polar=True)
     
    plt.xticks(angles[:-1], labels, color='grey', size=8)
     
    ax.set_rlabel_position(0)
    plt.yticks([1, 2, 3, 4, 5], ["1","2","3","4","5"], color="grey", size=7)
    plt.ylim(0,5)
     
    ax.plot(angles, analyzeResult, linewidth=1, linestyle='solid')
     
    ax.fill(angles, analyzeResult, 'b', alpha=0.1)
    
    plt.savefig(os.getcwd() + '/static/results.png')
if __name__ == '__main__':
    analyzeResult = [1, 3, 4.4,  0 ,1, 1]
    makingGraph(analyzeResult)