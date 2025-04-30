from werkzeug.security import generate_password_hash

plain_text_password = "testpin"  # CHANGE THIS to your desired prototype PIN
hashed_password = generate_password_hash(plain_text_password)

print(hashed_password)  # This is what you'll put in your database