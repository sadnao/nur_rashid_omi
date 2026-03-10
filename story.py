import textwrap

story = '''You are the captain of Skybound Express, a futuristic cargo airline responsible for delivering critical supplies to cities located around airports across the world. Outside these airport zones, the environment has become uninhabitable, so these locations are the last safe hubs for human survival.
Each airport faces different challenges such as harsh weather conditions, unstable air currents, and dangerous storms. Governments rely heavily on pilots like you to transport essential goods such as food, medicine, and technology.
One day, your assistant receives an emergency signal from a distant city where communications have suddenly stopped. Without urgent supplies, the population faces a severe crisis. You must travel across multiple airports, carefully manage your fuel and money, complete delivery missions, and avoid hazards to save the city.
'''

# Set column width to 80 characters
wrapper = textwrap.TextWrapper(width=80, break_long_words=False, replace_whitespace=False)
# Wrap text
word_list = wrapper.wrap(text=story)


def getStory():
    return word_list