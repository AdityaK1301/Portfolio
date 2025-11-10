import streamlit as st
from pathlib import Path
import pandas as pd

try:
    from streamlit_navigation import Page, Navigation
except ImportError:
    class Page:
        def __init__(self, func, title, icon, default=False):
            self.func = func
            self.title = title
            self.icon = icon
            self.default = default
    
    class Navigation:
        def __init__(self, pages):
            self.pages = pages
        
        def run(self):
            tabs = st.tabs([page.title for page in self.pages])
            for i, (tab, page) in enumerate(zip(tabs, self.pages)):
                with tab:
                    page.func()

st.set_page_config(
    page_title="Portfolio",
    
    layout="wide"
)

def home():
    


    
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
               padding: 2rem; border-radius: 15px; color: white; margin-bottom: 2rem;'>
        <h2 style='color: white; text-align: center; margin-bottom: 1rem;'>👋 About Me</h2>
        <p style='text-align: center; font-size: 1.1rem; margin-bottom: 0;'>
        Transforming complex challenges into intelligent solutions through cutting-edge technology
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        I'm a **Computer Science graduate** from **Bennett University**, equipped with a strong foundation in 
        **Data Structures & Algorithms** and specialized expertise in **Artificial Intelligence & Machine Learning**.
        
        My passion lies in architecting intelligent systems that leverage **Generative AI** and **Large Language Models** 
        to solve real-world problems. I thrive on building scalable, efficient solutions that bridge the gap between 
        theoretical concepts and practical applications.
        
        ### 🎯 What I Bring:
        - **AI/ML Expertise**: Deep learning, neural networks, and modern AI architectures
        - **Full-Stack AI Development**: End-to-end solution design and implementation
        - **Problem-Solving Mindset**: Algorithmic thinking and optimized system design
        - **Technical Proficiency**: Python-centric development with robust engineering practices
        """)
    
    with col2:
        st.markdown("""
        <div style='background-color: #1a1a1a; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #764ba2;'>
            <h4 style='color: #764ba2;'>📍 Location</h4>
            <p>Delhi, India</p>
            
        <h4 style='color: #764ba2;'>🎓 Education</h4>
            <p>B.Tech CSE<br>Bennett University</p>
            
        <h4 style='color: #764ba2;'>🤖 Specialization</h4>
            <p>AI/ML Engineering<br>Generative AI</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.header("🛠️ Knowledge Base")
    
    tab1, tab2, tab3 = st.tabs(["Programming & Databases", "AI/ML Stack", "Tools & Frameworks"])
    
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Languages**")
            st.markdown("- 🐍 Python")
            st.markdown("- ⚡ C++")
            st.markdown("- 🗄️ SQL")
        with col2:
            st.markdown("**Databases**")
            
            st.markdown("- 🍃 MongoDB")
            st.markdown("- 🐬 MySQL")
    
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**AI/ML Core**")
            st.markdown("- 🤖 Generative AI")
            st.markdown("- 🧠 LLMs")
            st.markdown("- 🔍 RAG")
            st.markdown("- 🎓 Machine Learning and Deep Learning")
        with col2:
            st.markdown("**Libraries**")
            st.markdown("- 📊 TensorFlow/Keras")
            st.markdown("- 🐼 Pandas")
            st.markdown("- 🔢 NumPy")
            st.markdown("- 📈 Matplotlib")
    
    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Development**")
            st.markdown("- 🌐 Flask")
            st.markdown("- 🔌 REST APIs")
            st.markdown("- 🎈 Streamlit")
        with col2:
            st.markdown("**Tools**")
            st.markdown("- 📓 Jupyter")
            st.markdown("- 💻 VS Code")
            st.markdown("- 🔧 Git & GitHub")
            st.markdown("- 🤝 Google Colab")
    
    
