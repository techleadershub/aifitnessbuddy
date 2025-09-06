"""
OpenAI API integration for AI Fitness Buddy
Handles communication with OpenAI to generate personalized workout plans
"""

import streamlit as st
from openai import OpenAI
from config import OPENAI_API_KEY, WORKOUT_PROMPT_TEMPLATE

def initialize_openai_client():
    """
    Initialize and return OpenAI client
    """
    if not OPENAI_API_KEY:
        st.error("⚠️ OpenAI API key not found! Please set your OPENAI_API_KEY in the .env file.")
        st.info("💡 Create a .env file in your project directory with: OPENAI_API_KEY=your_key_here")
        return None
    
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        return client
    except Exception as e:
        st.error(f"❌ Error initializing OpenAI client: {str(e)}")
        return None

def generate_workout_plan(user_data):
    """
    Generate a personalized workout plan using OpenAI API
    
    Args:
        user_data (dict): Dictionary containing user's fitness information
    
    Returns:
        str: Generated workout plan or None if error occurred
    """
    
    # Initialize OpenAI client
    client = initialize_openai_client()
    if not client:
        return None
    
    # Format the prompt with user data
    prompt = WORKOUT_PROMPT_TEMPLATE.format(
        fitness_goal=user_data['fitness_goal'],
        activity_level=user_data['activity_level'],
        workout_type=user_data['workout_type'],
        days_per_week=user_data['days_per_week'],
        minutes_per_session=user_data['minutes_per_session'],
        age=user_data['age'],
        weight=user_data['weight'],
        height=user_data['height'],
        limitations=user_data['limitations']
    )
    
    try:
        # Show progress indicator
        with st.spinner("🤖 Your AI Fitness Buddy is creating your personalized workout plan..."):
            
            # Make API call to OpenAI
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # You can change to gpt-4 if you have access
                messages=[
                    {
                        "role": "system", 
                        "content": "You are a professional fitness trainer with expertise in creating safe, effective, and personalized workout plans."
                    },
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ],
                max_tokens=2000,
                temperature=0.7
            )
            
            # Extract the workout plan from the response
            workout_plan = response.choices[0].message.content
            return workout_plan
            
    except Exception as e:
        st.error(f"❌ Error generating workout plan: {str(e)}")
        st.info("💡 This might be due to:")
        st.info("- Invalid API key")
        st.info("- Insufficient API credits")
        st.info("- Network connection issues")
        return None

def display_workout_plan(workout_plan):
    """
    Display the generated workout plan in a nicely formatted way
    
    Args:
        workout_plan (str): The workout plan text from OpenAI
    """
    if workout_plan:
        st.success("🎉 Your personalized workout plan is ready!")
        
        # Create an expandable section for the workout plan
        with st.expander("📋 Your Complete Workout Plan", expanded=True):
            st.markdown(workout_plan)
        
        # Add download button
        st.download_button(
            label="📄 Download Your Workout Plan",
            data=workout_plan,
            file_name="my_workout_plan.txt",
            mime="text/plain",
            type="secondary"
        )
        
        # Add feedback section
        st.subheader("💬 How was your experience?")
        feedback = st.text_area(
            "Share your thoughts about the workout plan:",
            placeholder="Any suggestions or feedback about your personalized plan?"
        )
        
        if st.button("📨 Submit Feedback", type="secondary"):
            if feedback:
                st.success("Thank you for your feedback! 🙏")
                # In a real app, you might want to save this feedback to a database
            else:
                st.warning("Please enter some feedback before submitting.")

def check_api_status():
    """
    Check if OpenAI API is properly configured and accessible
    """
    if not OPENAI_API_KEY:
        return False, "API key not found"
    
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        # Test with a simple request
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=5
        )
        return True, "API connection successful"
    except Exception as e:
        return False, f"API error: {str(e)}"
