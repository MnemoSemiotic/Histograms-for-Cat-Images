from os import listdir, getcwd
from skimage.io import imread



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

    print(type(cat_image))
    print(cat_image.shape)