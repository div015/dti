
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("path/to/your/firebase/credentials.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Adding a user to the database (for example)
def add_user(user_id, name, medication_list):
    doc_ref = db.collection('users').document(user_id)
    doc_ref.set({
        'name': name,
        'medication_list': medication_list,
        'adherence_history': []
    })
    print("User added successfully!")
