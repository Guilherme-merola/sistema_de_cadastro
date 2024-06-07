import tkinter as tk

class Login(tk.Frame):
    def __init__(self: object, master: tk) -> None:
        super().__init__(master)
        self.pack()
        self.design()

    def design(self: object) -> None:
        #Login
        self.label_login = tk.Label(self, text="Login:")
        self.label_login.grid(row=0, column=0, padx=15, pady=5)
        self.input_login = tk.Entry(self)
        self.input_login.grid(row=0, column=1, padx=15, pady=5)

        #Senha
        self.label_senha = tk.Label(self, text="Senha:")
        self.label_senha.grid(row=1, column=0, padx=15, pady=5)
        self.input_senha = tk.Entry(self, show="*")
        self.input_senha.grid(row=1, column=1, padx=15, pady=5)

        #Mensagem
        self.label_mensagem = tk.Label(self, text="")
        self.label_mensagem.grid(row=2, column=1, padx=15, pady=10)

        #Botão
        self.botao_logar = tk.Button(self, text="Logar", command=lambda: self.logar(self.input_login.get(),
                                                                                    self.input_senha.get()))
        self.botao_logar.grid(row=2, column=0, padx=15, pady=10)
        self.botao_cadastrar = tk.Button(self, text="Cadastrar", command=lambda: self.master.trocar_tela("cadastro"))
        self.botao_cadastrar.grid(row=2, column=1, padx=15, pady=10)
        
    def logar(self: object, login: str, senha: str) -> tk:
        """
        Método responsável por chamar o master e executar seu método de
        realizar login.
        """
        return self.master.logar(login, senha)
    
    def exibir_mensagem(self: object, texto: str) -> tk:
        """
        Método resposável por exibir uma mensagem de erro no label_mensagem.
        """
        self.botao_cadastrar.grid(row=3, column=1, padx=15, pady=10)
        self.botao_logar.grid(row=3, column=0, padx=15, pady=10)
        return self.label_mensagem.config(text=texto)
        