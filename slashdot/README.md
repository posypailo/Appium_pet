# Slashdot Mobile Automation Project

## Project Structure

```plaintext
├── actions
│   ├── multiple_elements_actions.py
│   ├── single_element_actions.py
│   └── __init__.py
├── configs
│   ├── android_chrome_config.py
│   └── __init__.py
├── constants
│   ├── global_data.py
│   └── __init__.py
├── drivers
│   ├── chromedriver.exe
│   └── __init__.py
├── pages
│   ├── base_page.py
│   ├── android
│   │   ├── slashdot_page.py
│   │   └── __init__.py
│   └── __init__.py
├── tests
│   ├── conftest.py
│   ├── test_slashdot.py
│   └── __init__.py
├── utils
│   ├── driver_factory.py
│   ├── logger.py
│   ├── multiple_elements_wait_utils.py
│   ├── number_to_words_util.py
│   ├── single_element_wait_utils.py
│   └── __init__.py
└── __init__.py
```

## Description

This project is designed for mobile test automation using Appium and Python. It follows a structured and modular approach to keep the code clean, maintainable, and scalable.

## Directories and Files

### `actions/`

Contains classes for actions that can be performed on single and multiple elements.

- **multiple_elements_actions.py**: Defines actions that can be performed on multiple elements.
- **single_element_actions.py**: Defines actions that can be performed on a single element.

### `configs/`

Contains configuration files.

- **android_chrome_config.py**: Configuration for running tests on Android Chrome.

### `constants/`

Contains global constants.

- **global_data.py**: Defines global constants used across the project.

### `drivers/`

Contains driver executables and initialization files.

- **chromedriver.exe**: Chrome driver executable for running tests on Chrome.

### `pages/`

Contains page object classes.

- **base_page.py**: Base page class that other page classes inherit from.
- **android/**: Directory for Android-specific page objects.
  - **slashdot_page.py**: Page object class for the Slashdot page on Android.

### `tests/`

Contains test cases and test configurations.

- **conftest.py**: Configuration file for pytest.
- **test_slashdot.py**: Test cases for the Slashdot page.

### `utils/`

Contains utility classes and methods.

- **driver_factory.py**: Factory class for creating driver instances.
- **logger.py**: Logger utility for logging messages.
- **multiple_elements_wait_utils.py**: Utility methods for waiting on multiple elements.
- **number_to_words_util.py**: Utility for converting numbers to words.
- **single_element_wait_utils.py**: Utility methods for waiting on single elements.


 ## 1. Setup

**Clone the repository**:
   ```sh
   git clone https://github.com/posypaylo/Appium_pet.git
   cd <repository_directory>
   ```

 ## 2. Install dependencies:

**pip install -r requirements.txt**


 ## 3. Configure the environment:

- Ensure you have the necessary drivers (e.g., chromedriver) in the drivers/ directory.
- Update any configuration files in the configs/ directory as needed for your specific setup.


 ## 4. Run tests:

   ```sh
    pytest
   ```
## **Contributing**

Contributions are welcome! Please follow these steps:

1.    Fork the repository.
2.    Create a new branch (git checkout -b feature-branch).
3.    Make your changes and commit them (git commit -m 'Add some feature').
4.    Push to the branch (git push origin feature-branch).
5.    Create a new pull request.