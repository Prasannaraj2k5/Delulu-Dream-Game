import sys
sys.stdout.reconfigure(encoding='utf-8')

MAX_ATTEMPTS = 5  # Limit number of portal choices
attempts = 0

delulu_meter = 0  # Tracks how delulu the player becomes

print("🌙✨ Welcome to the *Delulu World* ✨🌙")
print("You have fallen into a surreal dimension between the stars and your subconscious.")
print("Your soul floats gently... where will your dream take you?")
name = input("What’s your dreamy name, 🌸: ")
print(f"\nHello {name}, your soul has slipped between stars and thoughts...")

paths_done = set()

while attempts < MAX_ATTEMPTS:
    print("\n🌌 A glowing portal appears in front of you. What do you follow?")
    print("1. 🌕 The Moonlight Path (mystic & calm)")
    print("2. 🕯️ The Candlelit Corridor (soft but strange)")
    print("3. 🌀 The Glitch in Reality (chaotic delulu energy)")
    print("4. 🌊 The Ocean of Echoes (deep, dreamy, mysterious)")
    print("5. 🧩 The Puzzle Paradox (logic-bending and weird)")
    print("🌈 Or... try something mysterious? (Hint:wonders of world)")

    choice = input("Choose 1-5 or a hidden number (or type 'exit' to finish): ")

    if choice == "exit":
        break
    elif choice in paths_done:
        print("🚫 You’ve already wandered this path. Try a new one!")
        continue
    else:
        paths_done.add(choice)
        attempts += 1

    # ------------------ Moonlight Path ------------------
    if choice == "1":
        print("\nYou walk into a moonlit garden. A deer with constellations in its eyes bows to you.")
        print("‘Only the dreamer can awaken the dream,’ it whispers.")
        print("Do you:")
        print("1. Follow the deer deeper into the glowing forest")
        print("2. Lie under the moon and enter meditation")

        moon_path = input("Choose 1 or 2: ")

        if moon_path == "1":
            delulu_meter += 20
            print("🌿 You become stardust incarnate. You’re now a moon spirit roaming the dreamscape. 🐚🌙")
        elif moon_path == "2":
            delulu_meter += 10
            print("🧘‍♀️ You find divine peace. You wake up in real life... but your aura glows softly forever.")
        else:
            print("🌫️ The moon fades. You drift endlessly in a beautiful nothing.")

    # ------------------ Candlelit Corridor ------------------
    elif choice == "2":
        print("\nYou find yourself in a velvet-lit room with floating books and whispering candles.")
        print("A mirror shows all your past lives dancing in a spiral.")
        print("‘Do you want to remember… or forget?’")
        print("1. Remember everything")
        print("2. Forget and float freely")

        candle_path = input("Choose 1 or 2: ")

        if candle_path == "1":
            delulu_meter += 20
            print("📖 You recall every delulu version of yourself: queen, time-traveler, frog. You become a dream witch. 🔮")
        elif candle_path == "2":
            delulu_meter += 10
            print("🌬️ You float into peaceful non-memory. A soft existence. You become wind with eyeliner.")
        else:
            print("🕯️ You get stuck between memory and forgetting. You become... aesthetic static.")

    # ------------------ Glitch in Reality ------------------
    elif choice == "3":
        print("\nYou tumble through a glitch tunnel: neon clouds, TikTok trends, and random frogs fly by.")
        print("‘404: Reality Not Found.’ Do you:")
        print("1. Dance with the chaos")
        print("2. Attempt to reboot the dream")

        glitch_path = input("Choose 1 or 2: ")

        if glitch_path == "1":
            delulu_meter += 20
            print("🪩 You become the MC in every universe. You speak only in captions now. 💅💻")
        elif glitch_path == "2":
            delulu_meter += 10
            print("🔁 You reboot… but now the dream is recursive. You’re in an infinite vibe loop.")
        else:
            print("🌀 You transform into a broken GIF and become internet legend.")

    # ------------------ Ocean of Echoes ------------------
    elif choice == "4":
        print("\nYou dive into a shimmering ocean where whispers echo like lullabies.")
        print("A mermaid with glowing hair offers you a conch shell.")
        print("Do you:")
        print("1. Listen to the conch")
        print("2. Follow the mermaid to the coral castle")

        ocean_path = input("Choose 1 or 2: ")

        if ocean_path == "1":
            delulu_meter += 10
            print("🐚 You hear your future in song. You become a dream oracle, half-human, half-melody.")
        elif ocean_path == "2":
            delulu_meter += 15
            print("🧜 You become the ruler of the lucid reef, crowned in coral and secrets.")
        else:
            print("🌊 The tide takes you into unknown depths. Beautiful, but lost.")

    # ------------------ Puzzle Paradox ------------------
    elif choice == "5":
        print("\nYou fall into a world made of cubes and riddles, where time loops and clocks run backward.")
        print("An AI in a mirror mask asks: ‘What is more real: logic or illusion?’")
        print("1. Trust logic and solve the paradox")
        print("2. Embrace the illusion and rewrite the rules")

        puzzle_path = input("Choose 1 or 2: ")

        if puzzle_path == "1":
            delulu_meter += 9
            print("🧠 You escape the paradox but remain... logical. Too logical. You’re now a dream nerd.")
        elif puzzle_path == "2":
            delulu_meter += 19
            print("♾️ You bend reality. You’re a dream hacker now, breaking boundaries for fun.")
        else:
            print("🧩 You dissolve into an unsolved puzzle. Forever intriguing.")

    # ------------------ Secret Bonus Path ------------------
    elif choice == "7":
        delulu_meter += 25
        print("\n🌈✨ You unlocked a hidden realm: *The Aesthetic Archive* ✨🌈")
        print("Here lie every version of you imagined by Tumblr, Pinterest, and daydreams.")
        print("You wear every outfit you’ve ever moodboarded. Even the ones you denied wanting.")
        print("The archive glows. You become a digital deity. You are now… legendary.")

    # ------------------ Invalid Choice ------------------
    else:
        print("🌠 You hesitated. The dream faded. But the vibe lives on…")

# ------------------ Ending Section ------------------
print("\n🌟 Your Delulu Meter Score:", delulu_meter, "/ 100")

if delulu_meter >= 90:
    print("👑 Delulu Supreme Overlord – Reality bows to your vibes.")
elif delulu_meter >= 70:
    print("✨ Transcendent Dreamwalker – You manifest universes.")
elif delulu_meter >= 50:
    print("🌟 Main Character Maxed – You radiate plot armor.")
elif delulu_meter >= 30:
    print("💫 Dreamcore Royalty – Keep floating, stargirl.")
elif delulu_meter >= 10:
    print("🫧 Softcore delulu – You're glowing gently. Almost there.")
else:
    print("☁️ You’re still grounded... maybe too grounded. Try again, dream bean.")

print("\n🔁 Replay another day to wander deeper into the Delulu World ✨")

input("\n🎮 Press Enter to exit the dream... 🌙")