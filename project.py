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

/* =========================================================
   DARK BLUE ANIMATED BACKGROUND
   ========================================================= */

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


/* =========================================================
   FLOATING PARTICLES
   ========================================================= */

.particle {
    position: fixed;
    width: 5px;
    height: 5px;
    background: rgba(120, 200, 255, 0.8);
    border-radius: 50%;
    pointer-events: none;
    z-index: 0;

    box-shadow:
        0 0 6px rgba(100, 190, 255, 0.8),
        0 0 15px rgba(70, 160, 255, 0.6);

    animation: floatParticle linear infinite;
}

@keyframes floatParticle {
    0% {
        transform: translateY(110vh) scale(0.3);
        opacity: 0;
    }

    10% {
        opacity: 1;
    }

    50% {
        transform: translateY(50vh) scale(1);
        opacity: 0.9;
    }

    90% {
        opacity: 0.7;
    }

    100% {
        transform: translateY(-10vh) scale(0.2);
        opacity: 0;
    }
}

.p1 {
    left: 5%;
    animation-duration: 8s;
}

.p2 {
    left: 15%;
    animation-duration: 11s;
    animation-delay: 2s;
}

.p3 {
    left: 25%;
    animation-duration: 9s;
    animation-delay: 4s;
}

.p4 {
    left: 35%;
    animation-duration: 13s;
    animation-delay: 1s;
}

.p5 {
    left: 45%;
    animation-duration: 10s;
    animation-delay: 3s;
}

.p6 {
    left: 55%;
    animation-duration: 12s;
    animation-delay: 5s;
}

.p7 {
    left: 65%;
    animation-duration: 9s;
    animation-delay: 2s;
}

.p8 {
    left: 75%;
    animation-duration: 14s;
    animation-delay: 4s;
}

.p9 {
    left: 85%;
    animation-duration: 10s;
    animation-delay: 1s;
}

.p10 {
    left: 95%;
    animation-duration: 12s;
    animation-delay: 6s;
}

.p11 {
    left: 10%;
    width: 3px;
    height: 3px;
    animation-duration: 15s;
    animation-delay: 6s;
}

.p12 {
    left: 30%;
    width: 4px;
    height: 4px;
    animation-duration: 17s;
    animation-delay: 8s;
}

.p13 {
    left: 50%;
    width: 3px;
    height: 3px;
    animation-duration: 14s;
    animation-delay: 7s;
}

.p14 {
    left: 70%;
    width: 4px;
    height: 4px;
    animation-duration: 16s;
    animation-delay: 5s;
}

.p15 {
    left: 90%;
    width: 3px;
    height: 3px;
    animation-duration: 13s;
    animation-delay: 9s;
}


/* =========================================================
   BUTTON ANIMATION
   ========================================================= */

.stButton > button {
    position: relative;
    overflow: hidden;

    transition:
        transform 0.15s ease,
        box-shadow 0.2s ease;

    box-shadow:
        0 0 0 rgba(80, 170, 255, 0);
}


/* =========================================================
   HOVER GLOW
   ========================================================= */

.stButton > button:hover {
    transform:
        translateY(-3px)
        scale(1.03);

    box-shadow:
        0 0 10px rgba(80, 170, 255, 0.5),
        0 0 25px rgba(80, 170, 255, 0.35),
        0 0 45px rgba(80, 170, 255, 0.2);
}


/* =========================================================
   MOVING SHINE
   ========================================================= */

.stButton > button::after {
    content: "";

    position: absolute;

    top: -100%;
    left: -120%;

    width: 60%;
    height: 300%;

    background: linear-gradient(
        90deg,
        transparent,
        rgba(255, 255, 255, 0.7),
        transparent
    );

    transform: rotate(25deg);

    pointer-events: none;
}

.stButton > button:hover::after {
    animation: buttonShine 0.8s ease;
}

@keyframes buttonShine {
    0% {
        left: -120%;
    }

    100% {
        left: 150%;
    }
}


/* =========================================================
   CLICK GLOW
   ========================================================= */

.stButton > button:active {
    transform: scale(0.94);

    box-shadow:
        0 0 15px rgba(120, 210, 255, 0.9),
        0 0 35px rgba(80, 170, 255, 0.7),
        0 0 60px rgba(80, 170, 255, 0.5);

    transition: 0.05s;
}


/* =========================================================
   CLICK PULSE
   ========================================================= */

.stButton > button:active::before {
    content: "";

    position: absolute;

    top: 50%;
    left: 50%;

    width: 10px;
    height: 10px;

    border-radius: 50%;

    background: rgba(255, 255, 255, 0.95);

    transform: translate(-50%, -50%);

    animation: clickPulse 0.5s ease-out;

    pointer-events: none;
}

@keyframes clickPulse {
    0% {
        width: 10px;
        height: 10px;
        opacity: 1;

        box-shadow:
            0 0 10px white;
    }

    50% {
        opacity: 0.7;
    }

    100% {
        width: 180px;
        height: 180px;
        opacity: 0;

        box-shadow:
            0 0 40px rgba(100, 200, 255, 0.8);
    }
}


/* =========================================================
   TITLES
   ========================================================= */

