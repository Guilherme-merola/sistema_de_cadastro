import json
import bcrypt

class Pessoa:
    def __init__(self: object, codigo: int, login: str, senha: str, email: str) -> None:
        self.__codigo = codigo
        self.__login = login
        self.__senha = senha
        self.__email = email

    @property
    def login(self: object) -> str:
        return self.__login
    
    @login.setter
    def login(self: object, login: str) -> None:
        self.__login = login
    
    @property
    def codigo(self: object) -> int:
        return self.__codigo
    
    @codigo.setter
    def codigo(self: object, novo_codigo: int) -> None:
        cadastro = Pessoa.carregar_cadastros()
        if novo_codigo in cadastro["Codigo"]:
            raise ValueError("Código já existente")
        self.__codigo = novo_codigo
    
    @property
    def senha(self: object) -> str:
        return self.__senha
    
    @senha.setter
    def senha(self: object, senha: str) -> None:
        self.__senha = senha

    @property
    def email(self: object) -> str:
        return self.__email
    
    @email.setter
    def email(self: object, email: str) -> None:
        self.__email = email

    def __str__(self: object) -> str:
        return f"""Código: {self.codigo}\n\
Login: {self.login}\n\
Senha: {self.senha}\n\
Email: {self.email}"""
    
    @staticmethod
    def cadastrar(login_fornecido: str, senha_fornecido: str, email_fornecido: str) -> None:
        """
        Função responsável por registrar os novos cadastro no arquivo JSON.

        O método verifica se a senha que foi fornecida já está registrada por algum outro cadastro,
        caso haja a utilização resultará em um erro, caso contrário prosseguirá para a escrita no JSON.

        O código do cadastro é feito automáticamente pelo sistema, não havendo a necessidade de saber
        qual o ultimo número cadastrado.  
        """
        cadastros = Pessoa.carregar_cadastros()
        max_codigo = max(cadastros["Codigo"]) if cadastros["Codigo"] else 0
        cadastros["Codigo"].append(max_codigo+1)
        cadastros["Login"].append(login_fornecido)
        cadastros["Senha"].append(Pessoa.criptografar_senha(senha_fornecido))
        cadastros["Email"].append(email_fornecido)
        with open("cadastros.json", "w", encoding="utf-8") as f:
            json.dump(cadastros, f, ensure_ascii=False, indent=4)
            

    @staticmethod
    def carregar_cadastros() -> dict:
        """
        Método responsável por buscar o arquivo JSON e retorná-lo para outros métodos que o chamam.
        """
        try:
            with open("cadastros.json", "r", encoding="utf-8") as f:
                dados = json.load(f)
        except FileNotFoundError:
            dados = {"Codigo": [], "Login": [], "Senha": [], "Email": []}
        return dados
    
    @staticmethod
    def logar(login_fornecido: str, senha_fornecida: str) -> None | object:
        """
        Método responsável por buscar o cadastro registrado e verificar se o login e senha
        informados estão salvos, caso o login e senha estejam corretos ira retornar um
        método responsável por instânciar objetos, caso contrário o retorno será None.
        """
        cadastros = Pessoa.carregar_cadastros()
        for indice, (login, senha) in enumerate(zip(cadastros["Login"], cadastros["Senha"])):
            if login == login_fornecido and Pessoa.verificar_senha(senha_real=senha, senha_informada=senha_fornecida):
                return Pessoa.instanciar_objeto(indice)
        return
    
    @staticmethod
    def buscar_cadastro_codigo(codigo_busca: int) -> None | object:
        """
        Método resposável por varrer o arquivo JSON e procurar algum registro com o código que
        foi passado como parâmetro, caso o código seja encontrado ira retornar um
        método responsável por instânciar objetos, caso contrário o retorno será None.
        """
        cadastros = Pessoa.carregar_cadastros()
        for indice, codigo in enumerate(cadastros["Codigo"]):
            if codigo == codigo_busca:
                return Pessoa.instanciar_objeto(indice)
        return

    @staticmethod
    def buscar_cadastro_login(login_busca: str) -> None | object:
        """
        Método resposável por varrer o arquivo JSON e procurar algum registro com o login que
        foi passado como parâmetro, caso o login seja encontrado ira retornar um
        método responsável por instânciar objetos, caso contrário o retorno será None.
        """
        cadastros = Pessoa.carregar_cadastros()
        for indice, login in enumerate(cadastros["Login"]):
            if login == login_busca:
                return Pessoa.instanciar_objeto(indice)
        return

    @staticmethod
    def instanciar_objeto(indice: int) -> object:
        """
        Método responsável por encontrar os objetos pelo seu indice no JSON e então 
        os retorna como um objeto.
        """
        cadastros = Pessoa.carregar_cadastros()
        return Pessoa(cadastros["Codigo"][indice], cadastros["Login"][indice],
                        cadastros["Senha"][indice], cadastros["Email"][indice])

    @staticmethod
    def criptografar_senha(senha: str) -> str:
        """
        Método resposável por criptografar a senha e retorna a senha criptografada.
        """
        criptografia = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt())
        return criptografia.decode("utf-8")
    
    @staticmethod
    def verificar_senha(senha_real: str, senha_informada: str) -> bool:
        """
        Método responsável por verificar se a senha informada está correta.
        Retorna um bool.
        """
        return bcrypt.checkpw(senha_informada.encode("utf-8"), senha_real.encode("utf-8"))
