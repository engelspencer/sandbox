story = '''
It happened in ancient times that a slave named Androcles escaped from his master and fled into the forest, and he wandered there for a long time until he was weary.

Just then he heard a lion near him moaning and groaning and at times roaring terribly.  And when  he tried to get up, there he saw the lion coming towards him.

Instead of attacking him it kept on moaning and groaning and looking at Androcles, who saw that the lion was holding out his right paw, which was covered with blood and very much swollen. Looking more closely at it, Androcles saw a great big thorn pressed into the paw, which was the cause of all the lion’s trouble.

Plucking up courage, he seized hold of the thorn and drew it out of the lion’s paw, who roared with pain when the thorn came out, but soon after found such relief from it that he rubbed up against Androcles, and showed  that he knew, that he was truly thankful for being relieved from such pain.

One day, a number of soldiers came marching through the forest and found Androcles. They took him prisoner and brought him back to the town, and he was condemned to death because he had fled from his master.

Now it used to be the custom to throw murderers and other criminals to the lions,  and on the appointed day he was led forth into the arena.

The Emperor of Rome was in the royal box that day and gave the signal for the lion to come out and attack Androcles. But when it came out of its cage and got near Androcles, what do you think it did? Instead of jumping upon him, it rubbed up against him, and stroked him with its paw.

It was of course the lion which Androcles had met in the forest. The Emperor summoned Androcles to him. So Androcles told the Emperor all that had happened to him and how the lion was showing gratitude for his having relieved it of the thorn. Thereupon, the emperor pardoned Androcles and ordered his master to set him free, while the lion was taken back into the forest and let loose to enjoy freedom once more.
'''
print(story)

slave = input("Enter a noun: ")
androcles = input("Enter a person: ")
master = input("Enter a person: ")
lionSounds = [input("Enter three verbs that make sounds: "),input(),input()]
attack = input("Enter a verb: ")
thorn = input("Enter a noun: ")
plucking = input("Enter a verb: ")
drew = input("Enter a past-tense verb: ")
pain = input("Enter a noun: ")
rubbed = input("Enter a past-tense verb: ")
soldiers = input("Enter a plural noun: ")
forest = input("Enter a place: ")
town = input("Enter a place: ")
death = input("Enter a state of being: ")
murderers = input("Enter a plural noun: ")
otherCriminals = input("Enter a plural noun: ")
arena = input("Enter a place: ")
emperor = input("Enter a person's title")
signal = input("Enter a noun: ")

story = story.replace("slave", slave)
story = story.replace("Androcles", androcles)
story = story.replace("master", master)
story = story.replace("moaning", lionSounds[0])
story = story.replace("groaning", lionSounds[1])
story = story.replace("roaring", lionSounds[2])
story = story.replace("roared", lionSounds[2])
story = story.replace("attacking", attack)
story = story.replace("attack", attack)
story = story.replace("thorn", thorn)
story = story.replace("plucking", plucking)
story = story.replace("drew", drew)
story = story.replace("pain", pain)
story = story.replace("rubbed", rubbed)
story = story.replace("soldiers", soldiers)
story = story.replace("forest", forest)
story = story.replace("town", town)
story = story.replace("death", death)
story = story.replace("murderers", murderers)
story = story.replace("other criminals", otherCriminals)
story = story.replace("arena", arena)
story = story.replace("Emperor", emperor)
story = story.replace("emperor", emperor)
story = story.replace("signal", signal)
