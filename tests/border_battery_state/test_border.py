from tests import conftest
import pytest


class TestRun:
    """Проверка переключений BatteryState"""

    def test_01(self, test_data_01, test_result_01):
        """BatteryVoltage border value 500V => 800V.
        BatteryState Ready => Ready"""
        conftest.change_all_pins(start_params=test_data_01)
        conftest.check_all_params(start_params=test_data_01)
        conftest.api_lib.set_battery_voltage_pin(conftest.stand_address, 800)
        response = conftest.get_all_params()

        assert test_result_01 == response

    @pytest.mark.skip(reason='BUG-2. При переходе BatteryState в Error, ожидается что все PIN будут == 0. '
                             'Но Gear_1, Gear_2, AccPedal и BrakePedal == 0.01. В спецификации указано значение 0. '
                             'BUG-5. Отсутствует сброс ReqTorque в 0 Nm при повышении напряжения батареи выше 800V')
    def test_02(self, test_data_02, test_result_02):
        """BatteryVoltage border value 500V => 800.01V.
        BatteryState Ready => Error"""
        conftest.change_all_pins(start_params=test_data_02)
        conftest.check_all_params(start_params=test_data_02)
        conftest.api_lib.set_battery_voltage_pin(conftest.stand_address, 800.01)
        response = conftest.get_all_params()

        assert test_result_02 == response

    def test_03(self, test_data_03, test_result_03):
        """BatteryVoltage border value 500V => 400.01V.
        BatteryState Ready => Ready"""
        conftest.change_all_pins(start_params=test_data_03)
        conftest.check_all_params(start_params=test_data_03)
        conftest.api_lib.set_battery_voltage_pin(conftest.stand_address, 400.01)
        response = conftest.get_all_params()

        assert test_result_03 == response

    def test_04(self, test_data_04, test_result_04):
        """BatteryVoltage border value 500V => 400V.
        BatteryState Ready => NotReady"""
        conftest.change_all_pins(start_params=test_data_04)
        conftest.check_all_params(start_params=test_data_04)
        conftest.api_lib.set_battery_voltage_pin(conftest.stand_address, 400)
        response = conftest.get_all_params()

        assert test_result_04 == response

    def test_05(self, test_data_05, test_result_05):
        """BatteryVoltage border value 500V => 0.01V.
        BatteryState Ready => NotReady"""
        conftest.change_all_pins(start_params=test_data_05)
        conftest.check_all_params(start_params=test_data_05)
        conftest.api_lib.set_battery_voltage_pin(conftest.stand_address, 0.01)
        response = conftest.get_all_params()

        assert test_result_05 == response

    @pytest.mark.skip(reason='BUG-2. При переходе BatteryState в Error, ожидается что все PIN будут == 0. '
                             'Но Gear_1, Gear_2, AccPedal и BrakePedal == 0.01. В спецификации указано значение 0')
    def test_06(self, test_data_06, test_result_06):
        """BatteryVoltage border value 500V => 0V.
        BatteryState Ready => Error"""
        conftest.change_all_pins(start_params=test_data_06)
        conftest.check_all_params(start_params=test_data_06)
        conftest.api_lib.set_battery_voltage_pin(conftest.stand_address, 0)
        response = conftest.get_all_params()

        assert test_result_06 == response

    @pytest.mark.GearPositionNeutral
    @pytest.mark.BrakePedalStateError
    @pytest.mark.skip(reason='BUG-2. При переходе BatteryState в Error, ожидается что все PIN будут == 0. '
                             'Но Gear_1, Gear_2, AccPedal и BrakePedal == 0.01. В спецификации указано значение 0')
    def test_07(self, test_data_07, test_result_07):
        """BatteryVoltage border value 0V => 0.01V.
        BatteryState Error => NotReady"""
        conftest.change_all_pins(start_params=test_data_07)
        conftest.check_all_params(start_params=test_data_07)
        conftest.api_lib.set_battery_voltage_pin(conftest.stand_address, 0.01)
        response = conftest.get_all_params()

        assert test_result_07 == response

    @pytest.mark.GearPositionNeutral
    @pytest.mark.BrakePedalStateError
    @pytest.mark.skip(reason='BUG-2. При переходе BatteryState в Error, ожидается что все PIN будут == 0. '
                             'Но Gear_1, Gear_2, AccPedal и BrakePedal == 0.01. В спецификации указано значение 0')
    def test_08(self, test_data_08, test_result_08):
        """BatteryVoltage border value 0V => 400.01V.
        BatteryState Error => Ready"""
        conftest.change_all_pins(start_params=test_data_08)
        conftest.check_all_params(start_params=test_data_08)
        conftest.api_lib.set_battery_voltage_pin(conftest.stand_address, 400.01)
        response = conftest.get_all_params()

        assert test_result_08 == response

    @pytest.mark.skip(reason='BUG-2. При переходе BatteryState в Error, ожидается что все PIN будут == 0. '
                             'Но Gear_1, Gear_2, AccPedal и BrakePedal == 0.01. В спецификации указано значение 0')
    @pytest.mark.GearPositionNeutral
    def test_09(self, test_data_09, test_result_09):
        """BatteryVoltage border value 400V => 0V.
        BatteryState NotReady => Error"""
        conftest.change_all_pins(start_params=test_data_09)
        conftest.check_all_params(start_params=test_data_09)
        conftest.api_lib.set_battery_voltage_pin(conftest.stand_address, 0)
        response = conftest.get_all_params()

        assert test_result_09 == response

    @pytest.mark.GearPositionNeutral
    def test_10(self, test_data_10, test_result_10):
        """BatteryVoltage border value 400V => 400.01V.
        BatteryState NotReady => Ready"""
        conftest.change_all_pins(start_params=test_data_10)
        conftest.check_all_params(start_params=test_data_10)
        conftest.api_lib.set_battery_voltage_pin(conftest.stand_address, 400.01)
        response = conftest.get_all_params()

        assert test_result_10 == response
