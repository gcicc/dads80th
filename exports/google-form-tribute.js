// ============================================================
// INSTRUCTIONS:
// 1. Go to https://script.google.com
// 2. Click "New project"
// 3. Delete the placeholder code and paste this entire file
// 4. Click Run (play button) — it will ask for permissions, allow them
// 5. Check your Google Drive — the form will appear there
// 6. Open the form, click Send, copy the link
// ============================================================

function createTributeForm() {
  var form = FormApp.create('Your Message for Dad — Vic\'s 80th Birthday Book');
  form.setDescription(
    'Write your personal message for the tribute book. It can be a memory, a thank-you, ' +
    'a funny story, or just a few words. Whatever you write will appear in the book ' +
    'in your own voice.\n\n' +
    'Don\'t overthink it. Even one sentence is perfect.'
  );
  form.setIsQuiz(false);
  form.setAllowResponseEdits(true);
  form.setCollectEmail(false);
  form.setLimitOneResponsePerUser(false);

  // Name
  form.addTextItem()
    .setTitle('Your name')
    .setRequired(true);

  // Relationship
  form.addListItem()
    .setTitle('Your relationship to Vic')
    .setChoiceValues([
      'Wife',
      'Son',
      'Daughter',
      'Daughter-in-law',
      'Son-in-law',
      'Grandson',
      'Granddaughter',
      'Brother',
      'Sister',
      'Nephew',
      'Niece',
      'Cousin',
      'Friend',
      'Fellow Veteran',
      'Other'
    ])
    .setRequired(true);

  // Main message
  form.addParagraphTextItem()
    .setTitle('Your message for Dad')
    .setHelpText(
      'This will appear in the book under your name. Write as much or as little as you want. ' +
      'A single sentence is great. A whole page is great too.'
    )
    .setRequired(true);

  // Memory
  form.addParagraphTextItem()
    .setTitle('A favorite memory with Dad')
    .setHelpText('If one specific moment comes to mind, tell us about it.')
    .setRequired(false);

  // Three words
  form.addTextItem()
    .setTitle('Describe Dad in exactly three words')
    .setRequired(false);

  // Legacy
  form.addParagraphTextItem()
    .setTitle('The thing about Dad you want his great-grandchildren to know someday')
    .setRequired(false);

  // Photo upload
  // NOTE: File upload requires the form to be in a shared drive or
  // the respondent to be signed in. If this causes friction for family,
  // just tell them to email photos to Greg instead.
  form.addParagraphTextItem()
    .setTitle('Have a photo with Dad?')
    .setHelpText(
      'Google Forms file upload can be tricky. Easiest: just text or email the photo to Greg. ' +
      'Or describe the photo here and we\'ll track it down.'
    )
    .setRequired(false);

  Logger.log('Form created: ' + form.getEditUrl());
  Logger.log('Share URL: ' + form.getPublishedUrl());
}
