import pytest
import pandas as pd
import calcul
df = pd.DataFrame({
    'pre_spe': [1, 2, 3, 1, 2, 3, 1, 2, 3],
    'rem_mon': [10.43, 10.23, 7.29, 4.0, 7.5, 8.0, 19.0, 28, 0.4]
})


def test_mean_by_spe():
    result = calcul.get_mean_by_spe(df)
    result = result['rem_moy'].squeeze()
    assert result[0] == 11.143333333333333
    assert result[2] == 5.2299999999999995


def test_rep_by_spe():
    result = calcul.get_per_by_spe(df)
    result = result['rem_tau'].squeeze()
    assert result[0] == 0.35245123879810225
