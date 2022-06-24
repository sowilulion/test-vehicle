from tests import conftest
import pytest

class TestRun:
    """Проверка граничных значений для BrakePedalState"""

    def test_01(self, test_data_01, test_result_01):
        """BrakePedalState border value 2V => 1.99V.
        Released => Pressed"""
        conftest.change_all_pins(start_params=test_data_01)
        conftest.check_all_params(start_params=test_data_01)
        conftest.api_lib.set_brake_pedal_pin(conftest.stand_address, 1.99)
        response = conftest.get_all_params()

        assert test_result_01 == response

    def test_02(self, test_data_02, test_result_02):
        """BrakePedalState border value 2V => 2.99V.
        Released => Released """
        conftest.change_all_pins(start_params=test_data_02)
        conftest.check_all_params(start_params=test_data_02)
        conftest.api_lib.set_brake_pedal_pin(conftest.stand_address, 2.99)
        response = conftest.get_all_params()

        assert test_result_02 == response

    @pytest.mark.skip(reason='BUG-3. При переходе BrakePedal из 1 в 0, ожидаю перехода GearPosition из Drive в Neutral.'
                             'Но этого не происходит')
    def test_03(self, test_data_03, test_result_03):
        """BrakePedalState border value 2V => 3V.
        Released => Error"""
        conftest.change_all_pins(start_params=test_data_03)
        conftest.check_all_params(start_params=test_data_03)
        conftest.api_lib.set_brake_pedal_pin(conftest.stand_address, 3)
        response = conftest.get_all_params()

        assert test_result_03 == response

    def test_04(self, test_data_04, test_result_04):
        """BrakePedalState border value 2V => 1V.
        Released => Pressed"""
        conftest.change_all_pins(start_params=test_data_04)
        conftest.check_all_params(start_params=test_data_04)
        conftest.api_lib.set_brake_pedal_pin(conftest.stand_address, 1)
        response = conftest.get_all_params()

        assert test_result_04 == response

    @pytest.mark.skip(reason='BUG-3. При переходе BrakePedal из 1 в 0, ожидаю перехода GearPosition из Drive в Neutral.'
                             'Но этого не происходит')
    def test_05(self, test_data_05, test_result_05):
        """BrakePedalState border value 2V => 0.99V.
        Released => Error"""
        conftest.change_all_pins(start_params=test_data_05)
        conftest.check_all_params(start_params=test_data_05)
        conftest.api_lib.set_brake_pedal_pin(conftest.stand_address, 0.99)
        response = conftest.get_all_params()

        assert test_result_05 == response
