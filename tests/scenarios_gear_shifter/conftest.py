import pytest


@pytest.fixture()
def test_data_01():
    return {'BatteryVoltage': 500, 'BrakePedal': 1, 'AccPedal': 1, 'Gear_2': 3.12, 'Gear_1': 0.67,
            'BatteryState': 'Ready', 'BrakePedalState': 'Pressed', 'GearPosition': 'Park', 'AccPedalPos': '0 %',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_data_02():
    return {'BatteryVoltage': 500, 'BrakePedal': 1, 'AccPedal': 1, 'Gear_2': 3.12, 'Gear_1': 0.67,
            'BatteryState': 'Ready', 'BrakePedalState': 'Pressed', 'GearPosition': 'Park', 'AccPedalPos': '0 %',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_data_03():
    return {'BatteryVoltage': 500, 'BrakePedal': 1, 'AccPedal': 1, 'Gear_2': 3.12, 'Gear_1': 0.67,
            'BatteryState': 'Ready', 'BrakePedalState': 'Pressed', 'GearPosition': 'Park', 'AccPedalPos': '0 %',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_data_04():
    return {'BatteryVoltage': 500, 'BrakePedal': 1, 'AccPedal': 1, 'Gear_2': 3.12, 'Gear_1': 0.67,
            'BatteryState': 'Ready', 'BrakePedalState': 'Pressed', 'GearPosition': 'Park', 'AccPedalPos': '0 %',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_data_05():
    return {'BatteryVoltage': 400, 'BrakePedal': 1, 'AccPedal': 1, 'Gear_2': 3.12, 'Gear_1': 0.67,
            'BatteryState': 'NotReady', 'BrakePedalState': 'Pressed', 'GearPosition': 'Neutral', 'AccPedalPos': '0 %',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_data_06():
    return {'BatteryVoltage': 500, 'BrakePedal': 1, 'AccPedal': 2.5, 'Gear_2': 3.12, 'Gear_1': 0.67,
            'BatteryState': 'Ready', 'BrakePedalState': 'Pressed', 'GearPosition': 'Park', 'AccPedalPos': '50 %',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_data_07():
    return {'BatteryVoltage': 500, 'BrakePedal': 2, 'AccPedal': 1, 'Gear_2': 3.12, 'Gear_1': 0.67,
            'BatteryState': 'Ready', 'BrakePedalState': 'Released', 'GearPosition': 'Park', 'AccPedalPos': '0 %',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_data_08():
    return {'BatteryVoltage': 500, 'BrakePedal': 0, 'AccPedal': 1, 'Gear_2': 3.12, 'Gear_1': 0.67,
            'BatteryState': 'Ready', 'BrakePedalState': 'Error', 'GearPosition': 'Neutral', 'AccPedalPos': '0 %',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_data_09():
    return {'BatteryVoltage': 500, 'BrakePedal': 1, 'AccPedal': 0, 'Gear_2': 3.12, 'Gear_1': 0.67,
            'BatteryState': 'Ready', 'BrakePedalState': 'Pressed', 'GearPosition': 'Park', 'AccPedalPos': 'Error',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_result_01():
    return {'BatteryVoltage': 500, 'BrakePedal': 1, 'AccPedal': 1, 'Gear_2': 2.28, 'Gear_1': 1.48,
            'BatteryState': 'Ready', 'BrakePedalState': 'Pressed', 'GearPosition': 'Neutral', 'AccPedalPos': '0 %',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_result_02():
    return {'BatteryVoltage': 500, 'BrakePedal': 1, 'AccPedal': 1, 'Gear_2': 1.48, 'Gear_1': 2.28,
            'BatteryState': 'Ready', 'BrakePedalState': 'Pressed', 'GearPosition': 'Reverse', 'AccPedalPos': '0 %',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_result_03():
    return {'BatteryVoltage': 500, 'BrakePedal': 1, 'AccPedal': 1, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Pressed', 'GearPosition': 'Drive', 'AccPedalPos': '0 %',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_result_04():
    return {'BatteryVoltage': 500, 'BrakePedal': 1, 'AccPedal': 1, 'Gear_2': 2.22, 'Gear_1': 1.11,
            'BatteryState': 'Ready', 'BrakePedalState': 'Pressed', 'GearPosition': 'Neutral', 'AccPedalPos': '0 %',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_result_05():
    return {'BatteryVoltage': 400, 'BrakePedal': 1, 'AccPedal': 1, 'Gear_2': 3.12, 'Gear_1': 0.67,
            'BatteryState': 'NotReady', 'BrakePedalState': 'Pressed', 'GearPosition': 'Neutral', 'AccPedalPos': '0 %',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_result_06():
    return {'BatteryVoltage': 500, 'BrakePedal': 1, 'AccPedal': 2.5, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Pressed', 'GearPosition': 'Park', 'AccPedalPos': '50 %',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_result_07():
    return {'BatteryVoltage': 500, 'BrakePedal': 2, 'AccPedal': 1, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Released', 'GearPosition': 'Park', 'AccPedalPos': '0 %',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_result_08():
    return {'BatteryVoltage': 500, 'BrakePedal': 0, 'AccPedal': 1, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Error', 'GearPosition': 'Neutral', 'AccPedalPos': '0 %',
            'ReqTorque': '0 Nm'}


@pytest.fixture()
def test_result_09():
    return {'BatteryVoltage': 500, 'BrakePedal': 1, 'AccPedal': 0, 'Gear_2': 0.67, 'Gear_1': 3.12,
            'BatteryState': 'Ready', 'BrakePedalState': 'Pressed', 'GearPosition': 'Park', 'AccPedalPos': 'Error',
            'ReqTorque': '0 Nm'}
