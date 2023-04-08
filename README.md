# Hangman
## User Experience
### Site Owner's goals
- To create an entertaining and interactive game of Hangman for user’s to enjoy
- To make it easy for users to interact with the game
- To have a scores system and to enable users to save their high scores
### User's goals
- To easily interact with the game
- To play a fun and entertaining game of Hangman
- To have clear instructions explaining the rules of the game
- To be clearly informed of what any errors are from any invalid inputs
- To view my score after each game
- To save my high scores to a high scores leaderboard
- To have the option to play the game again or quit
## Design
### Flowchart
I made the following flowchart to show the logic of the game from the start to the end, making sure to include any points where validity checks would be needed.

![Flowchart](docs/hangman_flowchart.png)
## Features
## Technologies
## Testing
### Validator Testing
### Testing User Stories
### Manual Testing
## Solved Bugs
## Deployment
### Deploying the Project
- This game was deployed to Heroku. The steps to do this are as follows:
    - Create an account with [Heroku](https://id.heroku.com/login).
    - On the Heroku dashboard, click the button that says "New", then click "Create new app".
    - Choose a unique name for the app.
    - Select your region, then click "Create app".
    -  Click on the "Settings" button on the menu.
    - Scroll down to the section "Config Vars" and click "Reveal Config Vars".
    - Enter CREDS in the field for key and copy and paste the creds.json file into the field for value and then click "Add".
    - Add another Config Var with the key Port and the value 8000.
    - Scroll down to the "Buildpacks" section and click "Add buildpack".
    - Select "python" and then "Save changes".
    - Then click "Add buildpack" again and select "node.js" and "Save changes".
    - Go to the "Deploy" button on the menu at the top.
    - Select GitHub as the deployment method and click the "Connect to GitHub" button.
    - Search for the repository "hangman" and then click "Connect".
    - Scroll to the bottom of the page and either click "Enable Automatic Deploys" in the Automatic deploys section or "Deploy branch" in the Manual deploy section.
### Forking the Project
### Cloning the Project
## Credits