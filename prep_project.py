# decide a name for the social media

# get the user name option for its social media
# have a random list of followers initially set up but be able to add more
# be able to "post" something and save it as a list, if you post multiple things save it to multiple lists
# check your notifications and have a randomly selected one everytime you check (have a list of those notifications)
# be able to "follow" someone and check its followers maybe with random
# be able to check your own followers
# have an option to close the app

random_quotes = ["Often the hardest person to forgive is yourself.", "Fall in love with someone who is both your safe place and your biggest adventure.", "Because things change, and friends leave, and life doesn’t stop for anybody.", "Joy is a decision, a really brave one, about how you’re going to respond to life.", "I hope that you find a sweet balance of self-love and adventure this year.", "Give yourself time.", "Honey, bee happy.", "Be kind to yourself.", "Sometimes the best thing you can do is not think, not wonder, not imagine, not obsess.", "Just breathe and have faith that everything will work out for the best.", "I have the freedom and power to create the life I desire.", "Know your worth. Don't ask for it. State it once and never accept anything less.", "Never forget that walking away from something unhealthy is brave, even if you stumble a little on your way out the door.", "Never feel guilty for choosing yourself."]

def random_quote_generator(random_quotes):
    import random
    random = random.choice(random_quotes)
    
# random.choice(list_notifications(d.values())) #print values from a dict

    print()
    print("Your random quote is:")
    print()
    print(random)
    print()
   

def create_an_account():

        print()
        print("What name would you like to choose? Please type in first and last name.")
        username_option = input("> ")
        username_option = username_option.title()
        print("Awesome! Your new account has the username {}".format(username_option))
        print()

followers_initial = ['Lance Coryell', 'Nia Chambliss', 'Cecily Pines', 'Osvaldo Alley', 'Fidel Stiles', 'Joslyn Mele', 'Nicolasa Steinman', 'Reginald Southern','Marlena Maynard', 'Avelina Behan', 'Otilia Vallee', 'Wallace Holliman', 'Hayden Andreas', 'Shawanna Starkes', 'Yuri Hepler', 'Eddie Smidt', 'Enoch Sly', 'Karima Spade', 'Leo Stevens', 'Nikole Tarvin', 'Lucia Rohe', 'Bernita Manion', 'Lana Rainbolt', 'Louie Wadlington', 'Ursula Boulden', 'Elli Gerace', 'Remedios Fairfax', 'Vashti Hammons', 'Shalanda Merkel']

def check_followers():
    while True:
        print()
        print(f"Looks like you already have {len(followers_initial)} followers.") 
        print()
        print("Would you like to see who's following you?")
        ans = input("> ")
        if ans.startswith("y") or ans.startswith("Y"):
            print()
            print("These are your followers:")
            print(*followers_initial, sep = "\n")
            print()
            break 
        elif ans.startswith("n") or ans.startswith("N"):
            print()
            print("Feel free to check it later")
            return  #make this only happen when you choose to end

posts = []
def make_posts(posts):
    print()
    print("What would you like to post?")
    post = input("> ")
    # new_post= {'content': post, 'date': datetime.now().strftime(%b-%d-%y'), }
    posts.append(post)
    while True:
        print("Would you like to post something else?")
        answer = input("> ")
        if answer.startswith("y") or answer.startswith("Y"):
            print()
            print("What would you like to post?")
            post = input("> ")
            posts.append(post)
        elif answer.startswith("n") or answer.startswith("N"):
            break
        else:
            print("Not a valid option, try again.")

def see_posts(posts):
    if len(posts) == 0:
        print()
        print("You haven't posted anything yet")
        print()
    if len(posts) >= 1:
        print()
        print("This is what you've posted so far:")
        print()
        print(*posts, sep = "\n")
        print()

followers_to_follow = ["Haywood Hoye", "Bernice Kimball", "Lamar Fegley", "Roberta Musto", "Tanesha Carmen", "Antonetta Weidman", "Jaleesa Renn", "Toshia Mccorkle", "Freeda Crumpler", "Yelena Mccree", "Shantel Parent", "Lyda Duque", "Angelica Mejias", "Sharon Chagnon", "Annamarie Gratz", "Garnet Olson", "Leanne Marsch", "Dominga Staudt", "Carlton Barsh", "Xiomara Hughley", "Kiana Swoboda"]

people_to_follow = []

def follow_someone(people_to_follow, followers_to_follow):
    print("Here's a list of users eligible to be followed currently: ")
    print()
    print(*followers_to_follow, sep = "\n")
    print()
    print("Who would you like to follow?")
    print()
    follow = input("> ")
    follow = follow.title()
    if follow in followers_to_follow:
        people_to_follow.append(follow)
        followers_to_follow.remove(follow)
        print()
        print("Great, you followed {}".format(follow))
        print()
    else:
        print("Not a valid option. Try again")

def see_who_u_follow(people_to_follow):
   
    if len(people_to_follow) >= 1:
        print()
        print("This is who you follow so far:")
        print()
        print(*people_to_follow,  sep = "\n")
        print()
        
    if len(people_to_follow) == 0:
        print()
        print("You haven't followed anyone yet.")
        print()
        

def close_account():
    print()
    print("We're sad to see you go but your account has been closed.")

def play_w_account():

    while True:
        print()
        print("What would you like to do today?")
        print("1. View your followers")
        print("2. Follow someone")
        print("3. See who you follow")
        print("4. Make a new post")    
        print("5. See your posts")
        print("6. Generate a random quote")
        print("7. Close your account")
        print()

        choice = input("Option: ")
        if choice == "1":
            check_followers()
        elif choice == "2":
            follow_someone(people_to_follow, followers_to_follow)
        elif choice == "3":
            see_who_u_follow(people_to_follow)
        elif choice == "4":
            make_posts(posts)
        elif choice == "5":
            see_posts(posts)
        elif choice == "6":
            random_quote_generator(random_quotes)
        elif choice == "7":
            close_account()
            break
        else:
            print("Not a valid option. Please type a numerical entry.")

    

def play():
    socialmedia_name = "Luni" 
    socialmedia_emoji = "\U0001F984 "

    print("Welcome to {} {}!".format(socialmedia_name, socialmedia_emoji))
    print("Please create your account.")
    create_an_account()

    play_w_account()
    
play()
 