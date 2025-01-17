def create_follow_up(question_type: str) -> str:
    """Generates a follow-up question based on the user's input."""
    question_mapping = {
        "scales": "Would you like some tips on playing scales at different speeds?",
        "chords": "Would you like to learn more about chord progressions?",
        "rhythm": "Would you like advice on improving your rhythm skills?",
        "arpeggios": "Would you like to learn how to practice arpeggios more effectively?",
        "finger exercises": "Would you like some finger exercises to improve your dexterity?",
        "ear training": "Would you like to practice identifying intervals and chords by ear?",
        "improvisation": "Would you like tips on how to start improvising over chord progressions?",
        "technique": "Would you like to focus on improving a specific playing technique, such as fingerpicking or alternate picking?",
        "jazz": "Would you like to dive into jazz theory or learn some jazz standards?",
        "classical": "Would you like to explore classical music theory or practice techniques?",
        "blues": "Would you like to learn about the blues scale and its applications?",
        "sight-reading": "Would you like to practice sight-reading new pieces or exercises?",
        "composition": "Would you like to learn more about composing your own music?",
        "music production": "Would you like tips on recording or producing your own music?",
    }
    for key, follow_up in question_mapping.items():
        if key in question_type.lower():
            return follow_up
    return "Is there something else you'd like help with, or would you like to explore another area of music?"