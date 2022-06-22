import requests
import json


class Pins:
    """Класс по работе с PIN API"""

    ALL_PINS_URL = 'api/pins'
    PIN_ID_GEAR1 = 1
    PIN_ID_GEAR2 = 2
    PIN_ID_ACC_PEDAL = 3
    PIN_ID_BRAKE_PEDAL = 4
    PIN_ID_BATTERY_VOLTAGE = 5
    SIGNAL_URL_GEAR1 = f'{ALL_PINS_URL}/{PIN_ID_GEAR1}'
    SIGNAL_URL_GEAR2 = f'{ALL_PINS_URL}/{PIN_ID_GEAR2}'
    SIGNAL_URL_ACC_PEDAL = f'{ALL_PINS_URL}/{PIN_ID_ACC_PEDAL}'
    SIGNAL_URL_BRAKE_PEDAL = f'{ALL_PINS_URL}/{PIN_ID_BRAKE_PEDAL}'
    SIGNAL_URL_BATTERY_VOLTAGE = f'{ALL_PINS_URL}/{PIN_ID_BATTERY_VOLTAGE}'

    def get_all_pins(self, address):
        """API получение списка всех PIN-ов"""

        url = f'{address}/{self.ALL_PINS_URL}'
        print(url)
        return requests.get(url=url)

    def get_gear1_pin(self, address):
        """API получение PIN GEAR1"""

        url = f'{address}/{self.SIGNAL_URL_GEAR1}'
        return requests.get(url=url)

    def get_gear2_pin(self, address):
        """API получение PIN GEAR2"""

        url = f'{address}/{self.SIGNAL_URL_GEAR2}'
        return requests.get(url=url)

    def get_acc_pedal_pin(self, address):
        """API получение PIN ACC_PEDAL"""

        url = f'{address}/{self.SIGNAL_URL_ACC_PEDAL}'
        return requests.get(url=url)

    def get_brake_pedal_pin(self, address):
        """API получение PIN BRAKE_PEDAL"""

        url = f'{address}/{self.SIGNAL_URL_BRAKE_PEDAL}'
        return requests.get(url=url)

    def get_battery_voltage_pin(self, address):
        """API получение PIN BATTERY_VOLTAGE"""

        url = f'{address}/{self.SIGNAL_URL_BATTERY_VOLTAGE}'
        return requests.get(url=url)

    def set_gear1_pin(self, address, value):
        """API смены значения PIN GEAR1"""

        url = f'{address}/{self.SIGNAL_URL_GEAR1}/update_pin'
        body = {'Voltage': value}
        return requests.post(url=url, data=body)

    def set_gear2_pin(self, address, value):
        """API смены значения PIN GEAR2"""

        url = f'{address}/{self.SIGNAL_URL_GEAR2}/update_pin'
        body = {'Voltage': value}
        return requests.post(url=url, data=body)

    def set_acc_pedal_pin(self, address, value):
        """API смены значения PIN ACC_PEDAL"""

        url = f'{address}/{self.SIGNAL_URL_ACC_PEDAL}/update_pin'
        body = {'Voltage': value}
        return requests.post(url=url, data=body)

    def set_brake_pedal_pin(self, address, value):
        """API смены значения PIN BRAKE_PEDAL"""

        url = f'{address}/{self.SIGNAL_URL_BRAKE_PEDAL}/update_pin'
        body = {'Voltage': value}
        return requests.post(url=url, data=body)

    def set_battery_voltage_pin(self, address, value):
        """API смены значения PIN BATTERY_VOLTAGE"""

        url = f'{address}/{self.SIGNAL_URL_BATTERY_VOLTAGE}/update_pin'
        body = {'Voltage': value}
        return requests.post(url=url, data=body)

    def set_all_pins(self, address, gear1_value=None, gear2_value=None, acc_pedal_value=None, brake_pedal_value=None,
                     battery_voltage_value=None):
        """API смены значения всех PIN-ов"""

        url = f'{address}/{self.ALL_PINS_URL}/update_pins'
        body = {"Pins": []}
        if gear1_value is not None:
            gear1_body = {"PinId": self.PIN_ID_GEAR1,
                          "Voltage": gear1_value}
            body["Pins"].append(gear1_body)
        if gear2_value is not None:
            gear2_body = {"PinId": self.PIN_ID_GEAR2,
                          "Voltage": gear2_value}
            body["Pins"].append(gear2_body)
        if acc_pedal_value is not None:
            acc_pedal_body = {"PinId": self.PIN_ID_ACC_PEDAL,
                              "Voltage": acc_pedal_value}
            body["Pins"].append(acc_pedal_body)
        if brake_pedal_value is not None:
            brake_pedal_body = {"PinId": self.PIN_ID_BRAKE_PEDAL,
                                "Voltage": brake_pedal_value}
            body["Pins"].append(brake_pedal_body)
        if battery_voltage_value is not None:
            battery_voltage_body = {"PinId": self.PIN_ID_BATTERY_VOLTAGE,
                                    "Voltage": battery_voltage_value}
            body["Pins"].append(battery_voltage_body)

        print(json.dumps(body))
        print(url)

        return requests.post(url=url, data=json.dumps(body))
