# ⚙️ Reparo — AI-Assisted Self-Healing Compiler

> *A smart compiler that doesn’t just throw errors — it helps you fix them.*

---

## 🚀 Overview

**Reparo** is a custom-designed programming language and compiler built from scratch with a focus on **developer experience**.

Unlike traditional compilers that simply stop at errors, Reparo introduces a **self-healing engine** that:

* Detects errors
* Explains them clearly
* Suggests possible fixes
* (Future) Automatically corrects code

---

## 🧠 Key Features

### 🔹 Custom Language (ReparoLang)

* Simple, Python-like syntax
* No unnecessary boilerplate
* Beginner-friendly and forgiving

### 🔹 Lexer (Tokenization Engine)

* Converts raw code into structured tokens
* Supports identifiers, numbers, operators, and keywords

### 🔹 Error Detection System

* Identifies syntax and semantic issues
* Provides meaningful error messages

### 🔹 🛠️ Self-Healing Engine (Core Feature)

* Suggests fixes for common mistakes
* Helps developers debug faster
* Designed to evolve into an AI-powered correction system

---

## 🧩 Current Architecture

```
Source Code
    ↓
Lexer → Tokens
    ↓
(Parser - upcoming)
    ↓
AST
    ↓
Interpreter
    ↓
AI Self-Healing Engine
```

---

## 🛠️ Tech Stack

* **Language:** Python
* **Concepts:** Compiler Design, AST, Tokenization
* **Future AI Integration:** Rule-based → ML-based suggestions

---

## 📂 Project Structure

```
reparo/
│
├── lexer.py
├── tokens.py
├── main.py
└── tests/
```

---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/reparo.git
cd reparo
```

### 2. Run the compiler

```bash
python main.py
```

### 3. Enter sample code

```plaintext
a = 5
print(a)
```

---

## 🧪 Example Output

```
Token(IDENTIFIER, 'a')
Token(OPERATOR, '=')
Token(NUMBER, '5')
Token(KEYWORD, 'print')
...
```

---

## 🔮 Future Roadmap

* [ ] Parser (AST generation)
* [ ] Interpreter (code execution)
* [ ] Advanced error detection
* [ ] Auto-fix engine (self-healing v2)
* [ ] Complexity analysis
* [ ] Optimization suggestions
* [ ] Natural language → code support
* [ ] UI-based code builder (Flutter-inspired)

---

## 🎯 Why Reparo?

Traditional compilers:

> ❌ "Error at line 3"

Reparo:

> ✅ "Error at line 3 — Missing variable. Did you mean to define it?"

---

## 🤝 Contributing

This is an experimental project exploring the intersection of **compiler design and AI**.
Contributions, ideas, and feedback are welcome.

---

## 📌 Author

**Anshul Bhardwaj**
Computer Science Engineering Student
Passionate about AI, systems, and building real-world tech

---

## ⭐ If you like this project

Give it a star ⭐ and follow the journey as Reparo evolves into a full AI-powered development tool.
