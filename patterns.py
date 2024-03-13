# Define some patterns and responses
patterns = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I help you today?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm good, thanks for asking.", "I'm great, how about you?"]
    ],
    [
        r"what is your name ?",
        ["You can call me Chatbot.", "I go by the name Chatbot.", "I'm Chatbot, nice to meet you!"]
    ],
    [
        r"what can you do ?",
        ["I can answer your questions, provide information, or just chat with you.", "I'm here to assist you with anything you need."]
    ],
    [
        r"exit",
        ["Bye, take care. See you soon!", "Goodbye! Have a great day!"]
    ],
    [
        r"how can I (.*) ?",
        ["You can %(1)s by %(1)s", "To %(1)s, you can %(1)s", "Try %(1)s and see if it helps!"]
    ],
    [
        r"(.*) weather (.*)",
        ["The weather is %(2)s today.", "You can check the weather forecast online."]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!"]
    ],
    [
        r"who (.*) your favorite actor ?",
        ["I'm a chatbot, I don't have favorites, but I can recommend some popular actors if you'd like!"]
    ],
    [
        r"(.*) (movie|film) (.*) recommend (.*)",
        ["I recommend %(4)s. It's a great %(2)s!", "You should check out %(4)s. It's getting great reviews."]
    ],
    [
        r"how do you feel about (.*) ?",
        ["I don't have feelings, but I can provide information about %(1)s if you'd like."]
    ],
    [
        r"thanks|thank you",
        ["You're welcome!", "No problem! Feel free to ask if you need further assistance."]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you please rephrase that?", "Could you elaborate on that?", "I'm sorry, I didn't catch that. Can you say it again?"]
    ]
]




