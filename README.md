# GPT-Automation

Welcome to **GPT-Automation**, a Python-based application designed to simplify and automate interactions with OpenAI's GPT models. This application processes input data and prompts using a specified GPT model and saves the generated output to a file. 🚀

---

## 📖 What Does This Application Do?
The `gpt-automation.py` script allows users to:

1. Specify the role of the user (`user`, `developer`, `assistant`).
2. Choose the OpenAI GPT model to use.
3. Provide a file containing the **prompt** to send to the GPT model.
4. Provide a file containing the **input data** to process.
5. Save the GPT-generated output to a file.

The script uses OpenAI's API to generate responses based on the provided parameters, making it suitable for tasks like text generation, summarization, and more.

---

## 🛠️ Technical Overview

### Key Features
- **Argument Parsing**: Uses Python's `argparse` to accept user inputs for role, model, prompt, input file, and output file.
- **Integration with OpenAI API**: Sends requests to OpenAI's chat completions endpoint using the specified model.
- **File Handling**: Reads prompt and input content from files and writes the generated output to a specified file.

### Code Breakdown
- **Argument Parsing**:
  Parses the following arguments from the command line:
  - `--role` (`-r`): Defines the user's role. Options: `user`, `developer`, `assistant`.
  - `--model` (`-m`): Specifies the GPT model to use.
  - `--prompt` (`-p`): Path to the file containing the prompt.
  - `--input` (`-i`): Path to the file containing the input data.
  - `--output` (`-o`): Path to the file where the output will be saved.

- **OpenAI API Call**:
  The script sends a request to the OpenAI API with the specified model and message content:

  ```python
  completion = client.chat.completions.create(
      model=args.model,
      messages=[{"role": args.role, "content": content}],
      response_format={"type": "text"}
  )
  ```

- **Error Handling**: The script does not currently handle API errors but can be extended with `try-except` blocks for robust error management.

- **File Operations**:
  - Reads prompt and input data from the specified files.
  - Concatenates them and sends the combined content to the OpenAI API.
  - Writes the generated response to the specified output file.

---

## 📋 Prerequisites
- Python 3
- A valid OpenAI API key

---

## 💻 Installation and Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/lepotekil/gpt-automation.git
cd gpt-automation
```

### Step 2: Create and Activate a Virtual Environment

#### Linux/MacOS
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install openai
```

#### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install openai
```

### Step 3: Export the OpenAI API Key

#### Linux/MacOS
```bash
export OPENAI_API_KEY="sk-example1234567890abcdef1234567890abcd"
```

#### Windows (PowerShell)
```powershell
$env:OPENAI_API_KEY="sk-example1234567890abcdef1234567890abcd"
```

---

## 🚀 How to Use

Run the application using the following command:

```bash
python gpt-automation.py \
    -r assistant \
    -m o1-mini \
    -p prompts/example_prompt.txt \
    -i input/example_input.txt \
    -o output/generated_output.txt
```

### Example
- **Prompt file (`prompts/example_prompt.txt`)**:
  ```
  Translate the following text into French:
  ```

- **Input file (`input/example_input.txt`)**:
  ```
  Hello, how are you today?
  ```

- **Generated Output (`output/generated_output.txt`)**:
  ```
  Bonjour, comment allez-vous aujourd'hui ?
  ```

---

## 📑 Notes on GPT Models

- You can find all available GPT models and their limitations on this page:
  👉 [OpenAI Model Limits](https://platform.openai.com/settings/organization/limits)

---

## 🧰 Troubleshooting

1. **Missing API Key Error**:
   Ensure the `OPENAI_API_KEY` environment variable is set correctly.

   ```bash
   echo $OPENAI_API_KEY
   ```

2. **Model Not Found Error**:
   Double-check the model name provided in the `-m` argument. Refer to the [OpenAI Model Limits](https://platform.openai.com/settings/organization/limits) for valid options.

3. **Permission Denied for Files**:
   Ensure you have read/write permissions for the specified prompt, input, and output files.

---

## 📂 File Structure

```
project-root/
├── gpt-automation.py    # Main application script
├── prompts/             # Directory for prompt files
├── input/               # Directory for input files
├── output/              # Directory for generated output files
├── README.md            # Documentation
└── .venv/               # Python virtual environment
```

---

## 🌟 Contributing
Feel free to submit issues or pull requests to improve the application. Contributions are welcome!

---

## 📜 License
This project is licensed under the MIT License.

