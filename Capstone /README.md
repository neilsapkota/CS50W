 CS50W Final Project Capstone-MyPokhara

 Youtube Video Link : https://www.youtube.com/watch?v=L3DeE4tJ0WQ


Introduction

MyPokhara is a community website developed for the residents of Pokhara city. While some features are still under maintenance, this website serves a vital purpose for the people of Pokhara to share their thoughts. It also aids in tourism, as tourists who wish to visit Pokhara can seek information about the city's tourism sites through the Blog Page. The Blog Page allows users to create posts, like posts, comment on posts, edit comments, delete comments, and perform many other actions.

Additionally, the site includes an About Page where the creator of this project (me) describes how the website works. The Home Page provides information about Pokhara, allowing people from other places to learn about the city. There are also Login and Register pages to ensure that only signed-in users can create posts and perform various operations.

 Distinctiveness and Complexity

Content Creation and Sharing:
 Similar to social media platforms, MyPokhara allows users to create and share content through blog posts. This fosters a sense of community and encourages the exchange of ideas and experiences.

Informative Resource:
 The project incorporates aspects of a tourism website by providing informative content about Pokhara. This makes it a valuable resource for visitors and residents alike, helping them explore the city's offerings.

I believe my project satisfies the distinctiveness and complexity requirements because it is unique compared to the other course projects. The projects in the course included:

1. **Search** - A clone of Google Search.
2. **Wiki** - A clone of Wikipedia.
3. **Commerce** - An auction website.
4. **Network** - A clone of Twitter.

MyPokhara is an interactive community site with blogging functions, where users can seek information about Pokhara and share their opinions in the comment section. This project was built using Django with four models on the back-end and JavaScript on the front-end for updating and displaying content, such as editing, deleting comments, and liking posts. The application is also mobile responsive, with each page sizing its elements to fit the width of a mobile device.


By combining these elements, MyPokhara goes beyond the scope of a singular purpose. It creates a space for both sharing stories and discovering information about Pokhara.



Unique Features of MyPokhara

1. **Blogging Functionality**: Users can create, edit, and delete posts, as well as comment on and like posts. This is different from the previous projects, which did not include such comprehensive user-generated content management.
2. **Tourism Information**: The website serves as a resource for tourists, providing information about Pokhara's attractions. This adds a layer of complexity and purpose beyond a simple blogging platform.
3. **Community Engagement**: The site is designed to foster community interaction among Pokhara residents, encouraging them to share their thoughts and experiences.
4. **Responsive Design**: The website is designed to be mobile-friendly, ensuring accessibility across different devices.

Unveiling the Technical Expertise
The project's technical foundation is built on two key technologies: Django and JavaScript. Let's explore how they contribute to MyPokhara's functionality:

Django: The Powerhouse Backend:

 Django serves as the backbone of MyPokhara, handling data storage, retrieval, and manipulation. It efficiently manages the user accounts, blog posts, comments, likes, and other website elements.

JavaScript: Interactive Frontend:

 JavaScript takes care of the user's interactive experience on the front-end.

  It enables features like the like button functionality (updating like counts without reloading the page) and potentially future functionalities like real-time chat.

This combination empowers MyPokhara to deliver a dynamic and user-friendly experience. The seamless interaction between Django's data management and JavaScript's front-end 

responsiveness makes MyPokhara a well-rounded web application.

Responsive Design: A User-Centric Approach

MyPokhara takes user experience a step further by incorporating responsive design principles.

 This ensures that the website adapts its layout to different screen sizes, be it a desktop computer, a tablet, or a mobile phone.
 
  This widens the project's reach and ensures accessibility for a broader audience.

In conclusion, MyPokhara surpasses the boundaries of a typical course project.

 It embraces a community-driven approach, leverages powerful technologies, and prioritizes user experience through responsive design.
 
 These aspects make MyPokhara a commendable effort in web development.



Files and What's Inside Them
-----------------------------------------------------------------------------------------------------------------------------------------------------
 pokhara

 static/static
------------------------------------------------------------------------------------------------------------------------------------
 **like.js**: This JavaScript file handles the front-end functionality related to liking posts.
 
 It sends asynchronous requests to the server to update the like count without reloading the page.
 
 **styles.css**: 
 
 This CSS file contains the styles that define the appearance of the website, ensuring it is visually appealing and consistent.

