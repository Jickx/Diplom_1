import pytest
from unittest.mock import Mock
from praktikum.bun import Bun


class TestBurger:

    def test_initial_stat(self, burger):
        assert burger.bun is None
        assert burger.ingredients == []

    @pytest.mark.parametrize(
        "bun_name,bun_price",
        [
            ("Булочка ржаная", 50.0),
            ("Булочка с кунжутом", 75.5),
            ("Brioche", 120.99),
        ],
        ids=["rye", "sesame", "brioche"]
    )
    def test_set_buns(self, burger, bun_name, bun_price):
        bun_mock = Mock(spec=Bun)
        bun_mock.get_name.return_value = bun_name
        bun_mock.get_price.return_value = bun_price

        burger.set_buns(bun_mock)

        assert burger.bun is bun_mock
