#importin some important shit or the whole game explodes
import mysql.connector
import random
from utilities import anim_print
from utilities import conn

def trivia_game():
    try:
        
        cursor = conn.cursor()

        #creating the table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS trivia_questions (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            question VARCHAR(255) NOT NULL,
                            option1 VARCHAR(255) NOT NULL,
                            option2 VARCHAR(255) NOT NULL,
                            option3 VARCHAR(255) NOT NULL,
                            option4 VARCHAR(255) NOT NULL,
                            correct_option INT NOT NULL
                        )''')
        conn.commit()

        # deletes everything from questions table in sql, otherwise duplicates will be generated fucking shit up in the process
        cursor.execute("TRUNCATE TABLE trivia_questions")

        # check if trivia questions exist already and insert if no questions in tavle UwU
        cursor.execute("SELECT COUNT(*) FROM trivia_questions")
        count = cursor.fetchone()[0]

        
            # questions followed by 4 potential aswers and a number representing the right aswer.
        questions = [
            ("What is the capital of France?", "Berlin", "London", "Paris", "Madrid", 3),
            ("Who wrote 'Hamlet'?", "Mark Twain", "William Shakespeare", "Charles Dickens", "Leo Tolstoy", 2),
            ("What is the largest planet in our solar system?", "Earth", "Jupiter", "Saturn", "Mars", 2),
            ("What is the chemical symbol for water?", "H30", "H2O2", "HO2", "H2O", 4),
            ("Which year did World War I begin?", "1914", "1918", "1939", "1945", 1),
            ("Which year did world war 2 end?", "1963", "1945", "1933", "1943", 2),
            ("What is the name of the volcano located near Tokyo, Japan called?", "Mount Fuji", "Mount Yari", "Mount Kita", "Mount Aino", 1),
            ("Who sang the title song for the latest Bond film, No Time to Die?", "Adele", "Sam Smith", "Billie Eilish", "Michael Jackson", 3),
            ("Which flies a green, white, and orange (in that order) tricolor flag? ", "ireland", "Ivory Coast", "Italy", "India", 1),
            ("What company makes the Xperia model of smartphone?", "samsung", "sony", "Nokia", "Apple", 2),
            ("Which city is home to the Brandenburg Gate?", "Vienna", "Zurich", "Berlin", "Frankfurt", 3),
            ("Which of the following is NOT a fruit?", "Rhubarb", "Tomatoes", "Avocados", "Potatoes", 1),
            ("Where was the first example of paper money used?", "China", "Turkey", "Greece", "Japan", 1),
            ("Who is generally considered the inventor of the motor car?", "Henry Ford", "Karl Benz", "Henry M. Leland", "Gottlieb Daimler", 2),
            ("If you were looking at Iguazu Falls, on what continent would you be?", "Asia", "Africa", "South America", "North America", 3),
            ("What number was the Apollo mission that successfully put a man on the moon for the first time in human history?", "Apollo 12", "Apollo 11", "Apollo 13", "Apollo 9", 2),
            ("Which of the following languages has the longest alphabet?", "Greek", "Russian", "Arabic", "Chinese", 2),
            ("Who was the lead singer of the band The Who?", "Roger Daltrey", "Don Henley", "Robert Plant", "Bob Geldof", 1),
            ("What spirit is used in making a Tom Collins?", "Vodka", "Rum", "Gin", "tequila", 3),
            ("The fear of insects is known as what?", "Entomophobia", "Arachnophobia", "Ailurophobia", "Arachibutyrophobia", 1),
            ("What was the name of the Franco-British supersonic commercial plane that operated from 1976-2003?", "Accord", "Mirage", "Concorde", "The Voyager", 3),
            ("Which horoscope sign is a fish?", "Seahorse", "Aquarius", "Cancer", "Pisces", 4),
            ("What is the largest US state (by landmass)?", "Texas", "California", "Florida", "Alaska", 4),
            ("Which app has the most total users?", "Tik Tok", "Snapchat", "Instagram", "Facebook", 3),
            ("Which Game of Thrones character is known as the Young Wolf?", "Robb Stark", "Arya Stark", "Sansa Stark", "Bran Stark", 1),
            ("What city hosted the 2002 Olympic Games?", "Tokyo", "Paris", "Beijing", "Sydney", 4),
            ("How many plays do people (generally) believe that Shakespeare wrote?", "47", "27", "57", "37", 4),
            ("Which of the following was considered one of the Seven Ancient Wonders?", "Colosseum", "Great Wall of China", "Colossus of Rhodes", "Göbekli Tepe", 3),
            ("Who directed the Academy Award-winning movie, Gladiator?", "Ridley Scott", "James Cameron", "Steven Soderbergh", "Michael Bay", 1),
            ("How long did dinosaurs live on the earth?", "100-150 million years", "150-200 million years", "200+ million years", "300+ million years", 1),
            ("What Italian city is famous for its system of canals?", "Rome", "Naples", "milan", "Venice", 4),
            ("What is the strongest muscle in the human body?", "Jaw", "Heart", "Glutes", "Tongue", 1),
            ("What is the longest-running Broadway show ever?", "Les Miserable", "The Lion King", "The Phantom of the Opera", "Hamilton", 3),
            ("Where was tea invented?", "England", "China", "India", "USA", 2),
            ("Where was the earliest documented case of the Spanish flu?", "Spain", "Mexico", "USA", "Argentina", 3),
            ("Which of the following languages is NOT driven from Latin?", "French", "Portuguese", "English", "Greek", 3),
            ]

            # Insert trivia questions into the 'trivia_questions' table
        cursor.executemany('''INSERT INTO trivia_questions (question, option1, option2, option3, option4, correct_option)
                                  VALUES (%s, %s, %s, %s, %s, %s)''', questions)

        conn.commit()
            
        

        cursor.execute("SELECT * FROM trivia_questions")
        questions = cursor.fetchall()

        if not questions:
            print("No trivia questions found in the database.")
            return

        # mixi mixi the questions
        random.shuffle(questions)

        score = 0
        total_questions = len(questions)

        # Set a limit on questions asked
        question_limit = min(3, total_questions)  # This thingy limits the questions to 3 per game

        # Loop through questions and print them out
        for i, question in enumerate(questions[:question_limit], start=1):
            q_id, question_text, option1, option2, option3, option4, correct_option = question
            anim_print(f"\nQuestion {i}: {question_text}")
            anim_print(f"\n1. {option1}")
            anim_print(f"\n2. {option2}")
            anim_print(f"\n3. {option3}")
            anim_print(f"\n4. {option4}")

            # Record users imput 
            user_answer = input(anim_print("\nYour answer (1-4) or 'q' to quit: "))
            # Exits the game if input = q
            if user_answer.lower() == 'q':
                anim_print("You chose to quit the game.")
                break

            # Check if the answer is correct and print shit on screen accordingly
            if user_answer.isdigit() and int(user_answer) == correct_option:
                anim_print("Correct!")
                score += 1
            else:
                anim_print(f"Wrong! The correct answer was option {correct_option}.")

        # print the final score
        anim_print(f"\nYour final score is {score} out of {i} questions.")
    except mysql.connector.Error as err:
        anim_print(f"Error: {err}")
    finally:
        return score
