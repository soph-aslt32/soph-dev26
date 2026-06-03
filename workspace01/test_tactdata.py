from tactdata import load_csv, load_tsv

def test_load_csv():
    filepath = "sample/44.log"
    df = load_csv(filepath)
    print(df)
    print(df.columns)
    assert df.shape == (6, 7)
    assert list(df.columns) == [
        "SubstID",
        "LotID",
        "CassetteID",
        "SlotID",
        "GlassID",
        "RecipeID",
        "InTime",
    ]
    assert df.iloc[0]["SubstID"] == 1
    assert df.iloc[0]["LotID"] == 1001
    assert df.iloc[0]["CassetteID"] == "C001"
    assert df.iloc[0]["SlotID"] == 1
    assert df.iloc[0]["GlassID"] == "G001"
    assert df.iloc[0]["RecipeID"] == "R001"
    assert df.iloc[0]["InTime"] == "2024-06-01 08:00:00"