def projects():
    st.header("🚀 Featured Projects")

    with st.expander("🤖 **LangChain RAG Chatbot** | AI Intern Project", expanded=False):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown("""
            **📝 Project Overview:**
            Advanced Retrieval-Augmented Generation chatbot built with LangChain, providing 
            intelligent question-answering capabilities with contextual understanding.
            
            **✨ Key Features:**
            - ✅ **RAG Architecture** for enhanced response generation
            - ✅ **Vector Database Integration** for efficient information retrieval
            - ✅ **Contextual Understanding** with advanced language models
            - ✅ **Scalable Design** for handling multiple query types
            
            **🛠️ Tech Stack:** `Python` `LangChain` `RAG` `Vector DB` `LLMs` `FAISS`
            """)
        
        with col2:
            st.metric("Architecture", "RAG", "Advanced AI")
            st.metric("Framework", "LangChain", "Modern Tooling")
            
            if st.button("🔗 View RAG Chatbot", key="rag"):
                st.markdown("[Open Project Repository](https://github.com/AdityaK1301/LangChain-RAG-Chatbot)")
    
    st.markdown("---")
    
    with st.expander("🎯 **EDUVISION – AI Career Advisor** ", expanded=False):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown("""
            **📝 Project Overview:**
            Developed an intelligent career guidance platform that analyzes resumes and provides 
            personalized job role recommendations and learning path suggestions.
            
            **✨ Key Achievements:**
            - ✅ **98% text extraction accuracy** from resumes
            - ✅ Integrated **Lightcast Open Skills API** for real-time market data
            - ✅ **TF-IDF & Sentence Transformers** for intelligent matching
            - ✅ **Streamlit-based** interactive web application
            
            **🛠️ Tech Stack:** `Python` `Streamlit` `Sentence Transformers` `TF-IDF` `Lightcast API` `NLP`
            """)
        
        with col2:
            st.metric("Accuracy", "98%", "Text Extraction")
            st.metric("API Integration", "Lightcast", "Real-time Data")
            
            if st.button("🔗 View EDUVISION", key="eduvision"):
                st.markdown("[Open Project Repository](https://github.com/AdityaK1301/EDUVISION)")
    
    st.markdown("---")
    
    with st.expander("👋 **Sign Language Detection** ", expanded=False):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown("""
            **📝 Project Overview:**
            Real-time sign language recognition system using computer vision and deep learning 
            for gesture detection and classification.
            
            **✨ Key Achievements:**
            - ✅ **87% mAP** using SSD-MobileNet with transfer learning
            - ✅ **Real-time processing** with OpenCV and TensorFlow
            - ✅ **Data augmentation** for improved model generalization
            - ✅ **Object Detection API** integration for efficient inference
            
            **🛠️ Tech Stack:** `TensorFlow` `OpenCV` `Object Detection API` `Python` `Computer Vision`
            """)
        
        with col2:
            st.metric("mAP Score", "87%", "Detection Accuracy")
            st.metric("Processing", "Real-time", "Live Video")
            
            if st.button("🔗 View Sign Language Project", key="signlang"):
                st.markdown("[Open Project Repository](https://github.com/AdityaK1301/Sign-Language-Detection)")
    
    st.markdown("---")
    
    
    with st.expander("📈 **Stock Price Prediction** ", expanded=False):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown("""
            **📝 Project Overview:**
            Machine learning system for predicting stock prices using time series analysis 
            and advanced forecasting models with financial data.
            
            **✨ Key Features:**
            - ✅ **Time Series Analysis** for financial data patterns
            - ✅ **Multiple ML Models** comparison and evaluation
            - ✅ **Real-time Data Processing** from financial APIs
            - ✅ **Predictive Analytics** for investment insights
            
            **🛠️ Tech Stack:** `Python` `Machine Learning` `Time Series` `Pandas` `Scikit-learn` `LSTM`
            """)
        
        with col2:
            st.metric("Domain", "Finance", "ML Application")
            st.metric("Technique", "Time Series", "Forecasting")
            
            if st.button("🔗 View Stock Prediction", key="stock"):
                st.markdown("[Open Project Repository](https://github.com/AdityaK1301/Stock-Price-Prediction)")
    


