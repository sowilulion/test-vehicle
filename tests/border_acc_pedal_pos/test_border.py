from tests import conftest


class TestRun:
    """Проверка граничных значения для AccPedalPos и ReqTorque"""

    def test_01(self, test_data_01, test_result_01):
        """AccPedal border value 2.5V => 0.99V.
        AccPedalPos 50% => Error"""
        conftest.change_all_pins(start_params=test_data_01)
        conftest.check_all_params(start_params=test_data_01)
        conftest.api_lib.set_set_acc_pedal_pin(conftest.stand_address, 0.99)
        response = conftest.get_all_params()

        assert test_result_01 == response

    def test_02(self, test_data_02, test_result_02):
        """AccPedal border value 2.5V => 1.99V.
        AccPedalPos 50% => 0%"""
        conftest.change_all_pins(start_params=test_data_02)
        conftest.check_all_params(start_params=test_data_02)
        conftest.api_lib.set_set_acc_pedal_pin(conftest.stand_address, 1.99)
        response = conftest.get_all_params()

        assert test_result_02 == response

    def test_03(self, test_data_03, test_result_03):
        """AccPedal border value 2.5V => 2V.
        AccPedalPos 50% => 30%"""
        conftest.change_all_pins(start_params=test_data_03)
        conftest.check_all_params(start_params=test_data_03)
        conftest.api_lib.set_set_acc_pedal_pin(conftest.stand_address, 2)
        response = conftest.get_all_params()

        assert test_result_03 == response

    def test_04(self, test_data_04, test_result_04):
        """AccPedal border value 2.5V => 2.49V.
        AccPedalPos 50% => 30%"""
        conftest.change_all_pins(start_params=test_data_04)
        conftest.check_all_params(start_params=test_data_04)
        conftest.api_lib.set_set_acc_pedal_pin(conftest.stand_address, 2.49)
        response = conftest.get_all_params()

        assert test_result_04 == response

    def test_05(self, test_data_05, test_result_05):
        """AccPedal border value 2.5V => 2.99V.
        AccPedalPos 50% => 50%"""
        conftest.change_all_pins(start_params=test_data_05)
        conftest.check_all_params(start_params=test_data_05)
        conftest.api_lib.set_set_acc_pedal_pin(conftest.stand_address, 2.99)
        response = conftest.get_all_params()

        assert test_result_05 == response

    def test_06(self, test_data_06, test_result_06):
        """AccPedal border value 2.5V => 3V.
        AccPedalPos 50% => 100%"""
        conftest.change_all_pins(start_params=test_data_06)
        conftest.check_all_params(start_params=test_data_06)
        conftest.api_lib.set_set_acc_pedal_pin(conftest.stand_address, 3)
        response = conftest.get_all_params()

        assert test_result_06 == response

    def test_07(self, test_data_07, test_result_07):
        """AccPedal border value 2.5V => 3.49V.
        AccPedalPos 50% => 100%"""
        conftest.change_all_pins(start_params=test_data_07)
        conftest.check_all_params(start_params=test_data_07)
        conftest.api_lib.set_set_acc_pedal_pin(conftest.stand_address, 3.49)
        response = conftest.get_all_params()

        assert test_result_07 == response

    def test_08(self, test_data_08, test_result_08):
        """AccPedal border value 2.5V => 3.5V.
        AccPedalPos 50% => Error"""
        conftest.change_all_pins(start_params=test_data_08)
        conftest.check_all_params(start_params=test_data_08)
        conftest.api_lib.set_set_acc_pedal_pin(conftest.stand_address, 3.5)
        response = conftest.get_all_params()

        assert test_result_08 == response
