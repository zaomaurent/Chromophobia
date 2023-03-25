import constantes
import fonctions
import sprites

def init():
  n_text = 0

def NPC_clik():
  global n_text
  left, middle, right = pg.mouse.get_pressed()
  if left:
    n_text += 1
  if right and n_text > 1:
    n_text -= 1
    
def NPC_text(n_text):
  if n_text == 1:
    #affichage du texte / suprimer l'encien texte
  elif n_text == 2:
    #passage au deuxieme texte / suprimer l'encien texte
