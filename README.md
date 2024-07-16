# Telegram Bot for Currency Conversion

This Telegram bot is written in Python and uses the `pyTelegramBotAPI` library to interact with Telegram and the `requests` library to get currency rates from the API of the National Bank of the Republic of Belarus (NBRB).

## Description

This bot responds to the `/start` and `/help` commands, providing the user with information on how to use the bot. The `/convert` command starts the currency conversion process. The user enters an amount, source currency, and target currency separated by a space, and the bot returns the converted amount based on the current exchange rates from the NBRB API.

## Installation

1. Make sure you have Python 3 installed.
2. Install the required libraries:
    '''bash
    pip install pyTelegramBotAPI requests
    '''

## Configuration

1. Create a `config.py` file and add your Telegram API key:
    '''python
    API_KEY = 'Enter KEY'
    '''

2. Download or clone the repository with the bot.

## Running

1. Run the `bot.py` file:
    '''bash
    python bot.py
    '''

## Note

Don't forget to replace **Enter KEY** with your actual Telegram API key.
