import colorgram
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import os


def rgb_vers_hex(rgb):
    # https://www.codespeedy.com/convert-rgb-to-hex-color-code-in-python/
    # La fonction prend en argument un TUPLE de couleur de format (r, g, b) et le converti
    # en HEX de format #FFFFFF

    a = '%02x%02x%02x' % rgb
    return "#" + a.upper()


def display_colors_and_proportions(img, n):
    # https://www.youtube.com/watch?v=mmjMQkUych8&ab_channel=Amulya%27sAcademy
    # pour ajuster individuellement les couleurs dans un Rectangle object

    colors = colorgram.extract(img, n)
    color_list, color_list_hex, proportion_list = [], [], []
    for i in colors:
        color = (i.rgb[0], i.rgb[1], i.rgb[2])
        color_list += [color]
        color_list_hex += [rgb_vers_hex(color)]
        proportion_list += [i.proportion*100]

    # Définition des variables
    color_array = np.array(color_list)
    m = len(color_array)
    proportion_array = np.array(proportion_list)
    x = np.arange(m)

    # Création de la figure qui contiendra les 2 sous graphes :
    fig = plt.figure(figsize=(8, 6))

    # Définition du premier sous-graphe de 3.
    ind = np.linspace(0, (m - 1), m, dtype=int).reshape(1, m)
    ax = fig.add_subplot(312)
    ax.imshow(color_array[ind])
    ax.set_yticks([])
    plt.xticks([])
    plt.title(f"Les {m} couleurs les plus présentes dans l'image")

    # Définition du graphique pour les proportion (graphique 2 de 3)
    plt.subplot(313)
    plt.title(f"La proportion de ces {m} couleurs dans l'image")
    plt.ylabel("Proportion (%)")
    plt.xticks([])
    plt.xlim([-0.5, m - 0.5])
    # On passe les barres individuelles dans une boucle pour
    # modifer les couleurs avec le format HEX obtenu :
    barres = plt.bar(x, proportion_array, width=1, edgecolor="black")
    for i, j in enumerate(barres):
        j.set_facecolor(color=color_list_hex[i])

    # Pour le troisième objet, convertir d'abord l'image en format .png
    im1 = Image.open(img)
    im1.save("image_graphe.png")

    # Conversion de l'image en array
    arr_im1 = mpimg.imread('image_graphe.png')

    # Construction du troisième sous-graphe (de 3)
    plt.subplot(311)
    plt.imshow(arr_im1)
    plt.xticks([])
    plt.yticks([])
    plt.title("Image analysée")

    # Affichage du graphe
    plt.show()

    # Supression de l'image .png
    os.remove("image_graphe.png")


if __name__ == "__main__":

    image = "amish_quilt.jpg"
    display_colors_and_proportions(image, 25)