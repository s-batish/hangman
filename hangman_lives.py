"""
Hangman lives images
"""
stages = [
    # final state: head, torso, both arms, both legs
    """
    _______________
    |             |
    |            ___
    |          ||   ||
    |         || x x ||
    |         ||  .  ||
    |     ||    \\_-_/     ||
    |      ||    |||     ||
    |       ||   |||   ||
    |         |||||||||
    |            |||
    |           || ||
    |          ||   ||
    |         ||     ||
    |        ||       ||
    |_____________________
    """,
    # head, torso, both arms, one leg
    """
    _______________
    |             |
    |            ___
    |          ||   ||
    |         || - x ||
    |         ||  .  ||
    |     ||    \\_=_/     ||
    |      ||    |||     ||
    |       ||   |||   ||
    |         |||||||||
    |            |||
    |              ||
    |               ||
    |                ||
    |                 ||
    |_____________________
    """,
    # head, torso, both arms
    """
    _______________
    |             |
    |            ___
    |          ||   ||
    |         || o o ||
    |         ||  .  ||
    |     ||    \\_o_/     ||
    |      ||    |||     ||
    |       ||   |||   ||
    |         |||||||||
    |            |||
    |
    |
    |
    |
    |_____________________
    """,
    # head, torso, one arm
    """
    _______________
    |             |
    |            ___
    |          ||   ||
    |         || o o ||
    |         ||  .  ||
    |           \\_~_/     ||
    |            |||     ||
    |            |||   ||
    |            ||||||
    |            |||
    |
    |
    |
    |
    |_____________________
    """,
    # head, torso
    """
    _______________
    |             |
    |            ___
    |          ||   ||
    |         || o o ||
    |         ||  .  ||
    |           \\_=_/
    |            |||
    |            |||
    |            |||
    |            |||
    |
    |
    |
    |
    |_____________________
    """,
    # head
    """
    _______________
    |             |
    |            ___
    |          ||   ||
    |         || o o ||
    |         ||  .  ||
    |           \\_-_/
    |
    |
    |
    |
    |
    |
    |
    |
    |_____________________
    """,
    # intitial state
    """
    _______________
    |             |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |_____________________
    """,
]