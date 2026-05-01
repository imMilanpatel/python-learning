# Python Learning Playground 🐍

Welcome to the Python Learning Playground! 🚀 This repository is your go-to resource for hands-on Python learning and exploration.

## About

👨‍💻 Hi, I'm Milan Patel! I'm passionate about Python and eager to share my learning journey with you. This repository contains a collection of Python files developed for learning and exploration purposes. The code is inspired by challenges from various GitHub repositories, making it an engaging and practical way to enhance your Python skills.

## Features

🔍 **Diverse Topics:** Explore a variety of Python concepts, from basic syntax to advanced topics, in a single repository.

🚀 **Hands-On Learning:** Dive into practical challenges and exercises designed to solidify your understanding and boost your coding skills.

🤝 **Community-driven:** Join a growing community of Python enthusiasts! Feel free to contribute, share your insights, and learn together.

## Repository Structure

### 📁 Automation/
Comprehensive test automation examples with multiple frameworks:

- **Excel/** - Excel automation with configuration management
  - `test_cases/` - Test suite with pytest configuration (test cases 06-10)
  - `first_tests/` - Introductory test examples (test cases 01-05)
  - `configs/` - Configuration files and credentials

- **Playwright/** - Modern web automation testing
  - `Basic_examples/` - Introduction to Playwright automation
  - `OrangeHRM/` - Page Object Model implementation for OrangeHRM application
  - `SauceDemo/` - Testing SauceDemo application with utilities
  - `YourStore/` - Full POM framework with tests and utilities

- **Selenium/** - Classic web automation framework
  - `test_basics.py` - Basic Selenium concepts
  - `IE_Browser/` - Internet Explorer specific tests
  - `YourStore/` - Selenium POM implementation

### 📚 Basics/
Foundational Python concepts and algorithms:

- **Basic misc/** - Algorithm challenges
  - Array operations (shifting, splitting, max values)
  - Pattern printing (triangles, sequences)
  - String manipulation (counting, word occurrences)
  - Number theory (Roman numerals, perfect numbers, powers)
  - Data structure problems

- **lists/** - List operations and manipulation
- **strings/** - String processing (word counting)
- **variables/** - Variable types and operations (integers, floats, strings)

### 🎮 Games/
Interactive game development:

- **Basic/QA JSON/** - Quiz/Question-Answer game with JSON data structure

### 🖥️ GUI/
Graphical User Interface projects:

- **Custom Tkinter/** - Modern GUI development
  - `Day Predictor/` - Day prediction application with background images

### 📝 LeetCode/
LeetCode algorithm challenges:

- Array and string problems
- Two sum algorithm
- Merge sorted lists
- Finding first occurrences

### 📁 File_RW/
File input/output operations:

- **XML/** - XML file reading and manipulation

### 🎵 Playlist_Downloader/
Playlist downloading utility:

- **YouDownload/** - YouTube playlist downloader with GUI interface

## Getting Started

🔧 Ready to embark on your Python learning journey? Follow these steps:

### Clone the Repository

```bash
git clone https://github.com/imMilanpatel/python-learning
cd python-learning
```

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

Install required dependencies (for automation and GUI projects):

```bash
pip install pytest playwright selenium pytube customtkinter
```

### Run Examples

**Navigate to any subdirectory and run Python files:**

```bash
# Run basic examples
python Basics/Basic\ misc/Array_max_value_inc.py

# Run Playwright tests
pytest Automation/Playwright/OrangeHRM/tests/test_login.py

# Run Selenium tests
pytest Automation/Selenium/

# Run Excel tests
pytest Automation/Excel/test_cases/
```

## Start Coding! 🚀

Tweak, experiment, and challenge yourself to enhance your Python proficiency.

## Contribution Guidelines 🤝 

Contributions are welcome! 
Whether you're a beginner or an experienced Pythonista, feel free to contribute to the repository. Here's how:

1. **Fork the repository.**
2. **Create a new branch:** `git checkout -b feature/new-feature`.
3. **Make your changes:** Whether it's fixing a bug, enhancing existing code, or adding new challenges.
4. **Commit your changes:** `git commit -m 'Add new feature'`.
5. **Push to your branch:** `git push origin feature/new-feature`.
6. **Submit a pull request and let's learn together!**

## Contact 📧 

Have questions or suggestions? Feel free to reach out to me:

- **Name:** Milan Patel 
- **Email:** milanpatel3116@gmail.com
- **LinkedIn Profile:** https://www.linkedin.com/in/milan-patel31/

Let's make learning Python a fun and collaborative experience! Happy coding! 🚀
