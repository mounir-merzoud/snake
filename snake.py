import pygame
import sys
import os
import subprocess

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)  # Ajout de la couleur rouge

# Initialisation de la fenêtre
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("menu snake")

# Charger l'image d'arrière-plan
background_image = pygame.image.load(os.path.join("image", "couverture.png"))
background_rect = background_image.get_rect()

# Fonte pour le texte des boutons
font = pygame.font.Font(None, 36)

def draw_rectangle_with_title(x, y, width, height, title, color):
    # Dessiner le rectangle
    pygame.draw.rect(screen, color, (x, y, width, height))

    # Dessiner le titre centré à l'intérieur du rectangle
    text_surface = font.render(title, True, WHITE)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

# Fonction pour créer un bouton
def create_button(x, y, width, height, text, action):
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, WHITE, button_rect)
    pygame.draw.rect(screen, BLACK, button_rect, 2)

    # Afficher le texte du bouton
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    # Vérifier si le bouton est cliqué
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            action()

# Fonction à exécuter lorsque le bouton "Run User File" est cliqué
def run_user_file_action():
    file_path = "main.py"  # Spécifiez le chemin du fichier main.py
    subprocess.run(["python", file_path])

# Fonction à exécuter lorsque le bouton "Run IA File" est cliqué
def run_ia_file_action():
    file_path = "ia.py"  # Spécifiez le chemin du fichier ia.py
    subprocess.run(["python", file_path])

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Afficher l'arrière-plan
    screen.blit(background_image, background_rect)
    
    # Dessiner un rectangle avec un titre
    draw_rectangle_with_title(200, 200, 400, 100, "SNAKE", RED)

    # Créer les boutons
    create_button(200, 400, 200, 50, "Jouer", run_user_file_action)
    create_button(400, 400, 200, 50, "Jouer IA", run_ia_file_action)

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
