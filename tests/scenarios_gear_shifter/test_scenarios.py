from tests import conftest


class TestRun:
    """Проверка переключения передач Gear Shifter"""

    def test_01(self, test_data_01, test_result_01):
        """GearPosition Park => Neutral."""
        conftest.change_all_pins(start_params=test_data_01)
        conftest.check_all_params(start_params=test_data_01)
        conftest.api_lib.set_gear1_pin(conftest.stand_address, 1.48)
        conftest.api_lib.set_gear2_pin(conftest.stand_address, 2.28)
        response = conftest.get_all_params()

        assert test_result_01 == response

    def test_02(self, test_data_02, test_result_02):
        """GearPosition Park => Reverse."""
        conftest.change_all_pins(start_params=test_data_02)
        conftest.check_all_params(start_params=test_data_02)
        conftest.api_lib.set_gear1_pin(conftest.stand_address, 2.28)
        conftest.api_lib.set_gear2_pin(conftest.stand_address, 1.48)
        response = conftest.get_all_params()

        assert test_result_02 == response

    def test_03(self, test_data_03, test_result_03):
        """GearPosition Park => Drive."""
        conftest.change_all_pins(start_params=test_data_03)
        conftest.check_all_params(start_params=test_data_03)
        conftest.api_lib.set_gear1_pin(conftest.stand_address, 3.12)
        conftest.api_lib.set_gear2_pin(conftest.stand_address, 0.67)
        response = conftest.get_all_params()

        assert test_result_03 == response

    def test_04(self, test_data_04, test_result_04):
        """GearPosition Park => Neutral.
        При выходе за обычные значения PIN1&2"""
        conftest.change_all_pins(start_params=test_data_04)
        conftest.check_all_params(start_params=test_data_04)
        conftest.api_lib.set_gear1_pin(conftest.stand_address, 1.11)
        conftest.api_lib.set_gear2_pin(conftest.stand_address, 2.22)
        response = conftest.get_all_params()

        assert test_result_04 == response

    def test_05(self, test_data_05, test_result_05):
        """Negative. GearPosition Neutral => Park.
        If BatteryState == Not Ready"""
        conftest.change_all_pins(start_params=test_data_05)
        conftest.check_all_params(start_params=test_data_05)
        conftest.api_lib.set_gear1_pin(conftest.stand_address, 0.67)
        conftest.api_lib.set_gear2_pin(conftest.stand_address, 3.12)
        response = conftest.get_all_params()

        assert test_result_05 == response

    def test_06(self, test_data_06, test_result_06):
        """Negative. GearPosition Park => Drive.
        If AccPedalPos == 50%"""
        conftest.change_all_pins(start_params=test_data_06)
        conftest.check_all_params(start_params=test_data_06)
        conftest.api_lib.set_gear1_pin(conftest.stand_address, 3.12)
        conftest.api_lib.set_gear2_pin(conftest.stand_address, 0.67)
        response = conftest.get_all_params()

        assert test_result_06 == response

    def test_07(self, test_data_07, test_result_07):
        """Negative. GearPosition Park => Drive.
        If BrakePedalState == Released"""
        conftest.change_all_pins(start_params=test_data_07)
        conftest.check_all_params(start_params=test_data_07)
        conftest.api_lib.set_gear1_pin(conftest.stand_address, 3.12)
        conftest.api_lib.set_gear2_pin(conftest.stand_address, 0.67)
        response = conftest.get_all_params()

        assert test_result_07 == response

    def test_08(self, test_data_08, test_result_08):
        """Negative. GearPosition Neutral => Drive.
        If BrakePedalState == Error"""
        conftest.change_all_pins(start_params=test_data_08)
        conftest.check_all_params(start_params=test_data_08)
        conftest.api_lib.set_gear1_pin(conftest.stand_address, 3.12)
        conftest.api_lib.set_gear2_pin(conftest.stand_address, 0.67)
        response = conftest.get_all_params()

        assert test_result_08 == response

    def test_09(self, test_data_09, test_result_09):
        """Negative. GearPosition Park => Drive.
        If AccPedalPos == Error"""
        conftest.change_all_pins(start_params=test_data_09)
        conftest.check_all_params(start_params=test_data_09)
        conftest.api_lib.set_gear1_pin(conftest.stand_address, 3.12)
        conftest.api_lib.set_gear2_pin(conftest.stand_address, 0.67)
        response = conftest.get_all_params()

        assert test_result_09 == response
