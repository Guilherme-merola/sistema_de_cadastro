from pessoa import Pessoa
import tkinter as tk
from login import Login
from cadastro import Cadastro
from tela_final import TelaFinal

class Main(tk.Tk):
    def __init__(self: object) -> None:
        super().__init__()
        self.__telas = {}
        self.__tela_atual = None
        self.adicionar_tela(Login, "login")
        self.adicionar_tela(Cadastro, "cadastro")
        self.adicionar_tela(TelaFinal, "tela_final")
        self.tela_atual = self.telas["login"](self)

    @property
    def telas(self: object) -> dict:
        return self.__telas
    
    @property
    def tela_atual(self: object) -> object:
        return self.__tela_atual
    
    @tela_atual.setter
    def tela_atual(self: object, tela: object) -> None:
        self.__tela_atual = tela

    def adicionar_tela(self: object, tela: Login | Cadastro | TelaFinal, nome: str) -> None:
        """
        Método responsável por adicionar as telas em um dicionario que servirão de armazenamento
        para as interfaces construidas.
        """
        if nome in self.telas:
            return
        else:
            self.telas[nome] = tela

    def trocar_tela(self: object, nome: str) -> None:
        """
        Método responsável por trocar a tela atual por outra interface passada como parâmetro.
        """
        if self.tela_atual is not None:
            self.tela_atual.pack_forget()
        self.tela_atual = self.telas[nome](self)
        self.tela_atual.pack(fill="both", expand=True)
        self.tela_atual.lift()

    def logar(self: object, login: str, senha: str) -> Pessoa | object:
        """
        Método responsável por executar o método logar da classe Pessoa e então instanciar um objeto
        desta classe.

        Há uma verificação se os dados foram preenchidos e se tudo estiver certo ira criar o 
        objeto de fato, caso contrário, resultará em uma mensagem avisando que deve preencher
        tais campos. 
        """
        if login and senha: 
            self.trocar_tela("tela_final")
            return Pessoa.logar(login, senha)
        else:
            return self.exibir_mensagem("Login Inválido")
            
    def cadastrar(self: object, login: str, senha: str, email: str) -> object:
        """
        Método resposável por executar o método cadastrar da classe Pessoa e após
        o cadastramento retornar a tela inicial de login.

        A função verifica se todos os dados foram preenchido e então executa o método
        de cadastrar, caso contrário, exibirá um mensagem informando que se deve 
        preencher todos os campos.
        """
        if login and senha and email:
            Pessoa.cadastrar(login, senha, email)
            return self.trocar_tela("login")
        else:
            return self.exibir_mensagem("Deve preencher todos os campos")

    def exibir_mensagem(self: object, texto: str) -> Login | Cadastro:
        """
        Método resposável por chamar os métodos da interfaces para exibir uma
        mensagem de erro.
        """
        return self.tela_atual.exibir_mensagem(texto)
            
if __name__ == "__main__":
    main = Main()
    main.mainloop()
