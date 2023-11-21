############################################################
# Name:Raj Rana,Joshua Levandoske,Surbhi Mehta
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
# CS115 MusicRecPlus Group Project
#
############################################################
import os

def load_database(filename):
    """Loads the database by accessing a variable(filename) as a .txt document(Made by Joshua)"""
    database = {}
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    [user, artists] = line.strip().split(':')
                    singersList = artists.split(",")
                    database[user] =singersList
        except Exception as e:
            print(f"Error loading database: {e}")
    return database

def save_database(filename, database):
    """Adds to the database by accessing .txt document (filename) and adding the list (database) to it.(Made by Joshua)"""
    try:
        with open(filename, 'w') as file:
            for user, artists in sorted(database.items()):
                file.write(f"{user}:{','.join(artists)}\n")
        print("Thank you for using MusicRecPlus! Exiting program...")
    except Exception as e:
        print(f"Error saving database: {e}")

def get_user_preferences():
    """Asks the user for their preferences and stores them in the database.(Made by Joshua)"""
    artists=[]
    pref=input("Enter your favorite artists(Click enter to finish): ")
    artists += [pref.strip().title()]
    x=True
    while x:
        artists_input = input("Enter your favorite artists(Click enter to finish): ")
        if artists_input=="":
            break
        artists+=[artists_input.strip()]
    return sorted(artists)

def matches(database,sign_in,other_user):
    """Counts the number of matches a users database has with others(Made by Raj)"""
    count=0
    for pref in database[sign_in]:
        if pref in database[other_user]:
            count+=1
    return count

def find_best_user(sign_in,database):
    """Finds the user with the most similar preferences to the target user (sign_in).(Made by Raj)"""
    best_user=''
    match=0
    h=filter_base(database)[0]
    for i in h:
        if i!=sign_in:
            cur_match=matches(database,sign_in,i)
            if(all(x in database[sign_in] for x in database[i])):
                continue
            if cur_match > match:
                best_user = i
                match = cur_match
    return best_user
        
def filter_base(database):
    """Takes any users who have been set to private mode out of the database for certain functions.(Made by Raj)"""
    new_dataBase=dict(database)
    temp_list=list(database.keys())
    for user in temp_list:
        if user[-1]=="$":
            del new_dataBase[user]
    return new_dataBase,temp_list        
            
def get_users_rec(sign_in,database):
    """Finds the user’s (sign_in) recommendations.(Made by Raj)"""
    recs=[]
    best_user=database[find_best_user(sign_in,database)]
    for i in best_user:
        if i not in database[sign_in]:
            recs.append(i)
    if len(recs)>0:
        print("Here are your recommendations:")
        for i in recs[0:3]:
            print(i.strip())
    else:
        print("No recommendations at this time. :(")

def all_artist(database):
    """Creates a list of all users prefrences combined together(Made by Raj)"""
    base=filter_base(database)[0]
    artist=[]
    for i in base:
        for pref in database[i]:
            artist.append(pref)
    return (artist)

def artist_popularity(database):
    """Itterates through all arist and returns the amount of users that have a prefrence of that artist.(Made by Raj)"""
    matches={}
    artist_list=all_artist(database)
    for artist in artist_list:
        if artist in matches:
            matches[artist]=matches[artist]+1
        else:
            matches[artist]=1
    return matches

def most_popArtist(database):
    """Lists the top three most popular artists(Made by Raj)"""
    popularity=artist_popularity(database)
    if max(popularity,key=popularity.get)==min(popularity,key=popularity.get):
        print("Here are the most popular artist:")
        for i in range(0,3):
            k=max(popularity,key=popularity.get)
            print(k.strip())
            del popularity[k]
    else:
        if max(popularity,key=popularity.get)==min(popularity,key=popularity.get):
            print("Sorry , no artists found .")
        else:
            print("Here are the most popular artist:")
            for i in range(0,3):
                k=max(popularity,key=popularity.get)
                if k==min(popularity,key=popularity.get):
                    break
                print(k.strip())
                del popularity[k]
    
def how_popular(database):
    """Calculates the amount of likes a given artist has.(Made by Surbhi)"""
    popularity=artist_popularity(database)
    k=max(popularity,key=popularity.get)
    print("The most popular artist has this many listeners: ")
    print(popularity[k])

def most_likeUser(database):
    """Finds the user with the most likes within database(Made by Surbhi)"""
    base=filter_base(database)[0]
    biggest_liker=[]
    likes=0
    for i in base:
        if len(base[i])==likes:
            biggest_liker+=[i]
            likes = len(base[i])
        elif len(base[i])>likes:
            biggest_liker=[]
            biggest_liker+=[i]
            likes = len(base[i])
    if len(biggest_liker)==0:
        print("Sorry , no user found .")
    else:
        print("Here are the users with the most likes:")
        for user in biggest_liker:
            print(user)

def delete_user_preferences(database,sign_in):
    """Asks the user which preferences to delete and deletes them(Made by Raj and Joshua)"""
    print("Here is a list of your current preferences: ")
    for i in database[sign_in]:
        print(i.strip())
    delet = input("Which artist to delete from preferences(Press enter to end): ")
    delete = delet.strip()
    if delete in database[sign_in]:
        database[sign_in].remove(delete)
        print(delete," has been removed from your prefrences.")
    else:
         print("Sorry, that artist is not in your preferences.")
def current_pref(database,sign_in):
    print("Here are your current preferences: ")
    for i in database[sign_in]:
        print(i.strip())
def print_menu():
    """Prints the menu(Made by Joshua)"""
    print("Enter a letter to choose an option:")
    print("e - Enter preferences")
    print("r - Get recommendations")
    print("p - Show most popular artists")
    print("h - How popular is the most popular")
    print("m - Which user has the most likes")
    print("s -Prints current preferences")
    print("d -Delete preferences")
    print("q - Save and quit")

def main():
    """Executes the main function of the music recommendation system by starting with
    Asking the name of the user and displaying the menu after they list their preferences((Made by Raj,Joshua, and Surbhi).
    """
    filename = "musicrecplus.txt"
    database = load_database(filename)
    
    sign_in = input("Enter your name ( put a $ symbol after your name if you wish your preferences to remain private ):")
    if sign_in not in database:
        print("Welcome, new user!")
        is_private = sign_in.endswith('$')
        preferences = get_user_preferences()
        database[sign_in] = preferences
        print("Preferences saved!")
    while True:
        print()
        print_menu()
        choice = input().lower()
        print()
        if choice == 'e':
            database[sign_in] += get_user_preferences()
            print("Preferences saved!")
        elif choice == 'r':
            if len(database)==1:
                print("No recommendations at this time. :(")
            else:
                get_users_rec(sign_in,database)
        elif choice == 'p':
            most_popArtist(database)
        elif choice == 'h':
            how_popular(database)
            pass
        elif choice == 'm':
            most_likeUser(database)
        elif choice == 'd':
            delete_user_preferences(database,sign_in)
        elif choice == 's':
            current_pref(database,sign_in)
        elif choice == 'q':
            save_database(filename, database)
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

