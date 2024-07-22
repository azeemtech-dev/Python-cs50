filename = input("Enter file name: ").strip().lower()
if filename.endswith(".jpg"):
    print("image/jpg")
elif filename.endswith(".jpeg"):
    print("image/jpeg")
elif filename.endswith(".txt"):
    print("text/txt")
elif filename.endswith(".png"):
    print("application/png")
elif filename.endswith(".pdf"):
    print("application/pdf")
elif filename.endswith(".gif"):
    print("image/gif")
else:
    print("application/octect-stream")



