from tkinter import *
from tkinter import messagebox 

tela = Tk()

tela.geometry("400x400")
tela.title("Tela Principal")
tela.config(background= "#154360")

peso = StringVar()
altura = StringVar()

def Calcular ():
    print("calculando")
    a = float(altura.get())
    p = float(peso.get())
    
    if a == 0:
        messagebox.showerror("Erro!", "A sua altura não pode ser 0")
    else:
        imc = p / (a*a)
        imc = round(imc, 1)
        print("O seu IMC é: ", imc)
        messagebox.showinfo("Mensagem","Seu IMC é de: " + str(imc))



LbTitle = Label(tela, text= " IMC 3.0 \n", font= "Bold 30", background= "#154360", foreground= "white")
caixaNome1 =  Entry(tela, textvariable= altura)

LbAsk = Label(tela, text= " Digite a sua altura [m]: \n", font= "Bold 11", background= "#154360", foreground= "white")
caixaNome2 =  Entry(tela, textvariable= peso)

LbTAskk = Label(tela, text = " Digite o seu peso [kg]: \n ", font= "Bold 11", background= "#154360", foreground= "white")
btnEnviar = Button (tela, command=Calcular, text= "Calcular", font= "Bold 11", background= "#34495E", foreground= "white", activebackground= "#1C2833")


#btn2= Button(command=Calcular , text="Teste")
LbName = Label(tela, text= "\n \n By Mari 🔢", font= "Bold 11", background= "#154360", foreground= "white")

LbTitle.pack()

LbAsk.pack()
caixaNome1.pack()

LbTAskk.pack()
caixaNome2.pack()

btnEnviar.pack(pady= 20)

LbName.pack()
#btn2.pack()
tela.mainloop()