"""
Google Cloud Function that accepts JSON with "title" and "text" and then creates a Google Doc based on that content

Consume the endpoint as follows:

curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Document",
    "text": "This is my document."
  }' \
  https://us-central1-PROJECT_ID.cloudfunctions.net/createDocument
  
"""

const {google} = require('googleapis');

exports.createDocument = (req, res) => {
  // Get the JSON document from the request body.
  const json = JSON.parse(req.body);

  // Get the Google Docs API client.
  const docs = google.docs({
    version: 'v4',
    credentials: require('./credentials.json'),
  });

  // Create a new document.
  const doc = docs.documents.create({
    title: json.title,
    body: json.text,
  });

  // Get the document ID.
  const documentId = doc.id;

  // Return a success response with the document ID.
  res.status(200).send({documentId});
};
