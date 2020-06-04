from os import listdir, getcwd
from skimage.io import imread
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def plot_image(img, title):
    fig, ax1 = plt.subplots(ncols=1, figsize=(18, 6), sharex=True, sharey=True)

    ax1.imshow(img, cmap='gray')
    ax1.set_title(title)
    ax1.axis('off')

def split_layers_to_3(im):
    return [im[: , :, channel] for channel in range(3)]

def plot_histogram(x, title):
    fig, ax = plt.subplots()

    sigma_ = np.std(x)
    mu_ = np.mean(x)

    x_ = np.ravel(x)
    min_ = x_.min()
    max_ = x_.max()
    range = max_ - min_

    count, bins, ignored = ax.hist(x_, 300, density=True)

    ax.set_xlabel(f'bins with fit line, plotted against precise values')
    ax.set_ylabel('Probability Density')
    ax.set_title(r'{0}: $\mu=${1:.3f}, $\sigma=${2:.3f}'.format(title, mu_, sigma_))

    sns.set_style('darkgrid')
    sns.distplot(x_, color='b', bins=75)

    plt.show()




if __name__ == "__main__":
    # print(getcwd())
    animals_lst = listdir('images')
    
    if '.DS_Store' in animals_lst:
        animals_lst.remove('.DS_Store')

    cwd = getcwd()

    animals_lst = [cwd + '/images/' + filename for filename in animals_lst]

    # for filename in animals_lst:
    #     print(filename)
    cat_image = imread(animals_lst[0])

    # print(type(cat_image))
    # print(cat_image.shape)

    plot_image(cat_image, animals_lst[0])

    r, g, b = split_layers_to_3(cat_image)

    print(r.shape)
    print(g.shape)
    print(b.shape)