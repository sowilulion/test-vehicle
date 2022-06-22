from settings import Settings
from library import Library
import pytest
import builtins


set_lib = Settings()
api_lib = Library()
stand_address = set_lib.get_host() + ':' + set_lib.get_port()
print(api_lib.get_all_pins(stand_address).json())
print(api_lib.get_gear1_pin(stand_address).json())
print(api_lib.get_gear2_pin(stand_address).json())
print(api_lib.get_acc_pedal_pin(stand_address).json())
print(api_lib.get_brake_pedal_pin(stand_address).json())
print(api_lib.get_battery_voltage_pin(stand_address).json())
print(api_lib.set_gear1_pin(stand_address, 1))
print(api_lib.set_gear2_pin(stand_address, 2))
print(api_lib.set_acc_pedal_pin(stand_address, 3))
print(api_lib.set_brake_pedal_pin(stand_address, 4))
print(api_lib.set_battery_voltage_pin(stand_address, 5))
print(api_lib.set_all_pins(address=stand_address,
                           gear1_value=1,
                           gear2_value=2,
                           acc_pedal_value=1,
                           brake_pedal_value=1,
                           battery_voltage_value=1).content)
print(api_lib.get_all_pins(stand_address).json())
print(api_lib.get_all_signals(stand_address).json())
print(api_lib.get_gear_position_signal(stand_address).json())
print(api_lib.get_acc_pedal_pos_signal(stand_address).json())
print(api_lib.get_brake_pedal_state_signal(stand_address).json())
print(api_lib.get_req_torque_signal(stand_address).json())
print(api_lib.get_battery_state_signal(stand_address).json())


def change_all_pins(stand_address, start_params):
    api_lib.set_battery_voltage_pin(stand_address, 500)
    api_lib.set_brake_pedal_pin(stand_address, 1)
    api_lib.set_acc_pedal_pin(stand_address, 1)

    api_lib.set_gear1_pin(stand_address, start_params["Gear_1"])
    api_lib.set_gear2_pin(stand_address, start_params["Gear_2"])
    api_lib.set_battery_voltage_pin(stand_address, start_params["BatteryVoltage"])
    api_lib.set_brake_pedal_pin(stand_address, start_params["BrakePedal"])
    api_lib.set_acc_pedal_pin(stand_address, start_params["AccPedal"])


def get_all_params(stand_address):
    response_gear1_pin = api_lib.get_gear1_pin(stand_address).json()
    response_gear2_pin = api_lib.get_gear2_pin(stand_address).json()
    response_acc_pedal_pin = api_lib.get_acc_pedal_pin(stand_address).json()
    response_brake_pedal_pin = api_lib.get_brake_pedal_pin(stand_address).json()
    response_battery_voltage_pin = api_lib.get_battery_voltage_pin(stand_address).json()
    response_gear_position_signal = api_lib.get_gear_position_signal(stand_address).json()
    response_acc_pedal_pos_signal = api_lib.get_acc_pedal_pos_signal(stand_address).json()
    response_brake_pedal_state_signal = api_lib.get_brake_pedal_state_signal(stand_address).json()
    response_req_torque_signal = api_lib.get_req_torque_signal(stand_address).json()
    response_battery_state_signal = api_lib.get_battery_state_signal(stand_address).json()

    return {'BatteryVoltage': response_battery_voltage_pin['Voltage'],
            'BrakePedal': response_brake_pedal_pin['Voltage'],
            'AccPedal': response_acc_pedal_pin['Voltage'],
            'Gear_2': response_gear2_pin['Voltage'],
            'Gear_1': response_gear1_pin['Voltage'],
            'BatteryState': response_battery_state_signal['Value'],
            'BrakePedalState': response_brake_pedal_state_signal['Value'],
            'GearPosition': response_gear_position_signal['Value'],
            'AccPedalPos': response_acc_pedal_pos_signal['Value'],
            'ReqTorque': response_req_torque_signal['Value']}


def check_all_params(stand_address, start_params):
    response = get_all_params(stand_address)

    if response['Gear_1'] != start_params['Gear_1']:
        raise Exception('PIN Gear_1 не соответствует назначенному. Тест не может быть продолжен')
    if response['Gear_2'] != start_params['Gear_2']:
        raise Exception('PIN Gear_2 не соответствует назначенному. Тест не может быть продолжен')
    if response['AccPedal'] != start_params['AccPedal']:
        raise Exception('PIN AccPedal не соответствует назначенному. Тест не может быть продолжен')
    if response['BrakePedal'] != start_params['BrakePedal']:
        raise Exception('PIN BrakePedal не соответствует назначенному. Тест не может быть продолжен')
    if response['BatteryVoltage'] != start_params['BatteryVoltage']:
        raise Exception('PIN BatteryVoltage не соответствует назначенному. Тест не может быть продолжен')
    if response['GearPosition'] != start_params['GearPosition']:
        raise Exception('Signal GearPosition не соответствует назначенному. Тест не может быть продолжен')
    if response['AccPedalPos'] != start_params['AccPedalPos']:
        raise Exception('Signal AccPedalPos не соответствует назначенному. Тест не может быть продолжен')
    if response['BrakePedalState'] != start_params['BrakePedalState']:
        raise Exception('Signal BrakePedalState не соответствует назначенному. Тест не может быть продолжен')
    if response['ReqTorque'] != start_params['ReqTorque']:
        raise Exception('Signal ReqTorque не соответствует назначенному. Тест не может быть продолжен')
    if response['BatteryState'] != start_params['BatteryState']:
        raise Exception('Signal BatteryState не соответствует назначенному. Тест не может быть продолжен')

@pytest.fixture()
def test_data1():
    return {'BatteryVoltage': 500,
            'BrakePedal': 2,
            'AccPedal': 2.5,
            'Gear_2': 0.67,
            'Gear_1': 3.12,
            'BatteryState': 'Ready',
            'BrakePedalState': 'Released',
            'GearPosition': 'Drive',
            'AccPedalPos': '50 %',
            'ReqTorque': '5000 Nm'}


@pytest.fixture()
def clean_pins():
    api_lib.set_battery_voltage_pin(stand_address, 0)

    yield

    print('Test end')


@pytest.fixture()
def test_result1():
    return {'BatteryVoltage': 500,
            'BrakePedal': 2,
            'AccPedal': 1,
            'Gear_2': 0.67,
            'Gear_1': 3.12,
            'BatteryState': 'Ready',
            'BrakePedalState': 'Released',
            'GearPosition': 'Drive',
            'AccPedalPos': '0 %',
            'ReqTorque': '0 Nm'}


def test_first(clean_pins, test_data1, test_result1):
    change_all_pins(stand_address=stand_address, start_params=test_data1)
    check_all_params(stand_address=stand_address, start_params=test_data1)
    api_lib.set_acc_pedal_pin(stand_address, 1)
    response = get_all_params(stand_address)

    assert test_result1 == response
