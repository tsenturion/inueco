def get_user_name(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    data = response.json()
    return data["name"]


from unittest.mock import Mock

mock = Mock()
mock.return_value = 10

result = mock()


from unittest.mock import patch

@patch("my_module.requests.get")
def test_get_user_name(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"name": "Алексей"}
    mock_get.return_value = mock_response

    result = get_user_name(1)

    self.assertEqual(result, "Алексей")


from requests import get


def test_get_user_name(self):
    with patch("my_module.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = {"name": "Алексей"}
        mock_get.return_value = mock_response

        result = get_user_name(1)

        self.assertEqual(result, "Алексей")


from unittest.mock import MagicMock

mock_list = MagicMock()
mock_list.__len__.return_value = 5

self.assertEqual(len(mock_list), 5)


mock_get.assert_called_once()
mock_get.assert_called_with("https://api.example.com/users/1")


def setUp(self):
    self.patcher = patch("my_module.requests.get")
    self.mock_get = self.patcher.start()

def tearDown(self):
    self.patcher.stop()
