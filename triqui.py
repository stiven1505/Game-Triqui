import pygame



#Inicializar modulos ( Todos porque es un juego pequeño ) - Initialize modules ( all because it's a small game)

pygame.init()

#Crear ventana para interectuar - Create window to interect
#Dimensiones del juego - Game dimensions 
screen = pygame.display.set_mode((500,500))
#Titulo para el juego - Title for the game 
pygame.display.set_caption("--Triqui--")

#Cargar recursos - Load resources

background = pygame.image.load('static/Fondo.png')
sunflower = pygame.image.load('static/Girasol.png')
rose = pygame.image.load('static/Rosa.png')

#Escalar o redimensionar las imagenes - Scale or resize images

background = pygame.transform.scale(background, (500,500))
sunflower = pygame.transform.scale(sunflower, (170,170))
rose = pygame.transform.scale(rose, (170,170))


#Crear matriz Bimensional y donde se van acomodar las coordenadas -  Create two-dimensional matrix and where the coordinates will be placed

coor = [[(25,25),(170,25),(315,25)],
        [(25,155),(170,155),(315,155)],
        [(25,300),(170,300),(315,300)],]

table = [['','',''],
         ['','',''],
         ['','','']]

shift = 'Sunflower'
game_over= False
clock = pygame.time.Clock()

#Funciones -functions
def grafic_board():
    screen.blit(background,(0,0))
    for f in range(3):
        for c in range(3):
            if table[f][c] == 'Sunflower' :
                draw_sunflower(f,c)
            elif table[f][c] == 'Rose' :
                draw_rose(f,c)
            

def draw_sunflower (f,c):
    screen.blit(sunflower,coor[f][c])

def draw_rose (f,c):
    screen.blit(rose,coor[f][c])

def winner ():
    
    for i in range(3):
        #Ganador horizontal - Horinzontal winner
        if table[i][0] == table[i][1] == table[i][2] != '':
            return True
        #Ganador vertical - Vertical winner
        if table[0][i] == table[1][i] == table[2][i] != '':
            return True
    #Ganador diagonal - Diagonal winner
    if table[0][0] == table[1][1] == table[2][2] != '':
            return True
    if table[0][2] == table[1][1] == table[2][0] != '':
            return True
    return False
def tie():
    # Check if all cells are filled without a winner - Compruebe si todas las celdas están llenas sin un ganador
    for i in range(3):
        for j in range(3):
            if table[i][j] == '':
                return False  # Not a tie if an empty cell exists - No es un empate si existe una celda vacia.
    return True  # Tie if all cells are filled - Empate si todas las celdas estan llenas

        
    
#Logica del juego - Game logic
while not game_over:
    #Manejar velocidad del juego - Handle game speed
    clock.tick(30)
    #Gestion de eventos - Event management
    for e in pygame.event.get():
        #Evento de x en la ventana - "X" event in window
        if e.type == pygame.QUIT:
            game_over=True
        #Evento para capturar el clic - Event to capture the clic
        elif e.type == pygame.MOUSEBUTTONUP:
            mouseX,mouseY = e.pos
            #Condicionar coordenadas de interes. - Condition coordinates of interest.
            if(mouseX >=25 and mouseX < 470) and (mouseY >=25 and mouseY <470 ):
                f = (mouseY - 25) // 140
                c = (mouseX - 25 ) // 140
                if table [f][c] == '':
                    table[f][c] = shift
                    #Definir ganador - Define winner
                    end_play_winner = winner()
                    if end_play_winner:
                        #messagebox.showinfo("Resultado", f"¡The player with the figure of {shift} has won!!")
                        print(f"The player with the figure of {shift} has won!!")
                        game_over=True
                        
                    #Definir empate - Define tie
                    end_play_tie = tie()
                    if end_play_tie:
                        #messagebox.showinfo("Resultado", f"it was a tie!")
                        print(f"it was a tie!")
                        game_over=True
                        
                    #con esto el turno va ir cambiando - With this the shift will change
                    shift = 'Rose' if shift =='Sunflower' else 'Sunflower'
            
        
    #Graficar los eventos -Graph the events
    grafic_board()
    
    
    #Actualizar la consola - Update the console
    pygame.display.update()
    
#Por si existe algun error - In case there is any error
pygame.quit()