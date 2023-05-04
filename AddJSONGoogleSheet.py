# Google Cloud Function that adds arbitrary json to a Google Sheet

const {google} = require('googleapis');

exports.addData = (req, res) => {
  // Get the JSON document from the request body.
  const json = JSON.parse(req.body);

  // Get the Google Sheets API client.
  const sheets = google.sheets({
    version: 'v4',
    credentials: require('./credentials.json'),
  });

  // Get the spreadsheet ID and range from the request body.
  const spreadsheetId = req.body.spreadsheetId;
  const range = req.body.range;

  // Append the JSON data to the spreadsheet.
  sheets.spreadsheets.values.append({
    spreadsheetId: spreadsheetId,
    range: range,
    values: json,
  });

  // Return a success response.
  res.status(200).send('OK');
};
