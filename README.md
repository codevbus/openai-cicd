# OpenAI-UI
Basic Flask-based OpenAI UI 

## Prerequisites
You'll need to have the latest version of Python installed, as well as [Poetry](https://python-poetry.org/) to run this. 

This project will also require an OpenAI API key generated with a paid usage plan.

## Getting Started
1. Clone the repository: `git clone git@github.com:codevbus/openai-ui.git`
2. Change into the newly cloned repository: `cd openai-ui`
3. Install the project dependencies with: `poetry install`
4. Set an environment variable for your API key: `export OPENAI_API_KEY='<your_key_here>'`(Note: if you add a space before the `export` command, shells like ZSH will not save the command to your history, which will protect your API key)
5. Run the project with: `poetry run python -m app`
6. Open `http://localhost:5000` in a browser window.
7. You should now be able to submit chat prompts to OpenAI!

## Planned Features
- Support for additional model selection
- Unit testing and integration testing of the OpenAI API
- Automated testing and deployment with GitHub Actions.