h1,
h2,
h3 {
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


/* =========================================================
   METRIC ANIMATION
   ========================================================= */

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

hr {
    opacity: 0.3;
}

</style>


<!-- FLOATING PARTICLES -->

<div class="particle p1"></div>
<div class="particle p2"></div>
<div class="particle p3"></div>
<div class="particle p4"></div>
<div class="particle p5"></div>
<div class="particle p6"></div>
<div class="particle p7"></div>
<div class="particle p8"></div>
<div class="particle p9"></div>
<div class="particle p10"></div>
<div class="particle p11"></div>
<div class="particle p12"></div>
<div class="particle p13"></div>
<div class="particle p14"></div>
<div class="particle p15"></div>

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

        st.success(
            "🎉 Profile created successfully!"
        )

        st.header(
            f"👋 Hello! My name is {name}."
        )

        st.write(
            f"🎂 I am **{age} years old**."
        )

        st.write(
            f"🏫 I go to **{school}**."
        )

        st.write(
            f"📚 My favorite subject is **{subject}**."
        )

        st.write(
            f"🎵 I enjoy **{hobby}**."
        )

        st.divider()

        st.subheader(
            "💙 About Me"
        )

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


st.markdown(
    "### 💙 Ready to calculate? ✨"
)

st.text_input(
    "Display",
    value=st.session_state.calc_display,
    disabled=True
)


# Calculator row 1
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


# Calculator row 2
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


# Calculator row 3
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


# Calculator row 4
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
                subject["marks"] /
                subject["maximum"]
            ) * 100

            subject_gpas.append(
                get_gpa(subject_percentage)
            )

        gpa = (
            sum(subject_gpas) /
            len(subject_gpas)
        )

        st.header(
            "🎉 Your Results"
        )

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

        st.header(
            "📊 Overall Performance"
        )

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

        st.header(
            "📚 Subject Results"
        )

        for subject in subjects:

            subject_percentage = (
                subject["marks"] /
                subject["maximum"]
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

if "quiz_title" not in st.session_state:
    st.session_state.quiz_title = ""


# =========================================================
# QUIZ SETUP
# =========================================================

if st.session_state.quiz_page == "setup":

    # =====================================================
    # QUIZ TITLE
    # =====================================================

    quiz_title = st.text_input(
        "🏷️ Quiz Title",
        placeholder="Example: Biology Chapter 1 Quiz",
        key="quiz_title_input"
    )

    st.caption(
        "💡 Give your quiz a title so it appears when you start the quiz!"
    )

    # =====================================================
    # NUMBER OF QUESTIONS
    # =====================================================

    number = st.number_input(
        "🔢 How many questions?",
        min_value=1,
        max_value=20,
        value=5,
        step=1,
        key="quiz_number"
    )

    questions = []

    # =====================================================
    # QUESTIONS
    # =====================================================

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

    # =====================================================
    # START QUIZ
    # =====================================================

    if st.button(
        "🚀 START QUIZ",
        use_container_width=True,
        key="start_quiz"
    ):

        valid = True

        # Check title
        if not quiz_title.strip():

            st.error(
                "⚠️ Please enter a title for your quiz."
            )

            valid = False

        # Check questions
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

            # Save title
            st.session_state.quiz_title = (
                quiz_title.strip()
            )

            # Save questions
            st.session_state.questions = questions

            # Reset quiz
            st.session_state.current = 0
            st.session_state.score = 0
            st.session_state.submitted = False

            # Go to quiz
            st.session_state.quiz_page = "quiz"

            st.rerun()

        elif quiz_title.strip():

            st.error(
                "⚠️ Please fill in every question and every option."
            )


# =========================================================
# QUIZ PAGE
# =========================================================

elif st.session_state.quiz_page == "quiz":

    questions = st.session_state.questions

    current = st.session_state.current

    total = len(questions)


    # =====================================================
    # RESULTS
    # =====================================================

    if current >= total:

        st.header(
            f"📚 {st.session_state.quiz_title}"
        )

        st.subheader(
            "🎉 Quiz Complete!"
        )

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

        st.progress(
            percentage / 100
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
            use_container_width=True,
            key="new_quiz"
        ):

            st.session_state.quiz_page = "setup"

            st.session_state.questions = []

            st.session_state.current = 0

            st.session_state.score = 0

            st.session_state.submitted = False

            st.session_state.quiz_title = ""

            st.rerun()


    # =====================================================
    # CURRENT QUESTION
    # =====================================================

    else:

        q = questions[current]

        # =================================================
        # QUIZ TITLE
        # =================================================

        st.header(
            f"📚 {st.session_state.quiz_title}"
        )

        st.write(
            f"**❓ Question {current + 1} of {total}**"
        )

        st.progress(
            (current + 1) / total
        )

        st.divider()

        # =================================================
        # QUESTION
        # =================================================

        st.subheader(
            q["question"]
        )

        letters = [
            "A",
            "B",
            "C",
            "D"
        ]

        def answer_text(letter):

            return (
                f"{letter}     {q[letter]}"
            )

        selected = st.radio(
            "💭 Choose your answer:",
            letters,
            format_func=answer_text,
            key=f"answer_{current}",
            disabled=st.session_state.submitted
        )


        # =================================================
        # SUBMIT
        # =================================================

        if not st.session_state.submitted:

            if st.button(
                "✅ SUBMIT ANSWER",
                use_container_width=True,
                key=f"submit_{current}"
            ):

                if selected == q["correct"]:

                    st.session_state.score += 1

                st.session_state.submitted = True

                st.rerun()


        # =================================================
        # ANSWER FEEDBACK
        # =================================================

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


            # =============================================
            # NEXT QUESTION
            # =============================================

            if current + 1 < total:

                if st.button(
                    "➡️ NEXT QUESTION",
                    use_container_width=True,
                    key=f"next_{current}"
                ):

                    st.session_state.current += 1

                    st.session_state.submitted = False

                    st.rerun()


            # =============================================
            # SEE RESULTS
            # =============================================

            else:

                if st.button(
                    "🏆 SEE RESULTS",
                    use_container_width=True,
                    key="see_results"
                ):

                    st.session_state.current += 1

                    st.rerun()
