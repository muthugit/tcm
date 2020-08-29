import pytest

# pytest.global_variable_1 = ''

# import pytest
# pytest.main(["test_tcm.py::test_api","--html", "report.html"])


from src import MuTCM

tcm = MuTCM('cases')
print(tcm.case_runs)

@pytest.mark.parametrize("data", tcm.case_runs)
def test_api(data):
    print(data)
    assert tcm.api_test(data) == data['expected']
