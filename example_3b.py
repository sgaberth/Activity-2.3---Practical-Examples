
web_data = ["techresearch and computervision"]
if "@" in web_data:
    print("e-mail address")
elif "0123456789" in web_data:
    print("phone number")
else:
    print("not e-mail nor phone")
