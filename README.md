# EXTENCORD

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Discord](https://img.shields.io/badge/Discord-Bot-5865F2)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Project-Modular-orange)

**EXTENCORD** is a modular and extensible Discord bot platform designed to be easily
expanded using standalone or integrated add-ons.
It allows features to be added, removed, or modified through independent modules,
without requiring changes to the core application.

The project focuses on **clean architecture**, **long-term maintainability**, and
**developer-friendly extensibility**, making it suitable not only for developers,
but also for users with little to no programming experience.

Extencord is designed so that both advanced developers and casual users can easily
enable, disable, or add their own features and add-ons without modifying the core
of the bot.


> [!WARNING]
> This project is still under active development.
> Some features may not work as expected or may contain bugs.
> If you encounter any issues, feel free to report them.


---

## 📑 Table of Contents
- [Features](#-features)
- [Basic Requirements](#-basic-requirements)
<!-- - [Usage](#-usage)
- [Modules](#-modules)
- [Contributing](#-contributing) -->

---

## 📌 Features

- **Modular add-on system**  
  The bot is built around a modular system that allows features to be added, removed,
  or replaced using standalone or integrated add-ons.

- **MongoDB database support**  
  Uses MongoDB for storing data in a reliable and scalable way.

- **Centralized command and event handling**  
  All commands and events are managed in a single, consistent system,
   keeping the codebase clean and organized.

- **Built-in add-ons**
  - **Music add-on** *(standalone)* — Enables music playback in voice channels using Lavalink.
  - **GTFS add-on** *(integrated)* — Provides access to transport data and schedules.

- **Open-source and extensible**  
  Fully open-source and designed to be easy to customize, extend, and adapt to
  different use cases.


---

## 🛠 Basic requirements

> Before running Extencord, make sure you have:

- Python 3.11+
- Discord bot created in the [Discord Developer Portal](https://discord.com/developers/applications)
- [MongoDB](https://www.mongodb.com) account
- Java (only needed for some modules, e.g. music playback)


---

