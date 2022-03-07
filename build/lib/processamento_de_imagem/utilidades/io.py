from skimage.io import imread, imsave

def read_imagem(caminho, cinza = False):
    imagem = imread(caminho, as_gray = cinza)
    return imagem

def save_imagem(imagem, caminho):
    imsave(caminho, imagem) 