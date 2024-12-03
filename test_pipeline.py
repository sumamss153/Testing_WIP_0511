import pandas as pd
import numpy as np
import pytest
from db_connection import connect_to_db

# get data
@pytest.fixture(scope='session', autouse=True)
def df():
    # Will be executed before the first test
    df = connect_to_db()
    print(df)
    yield df

# check if column exists
def test_col_exists(df):
    name = "participant_id"
    assert name in df.columns

# check for nulls
def test_null_check_pid(df):
    assert df['participant_id'].notnull().all()

# check for nulls
def test_null_check_fname(df):
    assert df['first_name'].notnull().all()

# check values are unique
def test_unique_check(df):
    assert pd.Series(df['participant_id']).is_unique

# check data type
def test_dtype_str(df):
    assert (df['first_name'].dtype == str or df['first_name'].dtype == 'O')
