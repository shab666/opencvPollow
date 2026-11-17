from PIL import Image, ImageDraw, ImageFont, ImageText

# Chargement de la police 
try:
    font = ImageFont.truetype("arial.ttf", 28)
except OSError:
    font = ImageFont.load_default(size=28)

# Création de l'objet Text sur deux lignes et ajout d'un contour
contenu = "zany ary ny texte"
text = ImageText.Text(contenu, font)
text.stroke(2, "#00d4ff")

# Récupération des coordonnées exactes (left, top, right, bottom)
left, top, right, bottom = text.get_bbox(align="center")

# Calcul de la largeur et hauteur réelles du texte (incluant le contour)
text_width = int(right - left)
text_height = int(bottom - top)

# Création de l'image avec une marge de 10px tout autour
padding = 10
img_width = text_width + (padding * 2)
img_height = text_height + (padding * 2)

im = Image.new("RGB", (img_width, img_height), color="#1e1e2e")
d = ImageDraw.Draw(im)

# Dessin du texte en compensant le décalage initial (left, top)
position_x = padding - left
position_y = padding - top
d.text((position_x, position_y), text, fill="#ffffff", align="center")

# Sauvegarde et affichage
im.save("carte_visite.png")
im.show()