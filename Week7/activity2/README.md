# Aquarium Management System

## Overview

This project is developed in Python to manage an aquarium in Auckland.

The system allows users to:
- Add fish to the aquarium
- Display fish inventory
- Identify fish categories

Fish Types:
- Goldfish
- Shark
- Angelfish
- Tuna
- Salmon

---

# Design Patterns Used

## 1. Factory Design Pattern

The Factory Pattern is used to create fish objects dynamically without exposing object creation logic.

Class Used:
- FishFactory

Purpose:
- Creates the correct fish object based on user input.

Example:
```python
fish = FishFactory.create_fish("Shark")