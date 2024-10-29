from entidade.motor import Motor
from entidade.roda import Roda
from entidade.pintura import Pintura
from limite.tela_peca import TelaPeca

class ControladorPecas:
    def __init__(self, controlador_sistema):
        self.__pecas = {
            "motor": [],
            "roda": [],
            "pintura": []
        }
        self.__tela_peca = TelaPeca()
        self.__controlador_sistema = controlador_sistema

    # Busca um motor específico pelo número do motor
    def pega_motor_por_num(self, num_motor: str):
        for motor in self.__pecas["motor"]:
            if motor.num_motor == num_motor:
                return motor
        return None

    # Busca uma roda específica pelo número de série
    def pega_roda_por_num(self, num_serie: str):
        for roda in self.__pecas["roda"]:
            if roda.num_serie == num_serie:
                return roda
        return None

    # Busca uma pintura específica pelo código de cor
    def pega_pintura_por_cod(self, codigo_cor: str):
        for pintura in self.__pecas["pintura"]:
            if pintura.codigo_cor == codigo_cor:
                return pintura
        return None

    # Adiciona uma peça ao sistema, garantindo que não exista duplicidade
    def inclui_peca(self):
        tipo_peca = self.__tela_peca.seleciona_tipo()
        if tipo_peca == "motor":
            dados_motor = self.__tela_peca.pega_dados_motor()
            if self.pega_motor_por_num(dados_motor["num_motor"]):
                self.__tela_peca.mostra_mensagem("Motor já cadastrado.")
                return
            motor = Motor(**dados_motor)
            self.__pecas["motor"].append(motor)
            self.__tela_peca.mostra_mensagem("Motor incluído com sucesso!")

        elif tipo_peca == "roda":
            dados_roda = self.__tela_peca.pega_dados_roda()
            if self.pega_roda_por_num(dados_roda["num_serie"]):
                self.__tela_peca.mostra_mensagem("Roda já cadastrada.")
                return
            roda = Roda(**dados_roda)
            self.__pecas["roda"].append(roda)
            self.__tela_peca.mostra_mensagem("Roda incluída com sucesso!")

        elif tipo_peca == "pintura":
            dados_pintura = self.__tela_peca.pega_dados_pintura()
            if self.pega_pintura_por_cod(dados_pintura["codigo_cor"]):
                self.__tela_peca.mostra_mensagem("Pintura já cadastrada.")
                return
            pintura = Pintura(**dados_pintura)
            self.__pecas["pintura"].append(pintura)
            self.__tela_peca.mostra_mensagem("Pintura incluída com sucesso!")

    # Lista todas as peças de um tipo específico, exibindo as informações detalhadas de cada peça
    def lista_pecas(self):
        tipo_peca = self.__tela_peca.seleciona_tipo()

        if tipo_peca == "motor":
            if not self.__pecas["motor"]:
                self.__tela_peca.mostra_mensagem("Nenhum motor cadastrado.")
            else:
                for motor in self.__pecas["motor"]:
                    self.__tela_peca.mostra_motor({
                        "num_motor": motor.num_motor, "potencia": motor.potencia,
                        "cilindrada": motor.cilindrada, "tipo_combustivel": motor.tipo_combustivel,
                        "num_cilindros": motor.num_cilindros, "torque": motor.torque
                    })

        elif tipo_peca == "roda":
            if not self.__pecas["roda"]:
                self.__tela_peca.mostra_mensagem("Nenhuma roda cadastrada.")
            else:
                for roda in self.__pecas["roda"]:
                    self.__tela_peca.mostra_roda({
                        "num_serie": roda.num_serie, "largura": roda.largura,
                        "perfil": roda.perfil, "tipo": roda.tipo, "diametro_aro": roda.diametro_aro,
                        "indice_carga": roda.indice_carga, "indice_velocidade": roda.indice_velocidade
                    })

        elif tipo_peca == "pintura":
            if not self.__pecas["pintura"]:
                self.__tela_peca.mostra_mensagem("Nenhuma pintura cadastrada.")
            else:
                for pintura in self.__pecas["pintura"]:
                    self.__tela_peca.mostra_pintura({
                        "codigo_cor": pintura.codigo_cor, "cor": pintura.cor,
                        "tipo": pintura.tipo, "camadas": pintura.camadas
                    })

    # Exclui uma peça, verificando primeiro se ela não está em uso por algum carro
    def exclui_peca(self):
        tipo_peca, identificador = self.__tela_peca.seleciona_peca()

        if tipo_peca == "motor":
            motor = self.pega_motor_por_num(identificador)
            if motor and self.__controlador_sistema.controlador_carros_classicos.verifica_disponibilidade_peca(tipo_peca, identificador):
                self.__tela_peca.mostra_mensagem("Motor está em uso em um carro. Não pode ser excluído.")
                return
            if motor:
                self.__pecas["motor"].remove(motor)
                self.__tela_peca.mostra_mensagem("Motor excluído com sucesso!")
                return
            self.__tela_peca.mostra_mensagem("Motor não encontrado.")

        elif tipo_peca == "roda":
            roda = self.pega_roda_por_num(identificador)
            if roda and self.__controlador_sistema.controlador_carros_classicos.verifica_disponibilidade_peca(tipo_peca, identificador):
                self.__tela_peca.mostra_mensagem("Roda está em uso em um carro. Não pode ser excluída.")
                return
            if roda:
                self.__pecas["roda"].remove(roda)
                self.__tela_peca.mostra_mensagem("Roda excluída com sucesso!")
                return
            self.__tela_peca.mostra_mensagem("Roda não encontrada.")

        elif tipo_peca == "pintura":
            pintura = self.pega_pintura_por_cod(identificador)
            if pintura and self.__controlador_sistema.controlador_carros_classicos.verifica_disponibilidade_peca(tipo_peca, identificador):
                self.__tela_peca.mostra_mensagem("Pintura está em uso em um carro. Não pode ser excluída.")
                return
            if pintura:
                self.__pecas["pintura"].remove(pintura)
                self.__tela_peca.mostra_mensagem("Pintura excluída com sucesso!")
                return
            self.__tela_peca.mostra_mensagem("Pintura não encontrada.")

    def abre_tela(self):
        lista_opcoes = {
            1: self.inclui_peca,
            2: self.lista_pecas,
            3: self.exclui_peca,
            0: self.__controlador_sistema.abre_tela
        }
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_peca.tela_opcoes()]()