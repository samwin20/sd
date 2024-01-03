import pandas as pd
import pytest

def check_csv_schema(file_path, expected_columns, expected_dtypes):
    df = pd.read_csv(file_path)

    # Check columns
    actual_columns = list(df.columns)
    assert actual_columns == expected_columns, f"Schema mismatch in file '{file_path}':\nExpected columns: {expected_columns}\nActual columns: {actual_columns}"

    # Check column types
    actual_dtypes = df.dtypes.to_dict()
    for col, expected_dtype in expected_dtypes.items():
        assert actual_dtypes[col] == expected_dtype, f"Data type mismatch in file '{file_path}', column '{col}':\nExpected type: {expected_dtype}\nActual type: {actual_dtypes[col]}"

@pytest.mark.parametrize("file_path, expected_columns, expected_dtypes", [
    ('file1.csv', ['column1', 'column2', 'column3'], {'column1': int, 'column2': float, 'column3': str}),
    ('file2.csv', ['columnA', 'columnB', 'columnC'], {'columnA': str, 'columnB': int, 'columnC': float}),
    ('file3.csv', ['col_X', 'col_Y', 'col_Z'], {'col_X': str, 'col_Y': object, 'col_Z': pd.Timestamp}),
])
def test_csv_schema(file_path, expected_columns, expected_dtypes):
    check_csv_schema(file_path, expected_columns, expected_dtypes)
