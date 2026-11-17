import cv2
import numpy as np

# Constantes globales
NUMBER = 200
DELAY = 25
window_width = 1600
window_height = 1000

def random_color(rng):
    # Génère un entier aléatoire non signé sur 32 bits
    icolor = int(rng.integers(0, 0xFFFFFFFF))
    # Retourne un tuple BGR (Bleu, Vert, Rouge) extrait des octets
    return (icolor & 255, (icolor >> 8) & 255, (icolor >> 16) & 255)

# Fonction de l'étape 2 : Dessiner des lignes aléatoires
def drawing_random_lines(image, window_name, rng):
    for i in range(NUMBER):
        
        pt1 = (int(rng.integers(-window_width, window_width * 2)), 
               int(rng.integers(-window_height, window_height * 2)))
        pt2 = (int(rng.integers(-window_width, window_width * 2)), 
               int(rng.integers(-window_height, window_height * 2)))
        
        # Dessiner la ligne avec cv2.line
        # Paramètres : image, point_depart, point_arrivee, couleur, épaisseur, type_de_ligne 
        color = random_color(rng)
        thickness = int(rng.integers(1, 10))
        cv2.line(image, pt1, pt2, color, thickness, cv2.LINE_8)
        
        # Afficher l'image mise à jour
        cv2.imshow(window_name, image)
        
        # Pause de DELAY millisecondes. Si l'utilisateur appuie sur une touche, on interrompt
        if cv2.waitKey(DELAY) >= 0:
            return -1
            
    return 0

def main():
    window_name = "dessin aleatoire"
    rng = np.random.default_rng(0xFFFFFFFF)

    # Création de la matrice noire de fond
    image = np.zeros((window_height, window_width, 3), dtype=np.uint8)

    # Lignes aléatoires
    result = drawing_random_lines(image, window_name, rng)
    
    if result == 0:
        # Attendre une touche à la fin pour garder la fenêtre ouverte
        cv2.waitKey(0)
        
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()