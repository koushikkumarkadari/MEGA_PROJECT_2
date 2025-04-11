import pyautogui
import pyperclip
import time
import re
import google.generativeai as genai
pyautogui.click(553, 736)
# Configure Gemini API
genai.configure(api_key="AIzaSyB13sOl_LVCm0WXFCuisoMAfRsubbQJhEA")
model = genai.GenerativeModel("gemini-1.5-flash-002")

def generate_reply(chat_history):
    try:
        prompt = (
            f"You are a friendly and fun person. Given the chat history below, "
            f"generate a smart and casual reply to the last message:\n\n{chat_history}\n\n"
            "Reply in 1-2 lines."
        )
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print("❌ Error generating reply:", e)
        return "Oops! Something went wrong."
def trail1():
    time.sleep(0.3)

    # Step 2: Select chat area
    pyautogui.moveTo(1247,210)
    pyautogui.mouseDown()
    pyautogui.moveTo(1243,651, duration=0.5)
    pyautogui.mouseUp()

    # Step 3: Copy selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    pyautogui.click(1137, 310)
    pyautogui.click(1037, 310)
    # Step 4: Get text from clipboard
    text = pyperclip.paste()
    return text
def trail2():
    time.sleep(0.3)

    # Step 2: Select chat area
    pyautogui.moveTo(573,217)
    pyautogui.mouseDown()
    pyautogui.moveTo(855,646, duration=0.5)
    pyautogui.mouseUp()

    # Step 3: Copy selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    pyautogui.click(1137, 310)
    pyautogui.click(1037, 310)
    # Step 4: Get text from clipboard
    text = pyperclip.paste()
    return text
def check_and_reply():
    result1=trail1()
    text=result1
    if(text==""):
        result2=trail2()
        text=result2
        
    print("\n📋 Copied chat:\n", text)

    # Step 5: Extract last message
    matches = re.findall(r'\[\d{1,2}:\d{2} [ap]m, \d{1,2}/\d{1,2}/\d{4}\] (.*?): (.+)', text)

    if matches:
        last_sender, last_message = matches[-1]
        print(f"🗣️ Last message from: {last_sender}\n💬 Message: {last_message}")

        if last_sender.lower() == "chikki":
            reply = generate_reply(text)
            print(f"\n🤖 Gemini's reply: {reply}")

            # Step 6: Click and type into text box
            pyautogui.click(637, 684)
            time.sleep(0.3)
            pyautogui.write(reply, interval=0.05)

            # Step 7: Click send button
            pyautogui.click(1328, 687)
            print("✅ Reply sent.")
        else:
            print("⏭️ Not from Chikki. Skipping reply.")
    else:
        print("⚠️ No valid messages found.")

# Continuous loop every 5 seconds
print("🔁 Auto-reply bot running... Press Ctrl+C to stop.")
time.sleep(3)

while True:
    
    check_and_reply()
    time.sleep(5)
