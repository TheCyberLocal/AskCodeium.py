# AskCodeium

## 🗺️ Project Overview

<table>
  <tr>
    <td style="padding: 10px;"><img src="./assets/codeium_logo.png" alt="" /></td>
    <td style="padding: 10px;">AskCodeium is an API designed to enable developer applications to interact with the Codeium chat service in real-time without requiring user accounts. The API focuses on simplicity and maintaining conversational context through thread management, providing a seamless integration experience for developers.</td>
  </tr>
</table>

## 🗝️ Key Features

- **Simplicity:** Easy setup and implementation process for developers, with clear documentation and examples.
- **Thread Context:** Allows applications to maintain the context of conversations across multiple queries.

## 🎯 Project Mission

The mission of AskCodeium is to democratize access to AI chat services by making them free, easy to integrate, and accessible for all developers.

## 💾 Installation

Install AskCodeium via pip:

```bash
pip install askcodeium
```

## ✨ AskCodeium in action!

```py
from AskCodeium import createChat

chat1 = createChat()

response = await chat1("What is the python programming language?")

print(response)
# Output Example:
# Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms like procedural, object-oriented, and functional programming.

response = await chat1("What did I previously ask you about?")

print(response)
# Output Example:
# You previously asked about the Python programming language.

chat1.clearHistory()

response = await chat1("What is the python programming language?")
print(response)
# Output Example:
# I'm sorry, I do not have the capability to recall previous interactions. How can I assist you today?
```

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
