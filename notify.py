# Firebase Function to check missed doses
def check_missed_doses(user_id):
    user_ref = db.collection('users').document(user_id)
    user = user_ref.get()
    
    if user.exists:
        adherence_history = user.to_dict()['adherence_history']
        last_dose_time = adherence_history[-1] if adherence_history else None
        
        # Assume the adherence threshold is set for a time window (e.g., 24 hours)
        if last_dose_time and time_since(last_dose_time) > 24:
            caregiver_ref = db.collection('caregivers').document(user_id)
            caregiver = caregiver_ref.get()
            if caregiver.exists:
                caregiver_data = caregiver.to_dict()
                caregiver_phone = caregiver_data['phone']
                send_sms(caregiver_phone, 'Reminder: The user has missed their medication.')
                print("Caregiver notified.")
                
def time_since(last_dose_time):
    # Dummy function to calculate time since the last dose
    # In a real scenario, this would compare current time and the last dose timestamp.
    return 25  # Assume 25 hours have passed
