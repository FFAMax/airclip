#!/usr/bin/env python3
# sudo apt install xclip
from flask import Flask, request
import subprocess
import shutil

app = Flask(__name__)

clipboard = ""

def write_to_clipboard(text):
    if shutil.which("wl-copy"):
        # Wayland
        try:
            subprocess.run(["wl-copy"], input=text.encode("utf-8"), check=True)
            print("✅ Text copied with wl-copy (Wayland)")
        except Exception as e:
            print("❌ wl-copy failed:", e)

    elif shutil.which("xclip"):
        # X11 with xclip
        try:
            subprocess.run(["xclip", "-selection", "clipboard"], input=text.encode("utf-8"), check=True)
            print("✅ Text copied with xclip (X11)")
        except Exception as e:
            print("❌ xclip failed:", e)

    elif shutil.which("xsel"):
        # X11 with xsel
        try:
            subprocess.run(["xsel", "--clipboard", "--input"], input=text.encode("utf-8"), check=True)
            print("✅ Text copied with xsel (X11)")
        except Exception as e:
            print("❌ xsel failed:", e)
    else:
        print("❌ No clipboard tool found (install xclip, xsel or wl-clipboard)")

@app.route("/set", methods=["POST"])
def set_clipboard():
    global clipboard
    clipboard = request.form.get("text", "")
    print("📥 Received:", clipboard)

    write_to_clipboard(clipboard)

    return "OK"

if __name__ == "__main__":
    print("🌐 Python clipboard server running on port 5000")
    app.run(host="0.0.0.0", port=5000)
    print("Press Ctrl+C to stop the server.")

# -------------------------------------------------------------
# 📱 iPhone Shortcut Setup (to use with this server):
#
# 1. Open the Shortcuts app on your iPhone
# 2. Create a new Shortcut named e.g. "Send to Linux"
# 3. Add action: "Get Clipboard"
# 4. Add action: "Get contents of URL"
#    - URL: http://<YOUR_LINUX_IP>:5000/set
#    - Method: POST
#    - Request Body: Form
#    - Add field:
#        Key: text
#        Value: Clipboard (insert variable)
# 5. Optional: Add to Home Screen for quick access
#
# That's it! Now when you run the shortcut, the iPhone clipboard
# will be sent over HTTP and stored into your Linux system clipboard.
#
# -------------------------------------------------------------
