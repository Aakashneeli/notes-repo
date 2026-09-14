from orm_example import run
def test_example(capsys):
    run()
    assert capsys.readouterr().out.splitlines() == [
        "flushed 1", "committed ['draft']", "rolled back", "remaining ['draft']"
    ]

def test_crud_mechanisms(capsys):
    from orm_crud import run as crud
    crud()
    assert capsys.readouterr().out.splitlines() == [
        "page 3 ['review']", "remaining ['private', 'ready']"
    ]
