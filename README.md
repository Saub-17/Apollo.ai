# Apollo.ai
A generative AI platform for generating poetry and semantic analysis for Vurbalize

(P.S. I could only deploy the front end part of my website, not the backend, because of the AWS free version's file size limit. The backend is working fine on localhost, but could not be deployed on AWS as mentioned earlier.)

Here is a working demo video of me running the website smoothly on localhost:

https://drive.google.com/drive/u/0/folders/1IafnRrZnJc7bql4ay3f3t-Zi5IEq8StI

Instructions to deploy the website on localhost:

Deploying backend:

Step 1 : Open the folder path: Apollo/backend on a powershell terminal (preferrably VSCode)
Step 2 : run the command: python .\apolloBot.py

Deploying frontend:

Step 1 : Open the folder : Apollo on a different powershell terminal (VSCode)
Step 2 : run the command : npm install (for instaaling all Node packages necessary for frontend deployment)
Step 3 : run the command : npm run start:frontend

The website is now deployed on localhost with a proper working flask backend.
(Note: if any libraries are not recognized by the editor, run the commands:
 pip install {library_name} on terminal
 so that the necessary libraries are installed in the path.)
