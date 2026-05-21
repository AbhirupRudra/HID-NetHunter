from HID_NetHunter import HID_NetHunter

if __name__ == "__main__":
    nethunter = HID_NetHunter()

    # Example usage: Type "Hello, World!" with a delay between each key press
    text = "Hello, World!"
    nethunter.send_text(text)