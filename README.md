# Lookbook CLI – Outfit Generator

A command-line tool that lets you store clothing items, filter them, and automatically generate full outfits based on season + vibe. I built this as my IS4010 Final Project to show I can design, test, and ship a real CLI application.

[![Tests](https://github.com/noahowens48/is4010-final-lookbook-cli/actions/workflows/tests.yml/badge.svg)](https://github.com/noahowens48/is4010-final-lookbook-cli/actions/workflows/tests.yml)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)

---

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Testing](#testing)
- [AI-Assisted Development](#ai-assisted-development)
- [License](#license)

---

## Installation

1. Clone the repo:
```bash
git clone https://github.com/noahowens48/is4010-final-lookbook-cli
cd is4010-final-lookbook-cli
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Usage

### Add a clothing item
```bash
python -m lookbook add-item \
  --name "Black Hoodie" \
  --category top \
  --season winter \
  --vibe streetwear
```

### List items by season + vibe
```bash
python -m lookbook list-items --season winter --vibe streetwear
```

### Generate an outfit
```bash
python -m lookbook generate --season winter --vibe streetwear
```

Example output:
```
🎲 Generated outfit:
- Top ID: 1
- Bottom ID: 2
- Shoes ID: 3
```

---

## Features

- Add & store clothing items locally  
- Filter items by category, season, or vibe  
- Automatically assemble an outfit (top + bottom + shoes)  
- Save generated outfits  
- JSON-based storage  
- Fully tested using pytest  
- Automated CI/CD pipeline using GitHub Actions  

---

## Testing

Run the full test suite:
```bash
pytest -v
```

---

## AI-Assisted Development

I used ChatGPT to brainstorm the project idea, outline my file structure, and break the build into steps. I also used it to help me understand how to organize a Python CLI app and how to structure filtering, storage, and generation logic.

I used GitHub Copilot inside VS Code for writing repetitive code faster, filling in boilerplate, suggesting function layouts, and helping debug when things weren’t working right. All final decisions and code were written, reviewed, and tested by me.

For more details and specific prompts, see **AGENTS.md**.

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