templates/pokhara
-----------------------------------------------------------------------------------------------------
**about.html**: This template file provides information about how the website works and its purpose.
  
 **blog.html**: This is the main page for blogs, displaying a list of all blog posts.
 
 **index.html**: This is the main homepage for the entire website, offering a general overview of Pokhara and the site's purpose.
 
 **chat.html**: This template file is for the Public Chat Page, where users can engage in real-time conversations.
 
 **marketplace.html**: This template file is for the Marketplace Page, where users can buy and sell items.
 
 **edit.html**: This template file is for editing posts, allowing users to modify their content.
 
 **create.html**: This template file is for creating new blog posts.
 
 **layout.html**: This is the base template for displaying all other templates. It contains the navigation bar and common elements.
 
 **login.html**: This template file is for logging in users.
 
 **register.html**: This template file is for registering new users.
 
 **post.html**: This template file displays individual posts when users click on "View Post."
 
 **user.html**: This template file provides details about the user, including their posts and comments.

admin.py
--------------------------------------------------------------------------------------------------------------------------------
This file registers Django models to be used in the application, allowing them to be managed through the Django admin interface.

models.py
--------------------------------------------------------------------------------------
**User**: An extension of Django's AbstractUser class model, storing user information.

**Posts**: Stores all the information about the posts created by users.

**Comments**: Stores all the information about the comments made on posts.

**Likes**: Stores all the information about the likes on posts.

urls.py
--------------------------------------------------------------------------------
This file contains the application's URLs, mapping them to the appropriate views.

views.py
-------------------------------------------------------------------------------------
This file contains all the views of the application and the form for the Event model.

It handles the logic for rendering templates and processing user input.



 mypokhara

settings.py
-----------------------------------------------------------------------------------------------------------------
This file is generated by Django and contains configuration settings for the project. 

It includes custom timezone settings, email settings, credentials from the .env file, and media storage settings.

urls.py
---------------------------------------------------------------------------
This file contains the project's URLs and settings for serving media files.

 Models

User
--------------------------------------------------------------------------------------------------
An extension of Django's AbstractUser class model.
 
It includes fields for storing user-specific information, such as username, email, and password.

Posts
---------------------------------------------------------------------------------------------
Stores all the information about the posts created by users.

Fields include title, content, timestamp, and a foreign key to the user who created the post.

Comments
------------------------------------------------------------------------------------------------------------------------------------------------
Stores all the information about the comments made on posts.

Fields include content, timestamp, a foreign key to the user who made the comment, and a foreign key to the post the comment is associated with.

Likes
----------------------------------------------------------------------------------------------------------
Stores all the information about the likes on posts.

Fields include a foreign key to the user who liked the post and a foreign key to the post that was liked.

How to Run the Application
----------------------------------------------------------------------------------------------------------------------------------
1. **Install Python**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Create a Virtual Environment**: Navigate to your project directory and create a virtual environment by running:
   ```bash
   python3 -m venv <name_of_virtualenv>
   ```
3. **Activate the Virtual Environment**: Activate the virtual environment. On Windows, run:
   ```bash
   <name_of_virtualenv>\Scripts\activate
   ```
   On macOS/Linux, run:
   ```bash
   source <name_of_virtualenv>/bin/activate
   ```
4. **Install Django**: Install Django within the virtual environment by running:
   ```bash
   pip install django
   ```
5. **Run the Server**: Navigate to your project directory and run the Django development server:
   ```bash
   python manage.py runserver
   ```
6. **Access the Application**: Open a web browser and go to `http://127.0.0.1:8000/` to access the application.

Conclusion
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
MyPokhara is a comprehensive and interactive community website that goes beyond the scope of the course projects by incorporating features such as blogging, tourism information, and community engagement.

The use of Django for the back-end and JavaScript for the front-end, along with a mobile-responsive design, showcases the distinctiveness and complexity of this project.

The site not only serves as a platform for residents to share their thoughts but also acts as a resource for tourists, making it a valuable addition to the community of Pokhara.
