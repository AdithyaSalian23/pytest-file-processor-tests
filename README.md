# 🧪 File Processor - Pytest Integration Tests

Integration testing for a simple Python file processing utility using `pytest` and `unittest.mock`.

## 📁 Project Structure

```bash
pytest/
├── file_processor_project/
│ ├── file_processor.py # Utility logic
│ └── test_file_processor.py # Tests with pytest + mock
└── pytest.ini # (Optional) config file
```

---


## ⚙️ Functionality

`process_file(file_path)` reads a file and returns:
- `"Empty file"` if no content
- `"Processed: <n> characters"` if content exists
- `"Error: <message>"` if exception occurs

## ✅ Tests

Uses `@patch("builtins.open")` to mock file behavior:
- `test_empty_file` – empty content
- `test_large_file` – large content
- `test_malformed_file` – simulated exception

## 🚀 Usage

```bash
git clone https://github.com/your-username/file-processor-pytest.git
cd file-processor-pytest
pip install pytest
pytest
```

---

## 💡 Author
Created by Adithya
