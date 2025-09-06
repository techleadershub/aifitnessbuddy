"""
AI Fitness Buddy - Main Streamlit Application
A personalized workout plan generator using OpenAI API
"""

import streamlit as st
from config import APP_TITLE, WELCOME_MESSAGE
from form_components import create_user_form, display_user_summary
from openai_integration import generate_workout_plan, display_workout_plan, check_api_status

def main():
    """
    Main function that runs the Streamlit app
    """
    # Configure the page
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon="💪",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .welcome-message {
        font-size: 1.2rem;
        text-align: center;
        margin: 1rem 0;
        padding: 1rem;
        background-color: #f0f2f6;
        border-radius: 10px;
        border-left: 5px solid #667eea;
    }
    .stButton > button {
        width: 100%;
        border-radius: 20px;
        height: 3rem;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Main header
    st.markdown(f"""
    <div class="main-header">
        <h1>💪 {APP_TITLE}</h1>
        <p>Your Personal AI-Powered Fitness Coach</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Welcome message
    st.markdown(f"""
    <div class="welcome-message">
        <p>{WELCOME_MESSAGE}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if 'workout_generated' not in st.session_state:
        st.session_state.workout_generated = False
    if 'user_data' not in st.session_state:
        st.session_state.user_data = None
    
    # Check API status in sidebar
    with st.sidebar:
        st.header("🔧 System Status")
        api_status, api_message = check_api_status()
        if api_status:
            st.success(f"✅ {api_message}")
        else:
            st.error(f"❌ {api_message}")
            st.info("💡 Make sure you have:")
            st.info("1. Created a .env file")
            st.info("2. Added OPENAI_API_KEY=your_key")
            st.info("3. Have sufficient API credits")
        
        st.header("📚 How it works")
        st.info("""
        1. **Fill out the form** with your fitness details
        2. **Submit** to generate your plan  
        3. **Review** your personalized workout
        4. **Download** and start your fitness journey!
        """)
    
    # Main app logic
    if not st.session_state.workout_generated:
        # Show the form
        user_data = create_user_form()
        
        if user_data:
            # Store user data in session state
            st.session_state.user_data = user_data
            
            # Display user summary
            st.markdown("---")
            display_user_summary(user_data)
            
            # Generate workout plan
            st.markdown("---")
            workout_plan = generate_workout_plan(user_data)
            
            if workout_plan:
                # Store the workout plan and mark as generated
                st.session_state.workout_plan = workout_plan
                st.session_state.workout_generated = True
                
                # Display the workout plan
                display_workout_plan(workout_plan)
                
                # Add button to start over
                st.markdown("---")
                col1, col2, col3 = st.columns([1, 1, 1])
                with col2:
                    if st.button("🔄 Create New Plan", type="secondary"):
                        # Reset session state
                        st.session_state.workout_generated = False
                        st.session_state.user_data = None
                        if 'workout_plan' in st.session_state:
                            del st.session_state.workout_plan
                        st.rerun()
    
    else:
        # Show the generated workout plan
        if 'workout_plan' in st.session_state:
            # Display user summary
            if st.session_state.user_data:
                display_user_summary(st.session_state.user_data)
                st.markdown("---")
            
            # Display the workout plan
            display_workout_plan(st.session_state.workout_plan)
            
            # Add button to start over
            st.markdown("---")
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                if st.button("🔄 Create New Plan", type="secondary"):
                    # Reset session state
                    st.session_state.workout_generated = False
                    st.session_state.user_data = None
                    if 'workout_plan' in st.session_state:
                        del st.session_state.workout_plan
                    st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem 0;">
        <p>Made with ❤️ using Streamlit and OpenAI API</p>
        <p>Stay fit, stay healthy! 💪</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
