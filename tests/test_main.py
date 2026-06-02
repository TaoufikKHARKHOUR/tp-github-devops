def test_diviser():
    assert diviser(10, 2) == 5.0

def test_diviser_par_zero():
    import pytest
    with pytest.raises(ValueError):
        diviser(10, 0)
EOF

def test_diviser():
    assert diviser(10, 2) == 5.0
