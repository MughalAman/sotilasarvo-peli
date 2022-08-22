import random
import os

rank_template = """
|---|
| A |
| B |
| C |
|___| 
"""

aliupseerioppilas = """
|---|
|   |
|   |
|===|
|___| 
"""

prikaatti_kenraali = """
|---|
| L |
| L |
| L |
| L |
|___| 
"""

ranks = ["sotamies", "aliupseerioppilas", "korpraali", "alikersantti", "upseerioppilas", "kersantti", "upseerikokelas", "ylikersantti", "v\u00E4\u00E4peli", "yliv\u00E4\u00E4peli", "sotilasmestari", "v\u00E4nrikki", "luutnantti", "yliluutnantti", "kapteeni", "majuri", "everstiluutnantti", "eversti", "prikaattikenraali", "kenraalimajuri", "kenraaliluutnantti","kenraali"]
def get_rank():
    return random.randint(0, 21)

def start_game():
    os.system('cls||clear')
    score = 0

    while True:
        rank = get_rank()
        print(f"pisteet: {score}")
        print("Arvaa sotilasarvo!")
        if rank == 0:
            print(rank_template.replace("A"," ").replace("B"," ").replace("C"," "))
        elif rank == 1:
            print(aliupseerioppilas)
        elif rank == 2:
            print(rank_template.replace("A"," ").replace("B","^").replace("C"," "))
        elif rank == 3:
            print(rank_template.replace("A"," ").replace("B","^").replace("C","^"))
        elif rank == 4:
            print(rank_template.replace("A"," ").replace("B","\u2666").replace("C"," "))
        elif rank == 5:
            print(rank_template.replace("A","^").replace("B","^").replace("C","^"))
        elif rank == 6:
            print(rank_template.replace("A"," ").replace("B","\u2666").replace("C","\u2666"))
        elif rank == 7:
            print(prikaatti_kenraali.replace("L","^"))
        elif rank == 8:
            print(rank_template.replace("A"," ").replace("B","\u25B2").replace("C"," "))
        elif rank == 9:
            print(rank_template.replace("A"," ").replace("B","\u25B2").replace("C","^"))
        elif rank == 10:
            print(rank_template.replace("A","\u25B2").replace("B","^").replace("C","^"))
        elif rank == 11:
            print(rank_template.replace("A"," ").replace("B","o").replace("C"," "))
        elif rank == 12:
            print(rank_template.replace("A"," ").replace("B","o").replace("C","o"))
        elif rank == 13:
            print(rank_template.replace("A","o").replace("B","|").replace("C","o"))
        elif rank == 14:
            print(rank_template.replace("A","o").replace("B","o").replace("C","o"))
        elif rank == 15:
            print(rank_template.replace("A"," ").replace("B","O").replace("C"," "))
        elif rank == 16:
            print(rank_template.replace("A"," ").replace("B","O").replace("C","O"))
        elif rank == 17:
            print(rank_template.replace("A","O").replace("B","O").replace("C","O"))
        elif rank == 18:
            print(rank_template.replace("A"," ").replace("B","\U0001F981").replace("C"," "))
        elif rank == 19:
            print(rank_template.replace("A"," ").replace("B","\U0001F981").replace("C","\U0001F981"))
        elif rank == 20:
            print(rank_template.replace("A","\U0001F981").replace("B","\U0001F981").replace("C","\U0001F981"))
        elif rank == 21:
            print(prikaatti_kenraali.replace("L","\U0001F981"))

        answer = input("Sotilasarvo: ")
        if answer.lower() == ranks[rank].lower():
            score += 1
            if random.randint(0,5) == 0:
                print("Haluatko arvata alempaa tai ylempää sotilasarvoa? (y/n)")
                if input().lower() == "y":
                    if random.randint(0,1) == 0:
                        print(f"Anna {rank} alempi sotilasarvo")
                        if input("Sotilasarvo: ").lower() == ranks[rank-1].lower():
                            score += 10
                        else:
                            print(f"H\u00E4visit! Sotilasarvo oli {ranks[rank-1]}. Pisteesi: {score}")
                            break
                    else:
                        print(f"Anna {rank} ylempi sotilasarvo")
                        if input("Sotilasarvo: ").lower() == ranks[rank+1].lower():
                            score += 10
                        else:
                            print(f"H\u00E4visit! Sotilasarvo oli {ranks[rank+1]}. Pisteesi: {score}")
                            break
                else:
                    continue
                
            os.system('cls||clear')
        else:
            print(f"H\u00E4visit! Sotilasarvo oli {ranks[rank]}. Pisteesi: {score}")
            break

if __name__ == "__main__":
    start_game()
