# Expense Tracker Bot

A Telegram-based expense tracking bot powered by OpenAI's language models. Track your daily expenses naturally through conversational interactions and gain insights with visual analytics.

## Project Description

**Expense Tracker Bot** is an intelligent Telegram bot that helps users manage their personal finances effortlessly. Instead of dealing with complex forms, simply chat with the bot in natural language to log expenses, categorize transactions, and generate spending reports.

### Key Features

- 💬 **Natural Language Processing**: Log expenses by simply messaging the bot naturally (e.g., "I spent $50 on groceries")
- 📊 **Visual Analytics**: Generate charts and graphs to visualize spending patterns
- 💾 **Persistent Storage**: All expenses are securely stored in a database
- 🤖 **AI-Powered**: Powered by OpenAI's language models for intelligent expense categorization
- 📱 **Telegram Integration**: Seamless integration with Telegram platform

## Installation

### Prerequisites

- Python 3.8 or higher
- Telegram account and bot token (get one from [@BotFather](https://t.me/botfather))
- OpenAI API key (get one from [OpenAI Console](https://platform.openai.com/api-keys))

### Setup Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/expense-tracker-bot.git
   cd expense-tracker-bot
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file in the project root with your credentials:
   ```bash
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the bot**:
   ```bash
   python src/bot.py
   ```

## Usage

Once the bot is running, search for it in Telegram using your bot username and start a conversation.

### Example Commands

- **Log an expense**: "I spent 50 euros on groceries today"
- **View spending summary**: "Show me my expenses from last week"
- **Generate chart**: "Create a chart of my spending by category"
- **Set budget**: "Set my monthly food budget to 300 euros"

The bot will process your request, categorize the expense, and store it in the database. Use the `/stats` command to view your spending analytics with visual charts.

## Tech Stack

### Core Dependencies

- **[python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)** (v22.7): Telegram Bot API wrapper
- **[OpenAI](https://github.com/openai/openai-python)** (v2.30.0): LLM integration for natural language understanding
- **[Pydantic](https://docs.pydantic.dev)** (v2.12.5): Data validation and settings management
- **[python-dotenv](https://github.com/theskumar/python-dotenv)** (v1.2.2): Environment variable management

### Utility Libraries

- **httpx** (v0.28.1): Async HTTP client
- **tqdm** (v4.67.3): Progress bars for batch operations
- **typing-inspection** (v0.4.2): Runtime type annotation utilities

### Development

- Python 3.8+
- Git for version control

## File Structure

```
expense-tracker-bot/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (credentials)
├── .env.example             # Example environment file
├── .gitignore               # Git ignore rules
│
├── src/                     # Source code
│   ├── bot.py              # Main Telegram bot logic and handlers
│   ├── llm.py              # OpenAI API integration and prompts
│   ├── database.py         # Database models and operations
│   └── charts.py           # Analytics and visualization functions
│
└── tests/                   # Test suite
    └── (test files)
```

### Module Descriptions

| Module | Purpose |
|--------|---------|
| `bot.py` | Core Telegram bot implementation, message handlers, and command processing |
| `llm.py` | Integration with OpenAI API for natural language understanding and expense categorization |
| `database.py` | Database connection, schema definition, and CRUD operations for expenses |
| `charts.py` | Generation of spending charts and visual analytics |

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions, please open an issue on the [GitHub repository](https://github.com/yourusername/expense-tracker-bot/issues).
