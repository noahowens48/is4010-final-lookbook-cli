# Lookbook CLI

A simple Python command-line app that lets you store clothing items and automatically generate outfits based on season and vibe. It helps you organize your wardrobe and quickly put together fits.

![Tests](https://github.com/USERNAME/is4010-final-lookbook-cli/actions/workflows/tests.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Testing](#testing)
- [AI-Assisted Development](#ai-assisted-development)
- [License](#license)

---

## Installation

1. Clone the repository:
   git clone https://github.com/USERNAME/is4010-final-lookbook-cli
   cd is4010-final-lookbook-cli
2. Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate
3. Install dependencies:
pip install -r requirements.txt

## Usage 
1. Add an item:
python -m lookbook add-item \
  --name "Black Hoodie" \
  --category top \
  --color black \
  --season winter \
  --vibe streetwear
2. List items (with filters): python -m lookbook list-items --season winter --vibe streetwear
3. Generate an outfit: 
python -m lookbook generate --season winter --vibe streetwear
Sample output:
🎲 Generated outfit:
- Top ID: 1
- Bottom ID: 2
- Shoes ID: 3

## Features:
Add clothing items (top, bottom, shoes, etc.)

Store season + vibe to match your personal style

Filter items by category, season, or vibe

Automatically generate a full outfit

Save generated outfits locally

Clean JSON-based storage

Fully tested with pytest

GitHub Actions CI pipeline to run tests on every push

## Testing
Run the full test suite:

```bash
pytest
```
Verbose mode:

pytest -v

**For Rust:**
```markdown
## Testing

Run the test suite:

```bash
cargo test
```
All tests must pass locally and in GitHub Actions.


### AI-Assisted Development

I used AI tools throughout this project mainly to help me think through the structure, debug errors faster, and write cleaner code.

ChatGPT: I used it for brainstorming project ideas, outlining the architecture, and getting examples of how to structure a Python CLI. I also used it when I got stuck on errors.

GitHub Copilot: I used it while writing most of the code. It helped with generating function skeletons, filling in repetitive logic, and speeding up test creation.

Example prompts I used:

“Help me outline a Python CLI that stores clothing items and generates outfits.”

“Why am I getting ImportError: cannot import name load_items?”

“Write pytest tests for filtering logic that uses dataclasses.”

Reflection:
AI mainly helped me move faster. It didn’t replace my thinking, but it helped me understand the problem and get unstuck quicker. Copilot was good for writing boilerplate, and ChatGPT helped explain errors and design patterns. Sometimes AI gave code that didn’t fit my project, so I still had to adjust things manually.

More detail is available in AGENTS.md.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.