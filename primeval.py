import random

# --- Skill Effect Functions ---
def crushing_bite(user, target):
    """Deals heavy damage, scaling with the user's attack."""
    damage = user.attack * 1.5
    final_damage = target.take_damage(damage)
    print(f"{user.name} unleashes a Crushing Bite on {target.name} for {int(final_damage)} extra damage!")

def herd_unity(user, target):
    """Temporarily increases the user's defense."""
    print(f"{user.name} uses Herd Unity, increasing its defense for one turn!")
    if 'defense_boost' not in user.status_effects:
        user.defense += 5
    user.status_effects['defense_boost'] = 1

def stealthy_hunt(user, target):
    """Deals a surprise attack with bonus damage."""
    damage = user.attack * 1.25
    final_damage = target.take_damage(damage)
    print(f"{user.name} performs a Stealthy Hunt on {target.name}, dealing a surprise blow for {int(final_damage)} damage!")

def terrifying_roar(user, target):
    """Decreases the target's attack for one turn."""
    print(f"{user.name} lets out a Terrifying Roar, stunning {target.name}!")
    target.attack = max(0, target.attack - 5)
    target.status_effects['attack_debuff'] = 1

def thagomizer_swing(user, target):
    """Hits the target with the tail spikes, causing a severe bleed effect."""
    damage = user.attack * 1.1
    final_damage = target.take_damage(damage)
    target.status_effects['bleed'] = 3 # 3 turns of bleed damage
    print(f"{user.name} swings its Thagomizer, striking {target.name} for {int(final_damage)} damage and causing a nasty bleed!")

def steadfast_defense(user, target):
    """Boosts the user's defense significantly."""
    user.defense += 15
    user.status_effects['defense_boost'] = 2 # Lasts 2 turns
    print(f"{user.name} hunkers down with a Steadfast Defense, its defenses rise!")

def aquatic_ambush(user, target):
    """A swift attack from the water, dealing solid damage."""
    damage = user.attack * 1.3
    final_damage = target.take_damage(damage)
    print(f"{user.name} performs an Aquatic Ambush on {target.name}, dealing {int(final_damage)} damage!")

def razor_claws(user, target):
    """Inflicts a devastating series of cuts with long claws."""
    damage = user.attack * 1.6
    final_damage = target.take_damage(damage)
    target.status_effects['bleed'] = 2
    print(f"{user.name} slashes with its massive claws, inflicting a deep wound on {target.name} for {int(final_damage)} damage and causing them to bleed!")

def sonic_crest(user, target):
    """Releases a startling, loud call that debuffs the enemy."""
    print(f"{user.name} lets out a booming call from its crest, momentarily stunning {target.name}!")
    target.attack = max(0, target.attack - 10)
    target.status_effects['attack_debuff'] = 1

def bone_shatter(user, target):
    """A crushing, blunt-force attack that bypasses some armor."""
    damage = (user.attack * 1.5) + (user.attack * 0.5 * (target.defense / target.base_defense))
    final_damage = target.take_damage(damage)
    print(f"{user.name} delivers a Bone Shatter attack, ignoring some of {target.name}'s defense and dealing {int(final_damage)} damage!")

def quill_barrage(user, target):
    """Launches a barrage of sharp quills at the opponent."""
    damage = user.attack * 0.75
    final_damage = target.take_damage(damage)
    print(f"{user.name} bristles and launches a barrage of quills at {target.name}, dealing {int(final_damage)} damage!")

# --- New Skill Effect Functions ---
def horn_charge(user, target):
    """Triceratops charges with its horn, dealing extra damage and stunning."""
    damage = user.attack * 1.4
    final_damage = target.take_damage(damage)
    target.status_effects['stun'] = 1
    print(f"{user.name} charges with its horn, dealing {int(final_damage)} damage and stunning {target.name}!")

def frill_guard(user, target):
    """Triceratops raises its frill, reducing incoming damage for 2 turns."""
    if 'defense_boost' not in user.status_effects:
        user.defense += 10
    user.status_effects['defense_boost'] = 2
    print(f"{user.name} raises its frill, boosting defense for 2 turns!")

def pack_tactics(user, target):
    """Velociraptor calls its pack, increasing attack for 2 turns."""
    if 'attack_boost' not in user.status_effects:
        user.attack += 8
    user.status_effects['attack_boost'] = 2
    print(f"{user.name} calls its pack, increasing attack for 2 turns!")

