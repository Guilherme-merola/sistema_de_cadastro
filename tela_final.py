import tkinter as tk

class TelaFinal(tk.Frame):
    def __init__(self: object, master: tk) -> None:
        super().__init__(master)
        self.pack()
        self.design()

    def design(self: object) -> None:
        #Label
        self.texto = tk.Label(self, text="Login realizado com sucesso!")
        self.texto.pack(padx=15, pady=10)

        #Botão
        self.botao_voltar = tk.Button(self, text="Voltar", command=lambda: self.master.trocar_tela("login"))
        self.botao_voltar.pack(padx=15, pady=10)