def experience():
    st.title("💼 Experience")
    
    st.markdown("""
    <div style='background: linear-gradient(135deg, #0c2461 0%, #1e3799 100%); 
               padding: 2rem; border-radius: 15px; margin-bottom: 2rem; color: white;'>
        <div style='display: flex; justify-content: space-between; align-items: start;'>
            <div style='flex: 3;'>
                <h2 style='color: white; margin-bottom: 0.3rem;'>AI Intern</h2>
                <h3 style='color: #BB86FC; margin-bottom: 1rem;'>Alexion Techno Pvt. Ltd.</h3>
                <p style='color: #e0e0e0; font-size: 1rem; line-height: 1.6;'>
                Developed an <b>AI-powered CBSE Q&A chatbot</b> using <b>LangChain</b>, <b>RAG</b>, and <b>Streamlit</b>, enabling intelligent retrieval over NCERT textbooks.<br><br>
Built and deployed <b>Flask REST APIs</b> for document processing and inference, integrating <b>voice-based interaction</b> with SpeechRecognition.<br><br>
Optimized performance through <b>Groq/Ollama LLMs</b> and <b>FAISS vector stores</b>, achieving a <b>40% reduction in response time</b> and improving scalability for educational AI solutions.
                </p>
            </div>
            <div style='flex: 1; text-align: right;'>
                <div style='background: rgba(255,255,255,0.1); padding: 0.5rem 1rem; 
                           border-radius: 20px; color: white; display: inline-block;'>
                    Sept 2025 - Present
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🛠️ Technologies & Achievements")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style='background-color: #1a1a1a; padding: 1rem; border-radius: 10px; border-left: 4px solid #4FC3F7;'>
        <h4 style='color: #4FC3F7;'>🤖 AI/ML Stack</h4>
        <table style='width: 100%; color: white;'>
        <tr><td>• LangChain</td></tr>
        <tr><td>• FAISS</td></tr>
        <tr><td>• Groq LLMs</td></tr>
        <tr><td>• SpeechRecognition</td></tr>
        </table>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background-color: #1a1a1a; padding: 1rem; border-radius: 10px; border-left: 4px solid #BB86FC;'>
        <h4 style='color: #BB86FC;'>🎯 Deliverables</h4>
        <table style='width: 100%; color: white;'>
        <tr><td>• CBSE Chatbot</td></tr>
        <tr><td>• Doc Processing</td></tr>
        <tr><td>• Voice Q&A</td></tr>
        </table>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background-color: #1a1a1a; padding: 1rem; border-radius: 10px; border-left: 4px solid #03DAC6;'>
        <h4 style='color: #03DAC6;'>🌐 Backend</h4>
        <table style='width: 100%; color: white;'>
        <tr><td>• Flask APIs</td></tr>
        <tr><td>• Scalable Arch</td></tr>
        <tr><td>• Real-time Processing</td></tr>
        </table>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style='background-color: #1a1a1a; padding: 1rem; border-radius: 10px; border-left: 4px solid #CF6679;'>
        <h4 style='color: #CF6679;'>📊 Impact</h4>
        <table style='width: 100%; color: white;'>
        <tr><td>• Edu Automation</td></tr>
        <tr><td>• Enhanced Learning</td></tr>
        <tr><td>• Scalable AI</td></tr>
        </table>
        </div>
        """, unsafe_allow_html=True)
   
    st.markdown("---")

    st.header("🎓 Education")
    
    st.markdown("""
    <div style='border-left: 3px solid #4FC3F7; padding-left: 2rem; margin-left: 1rem;'>
        <div style='position: relative; margin-bottom: 2rem;'>
            <div style='position: absolute; left: -2.5rem; top: 0; background: #4FC3F7; 
                       width: 20px; height: 20px; border-radius: 50%;'></div>
            <h3 style='color: #4FC3F7; margin-bottom: 0.5rem;'>B.Tech in Computer Science Engineering</h3>
            <h4 style='color: #BB86FC; margin-bottom: 0.5rem;'>Bennett University, Uttar Pradesh</h4>
            <p style='color: #888; font-style: italic;'>2021 – 2025</p>
            <p style='color: #e0e0e0; font-weight: bold;'>CGPA: 8.18/10.0</p>
        </div>
        
    <div style='position: relative; margin-bottom: 2rem;'>
        <div style='position: absolute; left: -2.5rem; top: 0; background: #BB86FC; 
                   width: 20px; height: 20px; border-radius: 50%;'></div>
        <h3 style='color: #BB86FC; margin-bottom: 0.5rem;'>CBSE Class XII</h3>
        <h4 style='color: #f0f0f0; margin-bottom: 0.5rem;'>Bharti Public School, Delhi</h4>
        <p style='color: #888; font-style: italic;'>2020 – 2021</p>
        <p style='color: #e0e0e0; font-weight: bold;'>Percentage: 79%</p>
    </div>
        
    <div style='position: relative; margin-bottom: 1rem;'>
        <div style='position: absolute; left: -2.5rem; top: 0; background: #03DAC6; 
                       width: 20px; height: 20px; border-radius: 50%;'></div>
            <h3 style='color: #03DAC6; margin-bottom: 0.5rem;'>CBSE Class X</h3>
            <h4 style='color: #f0f0f0; margin-bottom: 0.5rem;'>Bharti Public School, Delhi</h4>
            <p style='color: #888; font-style: italic;'>2018 – 2019</p>
            <p style='color: #e0e0e0; font-weight: bold;'>Percentage: 93.8%</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

    st.header("🏆 Certifications")
    
    row1_col1, row1_col2 = st.columns(2)
    row2_col1, row2_col2 = st.columns(2)
    
    with row1_col1:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%); 
                   padding: 1.5rem; border-radius: 15px; color: white; margin-bottom: 1rem; height: 180px;'>
            <div style='display: flex; align-items: center; margin-bottom: 1rem;'>
                <div style='background: rgba(255,255,255,0.2); padding: 0.5rem; border-radius: 10px; margin-right: 0.9rem;'>
                    <span style='font-size: 1.5rem;'>🤖</span>
                </div>
                <h3 style='color: white; margin: 0;'>Deep Learning with Tensorflow</h3>
            </div>
            <p style='margin-bottom: 1.5rem; font-size: 0.9rem;'>Advanced neural networks and deep learning concepts</p>
            <a href='https://www.credly.com/badges/fe06c226-603e-4f36-b474-450f928bbe86/print' 
               target='_blank' 
               style='background: white; color: #FF6B6B; padding: 0.5rem 1rem; border-radius: 8px; 
                      text-decoration: none; font-weight: bold; float: right; font-size: 0.9rem;'>
                View Credential ›
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    with row1_col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #4ECDC4 0%, #44A08D 100%); 
                   padding: 1.5rem; border-radius: 15px; color: white; margin-bottom: 1rem; height: 180px;'>
            <div style='display: flex; align-items: center; margin-bottom: 1rem;'>
                <div style='background: rgba(255,255,255,0.2); padding: 0.5rem; border-radius: 10px; margin-right: 1rem;'>
                    <span style='font-size: 1.5rem;'>☁️</span>
                </div>
                <h3 style='color: white; margin: 0;'>AWS ML Foundations</h3>
            </div>
            <p style='margin-bottom: 1.5rem; font-size: 0.9rem;'>Cloud-based ML services and infrastructure</p>
            <a href='https://www.credly.com/badges/f8b455d4-0b7e-4f6c-9897-c939e1d2e5a2/print' 
               target='_blank' 
               style='background: white; color: #4ECDC4; padding: 0.5rem 1rem; border-radius: 8px; 
                      text-decoration: none; font-weight: bold; float: right; font-size: 0.9rem;'>
                View Credential ›
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    with row2_col1:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%); 
                   padding: 1.5rem; border-radius: 15px; color: white; margin-bottom: 1rem; height: 180px;'>
            <div style='display: flex; align-items: center; margin-bottom: 1rem;'>
                <div style='background: rgba(255,255,255,0.2); padding: 0.5rem; border-radius: 10px; margin-right: 0.8rem;'>
                    <span style='font-size: 1.5rem;'>💻</span>
                </div>
                <h3 style='color: white; margin: 0;'>Software Engineering</h3>
            </div>
            <p style='margin-bottom: 1.5rem; font-size: 0.9rem;'>Software Design and Project Management</p>
            <a href='https://coursera.org/verify/M64SBDG72VD6' 
               target='_blank' 
               style='background: white; color: #4CAF50; padding: 0.5rem 1rem; border-radius: 8px; 
                      text-decoration: none; font-weight: bold; float: right; font-size: 0.9rem;'>
                View Credential ›
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    with row2_col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #9C27B0 0%, #673AB7 100%); 
                   padding: 1.5rem; border-radius: 15px; color: white; margin-bottom: 1rem; height: 180px;'>
            <div style='display: flex; align-items: center; margin-bottom: 1rem;'>
                <div style='background: rgba(255,255,255,0.2); padding: 0.5rem; border-radius: 10px; margin-right: 1rem;'>
                    <span style='font-size: 1.5rem;'>🧠</span>
                </div>
                <h3 style='color: white; margin: 0;'>Machine Learning for NLP</h3>
            </div>
            <p style='margin-bottom: 1.5rem; font-size: 0.9rem;'>Intro to Natural Language Processing</p>
            <a href='https://www.credly.com/go/gLvJRtzf' 
               target='_blank' 
               style='background: white; color: #9C27B0; padding: 0.5rem 1rem; border-radius: 8px; 
                      text-decoration: none; font-weight: bold; float: right; font-size: 0.9rem;'>
                View Credential ›
            </a>
        </div>
        """, unsafe_allow_html=True)


