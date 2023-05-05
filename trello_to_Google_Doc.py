"""
Creates a new Google Doc based on a Trello card. Example usage:

curl -X POST 
-H "Authorization: Bearer YOUR_API_KEY" 
-H "Content-Type: application/json" 
-d '{
"event": {
"action": "card_added",
"board_id": "YOUR_BOARD_ID",
"card_id": "YOUR_CARD_ID",
"list_id": "YOUR_LIST_ID"
}
}' 
"https://us-central1-PROJECT_ID.cloudfunctions.net/createGoogleDocFromTrelloCard"
"""

exports.createGoogleDocFromTrelloCard = async (event, context) => {
// Get the Trello card information from the event.
const cardId = event.data.cardId;
const boardId = event.data.boardId;
const listId = event.data.listId;

// Get the template document.
const templateDoc = await DocumentApp.openById('TEMPLATE_DOCUMENT_ID');

// Create a new Google Doc.
const doc = await DocumentApp.create(card.name);

// Copy the template document to the new document.
await doc.copyFrom(templateDoc);

// Replace the placeholders in the new document with the Trello card information.
const card = await TrelloApp.getCard(cardId);
for (const placeholder of ['{{cardTitle}}', '{{cardDescription}}', '{{cardLabels}}', '{{cardDueDate}}']) {
doc.replaceText(placeholder, card[placeholder]);
}

// Save the document.
await doc.save();

// Return the document ID.
return doc.getId();
};
