<h1 align="left" style="margin-bottom: 20px; font-weight: 500; font-size: 50px; color: black;">
  FastAPI Auth NanoID
</h1>

---

<h2> The project is based on <a href="https://pypi.org/project/fastapi-jwt-auth/" target="_blank">Fastapi-jwt-auth</a> that is no longer maintained.</h2>

**Documentation**: <a href="https://Kilian-Pichard.github.io/fastapi-auth-nanoid" target="_blank">https://Kilian-Pichard.github.io/fastapi-auth-nanoid</a>

**Source Code**: <a href="https://github.com/Kilian-Pichard/fastapi-auth-nanoid" target="_blank">https://github.com/Kilian-Pichard/fastapi-auth-nanoid</a>

---

## Features

A FastAPI extension that provides Authentication support using NanoID (secure, easy to use and lightweight).
Firstly, JWT auth will be available.

- Access tokens and refresh tokens
- Freshness Tokens
- Revoking Tokens
- Support for WebSocket authorization
- Support for adding custom claims to JSON Web Tokens
- Storing tokens in cookies and CSRF protection

## Installation

The easiest way to start working with this extension with pip

```bash
pip install fastapi-auth-nanoid
```

If you want to use asymmetric (public/private) key signing algorithms, include the <b>asymmetric</b> extra requirements.

```bash
pip install 'fastapi-auth-nanoid[asymmetric]'
```

## License

This project is licensed under the terms of the MIT license.
