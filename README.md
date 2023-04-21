# LatestYoutubeSubsciptionVideos

To use the Python script to check your subscriptions on YouTube and get a list with links to YouTube of every single one of your subscriptions' latest uploads with dates and times of upload next to the link, follow these steps:

Set up API credentials in the Google API Console
Go to the Google API Console (https://console.developers.google.com/).
Create a new project and enable the YouTube Data API v3.
Create API credentials for a new OAuth client ID.
Download the client secret JSON file and store it in a safe place.
Install the Google API client library for Python
Open your terminal or command prompt.
Run the command pip install google-api-python-client to install the library.
Clone the repository or create a new project
Clone the repository containing the Python script or create a new project.
Copy the Python script into your project directory.
Set up the Python environment
Open your terminal or command prompt.
Navigate to the project directory.
Create a virtual environment by running the command python -m venv env.
Activate the virtual environment by running the command source env/bin/activate (Mac/Linux) or env\Scripts\activate (Windows).
Install the required packages by running the command pip install -r requirements.txt.
Update the script with your API credentials
Open the Python script.
Replace path/to/client_secret.json with the actual path to your client secret JSON file.
Run the Python script
In your terminal or command prompt, run the command python youtube_subscriptions.py.
The script will write the list of latest videos to a file named latest_videos.txt in the same directory as the script.
The message "Latest videos from your subscriptions have been saved to latest_videos.txt." will be printed to the console when the script is done.
Check the output
Open the latest_videos.txt file to view the list of latest videos from your subscriptions with links to YouTube and dates and times of upload next to the link.
That's it! You have successfully used the Python script to check your subscriptions on YouTube and get a list of the latest videos from your subscriptions with links to YouTube and dates and times of upload next to the link.
