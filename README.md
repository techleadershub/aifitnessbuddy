# 💪 AI Fitness Buddy

A personalized workout plan generator powered by OpenAI API and built with Streamlit.

## 🌟 Features

- **Personalized Workout Plans**: Get customized workouts based on your fitness goals, activity level, and preferences
- **User-Friendly Interface**: Clean, intuitive form with comprehensive health and fitness questions
- **AI-Powered Recommendations**: Uses OpenAI's GPT model to generate detailed, professional workout plans
- **Multiple Workout Types**: Support for home, gym, equipment-based, and bodyweight workouts
- **Safety First**: Takes into account injuries and physical limitations
- **Download Plans**: Save your workout plan as a text file
- **Responsive Design**: Works great on desktop and mobile devices

## 📋 What the App Asks

The app collects the following information to create your personalized plan:

- **Fitness Goal**: Weight Loss, Muscle Gain, Endurance, Flexibility, General Fitness
- **Activity Level**: Sedentary, Lightly Active, Active, Very Active
- **Workout Preference**: Home, Gym, Equipment, Bodyweight
- **Time Commitment**: Days per week (1-7) and minutes per session (15-120)
- **Basic Health Info**: Age, weight, height
- **Limitations**: Any injuries or physical restrictions

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. **Clone or download this project**
   ```bash
   # If you have git installed
   git clone <your-repo-url>
   cd AIfitnessBuddy
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key**
   
   Create a folder named `.streamlit` and inside it create a file named `secrets.toml`:
   ```
   OPENAI_API_KEY = "your_openai_api_key_here"
   ```
   
   Replace `your_openai_api_key_here` with your actual OpenAI API key.

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   
   The app will automatically open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
AIfitnessBuddy/
├── app.py                 # Main Streamlit application
├── config.py              # Configuration and constants
├── form_components.py     # Form creation and validation
├── openai_integration.py  # OpenAI API integration
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .streamlit/
    └── secrets.toml      # Your API key (create this file)
```

## 🔧 File Explanations

- **`app.py`**: The main application file that runs the Streamlit interface
- **`config.py`**: Contains all configuration settings, form options, and the prompt template
- **`form_components.py`**: Handles the user input form, validation, and display functions
- **`openai_integration.py`**: Manages communication with the OpenAI API
- **`requirements.txt`**: Lists all Python packages needed to run the app

## 🛠️ Customization

### Changing the AI Model
In `openai_integration.py`, you can change the model:
```python
model="gpt-3.5-turbo"  # Change to "gpt-4" if you have access
```

### Adding New Fitness Goals
In `config.py`, modify the `FITNESS_GOALS` list:
```python
FITNESS_GOALS = [
    "Weight Loss",
    "Muscle Gain", 
    "Endurance",
    "Flexibility",
    "General Fitness",
    "Your New Goal"  # Add here
]
```

### Customizing the Prompt
Modify `WORKOUT_PROMPT_TEMPLATE` in `config.py` to change how the AI generates plans.

## ⚠️ Troubleshooting

### Common Issues

1. **"OpenAI API key not found"**
   - Make sure you created the `.streamlit/secrets.toml` file
   - Check that your API key is correct and in quotes
   - Ensure the `.streamlit` folder is in the same directory as `app.py`

2. **"Error generating workout plan"**
   - Check your internet connection
   - Verify you have sufficient OpenAI API credits
   - Try refreshing the page

3. **App won't start**
   - Make sure you installed all requirements: `pip install -r requirements.txt`
   - Check that you're using Python 3.7 or higher

### Getting Help

If you encounter issues:
1. Check the sidebar in the app for system status
2. Look at the error messages in your terminal
3. Ensure your OpenAI API key is valid and has credits

## 💡 Tips for Best Results

- Be specific about injuries or limitations
- Choose realistic time commitments
- Try different combinations to see various workout styles
- Download your plan and track your progress

## 🔒 Privacy & Security

- Your personal information is only sent to OpenAI to generate your workout plan
- No data is stored permanently by this application
- Your API key is kept secure in the `.env` file (never share this file)

## 📈 Future Enhancements

Potential improvements for this app:
- Progress tracking
- Workout history
- Integration with fitness trackers
- Meal planning suggestions
- Community features

---

**Enjoy your fitness journey! 💪**

*Made with ❤️ using Streamlit and OpenAI API*
