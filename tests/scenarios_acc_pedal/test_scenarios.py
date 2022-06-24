from tests import conftest
import pytest

class TestRun:
    """Проверка смены AccPedalPos и ReqTorque в зависимости от условий"""

    def test_01(self, test_data_01, test_result_01):
        """AccPedalPos 50% => 0%"""
        conftest.change_all_pins(start_params=test_data_01)
        conftest.check_all_params(start_params=test_data_01)
        conftest.api_lib.set_acc_pedal_pin(conftest.stand_address, 1)
        response = conftest.get_all_params()

        assert test_result_01 == response

    @pytest.mark.skip(
        reason='BUG-4. После перехода AccPedalPos в Error, GearPosition ушёл из Park в Neutral.'
               'Хотя в спеке об этом ни слова.')
    def test_02(self, test_data_02, test_result_02):
        """AccPedalPos 50% => Error"""
        conftest.change_all_pins(start_params=test_data_02)
        conftest.check_all_params(start_params=test_data_02)
        conftest.api_lib.set_acc_pedal_pin(conftest.stand_address, 4)
        response = conftest.get_all_params()

        assert test_result_02 == response

    @pytest.mark.skip(reason='BUG-3. При переходе BrakePedal из 1 в 0, ожидаю перехода GearPosition из Drive в Neutral.'
                             'Но этого не происходит')
    def test_03(self, test_data_03, test_result_03):
        """BrakePedalState Released => Error"""
        conftest.change_all_pins(start_params=test_data_03)
        conftest.check_all_params(start_params=test_data_03)
        conftest.api_lib.set_brake_pedal_pin(conftest.stand_address, 0)
        response = conftest.get_all_params()

        assert test_result_03 == response

    def test_04(self, test_data_04, test_result_04):
        """BrakePedalState Released => Pressed.
        If GearPosition == Drive"""
        conftest.change_all_pins(start_params=test_data_04)
        conftest.check_all_params(start_params=test_data_04)
        conftest.api_lib.set_brake_pedal_pin(conftest.stand_address, 1)
        response = conftest.get_all_params()

        assert test_result_04 == response

    def test_05(self, test_data_05, test_result_05):
        """BrakePedalState Released => Pressed.
        If GearPosition == Reverse"""
        conftest.change_all_pins(start_params=test_data_05)
        conftest.check_all_params(start_params=test_data_05)
        conftest.api_lib.set_brake_pedal_pin(conftest.stand_address, 1)
        response = conftest.get_all_params()

        assert test_result_05 == response

    def test_06(self, test_data_06, test_result_06):
        """BrakePedalState Pressed => Released.
        If GearPosition == Drive"""
        conftest.change_all_pins(start_params=test_data_06)
        conftest.check_all_params(start_params=test_data_06)
        conftest.api_lib.set_brake_pedal_pin(conftest.stand_address, 2)
        response = conftest.get_all_params()

        assert test_result_06 == response

    @pytest.mark.GearPositionNeutral
    @pytest.mark.BrakePedalStateError
    @pytest.mark.skip(reason='BUG-3. При переходе BrakePedal из 1 в 0, ожидаю перехода GearPosition из Drive в Neutral.'
                             'Но этого не происходит')
    def test_07(self, test_data_07, test_result_07):
        """BrakePedalState Error => Released"""
        conftest.change_all_pins(start_params=test_data_07)
        conftest.check_all_params(start_params=test_data_07)
        conftest.api_lib.set_brake_pedal_pin(conftest.stand_address, 2)
        response = conftest.get_all_params()

        assert test_result_07 == response

    @pytest.mark.GearPositionNeutral
    @pytest.mark.BrakePedalStateError
    @pytest.mark.skip(reason='BUG-3. При переходе BrakePedal из 1 в 0, ожидаю перехода GearPosition из Drive в Neutral.'
                             'Но этого не происходит')
    def test_08(self, test_data_08, test_result_08):
        """BrakePedalState Error => Pressed"""
        conftest.change_all_pins(start_params=test_data_08)
        conftest.check_all_params(start_params=test_data_08)
        conftest.api_lib.set_brake_pedal_pin(conftest.stand_address, 1)
        response = conftest.get_all_params()

        assert test_result_08 == response

    @pytest.mark.skip(reason='BUG-3. При переходе BrakePedal из 1 в 0, ожидаю перехода GearPosition из Drive в Neutral.'
                             'Но этого не происходит')
    def test_09(self, test_data_09, test_result_09):
        """BrakePedalState Pressed => Error"""
        conftest.change_all_pins(start_params=test_data_09)
        conftest.check_all_params(start_params=test_data_09)
        conftest.api_lib.set_brake_pedal_pin(conftest.stand_address, 4)
        response = conftest.get_all_params()

        assert test_result_09 == response

    def test_10(self, test_data_10, test_result_10):
        """BrakePedalState Pressed => Released.
        If GearPosition == Reverse"""
        conftest.change_all_pins(start_params=test_data_10)
        conftest.check_all_params(start_params=test_data_10)
        conftest.api_lib.set_brake_pedal_pin(conftest.stand_address, 2)
        response = conftest.get_all_params()

        assert test_result_10 == response
