import re
import random

reflections = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you": "me",
    "your": "my",
    "yours": "mine",
    "me": "you"
}

patterns = [
    (r"hello|hi|hey", ["Hello. How can I help you today?", "Hi there. What’s on your mind?"]),
    (r"my name is (.*)", ["Hello %1, it’s good to meet you.", "Nice to meet you %1."]),
    (r"i feel (.*)", ["Why do you feel %1?", "Tell me more about feeling %1."]),
    (r"i am (.*)", ["How long have you been %1?", "Why do you say you are %1?"]),
    (r"because (.*)", ["Is that really the reason?", "Does that reason explain everything?"]),
    (r"my mother is (.*)", ["Why do you say your mother is %1?", "What makes you feel that your mother is %1? "]),
    (r"i need (.*)", ["Why do you need %1?", "What would having %1 do for you?"]),
    (r"(.*)stress(.*)", ["Stress can be difficult. What are you doing to manage it?", "It sounds like your stress is important. Tell me more."]),
    (r"(.*)tired(.*)", ["Being tired can make things harder. Have you rested enough?", "What do you think is making you tired?"]),
    (r"quit", ["Goodbye! Take care.", "Thanks for chatting. Remember to rest."]),
    (r"(.*)", ["Please tell me more.", "Let's keep exploring that.", "How does that make you feel?"])
]


def reflect(fragment: str) -> str:
    words = fragment.lower().split()
    return ' '.join([reflections.get(word, word) for word in words])


def get_eliza_response(user_input: str) -> str:
    user_input = user_input.strip().lower()
    if not user_input:
        return "Please say something so I can answer."

    for pattern, responses in patterns:
        match = re.match(pattern, user_input)
        if match:
            response = random.choice(responses)
            # Replace captured groups and reflect pronouns
            for i in range(len(match.groups())):
                part = reflect(match.group(i + 1))
                response = response.replace(f"%{i+1}", part)
            return response

    return "I'm not sure I understand. Can you elaborate?"


if __name__ == "__main__":
    print("ELIZA Chatbot")
    print("Type 'quit' to stop.\n")

    while True:
        user_input = input('> ').strip()
        if not user_input:
            continue

        reply = get_eliza_response(user_input)
        print(reply)

        if re.match(r"^quit$", user_input.lower()):
            break