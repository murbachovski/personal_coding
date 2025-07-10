# 가상환경 생성
    # conda create -n gr python=3.9
    # pip install googletrans==4.0.0-rc1

import gradio as gr
from googletrans import Translator

# 번역기 객체 생성
translator = Translator()

# 번역 함수 정의
def translate_en_to_ko(text):
    translated = translator.translate(text, src='en', dest='ko')
    return translated.text

# 스타일 강화된 Gradio 인터페이스
with gr.Blocks(title="🌐 English to Korean Translator") as app:
    gr.Markdown("## 🌐 영어 → 한국어 번역기")
    gr.Markdown("입력한 **영어 문장**을 정확하고 자연스럽게 **한국어로 번역**해드립니다. 아래에 문장을 입력하고 `번역하기` 버튼을 눌러보세요!")

    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(label="영어 문장 입력", lines=6, placeholder="예: Artificial intelligence is transforming every industry.")
            translate_button = gr.Button("번역하기")

        with gr.Column():
            output_text = gr.Textbox(label="번역 결과 (한국어)", lines=6)

    translate_button.click(fn=translate_en_to_ko, inputs=input_text, outputs=output_text)

    gr.Examples(
        examples=[
            "Although artificial intelligence has made remarkable progress in recent years, especially in fields such as natural language processing and computer vision, there are still numerous ethical and technical challenges.",
            "The development of self-driving cars is a complex task that requires advanced AI algorithms and real-time data processing.",
            "Climate change is one of the most pressing global challenges of our time.",
        ],
        inputs=input_text
    )

app.launch()