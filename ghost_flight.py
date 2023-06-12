choice1 = input("You are a survivor of one of the pandemic-era “ghost” flights passing over the amazon rainforest, which contained only the pilot, co-pilot, and yourself. During the emergency landing the front of the plane was broken off leaving you alone with minimal damage, surrounded by tree limbs jutting through the windows. You awake to find yourself incredibly thirsty. SEARCH plane for water, or go into FOREST? ")

print()
if choice1.lower() == "search":
    choice2 = input("While searching the plane for water, you see movement outside one of the cabin windows. The shape passed by too quickly for you to discern what it actually was in the twilight. STAY in the plane or LEAVE to investigate?")
else: # that is, the choice is "forest."
      # incorrect input is handled by going to an arbitrary choice in each case
    choice2 = input("The forest is magnificent as well as the view of the amazon river basin below, as you realize you made the emergency landing in an overlook of the entire valley. This might actually be a good time to pray about your next move now that the immediate stress of the situation is beginning to clear up from your mind. At the same time there is a great sense of urgency to find the other section of the plane and the pilots. PRAY or CONTINUE to search.")

print()
if choice2.lower() == "stay":
    choice3 = input("You wait inside the plane to see if you can detect that movement again. However, the sun has now set completely making it pitch-dark outside, but the walkway in the plane is still illuminated by the faint greenish glow of the emergency lights. You are exhausted from having to leave early the previous morning, from the stress of the crash, and the time that has passed since. Rest in the BATHROOM, the row closest to the REAR of the plane, or continue to SEARCH for water?")
elif choice2.lower() == "leave":
    choice3 = input("There is still enough light outside to take in the beauty of this forest. You regretted not coming out of the plane sooner. The area where the plane landed was an elevated area of forest, overlooking the amazon river basin in a spectacular view. The reflection of the setting sun off of the water strikes your view through the pink misty clouds, illuminating small boats traversing the river. GO after the boats, or CONTINUE to investigate.")
elif choice2.lower() == "pray":
    choice3 = input("As you kneel down in prayer you realize that it can’t be a coincidence that all of this is happening to you and that there must be a higher reason for it all. You know that whatever that reason is, it is ultimately for your benefit and the benefit of others. You have a small notepad with you in your bag and realize that this might be a time to reflect for a moment and record what you have experienced and your prayer. RECORD or MOVE ON.")
else: # that is "continue"
    choice3 = input("You keep searching for the severed portion of the plane in the thick brush of the forest. It really seems incredible how far it must have separated from your section of the plane. It doesn’t make sense at all that it doesn’t seem to be located where it should, in an area near the front of the plane. You realize that the thickness and height of the trees in this area of the forest may have been the cause of the catastrophic damage during the emergency landing. You want to be able to get to a higher vantage point to be able to see if you can trace the path that the front section of the plane took when it impacted the canopy. At this same time you feel like you must be getting closer on foot and that trying to get to a higher position could cause a loss in much needed time. CLIMB into canopy or keep searching on FOOT?") 

print()
if choice3.lower() == "bathroom":
    print("When you head to the bathroom you hope to find a secure place to rest, where no entry from the outside is possible behind the locked door. Instead, when you open the door, you find that this section of the plane has been sheared by the impact and you realize that no section of the plane is sufficiently secure for your needs. Because it is too dark to go exploring, you decide you need better information about where you actually are. You know your GPS works anywhere without service. You take your phone off airplane mode and as soon as you do, you see a message appear on your phone saying SHARE BLTH CONTACT as a bluetooth notification. Then another one comes saying IM STILL HERE. These two messages keep coming to your phone, alternating back and forth. One of the pilots has “bluejacked” your phone–he is sharing contacts on his phone through bluetooth, except the contact titles were created to be messages. You spend about an hour trying to figure out how to exchange messages and realize you can create your own contacts on your phone, but instead of using a name as the name for the contact, you can use an actual short message instead. You then proceed to share the following message with the pilot: IM ALIVE")
elif choice3.lower() == "rear":
    print("You drift into a light, uncomfortable sleep in one of the many unoccupied passenger seats. The seat you chose was in the rear of the plane but there is a great deal of noise from nocturnal animals outside that makes it difficult to rest. The flying insects are also getting to be frustrating at this point. In fact, because of the hot muggy air inside the cabin, it soon becomes completely intolerable to stay inside and you begin to exit the plane to perhaps find a patch of forest floor to rest on while you decide your next move. To your astonishment you bump right into a net tied around the front of the plane, and you hear the sound of several torches igniting immediately after you contact the net. Three dark figures approach you, armed with bows and arrows, and proceed to wrap the net around you before you realize what’s happening.")
