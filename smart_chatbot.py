from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
texts = ["hello", "hi", "how are you", "bye"]
labels = ["greet", "greet", "status", "bye"]

# Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = MultinomialNB()
model.fit(X, labels)

print("AI Chatbot: Hello! Type 'bye' to exit")

while True:
    user = input("You: ")
    X_test = vectorizer.transform([user])
    prediction = model.predict(X_test)[0]

    if prediction == "greet":
        print("Bot: Hello!")
    elif prediction == "status":
        print("Bot: I am fine!")
    elif prediction == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand")
