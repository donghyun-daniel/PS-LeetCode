const fs = require('fs');

const commitMessage = fs.readFileSync(0, 'utf-8').trim();
const jsonPayload = JSON.stringify({
  text: commitMessage,
});

fs.writeFileSync(1, jsonPayload);
