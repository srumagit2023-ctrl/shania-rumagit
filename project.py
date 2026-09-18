import streamlit as st

# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="My App 💙",
    page_icon="💙",
    layout="centered"
)


# =========================================================
# DARK BLUE THEME + ANIMATIONS
# =========================================================

st.markdown("""
<style>

/* DARK BLUE ANIMATED BACKGROUND */
.stApp {
    background: linear-gradient(
        135deg,
        #06152f 0%,
        #0a2450 50%,
        #06152f 100%
    );
    background-size: 300% 300%;
    animation: blueBackground 12s ease infinite;
}

@keyframes blueBackground {
    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}


/* TITLES */
h1, h2, h3 {
    animation: fadeDown 0.8s ease-out;
}

@keyframes fadeDown {
    from {
        opacity: 0;
        transform: translateY(-15px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}


/* BUTTON ANIMATION */
.stButton > button {
    transition:
        transform 0.15s ease,
        box-shadow 0.15s ease;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 6px 18px rgba(80, 170, 255, 0.35);
}

.stButton > button:active {
    transform: scale(0.95);
}


/* METRIC ANIMATION */
[data-testid="stMetric"] {
    animation: popIn 0.5s ease-out;
}

@keyframes popIn {
    from {
        opacity: 0;
        transform: scale(0.94);
    }

    to {
        opacity: 1;
        transform: scale(1);
    }
}


/* DIVIDER */
hr {
    opacity: 0.3;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# MY PROFILE 👤
# =========================================================

st.title("👤 My Profile")

st.write(
    "✨ Fill in the information below to create your personalized profile."
)

name = st.text_input(
    "😊 What is your name?",
    key="profile_name"
)

age = st.number_input(
    "🎂 How old are you?",
    min_value=1,
    max_value=100,
    step=1,
    key="profile_age"
)

school = st.text_input(
    "🏫 What school do you go to?",
    key="profile_school"
)

subject = st.text_input(
    "📚 What is your favorite subject?",
    key="profile_subject"
)

hobby = st.text_input(
    "🎵 What is your favorite hobby?",
    key="profile_hobby"
)

if st.button(
    "✨ Create My Profile",
    key="create_profile",
    use_container_width=True
):

    if name and school and subject and hobby:

        st.success("🎉 Profile created successfully!")

        st.header(f"👋 Hello! My name is {name}.")

        st.write(f"🎂 I am **{age} years old**.")
        st.write(f"🏫 I go to **{school}**.")
        st.write(f"📚 My favorite subject is **{subject}**.")
        st.write(f"🎵 I enjoy **{hobby}**.")

        st.divider()

        st.subheader("💙 About Me")

        st.info(
            f"{name} is {age} years old and goes to {school}. "
            f"They enjoy {hobby} and their favorite subject is {subject}!"
        )

    else:

        st.warning(
            "⚠️ Please fill in all the fields before creating your profile."
        )


# =========================================================
# CALCULATOR 🧮
# =========================================================

st.divider()

st.title("🧮 Calculator")

st.caption(
    "✨ Tap the buttons and watch your calculation come to life!"
)

if "calc_display" not in st.session_state:
    st.session_state.calc_display = "0"


# =========================================================
# CALCULATOR FUNCTIONS
# =========================================================

def add_number(number):

    display = st.session_state.calc_display

    if display == "0" or display == "Error":

        st.session_state.calc_display = number

    else:

        st.session_state.calc_display += number


def add_operator(operator):

    display = st.session_state.calc_display

    if display == "Error":
        return

    if display == "0" and operator != "-":
        return

    if display[-1:] in "+-*/":

        st.session_state.calc_display = (
            display[:-1] + operator
        )

    else:

        st.session_state.calc_display += operator


def add_decimal():

    display = st.session_state.calc_display

    if display == "Error":

        st.session_state.calc_display = "0."
        return

    last_number = display

    for operator in "+-*/":

        if operator in last_number:

            last_number = last_number.split(operator)[-1]

    if "." not in last_number:

        st.session_state.calc_display += "."


def calculate():

    display = st.session_state.calc_display

    if display == "Error":
        return

    if display[-1:] in "+-*/":
        return

    try:

        answer = eval(
            display,
            {"__builtins__": None},
            {}
        )

        if isinstance(answer, float):

            if answer.is_integer():

                answer = int(answer)

            else:

                answer = round(answer, 10)

        st.session_state.calc_display = str(answer)

    except:

        st.session_state.calc_display = "Error"


def clear():

    st.session_state.calc_display = "0"


# =========================================================
# CALCULATOR DISPLAY
# =========================================================

st.markdown(
    "### 💙 Ready to calculate? ✨"
)

st.text_input(
    "Display",
    value=st.session_state.calc_display,
    disabled=True
)


# =========================================================
# CALCULATOR ROW 1
# =========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.button(
        "7️⃣",
        use_container_width=True,
        on_click=add_number,
        args=("7",),
        key="calculator_7"
    )

with c2:

    st.button(
        "8️⃣",
        use_container_width=True,
        on_click=add_number,
        args=("8",),
        key="calculator_8"
    )

with c3:

    st.button(
        "9️⃣",
        use_container_width=True,
        on_click=add_number,
        args=("9",),
        key="calculator_9"
    )

with c4:

    st.button(
        "➗",
        use_container_width=True,
        on_click=add_operator,
        args=("/",),
        key="calculator_divide"
    )


# =========================================================
# CALCULATOR ROW 2
# =========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.button(
        "4️⃣",
        use_container_width=True,
        on_click=add_number,
        args=("4",),
        key="calculator_4"
    )

with c2:

    st.button(
        "5️⃣",
        use_container_width=True,
        on_click=add_number,
        args=("5",),
        key="calculator_5"
    )

with c3:

    st.button(
        "6️⃣",
        use_container_width=True,
        on_click=add_number,
        args=("6",),
        key="calculator_6"
    )

with c4:

    st.button(
        "✖️",
        use_container_width=True,
        on_click=add_operator,
        args=("*",),
        key="calculator_multiply"
    )


# =========================================================
# CALCULATOR ROW 3
# =========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.button(
        "1️⃣",
        use_container_width=True,
        on_click=add_number,
        args=("1",),
        key="calculator_1"
    )

with c2:

    st.button(
        "2️⃣",
        use_container_width=True,
        on_click=add_number,
        args=("2",),
        key="calculator_2"
    )

with c3:

    st.button(
        "3️⃣",
        use_container_width=True,
        on_click=add_number,
        args=("3",),
        key="calculator_3"
    )

with c4:

    st.button(
        "➖",
        use_container_width=True,
        on_click=add_operator,
        args=("-",),
        key="calculator_minus"
    )


# =========================================================
# CALCULATOR ROW 4
# =========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.button(
        "0️⃣",
        use_container_width=True,
        on_click=add_number,
        args=("0",),
        key="calculator_0"
    )

with c2:

    st.button(
        "🔵 .",
        use_container_width=True,
        on_click=add_decimal,
        key="calculator_decimal"
    )

with c3:

    st.button(
        "➕",
        use_container_width=True,
        on_click=add_operator,
        args=("+",),
        key="calculator_plus"
    )

with c4:

    st.button(
        "🟰",
        use_container_width=True,
        on_click=calculate,
        key="calculator_equals"
    )


st.button(
    "🗑️ CLEAR",
    use_container_width=True,
    on_click=clear,
    key="calculator_clear"
)


# =========================================================
# GRADE CALCULATOR 📊
# =========================================================

st.divider()

st.title("📊 Grade Calculator")

st.write(
    "✨ Enter your subjects and marks to calculate your grades, "
    "percentage, and GPA."
)


# =========================================================
# GRADE FUNCTIONS
# =========================================================

def get_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 85:
        return "A"

    elif percentage >= 80:
        return "B+"

    elif percentage >= 75:
        return "B"

    elif percentage >= 70:
        return "C+"

    elif percentage >= 65:
        return "C"

    elif percentage >= 60:
        return "D"

    else:
        return "F"


def get_gpa(percentage):

    if percentage >= 90:
        return 4.0

    elif percentage >= 85:
        return 3.7

    elif percentage >= 80:
        return 3.3

    elif percentage >= 75:
        return 3.0

    elif percentage >= 70:
        return 2.7

    elif percentage >= 65:
        return 2.3

    elif percentage >= 60:
        return 2.0

    else:
        return 0.0


number_of_subjects = st.number_input(
    "📚 How many subjects do you have?",
    min_value=1,
    max_value=15,
    value=3,
    step=1,
    key="number_of_subjects"
)


# =========================================================
# GRADE FORM
# =========================================================

with st.form("grade_calculator_form"):

    subjects = []

    for i in range(int(number_of_subjects)):

        st.subheader(
            f"📖 Subject {i + 1}"
        )

        col1, col2, col3 = st.columns(
            [2, 1, 1]
        )

        with col1:

            subject_name = st.text_input(
                "Subject Name",
                placeholder="e.g. Mathematics",
                key=f"grade_name_{i}"
            )

        with col2:

            marks = st.number_input(
                "Your Marks",
                min_value=0.0,
                value=0.0,
                step=1.0,
                key=f"grade_marks_{i}"
            )

        with col3:

            maximum = st.number_input(
                "Maximum",
                min_value=1.0,
                value=100.0,
                step=1.0,
                key=f"grade_max_{i}"
            )

        subjects.append({
            "name": subject_name,
            "marks": marks,
            "maximum": maximum
        })

    calculate_grades = st.form_submit_button(
        "✨ Calculate My Grades",
        use_container_width=True
    )


# =========================================================
# GRADE RESULTS
# =========================================================

if calculate_grades:

    valid = True

    for subject in subjects:

        if not subject["name"].strip():

            st.error(
                "⚠️ Please enter a name for every subject."
            )

            valid = False
            break

        if subject["marks"] > subject["maximum"]:

            st.error(
                f"⚠️ {subject['name']}: Your marks cannot be "
                "higher than the maximum marks."
            )

            valid = False
            break


    if valid:

        total_marks = sum(
            subject["marks"]
            for subject in subjects
        )

        total_possible = sum(
            subject["maximum"]
            for subject in subjects
        )

        percentage = (
            total_marks / total_possible
        ) * 100

        overall_grade = get_grade(
            percentage
        )


        subject_gpas = []

        for subject in subjects:

            subject_percentage = (
                subject["marks"]
                / subject["maximum"]
            ) * 100

            subject_gpas.append(
                get_gpa(subject_percentage)
            )


        gpa = (
            sum(subject_gpas)
            / len(subject_gpas)
        )


        st.header("🎉 Your Results")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "📝 Total Marks",
                f"{total_marks:g}/{total_possible:g}"
            )

        with col2:

            st.metric(
                "📈 Percentage",
                f"{percentage:.1f}%"
            )


        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "🎓 GPA",
                f"{gpa:.2f}/4.0"
            )

        with col2:

            st.metric(
                "🏆 Overall Grade",
                overall_grade
            )


        st.header("📊 Overall Performance")

        st.progress(
            min(percentage / 100, 1.0)
        )


        if percentage >= 90:

            st.success(
                "🌟 Excellent! Outstanding performance!"
            )

        elif percentage >= 80:

            st.success(
                "🎉 Great job! Keep it up!"
            )

        elif percentage >= 70:

            st.info(
                "👍 Good work! Keep improving!"
            )

        elif percentage >= 60:

            st.warning(
                "📚 Keep studying and practicing!"
            )

        else:

            st.error(
                "💪 Keep working hard. You can improve!"
            )


        st.header("📚 Subject Results")

        for subject in subjects:

            subject_percentage = (
                subject["marks"]
                / subject["maximum"]
            ) * 100

            subject_grade = get_grade(
                subject_percentage
            )

            st.subheader(
                f"📖 {subject['name']}"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.write("**📝 Marks**")

                st.write(
                    f"{subject['marks']:g}/"
                    f"{subject['maximum']:g}"
                )

            with col2:

                st.write("**📈 Percentage**")

                st.write(
                    f"{subject_percentage:.1f}%"
                )

            with col3:

                st.write("**🏆 Grade**")

                st.write(
                    subject_grade
                )

            st.divider()


# =========================================================
# QUIZ MASTER 📝
# =========================================================

st.divider()

st.title("📝 Quiz Master")

st.write(
    "✨ Create your own multiple-choice quiz!"
)


# =========================================================
# QUIZ SESSION STATE
# =========================================================

if "quiz_page" not in st.session_state:
    st.session_state.quiz_page = "setup"

if "questions" not in st.session_state:
    st.session_state.questions = []

if "current" not in st.session_state:
    st.session_state.current = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "submitted" not in st.session_state:
    st.session_state.submitted = False


# =========================================================
# QUIZ SETUP
# =========================================================

if st.session_state.quiz_page == "setup":

    number = st.number_input(
        "🔢 How many questions?",
        min_value=1,
        max_value=20,
        value=5,
        step=1,
        key="quiz_number"
    )

    questions = []

    for i in range(int(number)):

        st.subheader(
            f"❓ Question {i + 1}"
        )

        question = st.text_input(
            "Question",
            key=f"question_{i}",
            placeholder="Example: What is the capital of France?"
        )

        col1, col2 = st.columns(2)

        with col1:

            option_a = st.text_input(
                "🅰️ Option A",
                key=f"option_a_{i}",
                placeholder="Paris"
            )

            option_c = st.text_input(
                "©️ Option C",
                key=f"option_c_{i}",
                placeholder="Rome"
            )

        with col2:

            option_b = st.text_input(
                "🅱️ Option B",
                key=f"option_b_{i}",
                placeholder="London"
            )

            option_d = st.text_input(
                "🆓 Option D",
                key=f"option_d_{i}",
                placeholder="Madrid"
            )

        correct = st.selectbox(
            "✅ Correct answer",
            ["A", "B", "C", "D"],
            key=f"correct_{i}"
        )

        questions.append({
            "question": question,
            "A": option_a,
            "B": option_b,
            "C": option_c,
            "D": option_d,
            "correct": correct
        })


    if st.button(
        "🚀 START QUIZ",
        use_container_width=True
    ):

        valid = True

        for q in questions:

            if (
                q["question"].strip() == ""
                or q["A"].strip() == ""
                or q["B"].strip() == ""
                or q["C"].strip() == ""
                or q["D"].strip() == ""
            ):

                valid = False
                break


        if valid:

            st.session_state.questions = questions
            st.session_state.current = 0
            st.session_state.score = 0
            st.session_state.submitted = False
            st.session_state.quiz_page = "quiz"

            st.rerun()

        else:

            st.error(
                "⚠️ Please fill in every question and every option."
            )


# =========================================================
# QUIZ
# =========================================================

elif st.session_state.quiz_page == "quiz":

    questions = st.session_state.questions

    current = st.session_state.current

    total = len(questions)


    # =====================================================
    # QUIZ RESULTS
    # =====================================================

    if current >= total:

        st.subheader("🎉 Quiz Complete!")

        score = st.session_state.score

        percentage = (
            score / total
        ) * 100


        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "🏆 Score",
                f"{score} / {total}"
            )

        with col2:

            st.metric(
                "📈 Percentage",
                f"{percentage:.1f}%"
            )


        if percentage >= 90:

            st.success(
                "🌟 Excellent! You're a Quiz Master!"
            )

        elif percentage >= 75:

            st.success(
                "🎉 Great job! Keep it up!"
            )

        elif percentage >= 50:

            st.info(
                "👍 Good effort! You can do even better!"
            )

        else:

            st.warning(
                "📚 Keep practicing! You'll improve!"
            )


        if st.button(
            "🔄 CREATE NEW QUIZ",
            use_container_width=True
        ):

            st.session_state.quiz_page = "setup"
            st.session_state.questions = []
            st.session_state.current = 0
            st.session_state.score = 0
            st.session_state.submitted = False

            st.rerun()


    # =====================================================
    # CURRENT QUESTION
    # =====================================================

    else:

        q = questions[current]

        st.write(
            f"**❓ Question {current + 1} of {total}**"
        )

        st.progress(
            (current + 1) / total
        )

        st.header(
            q["question"]
        )


        letters = [
            "A",
            "B",
            "C",
            "D"
        ]


        def answer_text(letter):

            return f"{letter}     {q[letter]}"


        selected = st.radio(
            "💭 Choose your answer:",
            letters,
            format_func=answer_text,
            key=f"answer_{current}",
            disabled=st.session_state.submitted
        )


        if not st.session_state.submitted:

            if st.button(
                "✅ SUBMIT ANSWER",
                use_container_width=True
            ):

                if selected == q["correct"]:

                    st.session_state.score += 1

                st.session_state.submitted = True

                st.rerun()


        else:

            if selected == q["correct"]:

                st.success(
                    "🎉 Correct! Great job!"
                )

            else:

                st.error(
                    f"❌ Wrong! The correct answer is "
                    f"**{q['correct']}**."
                )


            if current + 1 < total:

                if st.button(
                    "➡️ NEXT QUESTION",
                    use_container_width=True
                ):

                    st.session_state.current += 1
                    st.session_state.submitted = False

                    st.rerun()

            else:

                if st.button(
                    "🏆 SEE RESULTS",
                    use_container_width=True
                ):

                    st.session_state.current += 1

                    st.rerun()
