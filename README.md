# AdvancedNumber Class Assignment

![Python Tests](https://github.com/The-School-of-AI/epai-s21-ram/workflows/Python%20Tests/badge.svg)

## Overview
This project implements a custom numerical type in Python called `AdvancedNumber` that demonstrates the use of Python's special methods (magic methods) to create a rich, fully-featured numeric type.

## Features

### 1. Basic Operations
- Initialize with integer or float values
- Human-readable string representation
- Developer-focused representation

### 2. Arithmetic Operations
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Modulus (`%`)
- Works with both `AdvancedNumber` objects and regular numbers

### 3. Comparison Operations
- Less than (`<`)
- Less than or equal to (`<=`)
- Greater than (`>`)
- Greater than or equal to (`>=`)
- Equal to (`==`)
- Not equal to (`!=`)

### 4. Advanced Features
- Hashable (can be used in sets and as dictionary keys)
- Boolean conversion
- Callable objects (returns square of the value)
- Custom string formatting
- Cleanup notification on object destruction

## Installation

1. Clone this repository:
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install pytest
```

## Usage

```python
# Create AdvancedNumber objects
num1 = AdvancedNumber(5)
num2 = AdvancedNumber(3)

# Arithmetic operations
result = num1 + num2  # AdvancedNumber(8)
product = num1 * 2    # AdvancedNumber(10)

# Comparison
is_greater = num1 > num2  # True

# Callable behavior
squared = num1()  # 25

# Custom formatting
formatted = f"{num1:.2f}"  # "5.00"
hex_format = f"{num1:#x}"  # "0x5"
```

## Testing

Run the tests using pytest:

```bash
pytest
```

## Project Structure

```
.
├── advanced_number.py     # Main implementation
├── test_assignment.py     # Test suite
├── .gitignore            # Git ignore file
├── README.md             # This file
└── .github/
    └── workflows/
        └── python-tests.yml  # GitHub Actions workflow
```

## Requirements
- Python 3.9 or higher
- pytest (for running tests)

## Contributing
This is an assignment project. Please do not contribute directly.

