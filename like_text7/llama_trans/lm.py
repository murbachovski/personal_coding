import lmstudio as lms
import pyfiglet
from termcolor import colored
from deep_translator import GoogleTranslator

def trans_en_ko(text):
    '''
    한국어 => 영어 번역
    '''
    return GoogleTranslator(source='en', target='ko').translate(text)

def trans_ko_en(text):
    '''
    영어 => 한국어 번역
    '''
    return GoogleTranslator(source='ko', target='en').translate(text)

# 🎉 Welcome 메시지 출력
ascii_banner = pyfiglet.figlet_format("Welcome!")
colored_banner = colored(ascii_banner, color="yellow")
print(colored_banner)

print(colored("You are now chatting with TaskBot!", "blue"))
print(colored("Type your message below. Leave blank to exit.\n", "blue"))
print(colored("Input : Kor => Eng || Answer : Eng => Kor\n", "blue"))

# LMStudio 초기화
model = lms.llm()
chat = lms.Chat("You are a task focused AI assistant")

# 채팅 루프
while True:
    try:
        user_input = input("You (leave blank to exit): ")
        if not user_input:
            break
        # 입력 번역: ko → en
        user_input_translated = trans_ko_en(user_input)
    except EOFError:
        print()
        break

    chat.add_user_message(user_input_translated)
    prediction_stream = model.respond_stream(
        chat,
        on_message=chat.append,
    )

    # 응답 수집
    response_text = ""
    for fragment in prediction_stream:
        response_text += fragment.content

    translated_response = trans_en_ko(response_text)

    print("\n원본 답변: ", response_text.strip())
    print("번역된 답변: ", translated_response.strip())
