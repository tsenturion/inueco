from src.example import reverse


def test_reverse():
    assert reverse("Src") == "crS"

def test_reverse_for_empty_string():
    assert reverse("") == ""

def test_reverse_for_None():
    assert reverse(None) == None
