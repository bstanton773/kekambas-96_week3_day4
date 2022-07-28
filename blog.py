class Blog:
    def __init__(self):
        self.users = set()
        self.posts = []
        self.current_user = None
        
    # Method to add new users to the blog
    def create_new_user(self):
        # Get user info from input
        username = input('Please enter a username: ')
        # Check if there is already a user with username
        if username in {u.username for u in self.users}:
            print(f"User with username {username} already exists")
        else:
            password = input('Please enter a password: ')
            # Create a new User instance with info from input
            new_user = User(username, password)
            # Add user instance to the list of blog users
            self.users.add(new_user)
            print(f"{new_user} has been created!")
    
    # Method to log a user in
    def log_user_in(self):
        # Get user credentials
        username = input("What is your username? ")
        password = input("What is your password? ")
        for user in self.users:
            # Check if that user has the same username and password as the inputs
            if user.username == username and user.check_password(password):
                # If user has correct credentials, set the blog's current user to that user instance
                self.current_user = user
                print(f"{user} has been logged in")
                break
        # If no users in our blog user list have correct username/password, let them know
        else:
            print('Username and/or password is incorrect')
            
    # Method to log a user out
    def log_user_out(self):
        # Change the current_user attribute from the user to None
        self.current_user = None
        print('You have successfully logged out')
        
    # Method to create and add post to blog
    def create_post(self):
        # Check to make sure the user trying to create a post is logged in
        if self.current_user is not None:
            # Get title and body from user input
            title = input('Enter the title of your post: ').title()
            body = input('Enter the body of your post: ')
            # Create a new Post instance with user input
            new_post = Post(title, body, self.current_user)
            # Add the post object to the blog's list of posts
            self.posts.append(new_post)
            print(f"{new_post.title} has been created")
        else:
            print('You must be logged in to perform this action')
            
    # Method to view all posts
    def view_posts(self):
        if self.posts:
            for post in self.posts:
                print(post)
        else:
            print("There are currently no posts for this blog :(")


class User:
    id_counter = 1 # Class attribute keeping track of User IDs
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.id = User.id_counter
        User.id_counter += 1
        
    def __str__(self):
        return self.username
    
    def __repr__(self):
        return f"<User {self.id}|{self.username}>"
    
    def check_password(self, password_guess):
        return self.password == password_guess


class Post:
    
    id_counter = 1
    
    def __init__(self, title, body, author):
        """
        title: Str
        body: Str
        author: User
        """
        self.title = title
        self.body = body
        self.author = author
        self.id = Post.id_counter
        Post.id_counter += 1
        
    def __str__(self):
        formatted_post = f"""
        {self.id} - {self.title.title()}
        By: {self.author}
        {self.body}
        """
        return formatted_post
    
    def __repr__(self):
        return f"<Post {self.id}|{self.title}>"


# Define function to run blog
def run_blog():
    # Create an instance of the blog
    my_blog = Blog()
    # Keep looping while blog is 'running'
    while True:
        # if there is no current user logged in
        if my_blog.current_user is None:
            print("1. Sign Up\n2. Log In\n3. View All Posts\n5. Quit")
            to_do = input('Which option would you like to do? ')
            while to_do not in {'1', '5', '2', '3'}:
                to_do = input('Not valid. Please choose 1, 2, 3, or 5')
            # clear_output()
            if to_do == '5':
                print('Thanks for checking out our blog')
                break
            elif to_do == '1':
                # method to create new user
                my_blog.create_new_user()
            elif to_do == '2':
                # method to log user in
                my_blog.log_user_in()
            elif to_do == '3':
                # method to view all posts
                my_blog.view_posts()
        # If there is a current user (aka a logged in user)
        else:
            print("1. Log Out\n2. Create New Post\n3. View All Posts")
            to_do = input('Which option would you like to do? ')
            while to_do not in {'1', '2', '3'}:
                to_do = input('Not valid. Please choose 1, 2, 3')
            # clear_output()
            if to_do == '1':
                # method to log user out
                my_blog.log_user_out()
            elif to_do == '2':
                # method to create a new post
                my_blog.create_post()
            elif to_do == '3':
                # method to view all posts
                my_blog.view_posts()
            
            
            
# Execute the function
run_blog()