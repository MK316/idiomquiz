import streamlit as st

# Sentences with idiomatic phrases, where the preposition is replaced with a dynamically created blank
# Adding a translation of the sentence for better understanding
questions = [
    ("He is completely {} the new project. (enthusiastic)", "on board with", "그는 새 프로젝트에 완전히 동참하고 있습니다."),
    ("She is not {} talking to large groups. (comfortable)", "at ease with", "그녀는 큰 그룹 앞에서 말하는 것이 편하지 않습니다."),
    ("They are {} visiting us next summer. (excited)", "looking forward to", "그들은 내년 여름 우리를 방문할 것을 기대하고 있습니다.")
]

# Prepare questions by replacing placeholders with appropriate number of blanks
for i in range(len(questions)):
    num_blanks = len(questions[i][1].split())
    blanks = ' '.join(['______' for _ in range(num_blanks)])
    questions[i] = (questions[i][0].format(blanks), questions[i][1], questions[i][2])

# Initialize session state to keep track of the current question index and answer visibility
if 'index' not in st.session_state:
    st.session_state.index = 0
    st.session_state.show_answer = False

# Function to check the answer and replace the blank
def check_answer():
    st.session_state.show_answer = True

# Function to go to the next question
def next_question():
    if st.session_state.index < len(questions) - 1:
        st.session_state.index += 1
        st.session_state.show_answer = False
    else:
        st.session_state.display_text = "Completed"

# Display the question in a larger font
if 'display_text' not in st.session_state or st.session_state.display_text != "Completed":
    st.markdown(f"<h2 style='font-size:24px;'>{questions[st.session_state.index][0]}</h2>", unsafe_allow_html=True)
    # Display translation as a caption
    st.markdown(f"<caption style='color:grey;'>{questions[st.session_state.index][2]}</caption>", unsafe_allow_html=True)

if st.session_state.show_answer:
    answer = questions[st.session_state.index][1]
    st.markdown(f"<h3 style='font-size:20px;'>Answer: {answer}</h3>", unsafe_allow_html=True)

# Button to check the answer
st.button("Check answer", on_click=check_answer)

# Button to move to the next question
st.button("Next question", on_click=next_question)

# Optionally display 'Completed' when all questions are answered
if st.session_state.get('display_text', '') == "Completed":
    st.markdown("<h2 style='font-size:24px;'>Completed</h2>", unsafe_allow_html=True)
