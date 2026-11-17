import cv2
import numpy as np

# Constantes globales
NUMBER = 100
DELAY = 5
window_width = 900
window_height = 600

# Fonction pour générer une couleur aléatoire
def random_color(rng):
    icolor = int(rng.integers(0, 0xFFFFFFFF))
    return (icolor & 255, (icolor >> 8) & 255, (icolor >> 16) & 255)

# Lignes aléatoires
def drawing_random_lines(image, window_name, rng):
    for i in range(NUMBER):
        pt1 = (int(rng.integers(-window_width, window_width * 2)), 
               int(rng.integers(-window_height, window_height * 2)))
        pt2 = (int(rng.integers(-window_width, window_width * 2)), 
               int(rng.integers(-window_height, window_height * 2)))
        color = random_color(rng)
        thickness = int(rng.integers(1, 10))
        cv2.line(image, pt1, pt2, color, thickness, cv2.LINE_8)
        cv2.imshow(window_name, image)
        if cv2.waitKey(DELAY) >= 0:
            return -1
    return 0

# Rectangles aléatoires
def drawing_random_rectangles(image, window_name, rng):
    for i in range(NUMBER):
        pt1 = (int(rng.integers(0, window_width)), int(rng.integers(0, window_height)))
        pt2 = (int(rng.integers(0, window_width)), int(rng.integers(0, window_height)))
        color = random_color(rng)
        thickness = int(rng.integers(-1, 10))
        cv2.rectangle(image, pt1, pt2, color, thickness, cv2.LINE_8)
        cv2.imshow(window_name, image)
        if cv2.waitKey(DELAY) >= 0:
            return -1
    return 0

# Ellipses aléatoires
def drawing_random_ellipses(image, window_name, rng):
    for i in range(NUMBER):
        center = (int(rng.integers(0, window_width)), int(rng.integers(0, window_height)))
        
        # Taille des axes aléatoire
        axes = (int(rng.integers(0, 200)), int(rng.integers(0, 200)))
        
        # Angles aléatoires pour la rotation et les arcs
        angle = int(rng.integers(0, 180))
        startAngle = int(rng.integers(0, 360))
        endAngle = int(rng.integers(0, 360))
        
        color = random_color(rng)
        thickness = int(rng.integers(-1, 10))
        
        # cv2.ellipse prend : image, centre, axes, angle, startAngle, endAngle, couleur, épaisseur
        cv2.ellipse(image, center, axes, angle, startAngle, endAngle, color, thickness, cv2.LINE_8)
        
        cv2.imshow(window_name, image)
        if cv2.waitKey(DELAY) >= 0:
            return -1
    return 0

def main():
    window_name = "Drawing_2 Tutorial"
    rng = np.random.default_rng(0xFFFFFFFF)

    image = np.zeros((window_height, window_width, 3), dtype=np.uint8)

    # Exécution séquentielle des étapes
    if drawing_random_lines(image, window_name, rng) != 0:
        cv2.destroyAllWindows()
        return
    if drawing_random_rectangles(image, window_name, rng) != 0:
        cv2.destroyAllWindows()
        return
    if drawing_random_ellipses(image, window_name, rng) != 0:
        cv2.destroyAllWindows()
        return

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()