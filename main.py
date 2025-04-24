from Speech import get_voice_command
from TTS import speak
from database import insert_transaction, fetch_transactions, calculate_balance

def transaction_input(text):
    words = text.split()
    amount = None
    category = ""
    for i, word in enumerate(words):
        if word.replace('.', '', 1).isdigit():
            amount = float(word)
            category = " ".join(words[:i])
            break
    return category, amount

def handle_add(trans_type):
    speak("Tell me the " + trans_type + " category and amount.")
    text = get_voice_command("Listening...")
    category, amount = transaction_input(text)
    if category and amount:
        insert_transaction(trans_type, category, amount)
        speak(trans_type.title() + " of ₹" + str(amount) + " added under " + category + ".")
    else:
        speak("Sorry, I couldn't understand that.")

def handle_show_transactions():
    transactions = fetch_transactions()
    if not transactions:
        speak("No transactions found.")
        return
    for t in transactions:
        print(t[4], " - ", t[1].title(), " | ", t[2], ": ₹", str(t[3]))
    speak("Showing " + str(len(transactions)) + " transactions.")

def handle_show_balance():
    balance = calculate_balance()
    speak("Your current balance is ₹" + "{:.2f}".format(balance))

def main():
    speak("Welcome to your voice-controlled expense tracker.")
    while True:
        speak("Say a command like add expense, add gain, show balance, show transactions, or exit.")
        command = get_voice_command()

        if "add expense" in command:
            handle_add("expense")
        elif "add gain" in command or "add income" in command:
            handle_add("gain")
        elif "show transactions" in command:
            handle_show_transactions()
        elif "show balance" in command:
            handle_show_balance()
        elif "exit" in command:
            speak("See you; Bye Bye!")
            break
        else:
            speak("Command not recognized. Try again.")

if __name__ == "__main__":
    main()
