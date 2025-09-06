"""
Form components for the AI Fitness Buddy app
Contains all the form elements and input validation functions
"""

import streamlit as st
from config import (
    FITNESS_GOALS, 
    ACTIVITY_LEVELS, 
    WORKOUT_TYPES, 
    DAYS_PER_WEEK_OPTIONS, 
    MINUTES_PER_SESSION_OPTIONS
)

def create_user_form():
    """
    Creates and displays the user information form
    Returns a dictionary with all user inputs
    """
    st.subheader("📋 Tell us about yourself")
    
    with st.form("user_info_form"):
        # Create two columns for better layout
        col1, col2 = st.columns(2)
        
        with col1:
            # Fitness Goal Selection
            fitness_goal = st.selectbox(
                "🎯 What's your fitness goal?",
                FITNESS_GOALS,
                help="Choose your primary fitness objective"
            )
            
            # Activity Level Selection
            activity_level = st.selectbox(
                "🏃 What's your current activity level?",
                ACTIVITY_LEVELS,
                help="How active are you in your daily life?"
            )
            
            # Workout Type Preference
            workout_type = st.selectbox(
                "🏋️ Where do you prefer to workout?",
                WORKOUT_TYPES,
                help="Choose your preferred workout environment"
            )
        
        with col2:
            # Time Commitment
            st.write("⏰ **Time Commitment**")
            days_per_week = st.selectbox(
                "Days per week:",
                DAYS_PER_WEEK_OPTIONS,
                index=2,  # Default to 3 days
                help="How many days per week can you commit to working out?"
            )
            
            minutes_per_session = st.selectbox(
                "Minutes per session:",
                MINUTES_PER_SESSION_OPTIONS,
                index=2,  # Default to 45 minutes
                help="How long can each workout session be?"
            )
        
        # Health Information Section
        st.write("🏥 **Basic Health Information**")
        
        # Create three columns for health info
        health_col1, health_col2, health_col3 = st.columns(3)
        
        with health_col1:
            age = st.number_input(
                "Age (years):",
                min_value=13,
                max_value=100,
                value=25,
                help="Your current age"
            )
        
        with health_col2:
            weight = st.number_input(
                "Weight (kg):",
                min_value=30.0,
                max_value=300.0,
                value=70.0,
                step=0.5,
                help="Your current weight in kilograms"
            )
        
        with health_col3:
            height = st.number_input(
                "Height (cm):",
                min_value=100,
                max_value=250,
                value=170,
                help="Your height in centimeters"
            )
        
        # Injuries/Limitations
        limitations = st.text_area(
            "🩹 Any injuries or physical limitations?",
            placeholder="e.g., knee injury, back problems, etc. (Leave blank if none)",
            help="This helps us create a safe workout plan for you"
        )
        
        # Submit Button
        submitted = st.form_submit_button(
            "🚀 Generate My Workout Plan",
            type="primary",
            use_container_width=True
        )
        
        if submitted:
            # Validate required fields
            if validate_form_data(age, weight, height):
                return {
                    "fitness_goal": fitness_goal,
                    "activity_level": activity_level,
                    "workout_type": workout_type,
                    "days_per_week": days_per_week,
                    "minutes_per_session": minutes_per_session,
                    "age": age,
                    "weight": weight,
                    "height": height,
                    "limitations": limitations if limitations else "None"
                }
            else:
                return None
    
    return None

def validate_form_data(age, weight, height):
    """
    Validates the form data and shows error messages if needed
    """
    if age < 13 or age > 100:
        st.error("Please enter a valid age between 13 and 100 years.")
        return False
    
    if weight < 30 or weight > 300:
        st.error("Please enter a valid weight between 30 and 300 kg.")
        return False
    
    if height < 100 or height > 250:
        st.error("Please enter a valid height between 100 and 250 cm.")
        return False
    
    return True

def display_user_summary(user_data):
    """
    Displays a summary of the user's information before generating the plan
    """
    st.subheader("📊 Your Profile Summary")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f"**🎯 Goal:** {user_data['fitness_goal']}")
        st.write(f"**🏃 Activity Level:** {user_data['activity_level']}")
        st.write(f"**🏋️ Workout Type:** {user_data['workout_type']}")
    
    with col2:
        st.write(f"**⏰ Schedule:** {user_data['days_per_week']} days/week, {user_data['minutes_per_session']} min/session")
        st.write(f"**👤 Age:** {user_data['age']} years")
        st.write(f"**⚖️ Weight:** {user_data['weight']} kg, **📏 Height:** {user_data['height']} cm")
    
    if user_data['limitations'] != "None":
        st.write(f"**🩹 Limitations:** {user_data['limitations']}")