def tail_whip(user, target):
    """Stegosaurus whips its tail, lowering enemy defense."""
    if 'defense_debuff' not in target.status_effects:
        target.defense = max(0, target.defense - 8)
    target.status_effects['defense_debuff'] = 2
    print(f"{user.name} whips its tail, lowering {target.name}'s defense!")

def crest_echo(user, target):
    """Parasaurolophus echoes a call, healing itself slightly."""
    heal = 15
    user.health = min(user.max_health, user.health + heal)
    print(f"{user.name} echoes a call, healing {heal} HP!")

def omnivore_swipe(user, target):
    """Deinocheirus swipes with claws, dealing moderate damage."""
    damage = user.attack * 1.2
    final_damage = target.take_damage(damage)
    print(f"{user.name} swipes with claws, dealing {int(final_damage)} damage!")

def scythe_slash(user, target):
    """Therizinosaurus slashes with scythe claws, high crit chance."""
    crit = random.random() < 0.3
    damage = user.attack * (2 if crit else 1.3)
    final_damage = target.take_damage(damage)
    print(f"{user.name} slashes with scythe claws for {int(final_damage)} damage!{' (Critical!)' if crit else ''}")

def tooth_blitz(user, target):
    """Nigersaurus blitzes with teeth, multi-hit attack."""
    hits = random.randint(2, 4)
    total_damage = 0
    for _ in range(hits):
        total_damage += target.take_damage(user.attack * 0.5)
    print(f"{user.name} blitzes with its teeth for {int(total_damage)} total damage over {hits} hits!")

# --- New Dinosaur Skill Functions ---
def armored_bash(user, target):
    """Ankylosaurus bashes with its club tail, high defense and stun."""
    damage = user.attack * 1.3
    final_damage = target.take_damage(damage)
    target.status_effects['stun'] = 1
    print(f"{user.name} bashes with its club tail, dealing {int(final_damage)} damage and stunning {target.name}!")

def shell_shield(user, target):
    """Ankylosaurus shields itself, greatly increasing defense for 2 turns."""
    user.defense += 20
    user.status_effects['defense_boost'] = 2
    print(f"{user.name} shields itself, greatly increasing defense!")

def tail_sweep(user, target):
    """Ankylosaurus sweeps its tail, lowering enemy attack."""
    if 'attack_debuff' not in target.status_effects:
        target.attack = max(0, target.attack - 7)
    target.status_effects['attack_debuff'] = 2
    print(f"{user.name} sweeps its tail, lowering {target.name}'s attack!")

def leap_strike(user, target):
    """Pachycephalosaurus leaps and strikes, chance to stun."""
    damage = user.attack * 1.2
    final_damage = target.take_damage(damage)
    if random.random() < 0.25:
        target.status_effects['stun'] = 1
        print(f"{user.name} leaps and strikes, dealing {int(final_damage)} damage and stunning {target.name}!")
    else:
        print(f"{user.name} leaps and strikes, dealing {int(final_damage)} damage!")

def headbutt(user, target):
    """Pachycephalosaurus headbutts, lowering enemy defense."""
    if 'defense_debuff' not in target.status_effects:
        target.defense = max(0, target.defense - 6)
    target.status_effects['defense_debuff'] = 2
    print(f"{user.name} headbutts, lowering {target.name}'s defense!")

def bone_crush(user, target):
    """Pachycephalosaurus crushes bones, bypassing some defense."""
    damage = user.attack * 1.1 + 8
    final_damage = target.take_damage(damage)
    print(f"{user.name} crushes bones, dealing {int(final_damage)} damage!")

def glide_strike(user, target):
    """Microraptor glides and strikes, chance to dodge next attack."""
    damage = user.attack * 1.1
    final_damage = target.take_damage(damage)
    user.status_effects['dodge'] = 1
    print(f"{user.name} glides and strikes, dealing {int(final_damage)} damage and will dodge next attack!")

def feather_flurry(user, target):
    """Microraptor flurries feathers, lowering enemy accuracy."""
    target.status_effects['accuracy_debuff'] = 2
    print(f"{user.name} flurries feathers, lowering {target.name}'s accuracy!")

