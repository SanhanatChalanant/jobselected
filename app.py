import streamlit as st

def main():
    st.title("Job Selector Test")
    st.write("Answer the following questions to find your ideal job.")
    image_url = "https://drive.google.com/uc?id=13KxTN7o8-wKQg9RcP7uw7YEfJJvIN6_u"
    st.image(image_url, use_column_width=True)

    # Questions
    questions = [
        "คุณสนุกกับการแก้ปัญหามากแค่ไหน?",
        "คุณสบายใจแค่ไหนกับการขายและการสร้างความสัมพันธ์กับลูกค้า?",
        "คุณสนใจที่จะทำความเข้าใจในวงกว้างเกี่ยวกับธุรกิจประเภทต่างๆ มากน้อยเพียงใด?",
        "ทักษะการสร้างเครือข่ายและการสร้างความสัมพันธ์ของคุณแข็งแกร่งแค่ไหน?",
         "คุณมีความคิดสร้างสรรค์แค่ไหน และคุณสนุกกับการทำความเข้าใจพฤติกรรมผู้บริโภคมากแค่ไหน",
         "คุณเป็นคนมีระเบียบและมีความละเอียดรอบคอบแค่ไหน?",
         "คุณสะดวกใจแค่ไหนกับการพูดในที่สาธารณะและการนำเสนอ?",
         "คุณมั่นใจในทักษะความเป็นผู้นำของคุณแค่ไหน?",
         "คุณสะดวกแค่ไหนกับการวิเคราะห์ข้อมูลและวิธีการเชิงปริมาณ",
         "คุณปรับตัวได้แค่ไหนกับสภาพแวดล้อมที่เปลี่ยนแปลงและความท้าทายใหม่ๆ"
    ]

    # User responses
    
    user_responses = []

    # Display questions and collect user responses
    for i, question in enumerate(questions):
        user_response = st.slider(question, 1, 5)
        user_responses.append(user_response)

    # Submit button
    submit_button = st.button("Submit")

    # Job recommendation based on user responses
    if submit_button:
        job_recommendation = get_job_recommendation(user_responses)
        st.subheader("Job Recommendation:")
        st.write(job_recommendation)

def get_job_recommendation(responses):
    # Define the mapping of job recommendations and corresponding weightage for each question
    job_mapping = {
        "Consultant": [0.8, 0.5, 0.6, 0.7, 0.7, 0.4, 0.5, 0.4, 0.4, 0.5],
        "Sales Engineer": [0.6, 0.7, 0.4, 0.6, 0.6, 0.6, 0.7, 0.5, 0.4, 0.5],
        "Management Trainee": [0.5, 0.4, 0.6, 0.5, 0.4, 0.7, 0.4, 0.7, 0.5, 0.6],
        "Business Development": [0.6, 0.6, 0.5, 0.7, 0.4, 0.5, 0.6, 0.7, 0.4, 0.5],
        "Marketing": [0.4, 0.4, 0.5, 0.4, 0.8, 0.4, 0.5, 0.4, 0.6, 0.7]
    }

    # Calculate cumulative scores for each job based on user responses
    job_scores = {}
    for job, weights in job_mapping.items():
        job_scores[job] = sum(weight * response for weight, response in zip(weights, responses))

    # Find the job with the highest score
    recommended_job = max(job_scores, key=job_scores.get)

    # If the highest score is below a certain threshold, provide a generic recommendation
    if job_scores[recommended_job] < 2.0:
        return "Based on your responses, we recommend exploring various job roles to identify your ideal career path."

    return recommended_job

if __name__ == "__main__":
    main()
