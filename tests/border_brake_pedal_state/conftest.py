import pytest


@pytest.fixture()
def test_data_01():
    return {'BatteryVoltage': 500, 'BrakePedal': 2, 'AccPedal': 2.5, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Released', 'GearPosition': 'Drive', 'AccPedalPos': '50 %',
            'ReqTorque': '5000 Nm'}


@pytest.fixture()
def test_data_02():
    return {'BatteryVoltage': 500, 'BrakePedal': 2, 'AccPedal': 2.5, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Released', 'GearPosition': 'Drive', 'AccPedalPos': '50 %',
            'ReqTorque': '5000 Nm'}


@pytest.fixture()
def test_data_03():
    return {'BatteryVoltage': 500, 'BrakePedal': 2, 'AccPedal': 2.5, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Released', 'GearPosition': 'Drive', 'AccPedalPos': '50 %',
            'ReqTorque': '5000 Nm'}


@pytest.fixture()
def test_data_04():
    return {'BatteryVoltage': 500, 'BrakePedal': 2, 'AccPedal': 2.5, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Released', 'GearPosition': 'Drive', 'AccPedalPos': '50 %',
            'ReqTorque': '5000 Nm'}


@pytest.fixture()
def test_data_05():
    return {'BatteryVoltage': 500, 'BrakePedal': 2, 'AccPedal': 2.5, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Released', 'GearPosition': 'Drive', 'AccPedalPos': '50 %',
            'ReqTorque': '5000 Nm'}


@pytest.fixture()
def test_result_01():
    return {'BatteryVoltage': 500, 'BrakePedal': 1.99, 'AccPedal': 2.5, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Pressed', 'GearPosition': 'Drive', 'AccPedalPos': '50 %',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_result_02():
    return {'BatteryVoltage': 500, 'BrakePedal': 2.99, 'AccPedal': 2.5, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Released', 'GearPosition': 'Drive', 'AccPedalPos': '50 %',
            'ReqTorque': '5000 Nm'}


@pytest.fixture()
def test_result_03():
    return {'BatteryVoltage': 500, 'BrakePedal': 3, 'AccPedal': 2.5, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Error', 'GearPosition': 'Neutral', 'AccPedalPos': '50 %',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_result_04():
    return {'BatteryVoltage': 500, 'BrakePedal': 1, 'AccPedal': 2.5, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Pressed', 'GearPosition': 'Drive', 'AccPedalPos': '50 %',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_result_05():
    return {'BatteryVoltage': 500, 'BrakePedal': 0.99, 'AccPedal': 2.5, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Error', 'GearPosition': 'Neutral', 'AccPedalPos': '50 %',
            'ReqTorque': '0 Nm'}
