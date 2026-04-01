from udoo_node.scope_adapter import HP54520AAdapter


def test_parse_identity_splits_vendor_model_and_serial():
    adapter = HP54520AAdapter()
    raw = "Hewlett-Packard,54520A,MY12345678,REV.A.01.00"
    parsed = adapter.parse_identity(raw)

    assert parsed["ok"] is True
    assert parsed["vendor"] == "Hewlett-Packard"
    assert parsed["model"] == "54520A"
    assert parsed["serial"] == "MY12345678"


def test_parse_scalar_returns_float_when_possible():
    adapter = HP54520AAdapter()
    parsed = adapter.parse_scalar("123.45")
    assert parsed["value"] == 123.45


def test_parse_preamble_extracts_basic_fields():
    adapter = HP54520AAdapter()
    raw = "0,1,500,1,1.0E-9,0.0,0,2.0E-3,0.0,0"
    parsed = adapter.parse_preamble(raw)

    assert parsed["parsed"]["points"] == "500"
    assert parsed["parsed"]["xincrement"] == "1.0E-9"
    assert parsed["parsed"]["yincrement"] == "2.0E-3"
