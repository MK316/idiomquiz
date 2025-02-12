import streamlit as st

# Sentences with idiomatic phrases, where the preposition is replaced with a dynamically created blank
# Korean translations are provided for better understanding
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

# Initialize session state to keep track of the current question index
if 'index' not in st.session_state:
    st.session_state.index = 0

# Function to check the answer and replace the blank
def check_answer():
    idx = st.session_state.index
    # Replace blanks with the correct answer
    phrase_with_answer = questions[idx][0].replace(' '.join(['______' for _ in questions[idx][1].split()]), questions[idx][1])
    st.session_state.display_text = phrase_with_answer

# Function to go to the next question
def next_question():
    if st.session_state.index < len(questions) - 1:
        st.session_state.index += 1
        st.session_state.display_text = questions[st.session_state.index][0]
    else:
        st.session_state.display_text = "Completed"

# Display the question
if 'display_text' not in st.session_state:
    st.session_state.display_text = questions[st.session_state.index][0]

st.markdown(f"<h2 style='font-size:24px;'>{st.session_state.display_text}</h2>", unsafe_allow_html=True)
st.caption(questions[st.session_state.index][2])

# Button to check the answer
if 'Completed' not in st.session_state.display_text:
    st.button("Check answer", on_click=check_answer)

# Button to move to the next question
st.button("Next question", on_click=next_question)

# Optionally display 'Completed' when all questions are answered
if st.session_state.display_text == "Completed":
    st.markdown("<h2 style='font-size:24px;'>Completed</h2>", unsafe_allow_html=True)
