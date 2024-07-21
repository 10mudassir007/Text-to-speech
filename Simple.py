import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()
select_rate = int(input('Enter speed of speech(in terms of words per minute,150 is the normal) : '))
select_volume = int(input('Enter volume 0 to 100 : '))/100
# Set properties (optional)
engine.setProperty('rate', select_rate)  # Speed of speech
engine.setProperty('volume', select_volume)  # Volume level (0.0 to 1.0)
voices = engine.getProperty('voices')
select_voice = int(input('Enter 0 for male voice and 1 for female voice : '))
if select_voice == 0:
    engine.setProperty('voice', voices[0].id)
if select_voice == 1:
    engine.setProperty('voice', voices[1].id)
# Convert text to speech
text = input('Enter text to speak : ')
text = """God sees the truth, but waits
Leo tolstoy
In the town of Vladimir lived a young merchant named Ivan Dmitrich Aksionov.
He had two shops and a house of his own.
Aksionov was a handsome, fair-haired, curly-headed fellow, full of fun, and very
fond of singing. When quite a young man he had been given to drink, and was
riotous when he had had too much; but after he married he gave up drinking,
except now and then.
One summer Aksionov was going to the Nizhny Fair, and as he bade good-bye to
his family, his wife said to him, "Ivan Dmitrich, do not start to-day; I have had a
bad dream about you."
Aksionov laughed, and said, "You are afraid that when I get to the fair I shall go on
a spree."
His wife replied: "I do not know what I am afraid of; all I know is that I had a bad
dream. I dreamt you returned from the town, and when you took off your cap I saw
that your hair was quite grey."
Aksionov laughed. "That's a lucky sign," said he. "See if I don't sell out all my
goods, and bring you some presents from the fair."
So he said good-bye to his family, and drove away. When he had travelled halfway, he met a merchant whom he knew, and they put up at the same inn for the
night. They had some tea together, and then went to bed in adjoining rooms.
It was not Aksionov's habit to sleep late, and, wishing to travel while it was still
cool, he aroused his driver before dawn, and told him to put in the horses.
Then he made his way across to the landlord of the inn (who lived in a cottage at
the back), paid his bill, and continued his journey.
When he had gone about twenty-five miles, he stopped for the horses to be fed.
Aksionov rested awhile in the passage of the inn, then he stepped out into the
porch, and, ordering a samovar to be heated, got out his guitar and began to play.
Suddenly a troika drove up with tinkling bells and an official alighted, followed by
two soldiers. He came to Aksionov and began to question him, asking him who he
was and whence he came. Aksionov answered him fully, and said, "Won't you
have some tea with me?" But the official went on cross-questioning him and asking
him. "Where did you spend last night? Were you alone, or with a fellow-merchant?
Did you see the other merchant this morning? Why did you leave the inn before
dawn?"
Aksionov wondered why he was asked all these questions, but he described all that
had happened, and then added, "Why do you cross-question me as if I were a thief
or a robber? I am travelling on business of my own, and there is no need to
question me."
Then the official, calling the soldiers, said, "I am the police-officer of this district,
and I question you because the merchant with whom you spent last night has been
found with his throat cut. We must search your things."
They entered the house. The soldiers and the police-officer unstrapped Aksionov's
luggage and searched it. Suddenly the officer drew a knife out of a bag, crying,
"Whose knife is this?"
Aksionov looked, and seeing a blood-stained knife taken from his bag, he was
frightened.
"How is it there is blood on this knife?"
Aksionov tried to answer, but could hardly utter a word, and only stammered: "I--
don't know--not mine." Then the police-officer said: "This morning the merchant
was found in bed with his throat cut. You are the only person who could have done
it. The house was locked from inside, and no one else was there. Here is this blood-"""
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()


save_file = input('Save file, Y/N : ')
if save_file == 'Y':
    name = input('Enter name of file with extension : ')
    engine.save_to_file(text,name)                



