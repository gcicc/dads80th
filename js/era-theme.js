// Era theme detection — applies chapter-specific CSS classes to body
(function() {
  const eraMap = {
    'ch01-roots':        'era-doowop',
    'ch02-service':      'era-military',
    'ch03-yvonne':       'era-summer-of-love',
    'ch04-education':    'era-eighties',
    'ch05-entrepreneur': 'era-italian',
    'ch06-veterans':     'era-brotherhood',
    'ch07-family':       'era-family',
    'ch08-golden-years': 'era-golden',
    'ch09-voices':       'era-celebration',
    'ch10-happy-80th':   'era-celebration',
    'timeline':          'era-golden',
    'family-tree':       'era-family',
    'correct-the-record':'era-celebration'
  };

  const path = window.location.pathname;
  for (const [slug, eraClass] of Object.entries(eraMap)) {
    if (path.includes(slug)) {
      document.body.classList.add(eraClass);
      break;
    }
  }

  // If on index/home page
  if (path.endsWith('/') || path.endsWith('index.html')) {
    document.body.classList.add('era-home');
  }
})();
