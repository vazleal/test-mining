import os
from pathlib import Path
import pandas as pd
import pandas.testing as pdt

from io_utils import load_from_csv


def test_load_from_csv():
    datas_dir = Path('datas')
    datas_dir.mkdir(exist_ok=True)
    filename = 'temp_test.csv'
    filepath = datas_dir / filename

    test_df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
    test_df.to_csv(filepath, index=False)

    try:
        loaded = load_from_csv(filename)
        assert loaded is not None
        pdt.assert_frame_equal(loaded, test_df)
    finally:
        if filepath.exists():
            filepath.unlink()

