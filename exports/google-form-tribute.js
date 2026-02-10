// ============================================================
// TRIBUTE FORM v2 — with file upload + audio
// ============================================================
// INSTRUCTIONS:
// 1. Go to https://script.google.com
// 2. Open your EXISTING tribute project (or create new)
// 3. Replace ALL code with this file
// 4. Click Run — authorize if prompted
// 5. A NEW form appears in Drive (old one still exists)
// 6. Open new form → Send → copy link
// 7. Delete the old form from Drive when ready
// ============================================================

function createTributeForm() {
  var form = FormApp.create('Your Message for Dad \u2014 Vic\'s 80th Birthday Book');
  form.setDescription(
    'Write your personal message for the tribute book. It can be a memory, a thank-you, ' +
    'a funny story, or just a few words. Whatever you write will appear in the book ' +
    'in your own voice.\n\n' +
    'Don\'t overthink it. Even one sentence is perfect.\n\n' +
    'You can also upload photos and voice memos at the end!'
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

  // --- Upload section ---
  form.addPageBreakItem()
    .setTitle('Photos & Voice Memos')
    .setHelpText(
      'Share a photo with Dad, or record a voice memo telling your story.\n\n' +
      'VOICE MEMO TIP: On your phone, open Voice Memos (iPhone) or Recorder (Android), ' +
      'record yourself talking about Dad, save it, then upload here.\n\n' +
      'NOTE: File upload requires you to be signed into a Google account. ' +
      'If that\'s a hassle, just text or email files to Greg at gcicconetti@gmail.com.'
    );

  form.addFileUploadItem()
    .setTitle('Upload a photo with Dad')
    .setHelpText(
      'A photo of you with Dad, a family photo, or any photo that goes with your message. ' +
      'Multiple photos welcome.'
    )
    .setRequired(false)
    .setMaxFiles(10)
    .setMaxFileSize(10485760);  // 10 MB per file

  form.addFileUploadItem()
    .setTitle('Upload a voice memo')
    .setHelpText(
      'Record yourself telling a story, sharing a memory, or just saying what Dad means to you. ' +
      'We\'ll transcribe it and include it in the book. Even 30 seconds is perfect. ' +
      'Accepted formats: .m4a, .mp3, .wav, .ogg, .mp4'
    )
    .setRequired(false)
    .setMaxFiles(3)
    .setMaxFileSize(26214400);  // 25 MB per file

  // Fallback for non-Google users
  form.addParagraphTextItem()
    .setTitle('Can\'t upload? Describe what you\'d like to share')
    .setHelpText(
      'If file upload isn\'t working for you, just describe the photo or voice memo here ' +
      'and text/email it to Greg at gcicconetti@gmail.com.'
    )
    .setRequired(false);

  Logger.log('Form created: ' + form.getEditUrl());
  Logger.log('Share URL: ' + form.getPublishedUrl());
  Logger.log('NOTE: Because this form has file upload, respondents must be signed into Google.');
}
