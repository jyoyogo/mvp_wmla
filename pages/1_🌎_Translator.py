import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import time
import streamlit as st
import streamlit.components.v1 as components

from components import authenticate as authenticate

# Title for the page and nice icon
st.set_page_config(page_title="NMT", page_icon="🤖")

# Header
st.title("Translator")

if authenticate.validate_credential():
    # Language selection
    source_lang_col, target_lang_col = st.columns(2)
    with source_lang_col:
        source_lang_options = ("ko", "en")
        st.write("Source Language")
        source_lang = st.selectbox("", source_lang_options)

    with target_lang_col:
        target_lang_options = ("en", "ko")
        st.write("Target Language")
        target_lang = st.selectbox("", target_lang_options)

    lang2key = {"ko":"ko_KR", "en":"en_XX"}

    # Form to add your items
    with st.form("my_form"):

        # Textarea to type the source text.
        user_input = st.text_area("Source Text", max_chars=1000)

        # Translate with CTranslate2 model(API)
        if user_input != '':
            start = time.time()
            #result = request.post(xxx)
            hypotheses = {"translatedText":[{"translated":"(월요일 발행 기사 중복, 본문 변경 없음) 8월 15일 로이터=런던) 호주 우라늄 광부 아우라 에너지는 9월 말까지 런던 증시의 AIM 시장에 주식을 상장할 계획이며 285만 파운드(37억 달러)를 목표로 하고 있다고 월요일 밝혔다."}]}
            end = time.time()

        # Create a button
        submitted = st.form_submit_button("Translate")

        # If the button pressed, print the translation
        # Here, we use "st.info", but you can try "st.write", "st.code", or "st.success".
        if submitted:
            st.write("Translation")
            st.info(' '.join([h['translated'] for h in hypotheses["translatedText"]]))

        # Add the following JavaScript code to simulate a click on the "Translate" button when the user presses Shift + Enter.
        components.html(
        """
        <script>
        const doc = window.parent.document;
        buttons = Array.from(doc.querySelectorAll('button div[data-testid="stMarkdownContainer"]'));
        const submit_button = buttons.find(el => el.innerText === 'Translate');
        doc.addEventListener('keydown', function(e) {
            if (e.shiftKey && e.keyCode == 13){
                submit_button.click();
            }
        });
        </script>
        """,
        height=0,
        width=0,
    )
else:
    st.markdown(
    """
    ### You must be logged in to use the translator!
    If you don't have an account, please contact Jihyo Kim at (☎️4804)
    """
)
