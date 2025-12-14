LinkedIn Insights Microservice

This project is a backend service built using FastAPI that fetches and stores basic insights about a LinkedIn company page using its Page ID (the last part of the LinkedIn URL).

Example:
https://www.linkedin.com/company/deepsolv/
Page ID → deepsolv

How it works: 
1. Accepts a LinkedIn Page ID
2. Checks if the page already exists in the database
3. If not present, scrapes publicly available data from LinkedIn
4. Stores the data in a database
5. Returns the stored data via REST APIs

API Endpoints
GET /pages/{page_id}
GET /pages/search
