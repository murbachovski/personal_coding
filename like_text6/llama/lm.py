import lmstudio as lms
import pyfiglet
from termcolor import colored

# 🎉 Welcome 메시지 출력
ascii_banner = pyfiglet.figlet_format("Welcome!")
colored_banner = colored(ascii_banner, color="yellow")
print(colored_banner)

print(colored("You are now chatting with TaskBot!", "blue"))
print(colored("Type your message below. Leave blank to exit.\n", "blue"))

# LMStudio 초기화
model = lms.llm()
chat = lms.Chat("You are a task focused AI assistant")

# 채팅 루프
while True:
    try:
        user_input = input("You (leave blank to exit): ")
    except EOFError:
        print()
        break
    if not user_input:
        break
    chat.add_user_message(user_input)
    prediction_stream = model.respond_stream(
        chat,
        on_message=chat.append,
    )
    print("Bot: ", end="", flush=True)
    for fragment in prediction_stream:
        print(fragment.content, end="", flush=True)
    print()