def contact():
    st.title("📬 Contact Me")
    st.write("""
    📱 [+91-8076485189]  
             
    📧 [Mail](mailto:adityaksingh1301@gmail.com) 
              
    🌐 [LinkedIn](https://www.linkedin.com/in/aditya-kumar-singh-3a0a83246/)  
             
    💻 [GitHub](https://github.com/AdityaK1301)  
             
    🧠 [LeetCode](https://leetcode.com/u/Adityaa_1301/)  
    
    """)

    resume_path = Path("Aditya_Resume.pdf")
    if resume_path.exists():
        with open(resume_path, "rb") as pdf_file:
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.download_button(
                    "**🎯 Download My Resume (PDF)**",
                    data=pdf_file,
                    file_name="Aditya_Kumar_Singh_Resume.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                    type="primary"
                )
    else:
        st.error("Resume file not found. Please check the file path.")
    st.markdown("---")
    st.info("💬 I'm always open to collaboration, internships, or AI/ML research discussions.")
    st.markdown("<br><center>© 2025 Aditya Kumar Singh | Built with ❤️ using Streamlit</center>", unsafe_allow_html=True)

st.markdown("# Aditya Kumar Singh")
st.markdown("---")


home_page = st.Page(home, title="About Me", icon=":material/home:", default=True)
projects_page = st.Page(projects, title="Projects", icon=":material/rocket_launch:")
experience_page = st.Page(experience, title="Experience and Education", icon=":material/work:")
contact_page = st.Page(contact, title="Contact", icon=":material/contact_mail:")

pg = st.navigation([home_page, projects_page, experience_page, contact_page])

pg.run()

