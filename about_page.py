import streamlit as st

def show_about_page():
    """Display the 'About Me' page in the Streamlit app."""
    st.title("About Me")
    
    col1, col2 = st.columns(2)
    with col1:
        st.header("Hi, I'm Rodrigues!")
        st.write("""
        ### Data Scientist & Software Engineer
        Based in New Haven, Connecticut, I specialize in turning data into actionable insights and powerful software solutions.
        """)
        
    with col2:
        # Update the image file path to use an existing file
        st.image("assets/images/main-rodrigues.jpg", width=300, caption="Hello from Rodrigues!")

    st.write("---")
    
    st.header("Project Background")
    st.write("""
    This project is a comprehensive machine learning model focused on predicting software developer salaries globally.
    Utilizing the Stack Overflow Developer Survey data, this tool leverages advanced data science techniques to provide accurate and relevant salary predictions.
    """)
    
    st.subheader("Technologies Used")
    techs = ["Python", "Pandas", "Scikit-Learn", "Streamlit", "Matplotlib", "Jupyter Notebook"]
    for tech in techs:
        st.write(f"- {tech}")

    st.subheader("Notebook Snapshots")
    col1, col2 = st.columns(2)
    with col1:
        # Update to use another existing file
        st.image("assets/images/jupyter-notebook.png", caption="Data Cleaning Process")
    with col2:
        # If you don't have another image, you might repeat the same or remove this
        st.image("assets/images/vs-bulding.png", caption="Model Building Process")
    
    st.write("---")
    st.header("Why this project?")
    st.write("""
    - **Skill Enhancement**: To refine my data science and machine learning skills.
    - **Real-world Application**: To apply theoretical knowledge in a practical, impactful manner.
    - **Community Contribution**: To aid peers in the tech industry by providing a useful tool for career development.
    """)

    st.write("---")
    st.header("Connect with Me")
    st.markdown("""
    - **LinkedIn**: [Your LinkedIn](https://www.linkedin.com/in/allahu-rodrigues)
    - **GitHub**: [Your GitHub](https://github.com/AllahuRodrigues)
    """)
    
    with open("Rodrigues_Allah-u-abha_Resume.pdf", "rb") as file:
        btn = st.download_button(
            label="Download my Resume",
            data=file,
            file_name="Rodrigues_Allah-u-abha_Resume.pdf",
            mime="application/octet-stream"
        )
    
    if st.button('Show More About the Project'):
        with st.expander("See Explanation"):
            st.write("""
            Detailed explanation about the project methodologies, data handling, challenges faced,
            and solutions implemented.
            """)
            st.image("assets/images/explore-menu.png", caption="In-depth Methodology")

if __name__ == "__main__":
    show_about_page()
