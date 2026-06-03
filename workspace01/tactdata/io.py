from __future__ import annotations

import csv
from pathlib import Path

import pandas as pd


def load_tsv(
    filepath: str | Path,
    header: bool = True,
) -> tuple[list[str] | None, list[list[str]]]:
    """タブ区切りの txt ファイルを行列として読み込む。

    Parameters
    ----------
    filepath : str | Path
        読み込むファイルのパス。
    header : bool, optional
        先頭行をヘッダーとして扱う場合は True（デフォルト）。
        ヘッダーなしの場合は False を指定する。

    Returns
    -------
    headers : list[str] | None
        ヘッダー行の値のリスト。``header=False`` の場合は None。
    rows : list[list[str]]
        データ行の 2 次元リスト（文字列）。
    """
    path = Path(filepath)
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter="\t")
        if header:
            headers: list[str] | None = next(reader)
            rows = [row for row in reader]
        else:
            headers = None
            rows = [row for row in reader]
    return headers, rows


def load_csv(
    filepath: str | Path,
    header: bool = True,
) -> pd.DataFrame:
    """カンマ区切りのテキストファイルを DataFrame として読み込む。

    各要素の前後の空白は自動的に削除される。

    Parameters
    ----------
    filepath : str | Path
        読み込むファイルのパス（拡張子は問わない）。
    header : bool, optional
        先頭行をヘッダーとして扱う場合は True（デフォルト）。
        ヘッダーなしの場合は False を指定する。

    Returns
    -------
    pd.DataFrame
        読み込んだデータの DataFrame。
    """
    path = Path(filepath)
    if header:
        df = pd.read_csv(path, encoding="utf-8")
        # ヘッダー（列名）の前後の空白を削除
        df.columns = df.columns.str.strip()
    else:
        df = pd.read_csv(path, encoding="utf-8", header=None)
    
    # 各要素の前後の空白を削除
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
    
    return df
