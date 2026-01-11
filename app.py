from services import login_user, create_order
from database import connect_db

print("Starting Enterprise App")

# Hardcoded DB credentials (Security issue)
db = connect_db("root", "root123")

# Hardcoded user credentials (Security issue)
user = login_user("admin", "admin123")

if user:
    create_order(user, 15000)
else:
    print("Login failed")
