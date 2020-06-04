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


def avg_image(im):
    lay1, lay2, lay3  = split_layers_to_3(im)

    avgd = (1./3.)*lay1 + (1./3.)*lay2 + (1./3.)*lay3
    return avgd.astype(int)


def plot_histogram(x, title):
    fig, ax = plt.subplots()

    sigma_ = np.std(x)
    mu_ = np.mean(x)

    x_ = np.ravel(x)
    min = x_.min()
    max = x_.max()
    range = max - min

    _, bins, _ = ax.hist(x_, 300, density=True)

    bins = int(range / 3.5)

    ax.set_xlabel('{} bins with fit line, plotted against precise values'.format(bins))
    ax.set_ylabel('Probability Density')
    ax.set_title(r'{0}: $\mu=${1:.3f}, $\sigma=${2:.3f}'.format(title.split('/')[-1], mu_, sigma_))

    sns.set_style('darkgrid')
    sns.distplot(x_, color="b", bins=75)

    plt.show()


def convert_to_grayscale(im):
    gray = rgb2gray(im)
    gray = 255 * gray
    return gray.astype(np.uint8)


def plot_histograms(im, title, images=False):
    gray = convert_to_grayscale(im)

    avgd_img = avg_image(im)

    R, G, B = split_layers_to_3(im)

    if images==True:
        plot_image(gray, 'grayscale/luminance (weighted channels)')
    plot_histogram(gray, f'{title}: Luminosity Histogram')

    if images==True:
        plot_image(avgd_img, '3 channels averaged to 1 channel')
    plot_histogram(avgd_img, f'{title[0:-1]}: Averaged Histogram')

    if images==True:
        plot_image(R, 'Red Channel')
    plot_histogram(R, f'{title[0:-1]}: Reds Histogram')

    if images==True:
        plot_image(G, 'Green Channel')
    plot_histogram(G, f'{title[0:-1]}: Greens Histogram')

    if images==True:
        plot_image(B, 'Blue Channel')
    plot_histogram(B, f'{title[0:-1]}: Blues Histogram')


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