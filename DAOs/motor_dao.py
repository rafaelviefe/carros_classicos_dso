from DAOs.dao import DAO
from entidade.motor import Motor

class MotorDAO(DAO):
    def __init__(self):
        super().__init__('motores.pkl')

    def add(self, motor):
        if((motor is not None) and isinstance(motor, Motor) and isinstance(motor.num_motor, str)):
            super().add(motor.num_motor, motor)

    def update(self, motor):
        if((motor is not None) and isinstance(motor, Motor) and isinstance(motor.num_motor, str)):
            super().update(motor.num_motor, motor)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)