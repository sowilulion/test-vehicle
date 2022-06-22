import requests


class Signals:
    """Класс по работе с Signals API"""

    ALL_SIGNALS_URL = 'api/signals'
    SIGNAL_ID_GEAR_POSITION = 1
    SIGNAL_ID_ACC_PEDAL_POS = 2
    SIGNAL_ID_BRAKE_PEDAL_STATE = 3
    SIGNAL_ID_REQ_TORQUE = 4
    SIGNAL_ID_BATTERY_STATE = 5

    def get_all_signals(self, address):
        """Метод получения состояния всех сигналов"""

        url = f'{address}/{self.ALL_SIGNALS_URL}'
        return requests.get(url=url)

    def get_gear_position_signal(self, address):
        """Метод получения состояния сигнала GearPosition"""

        url = f'{address}/{self.ALL_SIGNALS_URL}/{self.SIGNAL_ID_GEAR_POSITION}'
        return requests.get(url=url)

    def get_acc_pedal_pos_signal(self, address):
        """Метод получения состояния сигнала AccPedalPos"""

        url = f'{address}/{self.ALL_SIGNALS_URL}/{self.SIGNAL_ID_ACC_PEDAL_POS}'
        return requests.get(url=url)

    def get_brake_pedal_state_signal(self, address):
        """Метод получения состояния сигнала BrakePedalState"""

        url = f'{address}/{self.ALL_SIGNALS_URL}/{self.SIGNAL_ID_BRAKE_PEDAL_STATE}'
        return requests.get(url=url)

    def get_req_torque_signal(self, address):
        """Метод получения состояния сигнала ReqTorque"""

        url = f'{address}/{self.ALL_SIGNALS_URL}/{self.SIGNAL_ID_REQ_TORQUE}'
        return requests.get(url=url)

    def get_battery_state_signal(self, address):
        """Метод получения состояния сигнала BatteryState"""

        url = f'{address}/{self.ALL_SIGNALS_URL}/{self.SIGNAL_ID_BATTERY_STATE}'
        return requests.get(url=url)
