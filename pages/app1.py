import streamlit as st

def app():
    st.title("Deduct AI: Bridging Legal Services Gap")

    st.subheader("Objective:")
    st.markdown("Develop an A.I/M.L based app to assist Law Enforcement Agencies (LEA’s) in investigation, evidence collection, and drafting of charge sheets.", True)
    
    st.subheader("Why This Project Matters:")
    st.markdown("1. Complex Crime Scene: Investigations involve diverse evidence and scenarios, posing challenges.", True)
    st.markdown("2. Decision-Making Challenges: Investigators struggle to determine appropriate procedures based on evidence.", True)
    st.markdown("3. Legal Complexity: Navigating legal frameworks demands expertise and exhaustive knowledge.", True)
    st.markdown("4. Ethical Compliance and User Trust: Collaboration with legal experts crucial for ensuring ethical and legal standards.", True)
    st.markdown("<hr/>", True)

    st.subheader("Features of Our Solution:")
    st.markdown("1. Innovative Approach to Investigation: Utilizing advanced technology for a transformative impact on criminal investigations.", True)
    st.markdown("2. Automated Evidence Analysis: Streamlining the identification of sensitive items in crime scenes for investigators.", True)
    st.markdown("3. Guided Decision-Making: Providing clear procedural recommendations to simplify decision-making processes.", True)
    st.markdown("4. User-Friendly and Ethical: Developing a user-friendly tool that ensures transparency and trust in the pursuit of justice.", True)
    st.markdown("<hr/>", True)

    st.subheader("Solution Description:")
    st.markdown("1. Suggest the kind of evidence to be collected:", True)
    st.markdown("   - Advanced Object Detection: Implementing YOLO for precise identification of evidence in crime scene images.", True)
    st.markdown("   - Transfer Learning for Precision: Fine-tuning models through transfer learning for accurate recognition of specialized crime scene evidence.", True)
    st.markdown("   - Contextual Analysis Algorithms: Using advanced algorithms to process data contextually, offering specific suggestions for evidence collection based on identified objects.", True)
    st.markdown("2. Procedure to be followed - Seizure, Arrest, Chemical, Examination etc.:", True)
    st.markdown("   - Rule-Based Procedure Recommendations: Decision trees guide actions like seizure, arrest, and chemical examinations based on evidence.", True)
    st.markdown("   - Algorithmic Decision-Making: Algorithms dynamically determine and optimize the sequence of investigative procedures.", True)
    st.markdown("3. To suggest Sections of law that would be applicable in an FIR:", True)
    st.markdown("   - Legal Text Analysis with NLP: Employing Natural Language Processing (NLP) techniques for nuanced analysis of legal texts and identifying applicable law sections in an FIR.", True)
    st.markdown("   - Named Entity Recognition (NER): Utilizing NER to pinpoint legal entities, such as section numbers and legal terms, enhancing precision in suggesting relevant sections of law.", True)
    st.markdown("<hr/>", True)

    st.subheader("5G Use Case:")
    st.markdown("1. High-Speed Data Transfer for Model Updates: Leverage 5G for fast, secure A.I/M.L model updates, ensuring investigators access the latest tools.", True)
    st.markdown("2. On-Site Edge Computing for ML Processing: Employ 5G edge computing for on-site A.I/M.L, reducing evidence analysis latency in investigations.", True)
    st.markdown("3. Dynamic Decision Support with Low Latency: For low-latency decision support, offering investigators real-time procedural recommendations.", True)
    st.markdown("4. Biometric Data Analysis in Real Time: For real-time biometric analysis, improving speed & accuracy of identifying individuals in criminal activities.", True)
    st.markdown("5. 5G-Enabled Smart Surveillance Integration: Integrate 5G for enhanced real-time analysis in smart surveillance, facilitating quicker identification of relevant evidence.", True)
    st.markdown("<hr/>", True)

    st.subheader("Thank You for Your Time.")

# Run the Streamlit app
if __name__ == '__main__':
    app()
