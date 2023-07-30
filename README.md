# TopTechScore

TopTechScore is a ranking application for AI focused websites. It is built using Django for the backend and React for the frontend.

## Setup and Installation

### Backend
Navigate to the `backend` directory. 
Install the dependencies by running `pip install -r requirements.txt`.

Start the server by running `python manage.py runserver`.

### Frontend
Navigate to the `frontend` directory. 
Install the dependencies by running `npm install`.

Start the server by running `npm start`.

## Usage

### Backend
The backend is a Django REST API. You can access it at `http://localhost:8000/api/tools/`.

### Frontend
The frontend is a React application. You can access it at `http://localhost:3000`.

## Contributing

Contributions are welcome. Please fork the repository and create a pull request with your changes.

## License

This project is privately owned. Unauthorized copying of this file, via any medium is strictly prohibited. Proprietary and confidential.

### Deployment Instructions

Backend
1. Local Backend Environment

Make the necessary changes to your Django application on your local machine and test it thoroughly.

bash
Copy code
# Switch to the branch
git checkout main

# Pull the latest changes
git pull origin main
2. Push to Staging

bash
Copy code
# Switch to the branch
git checkout staging

# Merge changes from main
git merge main

# Push to staging
git push origin staging
This will trigger your CI pipeline. If all tests pass, it will deploy your changes to your Heroku staging environment.

3. Test on Staging

Check your staging environment thoroughly, including both automated tests and manual testing.

4. Push to Production

Once all tests pass and you're satisfied with your changes on staging, you can merge your changes to the main branch and push them. This will trigger your CI pipeline and, assuming all tests pass, deploy your changes to your Heroku production environment.

bash
Copy code
# Switch to the main branch
git checkout main

# Merge changes from staging
git merge staging

# Push to main
git push origin main
Frontend
1. Local Frontend Environment

Similarly to the backend, make the necessary changes to your React application on your local machine and test it thoroughly.

bash
Copy code
# Switch to the branch
git checkout main

# Pull the latest changes
git pull origin main
2. Push to Staging

bash
Copy code
# Switch to the branch
git checkout staging

# Merge changes from main
git merge main

# Push to staging
git push origin staging
This will trigger your CI pipeline. If all tests pass, it will deploy your changes to your Netlify staging environment.

3. Test on Staging

Check your staging environment thoroughly, including both automated tests and manual testing.

4. Push to Production

Once all tests pass and you're satisfied with your changes on staging, you can merge your changes to the main branch and push them. This will trigger your CI pipeline and, assuming all tests pass, deploy your changes to your Netlify production environment.

bash
Copy code
# Switch to the main branch
git checkout main

# Merge changes from staging
git merge staging

# Push to main
git push origin main
By keeping your frontend and backend processes separate, you'll have more granular control over the deployment process. You can deploy changes to your frontend or backend independently, and it also makes it easier to diagnose and fix issues that might come up during the process.

Remember, the specifics of these steps can vary slightly depending on your project, the technologies you're using, and your specific development workflow. But overall, this should give you a solid foundation for deploying your application in a systematic and reliable way.