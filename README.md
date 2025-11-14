PLAYWRIGHT-CONDUIT/
├── **pycache**/
├── .github/
│ └── workflows/
│ └── tests.yaml
├── .pytest_cache/
├── auth/
│ └── state.json
├── pages/
│ ├── **pycache**/
│ ├── article_page.py
│ ├── base_page.py
│ ├── filter_page.py
│ └── settings_page.py
├── screenshots/
├── tests/
│ ├── **pycache**/
│ ├── conftest.py
│ ├── test_case1_create_article.py
│ ├── test_case2_edit_article.py
│ ├── test_case3_delete_article.py
│ ├── test_case4_filter_by_tag.py
│ └── test_case5_update_settings.py
├── utils/
│ ├── **pycache**/
│ ├── **init**.py
│ ├── api_helper.py
│ ├── config.py
│ ├── data_generator.py
│ └── logger.py
├── venv/
├── .gitignore
├── README.md
├── report.html
├── requirements.txt
└── test_run.log

# Installation Guide

Follow these steps to set up the project locally:

### Clone the Repository

```bash
git clone https://github.com/MehediMashfan086/playwright-conduit.git
cd playwright-conduit
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the environment:

# Windows

```bash
venv\Scripts\activate
```

# Mac/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright Browsers

```bash
playwright install
```

### Running Tests

# Run all tests:

```bash
pytest -v --html=report.html --self-contained-html
```

# Run a specific test file:

```bash
pytest tests/test_case1_create_article.py
pytest tests/test_case2_edit_article.py
pytest tests/test_case3_delete_article.py
pytest tests/test_case4_filter_by_tag.py
pytest tests/test_case5_update_settings.py
```

# Run tests with logs:

```bash
pytest -s -v
```

# Run tests in parallel:

```bash
pytest -n 4
```

### Reports

# After running tests with:

```bash
pytest -v --html=report.html --self-contained-html
```

A report will be generated as report.html in the project root.
Open it in a browser to view detailed results.

### Test Cases

# Test Case 1: Create Article via API

# Test Case 2: Edit Article via UI

# Test Case 3: Delete Article via UI

# Test Case 4: Filter by Tags via UI

# Test Case 5: Update Settings via UI
