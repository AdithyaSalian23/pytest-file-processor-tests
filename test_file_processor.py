import pytest
from unittest.mock import mock_open, patch
from .file_processor import process_file

@pytest.fixture
def mock_empty_file():
    return mock_open(read_data="")

@pytest.fixture
def mock_large_file():
    return mock_open(read_data="A" * 10000)

@pytest.fixture
def mock_malformed_file():
    m = mock_open()
    m.side_effect = Exception("Malformed content")
    return m

class TestFileProcessor:

    @patch("builtins.open")
    def test_empty_file(self, mock_open_builtin, mock_empty_file):
        mock_open_builtin.side_effect = mock_empty_file
        result = process_file("dummy.txt")
        assert result == "Empty file"

    @patch("builtins.open")
    def test_large_file(self, mock_open_builtin, mock_large_file):
        mock_open_builtin.side_effect = mock_large_file
        result = process_file("dummy.txt")
        assert result == "Processed: 10000 characters"

    @patch("builtins.open")
    def test_malformed_file(self, mock_open_builtin, mock_malformed_file):
        mock_open_builtin.side_effect = mock_malformed_file
        result = process_file("dummy.txt")
        assert "Error:" in result
