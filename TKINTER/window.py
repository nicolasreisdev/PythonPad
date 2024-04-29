from tkinter import *

window = Tk() #incializa o tkinter

class Application():
    def __init__(self): #inicializando a janela
        self.window = window
        self.tela()
        self.frames()
        self.botoes()
        self.window.mainloop() #mantem a janela aberta (loop infinito do draw da janela)        
    
    def tela(self): #configurações da janela
        self.window.title('CONTABILIDADE') #define o título da janela
        self.window.geometry("1000x500") #define o tamanho da janela  
        self.window.resizable(True,True) #define se a janela pode ser redimensionada
        self.window.maxsize(1200,700) #define o tamanho máximo da janela
        self.window.minsize(500, 250) #define o tamanho mínimo da janela
        self.window.configure(background='black') #define a cor de fundo da janela
    
    def frames(self): #configurações dos frames
        self.frame1 = Frame(self.window, bd = 3, relief = 'solid', highlightbackground='green', highlightthickness=2)
        self.frame1.place(relx = 0.02, rely = 0.02 , relwidth = 0.96 , relheight = 0.5)
        
    def botoes(self):
        #botao limpar
        self.bt_limpar = Button(self.frame1, text = 'Limpar', font = ('verdana', 10, 'bold'), bg = 'black', fg = 'white')
        self.bt_limpar.place(relx = 0.01, rely = 0.02, relwidth = 0.18, relheight = 0.1)
        #botao sair
        self.bt_limpar = Button(self.frame1, text = 'Sair', font = ('verdana', 10, 'bold'), bg = 'black', fg = 'white')
        self.bt_limpar.place(relx = 0.21, rely = 0.02, relwidth = 0.18, relheight = 0.1)
        #botao criar
        self.bt_limpar = Button(self.frame1, text = 'Criar', font = ('verdana', 10, 'bold'), bg = 'black', fg = 'white')
        self.bt_limpar.place(relx = 0.41, rely = 0.02, relwidth = 0.18, relheight = 0.1)
        #botao excluir
        self.bt_limpar = Button(self.frame1, text = 'Excluir', font = ('verdana', 10, 'bold'), bg = 'black', fg = 'white')
        self.bt_limpar.place(relx = 0.61, rely = 0.02, relwidth = 0.18, relheight = 0.1)
        #botao editar
        self.bt_limpar = Button(self.frame1, text = 'Editar', font = ('verdana', 10, 'bold'), bg = 'black', fg = 'white')
        self.bt_limpar.place(relx = 0.81, rely = 0.02, relwidth = 0.18, relheight = 0.1)
       
       
         


Application()