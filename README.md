# Website Evaluation Platform

The Website Evaluation Platform is a Django-based web application that utilizes machine learning to analyze user reviews and calculate website ratings based on those reviews. 

## Features
- User Registration and Authentication: Users can register and authenticate to access the platform. `complete`
- Submitting Reviews: Users can submit reviews for different websites. `complete`
- ML-based Rating Calculation: The platform employs machine learning techniques to analyze user reviews and calculate website ratings. `complete`
- Website Listing: The platform displays a list of websites along with their ratings and other relevant information. `complete`
- Admin Panel: An admin panel is provided to manage users, reviews, and websites. `complete`

## Installation and Setup
1. Clone the repository:

```shell
git clone git@github.com:theabdullahalam/ml-website-evaluation.git
```

2. Navigate to the project directory:
```shell
cd ml-website-evaluation
```

3. Create and activate a virtual environment (optional but recommended):
```shell
python -m venv venv
source venv/bin/activate
# linux
```

4. Install the required dependencies:
```shell
pip install -r requirements.txt
```

5. Set up the database:
```shell
python manage.py migrate
```

6. Create superuser:
```shell
python manage.py createsuperuser
```

7. Start the development server:
```shell
python manage.py runserver
```

8. Open your web browser and access the application at `http://localhost:8000`.

## Usage

- Create an account with `python manage.py createsuperuser`
- Log in to the admin panel:`http://localhost:8000/admin`
- Add a couple of websites
- Navigate to the homepage at `http://localhost:8000`
- Login as the admin or sign up as another user (it doesn't matter)
- Choose a website and submit a review
- The star rating will be automatically calculated based on the sentiment of the review