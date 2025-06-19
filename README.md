## 🧪 File Processor - Pytest Integration Tests

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python" />
  <img src="https://img.shields.io/badge/pytest-Testing-red?style=flat-square&logo=pytest" />
  <img src="https://img.shields.io/badge/unittest.mock-Mocking-grey?style=flat-square" />
  <img src="https://img.shields.io/badge/Open%20Source-MIT-green?style=flat-square" />
</p>

---

## 📝 Project Overview

A simple integration testing project using **`pytest`** and **`unittest.mock`** to test a Python file processor utility.

This project demonstrates mocking file operations using `@patch` and validating different input scenarios through automated test cases.

---

## 📁 Project Structure

```
pytest/
├── file_processor_project/
│ ├── file_processor.py # File processing logic
│ └── test_file_processor.py # Integration tests using pytest
└── pytest.ini # (Optional) Pytest configuration
```

---

## ⚙️ Functionality

The function `process_file(file_path)` performs the following:

- 🔹 Returns `"Empty file"` for files with no content
- 🔹 Returns `"Processed: <n> characters"` for files with text
- 🔹 Returns `"Error: <message>"` if an exception occurs

---

## ✅ Tests Included

Each test uses `unittest.mock.patch` to simulate file operations without creating actual files:

| Test Name             | Description                           |
|-----------------------|---------------------------------------|
| `test_empty_file`     | Mocks a file with no content          |
| `test_large_file`     | Mocks a file with large content       |
| `test_malformed_file` | Simulates an exception during read    |

---

## 🚀 Getting Started

### 🔧 Installation

```bash
git clone https://github.com/your-username/file-processor-pytest.git
cd file-processor-pytest
pip install pytest
```

### 🧪 Run Tests

```bash
pytest
```

You’ll see test results directly in your terminal showing which cases passed or failed.

## 🛠️ Tech Stack

| Tool              | Purpose                         |
|-------------------|---------------------------------|
| 🐍 **Python**      | Core language                   |
| 🧪 **Pytest**      | Testing framework               |
| 🧰 **unittest.mock** | Patching file I/O operations    |

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
Feel free to use, modify, and share!

---

## 👤 Author

Made with ❤️ by **Adithya Salian**  
📬 Let’s connect on [LinkedIn](https://www.linkedin.com/in/adithyasalian/)  
🔗 Check out more projects at [GitHub](https://github.com/AdithyaSalian23)