elif choice3.lower() == "search":
    print("The faint glow of the walkway makes it easy enough to continue searching through the luggage compartments for any kind of water bottles potentially left behind. In fact you are getting so used to opening and closing them that you aren’t really relying on sight anymore. The search appears to be in vain as you check every last compartment. After all, you were the only passenger on this ghost flight. You begin checking other areas of the plane and realize that there is a small service door near the bathroom that you hadn’t opened before. You find the flight attendant cart inside, loaded with snacks, water, and soda! Why do people always panic in these kinds of situations, when you might be able to just wait right here and be found soon enough?")
elif choice3.lower() == "go":
    print("The river is still several hundred feet away and it is no small task to descend from the forest overlook to the shore. Along the way you cross into another trail that leads back to several huts and shacks built along an elevated portion of shore and decide to try your luck with contacting the inhabitants. To your surprise they are all empty, and you discover a basket of food and provisions laid on the ground outside the door of the largest building, along with a simple hand-made canoe. Inside the basket is a hand-drawn map with a stick figure circled further down the river.")
elif choice3.lower() == "continue":
    print("There is no sign of any large animal life around the plane apart from tracks made by a large cat. You decide that any further investigation could result in an abrupt end to your life despite your dangerously curious nature. You realize that the only thing worse than having your life end prematurely is living with the regret of not having warned someone else of the danger. You set out to look for the severed section of the ship and encounter the pilots attempting to tend to one another’s wounds. They managed to get free from their seats but only the co-pilot is capable of walking without support. He was using the first aid kit to treat the less-fortunate captain. With all three of you reunited, the captain says “we were headed for you next but you have beat us to it. Let’s make a plan to get out of here.”")
elif choice3.lower() == "record":
    print("As you open up your notepad to write down your thoughts and experiences, you realize that the Spirit seems to have been directing your mind back to the plane wreckage. In particular, there is a section of the plane near the side exit doors that you think could have an essential item. You return to the plane to find that there are instructions near the exit door pointing out the aircraft survival kit location. You open it and discover an AM/FM radio. It’s time to find the pilots, call for help, and leave the forest.")
elif choice3.lower() == "move on":
    print("Your thirst has been getting worse but it hasn’t stopped you from wanting to slow down. It only seems to add to the urgency to find the other pilots. They would probably be in a lot worse condition than you considering how you received minimal damage from the crash. You continue to search for the severed portion with a prayer in your heart that they are still alive at least. The brush is thick and you realize that some kind of tool would have made it much easier to find the rest of the plane. You decide to shout out for help. There is a reply but it is a whistle that sounds almost like an animal call. Over several minutes the whistling gets louder and closer until you begin to hear the sound of a machete cutting through the brush. It turns out to be a fisherman who saw your plane fall and speaks to you in a native dialect. You can’t understand him but when he offers you his canteen of water, you are absolutely relieved.")
elif choice3.lower() == "foot":
    print("You finally discover the severed portion of the plane but you find that the pilots are nowhere to be found. You ponder where in the world they could have gone too. It is already getting dark and you realize that these pilots were thinking the same thing you were thinking. They must have wanted to find your section of the plane with urgency and decided to leave to look for YOU. You decide to write a note and leave it on the seat but as you do so you realize that they have left something behind. One of their phones is on the seat with a message that says “captain can’t walk on his own but we needed to find a safe place for the night. We will meet you at your section of the plane in the morning. We will also check back here in case we can’t find your section but we warn against staying here.”")
else: # that is "climb"
    print("You begin to climb one of the tallest trees and are able to reach almost to the top of the canopy. However once you get to the highest section of the tree you lose your ability to descend safely due to physical exhaustion. The payoff is that you do indeed get to see the descent path of the front section of the plane. You know exactly where it is now. The situation with climbing is getting somewhat desperate as you don’t have a very stable position to rest, and descent uses more energy than you thought it would. You are beggining to regret not getting any water beforehand as your body has become drenched in sweat. You are running out of time and you decide to wrap your trembling arms with vines to make up for your loss of grip while you mull it over. You let out a shout of exasperation as your muscles seem to be unable to support your weight much longer. Down below you hear a reply: “HANG IN THERE”")

if choice3 == "rear":
    print("\nTHE END. CONGRATS ON POTENTIALLY NOT DYING BUT WHO KNOWS. SCORE = 90")
elif choice3 == "record":
    print("\nTHE END. CONGRATS ON FINDING THE BEST SURIVAL OPTION. SCORE = 110")
else:
    print("\nTHE END. CONGRATS ON NOT DYING YET. SCORE = 100")