def tree_ambush(user, target):
    """Microraptor ambushes from trees, high damage if enemy is stunned."""
    damage = user.attack * (2 if 'stun' in target.status_effects else 1.2)
    final_damage = target.take_damage(damage)
    print(f"{user.name} ambushes from trees, dealing {int(final_damage)} damage!")

# --- Dinosaur Class ---
class Dinosaur:
    """Base class for all dinosaurs."""
    def __init__(self, name, health, attack, defense, species, description):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack = attack
        self.base_attack = attack
        self.defense = defense
        self.base_defense = defense
        self.species = species
        self.description = description
        self.skills = {}
        self.status_effects = {}
        self.can_use_skills = True

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        final_damage = max(0, damage - self.defense)
        self.health -= final_damage
        return final_damage

    def attack_target(self, target):
        # Handle dodge
        if hasattr(target, 'status_effects') and 'dodge' in target.status_effects:
            print(f"{target.name} dodges the attack!")
            del target.status_effects['dodge']
            return 0
        # Handle accuracy debuff
        miss_chance = 0.0
        if 'accuracy_debuff' in self.status_effects:
            miss_chance = 0.3
        if random.random() < miss_chance:
            print(f"{self.name}'s attack misses due to lowered accuracy!")
            return 0
        damage = random.randint(self.attack // 2, self.attack)
        final_damage = target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {int(final_damage)} damage!")
        return final_damage

    def learn_skill(self, skill_type, skill_name, skill_effect):
        """Adds a skill to the dinosaur's known skills."""
        if skill_type not in self.skills:
            self.skills[skill_type] = {}
        self.skills[skill_type][skill_name] = skill_effect

    def use_skill(self, skill_name, target):
        """Uses a learned skill on a target."""
        skill_found = False
        for skill_type, skills in self.skills.items():
            if skill_name in skills:
                skills[skill_name](self, target)
                skill_found = True
                break
        if not skill_found:
            print(f"{self.name} does not know that skill.")

    def apply_status_effects(self):
        """Applies damage and/or effects to itself."""
        if 'bleed' in self.status_effects:
            bleed_damage = 5
            self.health = max(0, self.health - bleed_damage)
            self.status_effects['bleed'] -= 1
            print(f"{self.name} suffers {bleed_damage} bleed damage! ({self.status_effects['bleed']} turns remaining)")
            if self.status_effects['bleed'] <= 0:
                del self.status_effects['bleed']
        # Handle stun
        if 'stun' in self.status_effects:
            print(f"{self.name} is stunned and cannot act this turn!")
            self.status_effects['stun'] -= 1
            if self.status_effects['stun'] <= 0:
                del self.status_effects['stun']
            # Skip rest of turn
            return True
        return False

    def end_turn_cleanup(self):
        """Resets temporary stat boosts/debuffs at the end of a turn."""
        for effect in list(self.status_effects.keys()):
            if effect.endswith('_boost') or effect.endswith('_debuff'):
                self.status_effects[effect] -= 1
                if self.status_effects[effect] <= 0:
                    if effect == 'defense_boost':
                        self.defense = self.base_defense
                    elif effect == 'attack_debuff':
                        self.attack = self.base_attack
                    elif effect == 'attack_boost':
                        self.attack = self.base_attack
                    elif effect == 'defense_debuff':
                        self.defense = self.base_defense
                    del self.status_effects[effect]
            elif effect == 'accuracy_debuff':
                self.status_effects[effect] -= 1
                if self.status_effects[effect] <= 0:
                    del self.status_effects[effect]
            elif effect == 'dodge':
                self.status_effects[effect] -= 1
                if self.status_effects[effect] <= 0:
                    del self.status_effects[effect]
            elif effect == 'stun':
                # handled in apply_status_effects
                continue

# --- Species-Specific Dinosaur Classes (Famous and Obscure) ---
class FamousDinosaur(Dinosaur):
    def __init__(self, name, health, attack, defense, species, description):
        super().__init__(name, health, attack, defense, species, description)
        self.dino_type = 'Famous'

class ObscureDinosaur(Dinosaur):
    def __init__(self, name, health, attack, defense, species, description):
        super().__init__(name, health, attack, defense, species, description)
        self.dino_type = 'Obscure'

class Tyrannosaurus(FamousDinosaur):
    def __init__(self, name):
        super().__init__(name, health=150, attack=30, defense=15, species="Tyrannosaurus", description="The apex predator, a powerful carnivore.")
        self.learn_skill('instinctual', 'Crushing Bite', crushing_bite)
        self.learn_skill('instinctual', 'Terrifying Roar', terrifying_roar)
        self.learn_skill('primordial', 'Bone Shatter', bone_shatter)

class Triceratops(FamousDinosaur):
    def __init__(self, name):
        super().__init__(name, health=200, attack=20, defense=25, species="Triceratops", description="A sturdy herbivore with a powerful horn and frill.")
        self.learn_skill('ancestral', 'Herd Unity', herd_unity)
        self.learn_skill('instinctual', 'Horn Charge', horn_charge)
        self.learn_skill('ancestral', 'Frill Guard', frill_guard)

class Velociraptor(FamousDinosaur):
    def __init__(self, name):
        super().__init__(name, health=80, attack=25, defense=10, species="Velociraptor", description="A swift and intelligent pack hunter.")
        self.learn_skill('adaptive', 'Stealthy Hunt', stealthy_hunt)
        self.learn_skill('instinctual', 'Pack Tactics', pack_tactics)
        self.learn_skill('adaptive', 'Aquatic Ambush', aquatic_ambush)

class Stegosaurus(FamousDinosaur):
    def __init__(self, name):
        super().__init__(name, health=180, attack=22, defense=20, species="Stegosaurus", description="An iconic herbivore with back plates and a spiked tail.")
        self.learn_skill('ancestral', 'Thagomizer Swing', thagomizer_swing)
        self.learn_skill('instinctual', 'Steadfast Defense', steadfast_defense)
        self.learn_skill('ancestral', 'Tail Whip', tail_whip)

class Parasaurolophus(FamousDinosaur):
    def __init__(self, name):
        super().__init__(name, health=160, attack=18, defense=15, species="Parasaurolophus", description="A duck-billed hadrosaur known for its long, curved crest.")
        self.learn_skill('adaptive', 'Sonic Crest', sonic_crest)
        self.learn_skill('ancestral', 'Crest Echo', crest_echo)
        self.learn_skill('adaptive', 'Aquatic Ambush', aquatic_ambush)

# --- New Famous Dinosaur Classes ---
class Ankylosaurus(FamousDinosaur):
    def __init__(self, name):
        super().__init__(name, health=210, attack=18, defense=30, species="Ankylosaurus", description="A heavily armored herbivore with a club tail.")
        self.learn_skill('ancestral', 'Armored Bash', armored_bash)
        self.learn_skill('ancestral', 'Shell Shield', shell_shield)
        self.learn_skill('instinctual', 'Tail Sweep', tail_sweep)

class Pachycephalosaurus(FamousDinosaur):
    def __init__(self, name):
        super().__init__(name, health=110, attack=22, defense=14, species="Pachycephalosaurus", description="A dome-headed dinosaur known for headbutting.")
        self.learn_skill('instinctual', 'Leap Strike', leap_strike)
        self.learn_skill('ancestral', 'Headbutt', headbutt)
        self.learn_skill('primordial', 'Bone Crush', bone_crush)

# --- Obscure Dinosaur Classes ---
class Microraptor(ObscureDinosaur):
    def __init__(self, name):
        super().__init__(name, health=60, attack=16, defense=8, species="Microraptor", description="A small, feathered dinosaur capable of gliding.")
        self.learn_skill('adaptive', 'Glide Strike', glide_strike)
        self.learn_skill('adaptive', 'Feather Flurry', feather_flurry)
        self.learn_skill('instinctual', 'Tree Ambush', tree_ambush)

class Deinocheirus(ObscureDinosaur):
    def __init__(self, name):
        super().__init__(name, health=140, attack=25, defense=20, species="Deinocheirus", description="An unusual giant omnivore with huge claws and a camel-like hump.")
        self.learn_skill('instinctual', 'Razor Claws', razor_claws)
        self.learn_skill('primordial', 'Bone Shatter', bone_shatter)
        self.learn_skill('adaptive', 'Omnivore Swipe', omnivore_swipe)

class Therizinosaurus(ObscureDinosaur):
    def __init__(self, name):
        super().__init__(name, health=150, attack=28, defense=18, species="Therizinosaurus", description="A peculiar, herbivorous theropod with enormous claws.")
        self.learn_skill('instinctual', 'Razor Claws', razor_claws)
        self.learn_skill('primordial', 'Scythe Slash', scythe_slash)
        self.learn_skill('ancestral', 'Steadfast Defense', steadfast_defense)

class Nigersaurus(ObscureDinosaur):
    def __init__(self, name):
        super().__init__(name, health=120, attack=15, defense=12, species="Nigersaurus", description="A small sauropod with a wide, straight-edged muzzle and 500 teeth.")
        self.learn_skill('adaptive', 'Tooth Volley', quill_barrage)
        self.learn_skill('instinctual', 'Tooth Blitz', tooth_blitz)
        self.learn_skill('ancestral', 'Herd Unity', herd_unity)

# --- Game Logic and Interface ---
def story_intro():
    """Prints the game's opening story for the hidden lab setting."""
    print("--- Primeval: Epoch of Claws ---")
    print("You awaken in a hidden genetic research facility, a product of forbidden experiments.")
    print("Alarms blare and containment systems fail around you as a power outage hits the lab.")
    print("Other genetically engineered prehistoric creatures are escaping, and you must too.")
    print("Fight your way through the compromised facility, battling other creatures to prove your dominance and earn your freedom.")
    print("-" * 35)

def intermission():
    """Prints a random story fragment between fights."""
    intermission_messages = [
        "The stench of ozone and ozone fills the air. You pass a containment unit, its glass cracked, and see a strange, glowing liquid seeping out.",
        "You hear a low rumbling sound from deep within the lab. It's not a dinosaur, but something else entirely.",
        "A series of high-pitched screeches echoes down a corridor. You pass a wall covered in fresh claw marks.",
        "You find a discarded tablet on the ground. The last log entry reads: 'Containment breach in Sector C. All personnel advised to evacuate.'",
        "A cool mist drifts out of a ventilation shaft, carrying the strange scent of ancient plants.",
        "You step over a charred console, its screen flickering with static. What could have caused such a powerful surge?",
        "Ahead, a massive steel door lies bent and torn, as if something incredibly powerful forced its way out.",
        "You stumble upon a nest of eggs, some cracked open, others pulsing with strange bioluminescence.",
        "A robotic arm twitches on the floor, its claw still clutching a vial of prehistoric DNA.",
        "You hear distant thunder, but realize it's the footsteps of something massive moving above.",
        "A wall display flickers, showing a map of the facility with several sectors marked 'breached'.",
        "You pass a mural depicting dinosaurs in battle, eerily similar to your own struggle.",
        "A strange fungus grows in the corners, glowing faintly and releasing spores into the air.",
        "You find a journal page: 'The hybridization project is out of control. We must shut it down.'",
        "A security drone buzzes past, its sensors fried, trailing sparks and smoke.",
        "You glimpse a shadowy figure darting between the containment pods—another escapee?",
        "The air grows thick with humidity and the distant roar of ancient beasts.",
    ]
    print("\n" + "-" * 35)
    print(random.choice(intermission_messages))
    print("-" * 35)

def choose_dinosaur():
    """Prompts the player to choose their dinosaur."""
    print("\nChoose your dinosaur:")
    print("Famous Dinosaurs:")
    print("1. Tyrannosaurus (Apex Predator)")
    print("2. Triceratops (Sturdy Herbivore)")
    print("3. Velociraptor (Swift Hunter)")
    print("4. Stegosaurus (Spiked Tail)")
    print("5. Parasaurolophus (Crested Vocalizer)")
    print("6. Ankylosaurus (Armored Tank)")
    print("7. Pachycephalosaurus (Dome-Headed Brawler)")
    print("\nObscure Dinosaurs:")
    print("8. Deinocheirus (Omnivorous Giant)")
    print("9. Therizinosaurus (Scythe-Clawed Herbivore)")
    print("10. Nigersaurus (500-toothed Grazer)")
    print("11. Microraptor (Gliding Predator)")

    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter your Tyrannosaurus' name: ")
        return Tyrannosaurus(name)
    elif choice == '2':
        name = input("Enter your Triceratops' name: ")
        return Triceratops(name)
    elif choice == '3':
        name = input("Enter your Velociraptor's name: ")
        return Velociraptor(name)
    elif choice == '4':
        name = input("Enter your Stegosaurus' name: ")
        return Stegosaurus(name)
    elif choice == '5':
        name = input("Enter your Parasaurolophus' name: ")
        return Parasaurolophus(name)
    elif choice == '6':
        name = input("Enter your Ankylosaurus' name: ")
        return Ankylosaurus(name)
    elif choice == '7':
        name = input("Enter your Pachycephalosaurus' name: ")
        return Pachycephalosaurus(name)
    elif choice == '8':
        name = input("Enter your Deinocheirus' name: ")
        return Deinocheirus(name)
    elif choice == '9':
        name = input("Enter your Therizinosaurus' name: ")
        return Therizinosaurus(name)
    elif choice == '10':
        name = input("Enter your Nigersaurus' name: ")
        return Nigersaurus(name)
    elif choice == '11':
        name = input("Enter your Microraptor's name: ")
        return Microraptor(name)
    else:
        print("Invalid choice. Choosing Tyrannosaurus by default.")
        return Tyrannosaurus("Rexy")

def start_combat(player, enemy):
    """Manages the combat loop between player and enemy."""
    print(f"\n--- A wild {enemy.name} ({enemy.species}) appears! ---")
    while player.is_alive() and enemy.is_alive():
        print(f"\n--- {player.name}'s Turn ---")
        print(f"Your HP: {int(player.health)}/{int(player.max_health)} | {enemy.name}'s HP: {int(enemy.health)}/{int(enemy.max_health)}")

        # Check for stun
        if player.apply_status_effects():
            player.end_turn_cleanup()
        else:
            action = input("Choose your action (attack, skill, info): ").lower()
            if action == "attack":
                player.attack_target(enemy)
            elif action == "skill":
                if not player.skills:
                    print("You have no skills yet!")
                    player.end_turn_cleanup()
                    continue

                print("Available skills:")
                for skill_type, skills in player.skills.items():
                    print(f"[{skill_type.capitalize()}]")
                    for skill_name in skills:
                        print(f" - {skill_name}")

                skill_choice = input("Enter skill name to use: ").strip()
                player.use_skill(skill_choice, enemy)
            elif action == "info":
                print(f"\n--- Player Stats ---")
                print(f"Name: {player.name}")
                print(f"Species: {player.species}")
                print(f"Health: {int(player.health)}/{int(player.max_health)}")
                print(f"Attack: {int(player.attack)}")
                print(f"Defense: {int(player.defense)}")
                print(f"Known Skills: {', '.join(skill for skills in player.skills.values() for skill in skills)}")
                player.end_turn_cleanup()
                continue
            else:
                print("Invalid action.")
                player.end_turn_cleanup()
                continue

            player.apply_status_effects()
            player.end_turn_cleanup()

        if enemy.is_alive():
            print(f"\n--- {enemy.name}'s Turn ---")
            # Check for stun
            if enemy.apply_status_effects():
                enemy.end_turn_cleanup()
            else:
                enemy.attack_target(player)
                enemy.apply_status_effects()
                enemy.end_turn_cleanup()

    if player.is_alive():
        print(f"\n{player.name} has defeated {enemy.name}!")
    else:
        print(f"\n{player.name} has been defeated by {enemy.name}. Game Over.")
        return False
    return True

def main():
    """Main game function to start the adventure."""
    story_intro()
    player_dino = choose_dinosaur()
    print(f"\nYou are a {player_dino.species} named {player_dino.name}. Good luck on your escape!")

    all_dinos = [
        Velociraptor("Snappy"),
        Triceratops("Tricie"),
        Tyrannosaurus("Rexy"),
        Stegosaurus("Spikey"),
        Parasaurolophus("Vocal"),
        Deinocheirus("Dino"),
        Therizinosaurus("Scythe"),
        Nigersaurus("Brushy"),
        Ankylosaurus("Tanky"),
        Pachycephalosaurus("Basher"),
        Microraptor("Glider"),
    ]

    while True:
        enemy = random.choice(all_dinos)
        # Reset stats and health for next encounter
        enemy.health = enemy.max_health
        enemy.attack = enemy.base_attack
        enemy.defense = enemy.base_defense
        enemy.status_effects = {}

        if not start_combat(player_dino, enemy):
            break
        
        intermission()

        choice = input("\nContinue your escape? (yes/no): ").lower()
        if choice != "yes":
            break

    print("\nGame over. Thanks for playing Primeval: Epoch of Claws!")

if __name__ == "__main__":
    main()