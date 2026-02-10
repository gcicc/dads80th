// ============================================================
// FACT-CHECK FORM v2 — with file upload + audio
// ============================================================
// INSTRUCTIONS:
// 1. Go to https://script.google.com
// 2. Open your EXISTING fact-check project (or create new)
// 3. Replace ALL code with this file
// 4. Click Run — authorize if prompted
// 5. A NEW form appears in Drive (old one still exists)
// 6. Open new form → Send → copy link
// 7. Delete the old form from Drive when ready
// ============================================================

function createFactCheckForm() {
  var form = FormApp.create('Correct the Record — Vic\'s 80th Birthday Book');
  form.setDescription(
    'We wrote a book about Dad\'s life based on research. We need YOU to tell us what we got right, ' +
    'what we got wrong, and what we missed.\n\n' +
    'For each claim, pick: TRUE / FALSE / I DON\'T KNOW.\n' +
    'Then add corrections or stories at the end of each section.\n\n' +
    'This takes about 10 minutes. Thank you!\n\n' +
    'TIP: You can upload photos and documents at the end. ' +
    'You can also record a voice memo on your phone and upload it.'
  );
  form.setIsQuiz(false);
  form.setAllowResponseEdits(true);
  form.setCollectEmail(false);
  form.setLimitOneResponsePerUser(false);

  var choices = ['TRUE', 'FALSE', 'I DON\'T KNOW'];

  // --- Name ---
  form.addTextItem()
    .setTitle('Your name')
    .setRequired(true);

  // --- Section: The Cicconetti Side ---
  form.addPageBreakItem().setTitle('The Cicconetti Side (Claims 1\u201313)');

  var cicconettiClaims = [
    '1. The Cicconetti name traces to Collepietro, Abruzzo, Italy',
    '2. The name means "little Cicco," from Franciscus',
    '3. The family has been in Collepietro since at least 1778',
    '4. Victor Sr. was born in Bayonne in 1925',
    '5. Victor Sr. married Eleanor Salone',
    '6. Eleanor was one of three Salone sisters: Marge, Eleanor, Josie',
    '7. The Salone sisters grew up on the Lower East Side of Manhattan',
    '8. During the Depression, the sisters spent time in an orphanage',
    '9. Their mother Anna worked as a sweatshop seamstress',
    '10. Victor Sr. and Eleanor raised six children in Bayonne',
    '11. The six children were: Victor, Dennis, Leanora, Bob, Loretta, Michael',
    '12. Victor Sr. died in 1980',
    '13. Eleanor died in 1997'
  ];

  cicconettiClaims.forEach(function(claim) {
    form.addMultipleChoiceItem()
      .setTitle(claim)
      .setChoiceValues(choices)
      .setRequired(false);
  });

  form.addParagraphTextItem()
    .setTitle('Corrections or additional info about the Cicconetti side')
    .setHelpText('What did we get wrong? What did we miss? Tell us anything.');

  // --- Section: Elia / Chiarolanza Side ---
  form.addPageBreakItem().setTitle('The Elia / Chiarolanza Side (Claims 14\u201321)');

  var eliaClaims = [
    '14. Yvonne\'s mother Mary\'s maiden name was Chiarolanza (family spelling: Chirolanza)',
    '15. The Chiarolanza family came from Campania, likely Montecorvino Rovella',
    '16. The 1940 Census shows Mary (age 20) in Bayonne with father Alfonso, mother Angelina, and 4 sisters',
    '17. Mary worked as a seamstress at the Maidenform factory, 154 Avenue E',
    '18. Frank Elia worked as a poultry processor',
    '19. Frank died around 1962, when Yvonne was about 14',
    '20. After Frank\'s death, Mary married Anthony Galella',
    '21. Greg named his son Anthony after Anthony Galella'
  ];

  eliaClaims.forEach(function(claim) {
    form.addMultipleChoiceItem()
      .setTitle(claim)
      .setChoiceValues(choices)
      .setRequired(false);
  });

  form.addParagraphTextItem()
    .setTitle('Corrections or additional info about the Elia / Chiarolanza side')
    .setHelpText('What did we get wrong? What did we miss? Tell us anything about Mom\'s family.');

  // --- Section: Military Service ---
  form.addPageBreakItem().setTitle('Victor\'s Military Service (Claims 22\u201326)');

  var militaryClaims = [
    '22. Victor joined the Air Force in 1965 at age 19',
    '23. He served as a medic',
    '24. He flew medical air evacuations in Southeast Asia',
    '25. His service ended in 1969',
    '26. "MedFlyBoy" was his nickname from service'
  ];

  militaryClaims.forEach(function(claim) {
    form.addMultipleChoiceItem()
      .setTitle(claim)
      .setChoiceValues(choices)
      .setRequired(false);
  });

  form.addParagraphTextItem()
    .setTitle('Corrections or stories about Dad\'s military service')
    .setHelpText('Bases, units, buddies, stories \u2014 anything about those years.');

  // --- Section: Yvonne & Wedding ---
  form.addPageBreakItem().setTitle('Yvonne & The Wedding (Claims 27\u201334)');

  var weddingClaims = [
    '27. Yvonne was born approximately April 1948',
    '28. She grew up in Bayonne',
    '29. Losing her father at ~14 shaped her resilience',
    '30. Her sister Mary Ann was her closest bond',
    '31. Victor and Yvonne married on August 20, 1967',
    '32. The wedding was at Assumption Catholic Church, Bayonne',
    '33. Victor was 21, Yvonne was 19',
    '34. Victor was still in the Air Force when they married'
  ];

  weddingClaims.forEach(function(claim) {
    form.addMultipleChoiceItem()
      .setTitle(claim)
      .setChoiceValues(choices)
      .setRequired(false);
  });

  form.addParagraphTextItem()
    .setTitle('Corrections or stories about Mom & the wedding')
    .setHelpText('How did you two meet? What do you remember about the wedding day?');

  // --- Section: Careers ---
  form.addPageBreakItem().setTitle('Careers (Claims 35\u201341)');

  var careerClaims = [
    '35. Victor was an administrator at Long Branch High School in the 1980s',
    '36. The Red Bank Register profiled him in 1987 as "Man with Many Missions"',
    '37. He also worked in the Asbury Park school district',
    '38. He retired from education in 2000',
    '39. Yvonne taught health in Jersey City public schools',
    '40. Yvonne retired in 2005',
    '41. Yvonne then served as Allied Health Vocational advisor for Hudson County'
  ];

  careerClaims.forEach(function(claim) {
    form.addMultipleChoiceItem()
      .setTitle(claim)
      .setChoiceValues(choices)
      .setRequired(false);
  });

  form.addParagraphTextItem()
    .setTitle('Corrections or stories about their careers')
    .setHelpText('Favorite students? Best stories from the classroom?');

  // --- Section: Restaurant & Veterans ---
  form.addPageBreakItem().setTitle('Restaurant & Veterans (Claims 42\u201347)');

  var restVetClaims = [
    '42. Victor and Yvonne co-owned an Italian restaurant with one of their sons',
    '43. Mary Ann Hurley ran a pizza bistro in Bayonne',
    '44. Victor was a founding member of VVA Chapter 12 in Ocean Township, NJ',
    '45. He served as president of Chapter 12',
    '46. He is a life member of the VA',
    '47. He is a life member of the DAV'
  ];

  restVetClaims.forEach(function(claim) {
    form.addMultipleChoiceItem()
      .setTitle(claim)
      .setChoiceValues(choices)
      .setRequired(false);
  });

  form.addParagraphTextItem()
    .setTitle('Corrections or stories about the restaurant or veterans work')
    .setHelpText('What was the restaurant called? Where was it? What years? Which son?');

  // --- Section: Family & Recent Years ---
  form.addPageBreakItem().setTitle('Family & Recent Years (Claims 48\u201359)');

  var familyClaims = [
    '48. Victor and Yvonne have two sons and one daughter',
    '49. Rich was born approximately August 1977',
    '50. Rich attended Rutgers University',
    '51. Rich married Sharon K. Doughty',
    '52. They have six grandchildren total',
    '53. Four grandchildren by 2007 (40th anniversary), two more since',
    '54. Victor and Yvonne live in Egg Harbor City / Galloway Township area',
    '55. They are regulars at Atlantic City',
    '56. At 75, Vic asked Greg to order him an air pistol for target practice',
    '57. After the 75th birthday party, Vic walked around the house laughing at memories',
    '58. Vic signs every email "Love DAD"',
    '59. Vic greets Greg as "Dearest Son" or "Dearest Greg"'
  ];

  familyClaims.forEach(function(claim) {
    form.addMultipleChoiceItem()
      .setTitle(claim)
      .setChoiceValues(choices)
      .setRequired(false);
  });

  form.addParagraphTextItem()
    .setTitle('Corrections, missing names, stories about family life')
    .setHelpText('We need names! All three children, all six grandchildren.');

  // --- Section: Timeline ---
  form.addPageBreakItem().setTitle('Timeline (Claims 60\u201367)');

  var timelineClaims = [
    '60. Born ~March 1946, Bayonne',
    '61. Air Force 1965\u20131969',
    '62. Married August 20, 1967',
    '63. Long Branch HS, 1980s',
    '64. Red Bank Register, 1987',
    '65. Retired from education, 2000',
    '66. 40th anniversary, 2007',
    '67. Turning 80, March 2026'
  ];

  timelineClaims.forEach(function(claim) {
    form.addMultipleChoiceItem()
      .setTitle(claim)
      .setChoiceValues(choices)
      .setRequired(false);
  });

  form.addParagraphTextItem()
    .setTitle('Any dates wrong or milestones we missed?');

  // --- Section: The Big Gaps ---
  form.addPageBreakItem().setTitle('The Big Gaps \u2014 What We Know We\'re Missing');

  form.addTextItem().setTitle('Victor\'s exact birthday (month/day/year)');
  form.addParagraphTextItem().setTitle('Names of all three children (full names + birth years)');
  form.addParagraphTextItem().setTitle('Names of all six grandchildren (names, ages, which child they belong to)');
  form.addParagraphTextItem().setTitle('The restaurant (name, location, years, which son)');
  form.addTextItem().setTitle('VVA Chapter 12 founding year');
  form.addParagraphTextItem().setTitle('Where Victor served in Vietnam (bases, locations)');
  form.addParagraphTextItem().setTitle('How did Victor and Yvonne meet?');
  form.addTextItem().setTitle('What do the grandkids call him?');
  form.addParagraphTextItem().setTitle('Anything else we should know');

  // --- Section: Upload Photos & Documents ---
  form.addPageBreakItem()
    .setTitle('Upload Photos, Documents & Voice Memos')
    .setHelpText(
      'Share photos of Dad, old documents, or even a voice memo.\n\n' +
      'VOICE MEMO TIP: On your phone, open the Voice Memos app (iPhone) or Recorder app (Android), ' +
      'record yourself talking, save it, then upload the file here.\n\n' +
      'NOTE: File upload requires you to be signed into a Google account. ' +
      'If that\'s a hassle, just text or email files to Greg at gcicconetti@gmail.com.'
    );

  form.addFileUploadItem()
    .setTitle('Upload photos of Dad')
    .setHelpText('Old photos, family photos, military photos \u2014 anything. Multiple files OK.')
    .setRequired(false)
    .setMaxFiles(10)
    .setMaxFileSize(10485760);  // 10 MB per file

  form.addFileUploadItem()
    .setTitle('Upload documents')
    .setHelpText('Newspaper clippings, letters, certificates, military records \u2014 anything you have.')
    .setRequired(false)
    .setMaxFiles(5)
    .setMaxFileSize(10485760);

  form.addFileUploadItem()
    .setTitle('Upload a voice memo')
    .setHelpText(
      'Record yourself on your phone telling a story about Dad, then upload the audio file here. ' +
      'We\'ll transcribe it and weave it into the book. Even 30 seconds is gold.'
    )
    .setRequired(false)
    .setMaxFiles(3)
    .setMaxFileSize(26214400);  // 25 MB per file for audio

  // --- Done ---
  Logger.log('Form created: ' + form.getEditUrl());
  Logger.log('Share URL: ' + form.getPublishedUrl());
  Logger.log('NOTE: Because this form has file upload, respondents must be signed into Google.');
}
