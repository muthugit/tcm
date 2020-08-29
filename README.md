# tcm
Yet another file based Test Case Management tool.

## Usage
```
from mutcm import TCMParser

tcm = TCMParser('cases')
print(tcm.case_runs)
# this should returns the JSON object with all runs

@pytest.mark.parametrize("data", tcm.case_runs)
def test_api(data):
    print(data)
    assert tcm.api_test(data) == data['expected']
```