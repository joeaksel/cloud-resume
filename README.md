# cloud-resume

I am hosting this online resume as a static website in an Azure blob storage container. The JavaScript visit counter stores the counter variable in an Azure Cosmos DB. I built an Azure Function App using Python to connect the frontend website to the backend DB. I implemented GitHub actions to create a CI/CD workflow that automatically updates the contents of the frontend when a git push is made. Finally, the site is secured with an SSL certificate using Azure CDN. 
