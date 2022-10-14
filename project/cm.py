import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from sklearn.metrics import confusion_matrix

def plot_confusion_matrix(y_true, y_pred, labels = [0,1], metric = None, figsize = (6,6)):
    fontsize = 14

    fig, ax = plt.subplots(figsize = figsize)
    plt.vlines(x = [0,1,2], ymin = 0, ymax = 2)
    plt.hlines(y = [0,1,2], xmin = 0, xmax = 2)

    plt.annotate(text = labels[0], xy = (0.5, 2.05), va = 'bottom', ha = 'center', fontsize = fontsize)
    plt.annotate(text = labels[1], xy = (1.5, 2.05), va = 'bottom', ha = 'center', fontsize = fontsize)
    plt.annotate(text = labels[0], xy = (-0.05, 1.5), va = 'center', ha = 'right', fontsize = fontsize, rotation = 90)
    plt.annotate(text = labels[1], xy = (-0.05, 0.5), va = 'center', ha = 'right', fontsize = fontsize, rotation = 90)

    plt.annotate(text = 'Predicted', xy = (1, 2.25), va = 'bottom', ha = 'center', fontsize = fontsize + 2, fontweight = 'bold')
    plt.annotate(text = 'Actual', xy = (-0.25, 1), va = 'center', ha = 'right', fontsize = fontsize + 2, fontweight = 'bold', rotation = 90)

    cm = confusion_matrix(y_true, y_pred)

    for i in range(2):
        for j in range(2):
            plt.annotate(text = cm[j][i], xy = (0.5 + i, 1.5 - j), fontsize = fontsize + 4, ha = 'center', va = 'center')


    plt.ylim(-0.2, 2.5)
    plt.xlim(-0.5, 2.1)
    
    if metric == 'accuracy':
        ax.add_patch(Rectangle(xy = (0,1), width = 1, height = 1, color = 'lightgreen'))
        ax.add_patch(Rectangle(xy = (1,0), width = 1, height = 1, color = 'lightgreen'))
        ax.add_patch(Rectangle(xy = (0,0), width = 1, height = 1, color = 'coral'))
        ax.add_patch(Rectangle(xy = (1,1), width = 1, height = 1, color = 'coral'))
        
        plt.annotate(text = 'Accuracy: {}'.format(round((cm[0][0] + cm[1][1]) / cm.sum(),3)), 
                     xy = (1, -0.1), ha = 'center', va = 'top', fontsize = fontsize + 2)
        
    if metric == 'sensitivity':
        ax.add_patch(Rectangle(xy = (1,0), width = 1, height = 1, color = 'lightgreen'))
        ax.add_patch(Rectangle(xy = (0,0), width = 1, height = 1, color = 'coral'))
        
        plt.annotate(text = 'Sensitivity: {}'.format(round((cm[1][1]) / cm[1].sum(),3)), 
                     xy = (1, -0.1), ha = 'center', va = 'top', fontsize = fontsize + 2)
        
    if metric == 'specificity':
        ax.add_patch(Rectangle(xy = (0,1), width = 1, height = 1, color = 'lightgreen'))
        ax.add_patch(Rectangle(xy = (1,1), width = 1, height = 1, color = 'coral'))
        
        plt.annotate(text = 'Specificity: {}'.format(round((cm[0][0]) / cm[0].sum(),3)), 
                     xy = (1, -0.1), ha = 'center', va = 'top', fontsize = fontsize + 2)
        
    if metric == 'precision':
        ax.add_patch(Rectangle(xy = (1,0), width = 1, height = 1, color = 'lightgreen'))
        ax.add_patch(Rectangle(xy = (1,1), width = 1, height = 1, color = 'coral'))
        
        plt.annotate(text = 'Precision: {}'.format(round((cm[1][1]) / cm[:,1].sum(),3)), 
                     xy = (1, -0.1), ha = 'center', va = 'top', fontsize = fontsize + 2)   

    plt.axis('off')

