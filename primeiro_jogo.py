import tkinter as tk
from tkinter import messagebox

# Criar a janela principal
root = tk.Tk()
root.title("Pedra, Papel e Tesoura")
root.geometry("500x600")

opcoes_validas = ("pedra", "papel", "tesoura")
icones = {"pedra": "🪨", "papel": "📄", "tesoura": "✂️"}

def tela_inicial():
    # Limpar tela
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Label(root, text="🪨 PEDRA, PAPEL E TESOURA ✂️", 
             font=("Arial", 20, "bold"), fg="#2C3E50").pack(pady=20)
    
    regras_texto = """
    REGRAS:
    • Pedra quebra Tesoura
    • Papel cobre Pedra  
    • Tesoura corta Papel
    """
    
    tk.Label(root, text=regras_texto, font=("Courier", 10), 
             justify='left').pack(pady=20)
    
    tk.Button(root, text="INICIAR JOGO", font=("Arial", 14, "bold"),
             bg="#27AE60", fg="white", command=tela_jogo).pack(pady=20)

def tela_jogo():
    for widget in root.winfo_children():
        widget.destroy()
    
    jogada1 = None
    jogada2 = None
    
    tk.Label(root, text="ESCOLHA SUAS JOGADAS", 
             font=("Arial", 16, "bold")).pack(pady=10)
    
    # Frame Jogador 1
    frame1 = tk.LabelFrame(root, text="JOGADOR 1", padx=10, pady=10)
    frame1.pack(side='left', padx=20, fill='both', expand=True)
    
    lbl1 = tk.Label(frame1, text="Aguardando...", font=("Arial", 12), fg="blue")
    lbl1.pack()
    
    # Frame Jogador 2
    frame2 = tk.LabelFrame(root, text="JOGADOR 2", padx=10, pady=10)
    frame2.pack(side='right', padx=20, fill='both', expand=True)
    
    lbl2 = tk.Label(frame2, text="Aguardando...", font=("Arial", 12), fg="red")
    lbl2.pack()
    
    resultado_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="purple")
    resultado_label.pack(pady=20)
    
    def escolher(jogador, opcao):
        nonlocal jogada1, jogada2
        if jogador == 1:
            jogada1 = opcao
            lbl1.config(text=f"{icones[opcao]} {opcao.capitalize()}")
        else:
            jogada2 = opcao
            lbl2.config(text=f"{icones[opcao]} {opcao.capitalize()}")
        
        if jogada1 and jogada2:
            jogar()
    
    def jogar():
        if jogada1 == jogada2:
            resultado = "EMPATE!"
        elif (jogada1 == "pedra" and jogada2 == "tesoura") or \
             (jogada1 == "tesoura" and jogada2 == "papel") or \
             (jogada1 == "papel" and jogada2 == "pedra"):
            resultado = "JOGADOR 1 VENCEU!"
        else:
            resultado = "JOGADOR 2 VENCEU!"
        
        resultado_label.config(text=resultado)
    
    # Botões do Jogador 1
    for opcao in opcoes_validas:
        tk.Button(frame1, text=f"{icones[opcao]} {opcao.capitalize()}",
                 command=lambda o=opcao: escolher(1, o)).pack(pady=5)
    
    # Botões do Jogador 2
    for opcao in opcoes_validas:
        tk.Button(frame2, text=f"{icones[opcao]} {opcao.capitalize()}",
                 command=lambda o=opcao: escolher(2, o)).pack(pady=5)
    
    tk.Button(root, text="VOLTAR", command=tela_inicial).pack(pady=10)

# Iniciar o jogo
tela_inicial()
root.mainloop()