class Motor:
    def __init__(self, num_motor: str, potencia: float, cilindrada: float, tipo_combustivel: str, num_cilindros: int, torque: float):
        if not isinstance(num_motor, str):
            raise TypeError("O numero do motor deve ser uma string")
        if not isinstance(potencia, float):
            raise TypeError("A potência deve ser um número decimal")
        if not isinstance(cilindrada, float):
            raise TypeError("A cilindrada deve ser um número decimal")
        if not isinstance(tipo_combustivel, str):
            raise TypeError("O tipo de combustível deve ser uma string")
        if not isinstance(num_cilindros, int):
            raise TypeError("O número de cilindros deve ser um número inteiro")
        if not isinstance(torque, float):
            raise TypeError("O torque deve ser um número decimal")

        self.__num_motor = num_motor
        self.__potencia = potencia
        self.__cilindrada = cilindrada
        self.__tipo_combustivel = tipo_combustivel
        self.__num_cilindros = num_cilindros
        self.__torque = torque

    @property
    def num_motor(self) -> str:
        return self.__num_motor

    @property
    def potencia(self) -> str:
        return self.__potencia

    @property
    def potencia(self) -> float:
        return self.__potencia

    @property
    def cilindrada(self) -> float:
        return self.__cilindrada

    @property
    def tipo_combustivel(self) -> str:
        return self.__tipo_combustivel

    @property
    def num_cilindros(self) -> int:
        return self.__num_cilindros

    @property
    def torque(self) -> float:
        return self.__torque