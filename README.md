# AskCodeium

## 🗺️ [Project Overview](https://github.com/TheCyberLocal/AskCodeium)

<table>
  <tr>
    <td style="padding: 10px;"><img src="https://github.com/TheCyberLocal/AskCodeium/blob/main/codeium_logo.png" alt="" /></td>
    <td style="padding: 10px;">AskCodeium is an API designed to enable developer applications to interact with the Codeium chat service in real-time without requiring user accounts. The API focuses on simplicity and maintaining conversational context through thread management, providing a seamless integration experience for developers.</td>
  </tr>
</table>

## 🗝️ Key Features

- **Simplicity:** Easy setup and implementation process for developers, with clear documentation and examples.
- **Thread Context:** Allows applications to maintain the context of conversations across multiple queries.
- **Open Source and Free:** There are many other AI chat APIs available, but what makes AskCodeium unique is its open-source and free nature.
- **Multiligual Availability:** AskCodeium allows developers to interact with the API across languages.

## 🎯 Project Mission

The mission of AskCodeium is to make AI chat APIs free, easy to integrate, and accessible for all developers.

## 💾 Installation

Install AskCodeium via pip:

```bash
pip install AskCodeium
```

## ✨ AskCodeium in action!

### 📑 [AskCodeium Documentation](./docs/askcodeium_docs.md)

```py
from AskCodeium import createChat

chat1 = createChat()

response = chat1("In short, what is the python programming language?")
print(response)
# Output Example:
# Python is a high-level, interpreted programming language known for its simplicity and readability.

response = chat1("What did I previously ask you about?")
print(response)
# Output Example:
# You previously asked about the Python programming language.

chat1.clear_history()

response = chat1("What did I previously ask you about?")
print(response)
# Output Example:
# I'm sorry, I do not have the capability to recall previous interactions. How can I assist you today?
```

Integrate artificial intelligence into your applications effortlessly with AskCodeium, the ultimate API for free and easy-to-use chat interactions. Simplify your development process with seamless thread management and maintain conversational context without the need for user accounts. Start using AskCodeium today!

## 🌎 Languages

### AskCodeium for Python

[![](https://img.shields.io/pypi/v/AskCodeium?color=blue&logo=pypi)](https://pypi.org/project/AskCodeium/)
[![](https://img.shields.io/badge/AskCodeium.py-black?logo=github&logoColor=white)](https://github.com/TheCyberLocal/AskCodeium.py)

### AskCodeium for JavaScript

[![](https://img.shields.io/npm/v/@thecyberlocal/askcodeium?color=blue&logo=npm)](https://www.npmjs.com/package/@thecyberlocal/askcodeium)
[![](https://img.shields.io/badge/AskCodeium.js-black?logo=github&logoColor=white)](https://github.com/TheCyberLocal/AskCodeium.js)

## 🌐 Socials

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/tzm01)
[![GitHub](https://img.shields.io/badge/GitHub-black?logo=github&logoColor=white)](https://github.com/TheCyberLocal)
[![PyPI](https://img.shields.io/badge/PyPI-3776AB?logo=pypi&logoColor=white)](https://pypi.org/user/TheCyberLocal/)
[![npm](https://img.shields.io/badge/npm-%23FFFFFF.svg?logo=npm&logoColor=D00000)](https://www.npmjs.com/~thecyberlocal)

## 💖 Support

If you find my content helpful or interesting, consider buying me a coffee. Every cup is greatly appreciated and fuels my work!

[![Buy Me a Coffee](https://img.shields.io/badge/-buy_me_a%C2%A0coffee-gray?logo=buy-me-a-coffee)](https://buymeacoffee.com/thecyberlocal)
[![PayPal](https://img.shields.io/badge/PayPal-00457C?logo=paypal&logoColor=white)](https://www.paypal.com/paypalme/TheCyberLocal)
[![Venmo](https://img.shields.io/badge/Venmo-008CFF?logo=venmo&logoColor=white)](https://www.venmo.com/TheCyberLocal)
