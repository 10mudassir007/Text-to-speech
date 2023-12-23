import elevenlabs
audio = elevenlabs.generate(text ='Hello world',
                            voice = 'Bella')

elevenlabs.play(audio)