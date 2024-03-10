// Require:
var postmark = require("postmark");

// Send an email:
var client = new postmark.ServerClient("cd8d27e7-e383-4d6d-ad5e-daa45fbcd2f5");

client.sendEmail({
  "From": "chris@chrisj.uk",
  "To": "gmail@chrisj.uk",
  "Subject": "Hello from Postmark",
  "HtmlBody": "<strong>Hello</strong> dear Postmark user.",
  "TextBody": "Hello from Postmark!",
  "MessageStream": "outbound"
});
