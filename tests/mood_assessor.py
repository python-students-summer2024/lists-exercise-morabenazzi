import os
import datetime


mood_mapping = {
    "happy": 2,
    "relaxed": 1,
    "apathetic": 0,
    "sad": -1,
    "angry": -2
}


data_dir = "data"
diary_file = os.path.join(data_dir, "mood_diary.txt")

def get_today_date():
    return str(datetime.date.today())

def read_mood_diary():
    if not os.path.exists(diary_file):
        return []
    with open(diary_file, 'r') as file:
        return [line.strip().split(',') for line in file]

def write_mood_to_diary(date_today, mood_int):
    with open(diary_file, 'a') as file:
        file.write(f"{date_today},{mood_int}\n")

def mood_input():
    while True:
        mood = input("Please enter your mood (happy, relaxed, apathetic, sad, angry): ").lower()
        if mood in mood_mapping:
            return mood_mapping[mood]
        else:
            print("Invalid mood. Please try again.")

def diagnose_disorder(mood_ints):
    mood_count = {"happy": 0, "relaxed": 0, "apathetic": 0, "sad": 0, "angry": 0}

    
    for mood_int in mood_ints:
        for mood, int_value in mood_mapping.items():
            if mood_int == int_value:
                mood_count[mood] += 1

    
    if mood_count["happy"] >= 5:
        diagnosis = "manic"
    elif mood_count["sad"] >= 4:
        diagnosis = "depressive"
    elif mood_count["apathetic"] >= 6:
        diagnosis = "schizoid"
    else:
        avg_mood = round(sum(mood_ints) / 7)
        diagnosis = next(mood for mood, int_value in mood_mapping.items() if int_value == avg_mood)

    
    print(f"Your diagnosis: {diagnosis}!")

def assess_mood():
    
    os.makedirs(data_dir, exist_ok=True)

    
    date_today = get_today_date()

    
    entries = read_mood_diary()

    
    for entry in entries:
        if entry[0] == date_today:
            print("Sorry, you have already entered your mood today.")
            return

    
    mood_int = mood_input()

    
    date_today = get_today_date()  
    write_mood_to_diary(date_today, mood_int)

    
    if len(entries) >= 6:
        
        last_7_entries = entries[-6:] + [[date_today, str(mood_int)]]
        mood_ints = [int(entry[1]) for entry in last_7_entries]
        diagnose_disorder(mood_ints)
