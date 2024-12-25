Direction = True
while Direction:
    go = input('Does he talk to them?')
    if go.lower() != 'yes':
        story = "They then stop talking and ask to who he is and he says his name but that the group of people then says there name and walk with him to the train station. They then proceed to explain to him about the mysterious train."  
        print(story)
        break
    else: 
        story = 'They ignore our hero and our heo decides to walk towards the station hoping that he can get there but instead he gets lost and is wondering where it is. No one around him is helping out so through trial and error that he does find the station.'
        print(story)
        break

Train = True
while Train:
    ex = input('Does he embark on the train?')
    if ex.lower() != 'yes':
        def story():
            return 'He hops on the train and makes it to merlin place and starts to talking to him about what is going on. Merlin then proceeds to explain to him that a lot has happened since he was gone and that merlin brings out a book which our hero and learned a lot.'
        print(story())
        break
    else:
        def story():
            return "He doesn't hop on the train and instead, he thinks he can walk to Merlins place which does and by the time he arrives. That merlin is already asleep so our hero decides to find a spot and sleep for night hoping that no one comes to him alive."
        print(story())
        break

Journey = True
while Journey:
    fro  = input('Do you accept or not accept this journey?')
    if fro.lower() == 'y':
        story = 'He accepts the journey and follows Merlin to the portal that leads to the land of magic and adventure. There he meets new friends and enemies, and discovers his true destiny.'
        print(story)
        break
    elif fro.lower() == 'n':
        story = 'He declines the journey and decides to stay in the world he knows. He bids farewell to Merlin and returns to his slumber, hoping to find some answers in his dreams.'
        print(story)
        break
    else:
        print('Please enter Y or N.')
