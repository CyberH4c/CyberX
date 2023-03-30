import instaloader

# Create an instance of the Instaloader class
L = instaloader.Instaloader()

# Prompt the user to enter the username of the account to retrieve information for
username = input("Enter the username of the Instagram account to retrieve information for: ")

# Retrieve the profile of the specified account
profile = instaloader.Profile.from_username(L.context, username)

# Print the basic information about the profile
print("Username:", profile.username)
print("Full Name:", profile.full_name)
print("Bio:", profile.biography)
print("Profile Picture URL:", profile.profile_pic_url)
print("Number of Posts:", profile.mediacount)
print("Number of Followers:", profile.followers)
print("Number of Following:", profile.followees)
