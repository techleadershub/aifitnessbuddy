"""
Configuration file for AI Fitness Buddy app
Contains all the constants and settings used throughout the app
"""

import streamlit as st

# OpenAI API Configuration - Using Streamlit Secrets
try:
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
except KeyError:
    OPENAI_API_KEY = None

# App Configuration
APP_TITLE = "AI Fitness Buddy"
WELCOME_MESSAGE = "Hi! I'm your AI Fitness Buddy. Let's create a personalized workout plan for you."

# Form Options
FITNESS_GOALS = [
    "Weight Loss",
    "Muscle Gain", 
    "Endurance",
    "Flexibility",
    "General Fitness"
]

ACTIVITY_LEVELS = [
    "Sedentary",
    "Lightly Active",
    "Active", 
    "Very Active"
]

WORKOUT_TYPES = [
    "Home",
    "Gym",
    "Equipment",
    "Bodyweight"
]

# Time commitment options
DAYS_PER_WEEK_OPTIONS = [1, 2, 3, 4, 5, 6, 7]
MINUTES_PER_SESSION_OPTIONS = [15, 30, 45, 60, 75, 90, 120]

# Prompt template for OpenAI
WORKOUT_PROMPT_TEMPLATE = """
You are a professional fitness trainer. Create a personalized workout plan based on the following user information:

**User Profile:**
- Fitness Goal: {fitness_goal}
- Current Activity Level: {activity_level}
- Preferred Workout Type: {workout_type}
- Time Commitment: {days_per_week} days per week, {minutes_per_session} minutes per session
- Age: {age} years
- Weight: {weight} kg
- Height: {height} cm
- Injuries/Limitations: {limitations}

Please provide:
1. A personalized workout plan for one week
2. Specific exercises with sets and reps
3. Safety tips based on their limitations
4. Progression suggestions
5. Nutrition tips that complement their fitness goal

Format the response in a clear, easy-to-follow structure with proper headings and bullet points.
"""
