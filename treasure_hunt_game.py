# 🏰 TREASURE HUNT ADVENTURE GAME
# Internship Task 1
# 👨‍💻 Developed by: Satvik Sharma

import random
print("""
========================================
🏰 TREASURE HUNT ADVENTURE GAME
========================================
""")
name = input("👤 Enter your name: ")
health = 100
gold = 0
print(f"\n🎉 Welcome {name}!")
print("⚔️ Your adventure begins...\n")
while health > 0:
    print("""
========================================
🎮 CHOOSE YOUR ACTION
1️⃣  Explore Forest 🌲
2️⃣  Enter Cave 🕳️
3️⃣  View Status 📊
4️⃣  Exit Game 🚪
========================================
""")
    choice = input("👉 Enter choice: ")

    # 🌲 FOREST EVENT
    if choice == "1":
        event = random.choice(["treasure", "enemy"])
        if event == "treasure":
            reward = random.randint(10, 50)
            gold += reward
            print(f"\n💎 You found treasure worth {reward} gold!\n")
        else:
            damage = random.randint(5, 20)
            health -= damage
            print(f"\n👹 Enemy attacked!")
            print(f"💔 You lost {damage} health.\n")

    # 🕳️ CAVE EVENT
    elif choice == "2":
        print("\n🕳️ You entered a dark cave...")
        event = random.choice(["monster", "magic"])
        if event == "monster":
            damage = random.randint(15, 30)
            health -= damage
            print(f"🐉 A monster attacked!")
            print(f"💔 You lost {damage} health.\n")
        else:
            heal = random.randint(10, 25)
            health += heal
            print(f"✨ Magic potion found!")
            print(f"❤️ You gained {heal} health.\n")
 
    # 📊 STATUS
    elif choice == "3":
        print(f"""
========================================
📊 PLAYER STATUS
👤 Name   : {name}
❤️ Health : {health}
💎 Gold   : {gold}
========================================
""")

    # 🚪 EXIT GAME
    elif choice == "4":
        print("\n👋 Exiting game...")
        break
 
    # ❌ INVALID INPUT
    else:
        print("\n❌ Invalid choice. Try again.\n")
 
    # 🏆 WIN CONDITION
    if gold >= 100:
        print(f"""
========================================
🏆 CONGRATULATIONS {name}!
💎 You collected 100 gold
🎉 YOU WON THE GAME!
========================================
""")
        break
 
    # ☠️ LOSE CONDITION
    if health <= 0:
        print(f"""
========================================
☠️ GAME OVER {name}
💔 You lost all your health.
========================================
""")