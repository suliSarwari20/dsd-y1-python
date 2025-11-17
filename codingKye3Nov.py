
favouritesongs = ["thick of it"]

def add_song(song):
    favouritesongs.append(song)
    print(f'"{song}" has been added to your favourite songs.')

def remove_song(song):
    if song in favouritesongs:
        favouritesongs.remove(song)
        print(f'"{song}" has been removed from your favourite songs.')
    else:
        print(f'"{song}" is not in your favourite songs list.')

action = input("Would you like to add or remove a song? (add/remove): ").strip().lower()

if action == "add":
    new_song = input("Enter the song you want to add: ")
    add_song(new_song)
elif action == "remove":
    song_to_remove = input("Enter the song you want to remove: ")
    remove_song(song_to_remove)
else:
    print("Invalid choice. Please type 'add' or 'remove'.")

print("Your favourite songs are now:", favouritesongs)
