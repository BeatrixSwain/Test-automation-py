# Test-automation-py :robot:

- doctest: Testing using doctest. :page_with_curl:
    - Def tests in algoritmos.py
    - usage python doctest_t/algoritmos.py
    - others:
        - cd doctest_t :black_nib:
            - python -m doctest test.txt
- pyTest: Testing using pytest. :snake:
    - function on pytestTesting
    - test.py define tests.
    - pytest pyTest_t/test.py

- world_unittest: Using unittest.
    - cd world_unitest
    - python test_world.py
    - coverage run test_world.py
    - coverage report worldModel.py
    - reports:
        - coverage run test_world.py
        - coverage report -m worldModel.py
        - coverage html worldModel.py


- Requeriments:
    - pip install pytest
    - pip install coverage

02.04.2021 - v.1.0.1