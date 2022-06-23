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
def test_data_06():
    return {'BatteryVoltage': 500, 'BrakePedal': 2, 'AccPedal': 2.5, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Released', 'GearPosition': 'Drive', 'AccPedalPos': '50 %',
            'ReqTorque': '5000 Nm'}


@pytest.fixture()
def test_data_07():
    return {'BatteryVoltage': 500, 'BrakePedal': 2, 'AccPedal': 2.5, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Released', 'GearPosition': 'Drive', 'AccPedalPos': '50 %',
            'ReqTorque': '5000 Nm'}


@pytest.fixture()
def test_data_08():
    return {'BatteryVoltage': 500, 'BrakePedal': 2, 'AccPedal': 2.5, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Released', 'GearPosition': 'Drive', 'AccPedalPos': '50 %',
            'ReqTorque': '5000 Nm'}


@pytest.fixture()
def test_result_01():
    return {'BatteryVoltage': 500, 'BrakePedal': 2, 'AccPedal': 0.99, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Released', 'GearPosition': 'Drive', 'AccPedalPos': 'Error',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_result_02():
    return {'BatteryVoltage': 500, 'BrakePedal': 2, 'AccPedal': 1.99, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Released', 'GearPosition': 'Drive', 'AccPedalPos': '0 %',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_result_03():
    return {'BatteryVoltage': 500, 'BrakePedal': 2, 'AccPedal': 2, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Released', 'GearPosition': 'Drive', 'AccPedalPos': '30 %',
            'ReqTorque': '3000 Nm'}


@pytest.fixture()
def test_result_04():
    return {'BatteryVoltage': 500, 'BrakePedal': 2, 'AccPedal': 2.49, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Released', 'GearPosition': 'Drive', 'AccPedalPos': '30 %',
            'ReqTorque': '3000 Nm'}


@pytest.fixture()
def test_result_05():
    return {'BatteryVoltage': 500, 'BrakePedal': 2, 'AccPedal': 2.99, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Released', 'GearPosition': 'Drive', 'AccPedalPos': '50 %',
            'ReqTorque': '5000 Nm'}


@pytest.fixture()
def test_result_06():
    return {'BatteryVoltage': 500, 'BrakePedal': 2, 'AccPedal': 3, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Released', 'GearPosition': 'Drive', 'AccPedalPos': '100 %',
            'ReqTorque': '10000 Nm'}


@pytest.fixture()
def test_result_07():
    return {'BatteryVoltage': 500, 'BrakePedal': 2, 'AccPedal': 3.49, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Released', 'GearPosition': 'Drive', 'AccPedalPos': '100 %',
            'ReqTorque': '10000 Nm'}


@pytest.fixture()
def test_result_08():
    return {'BatteryVoltage': 500, 'BrakePedal': 2, 'AccPedal': 3.5, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Released', 'GearPosition': 'Drive', 'AccPedalPos': 'Error',
            'ReqTorque': '0 Nm'}
