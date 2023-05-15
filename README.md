# Social Credit Bot
This is a Telegram bot that implements a social credit system within a supergroup chat. The bot allows users to assign positive or negative points (credits) to other users in the chat by sending specific stickers. The bot keeps track of users' social credits and enforces time restrictions on sticker assignments.

## Features
- Users can start the bot by sending the /start command.
- Stickers with the set name [PoohSocialCredit](https://t.me/addstickers/PoohSocialCredit) are used to assign credits.
- The bot checks if the sticker sender is allowed to assign credits based on the time restriction and their own credit balance.
- Users can check their own social credit balance by sending the /points command.
- The bot enforces a time limit of 5 minutes between each credit assignment.
- If a user's credit balance drops below 100, they can not assign credits.
## Files
The project consists of the following files:

- **bot.py**: Contains the main code for the Telegram bot, including message handlers and bot setup.
- **CONFIG.py**: A configuration file that stores the Telegram bot token.
- **queries.py**: Contains a Database class responsible for interacting with a MySQL database.
## Requirements
To run the bot, you need to have the following:

- Python 3.x
- **telebot** library
- **mysql-connector-python** library
- MySQL database
## Configuration
Before running the bot, make sure to configure the following:

- Update the MySQL database connection details in the queries.py file (host, user, password, database).
- Set your Telegram bot token in the **CONFIG.py** file.
## Usage
1. Install the required Python libraries: **telebot** and **mysql-connector-python**.
2. Set up a MySQL database and update the connection details in the **queries.py** file.
3. Set your Telegram bot token in the **CONFIG.py** file.
4. Run the **bot.py** file using Python: python **bot.py**.
5. Add the bot to a Telegram supergroup chat and interact with it using the available commands and stickers.

Please note that the bot requires continuous execution to function correctly. You may consider hosting it on a server or using a cloud platform.

## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## Disclaimer
This bot is provided as-is without any warranty. Use it at your own risk. The developers are not responsible for any damages or misuse caused by the bot.
