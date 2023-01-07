from company_blog import db
from company_blog.models import User


db.create_all()

user1 = User(email="admin_user@test.com", username="Admin User", Password="123", administrator="1")
db.session.add(user1)
db.session.commit()