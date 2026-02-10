# GREG Do This — Dad's 80th

Things only Greg can do. Check off as completed.

**Last updated:** 2026-02-09
**DEADLINE: March 2026 (~4 weeks)**

---

## BLOCKERS (do these first — they unblock everything else)

- [ ] **Send contribution templates to family** — email `contributions/*.md` files to: Yvonne, Rich, [other son], [daughter], Kathy Pacifico, Mike Hurley Jr., Mary Ann & Michael Hurley, AJ, Ellie, Frank & Valerie Elia. (Unblocks WS2, WS5)
- [ ] **Get children's and grandchildren's names** — blocks Ch7, family tree, Correct the Record. Ask Yvonne or Rich directly.
- [ ] **Choose Blurb book size** — 8×10" portrait or 10×8" landscape? Browse blurb.com. (Blocks WS4)

---

## PUBLISH THE BOOK ONLINE (do this week)

Everything below is set up and ready — you just need to do the GitHub + Google parts.

### Step 1: Create GitHub Repo & Push (15 min)

1. Go to https://github.com/new
2. Repo name: `dads80th`
3. **Private** (recommended — family personal data) or Public (free GitHub Pages)
4. Do NOT initialize with README (you already have one)
5. Copy the repo URL, then run:

```bash
cd ~/Dropbox/01-Active-Projects/dads80th
git remote add origin https://github.com/YOURUSERNAME/dads80th.git
git branch -M main
git add -A
git commit -m "Publish draft book with online contribution forms"
git push -u origin main
```

6. **If you chose Private repo:** You need GitHub Pro ($4/mo) or GitHub Free (org) for Pages on private repos. Alternatively, use a Public repo — the `noindex` meta tag is already set so search engines won't crawl it. The URL is obscure enough for a family project.

### Step 2: Enable GitHub Pages (5 min)

1. Go to your repo → Settings → Pages
2. Source: **GitHub Actions** (not "Deploy from branch")
3. The `publish.yml` workflow is already created — it will auto-deploy on every push to `main`
4. After the first push, wait ~2 min, then check: `https://YOURUSERNAME.github.io/dads80th/`

### Step 3: Update the repo URL in `_quarto.yml` (1 min)

Find this line in `_quarto.yml`:
```yaml
repo-url: https://github.com/YOURUSERNAME/dads80th
```
Replace `YOURUSERNAME` with your actual GitHub username.

---

## CREATE GOOGLE FORMS (do with ChatGPT)

You need two forms. Open ChatGPT and paste the prompts below.

### Form 1: Fact-Check Form

> **Prompt for ChatGPT:**
>
> I need you to help me build a Google Form. Here's the context: I wrote a tribute book for my dad's 80th birthday. I made 67 factual claims about his life based on research. I need family members to mark each claim TRUE, FALSE, or I DON'T KNOW, plus leave corrections.
>
> The form should have these sections (each is a page in the form):
>
> **Page 1 — Intro**
> - Title: "Correct the Record — Vic's 80th Birthday Book"
> - Description: "We wrote a book about Dad's life. We need YOU to tell us what we got right, what we got wrong, and what we missed. This takes about 10 minutes."
> - Field: "Your name" (short text, required)
>
> **Page 2 — The Cicconetti Side (Claims 1–13)**
> For each claim below, add a multiple-choice question with options: TRUE / FALSE / I DON'T KNOW
> 1. The Cicconetti name traces to Collepietro, Abruzzo, Italy
> 2. The name means "little Cicco," from Franciscus
> 3. The family has been in Collepietro since at least 1778
> 4. Victor Sr. was born in Bayonne in 1925
> 5. Victor Sr. married Eleanor Salone
> 6. Eleanor was one of three Salone sisters: Marge, Eleanor, Josie
> 7. The Salone sisters grew up on the Lower East Side of Manhattan
> 8. During the Depression, the sisters spent time in an orphanage
> 9. Their mother Anna worked as a sweatshop seamstress
> 10. Victor Sr. and Eleanor raised six children in Bayonne
> 11. The six children were: Victor, Dennis, Leanora, Bob, Loretta, Michael
> 12. Victor Sr. died in 1980
> 13. Eleanor died in 1997
> Then add: "Corrections or additional info about the Cicconetti side:" (long text, optional)
>
> **Page 3 — The Elia / Chiarolanza Side (Claims 14–21)**
> 14. Yvonne's mother Mary's maiden name was Chiarolanza (family spelling: Chirolanza)
> 15. The Chiarolanza family came from Campania, likely Montecorvino Rovella
> 16. The 1940 Census shows Mary (age 20) in Bayonne with father Alfonso, mother Angelina, and 4 sisters
> 17. Mary worked as a seamstress at the Maidenform factory, 154 Avenue E
> 18. Frank Elia worked as a poultry processor
> 19. Frank died around 1962, when Yvonne was about 14
> 20. After Frank's death, Mary married Anthony Galella
> 21. Greg named his son Anthony after Anthony Galella
> Then add: "Corrections or additional info about the Elia / Chiarolanza side:" (long text, optional)
>
> **Page 4 — Military Service (Claims 22–26)**
> 22. Victor joined the Air Force in 1965 at age 19
> 23. He served as a medic
> 24. He flew medical air evacuations in Southeast Asia
> 25. His service ended in 1969
> 26. "MedFlyBoy" was his nickname from service
> Then add: "Corrections or stories about Dad's military service:" (long text, optional)
>
> **Page 5 — Yvonne & The Wedding (Claims 27–34)**
> 27. Yvonne was born approximately April 1948
> 28. She grew up in Bayonne
> 29. Losing her father at ~14 shaped her resilience
> 30. Her sister Mary Ann was her closest bond
> 31. Victor and Yvonne married on August 20, 1967
> 32. The wedding was at Assumption Catholic Church, Bayonne
> 33. Victor was 21, Yvonne was 19
> 34. Victor was still in the Air Force when they married
> Then add: "Corrections or stories about Mom & the wedding:" (long text, optional)
>
> **Page 6 — Careers (Claims 35–41)**
> 35. Victor was an administrator at Long Branch High School in the 1980s
> 36. The Red Bank Register profiled him in 1987 as "Man with Many Missions"
> 37. He also worked in the Asbury Park school district
> 38. He retired from education in 2000
> 39. Yvonne taught health in Jersey City public schools
> 40. Yvonne retired in 2005
> 41. Yvonne then served as Allied Health Vocational advisor for Hudson County
> Then add: "Corrections or stories about their careers:" (long text, optional)
>
> **Page 7 — Restaurant & Veterans (Claims 42–47)**
> 42. Victor and Yvonne co-owned an Italian restaurant with one of their sons
> 43. Mary Ann Hurley ran a pizza bistro in Bayonne
> 44. Victor was a founding member of VVA Chapter 12 in Ocean Township, NJ
> 45. He served as president of Chapter 12
> 46. He is a life member of the VA
> 47. He is a life member of the DAV
> Then add: "Corrections or stories about the restaurant or veterans work:" (long text, optional)
>
> **Page 8 — Family & Recent Years (Claims 48–59)**
> 48. Victor and Yvonne have two sons and one daughter
> 49. Rich was born approximately August 1977
> 50. Rich attended Rutgers University
> 51. Rich married Sharon K. Doughty
> 52. They have six grandchildren total
> 53. Four grandchildren by 2007 (40th anniversary), two more since
> 54. Victor and Yvonne live in Egg Harbor City / Galloway Township area
> 55. They are regulars at Atlantic City
> 56. At 75, Vic asked Greg to order him an air pistol for target practice
> 57. After the 75th birthday party, Vic walked around the house laughing at memories
> 58. Vic signs every email "Love DAD"
> 59. Vic greets Greg as "Dearest Son" or "Dearest Greg"
> Then add: "Corrections, missing names, stories about family life:" (long text, optional)
>
> **Page 9 — Timeline (Claims 60–67)**
> 60. Born ~March 1946, Bayonne
> 61. Air Force 1965–1969
> 62. Married August 20, 1967
> 63. Long Branch HS, 1980s
> 64. Red Bank Register, 1987
> 65. Retired from education, 2000
> 66. 40th anniversary, 2007
> 67. Turning 80, March 2026
> Then add: "Any dates wrong or milestones we missed?" (long text, optional)
>
> **Page 10 — The Big Gaps**
> Add one long-text field for each:
> - "Victor's exact birthday (month/day/year):"
> - "Names of all three children (full names + birth years):"
> - "Names of all six grandchildren (names + ages + which child they belong to):"
> - "The restaurant (name, location, years, which son):"
> - "VVA Chapter 12 founding year:"
> - "Where Victor served in Vietnam (bases, locations):"
> - "How did Victor and Yvonne meet?"
> - "What do the grandkids call him?"
> - "Anything else we should know:"
>
> Give me step-by-step instructions to build this in Google Forms, or better yet, give me a Google Apps Script I can paste into script.google.com to auto-create the whole form.

### Form 2: Tribute Messages Form

> **Prompt for ChatGPT:**
>
> I need a second Google Form for collecting personal tribute messages for my dad's 80th birthday book. Each family member writes their own message.
>
> **Form title:** "Your Message for Dad — Vic's 80th Birthday Book"
> **Description:** "Write your personal message for the tribute book. It can be a memory, a thank-you, a funny story, or just a few words. Whatever you write will appear in the book in your own voice. Don't overthink it."
>
> **Fields:**
> 1. "Your name" (short text, required)
> 2. "Your relationship to Vic" (dropdown: Wife, Son, Daughter, Grandson, Granddaughter, Son-in-law, Daughter-in-law, Brother, Sister, Nephew, Niece, Cousin, Friend, Fellow Veteran, Other)
> 3. "Your message for Dad" (long text, required) — description: "This will appear in the book under your name. Write as much or as little as you want."
> 4. "A favorite memory with Dad" (long text, optional) — description: "If one specific moment comes to mind, tell us about it."
> 5. "Describe Dad in three words" (short text, optional)
> 6. "The thing about Dad you want his great-grandchildren to know someday" (long text, optional)
> 7. "Upload a photo with Dad" (file upload, optional) — description: "A photo of you with Dad, or any photo that goes with your message."
>
> Give me step-by-step instructions or a Google Apps Script to auto-create this form.

### After Creating the Forms

1. **Get each form's share link:** In Google Forms → Send → Link icon → Copy
2. The URL will look like: `https://docs.google.com/forms/d/e/1FAIpQLSe.../viewform`
3. The `YOUR_FORM_ID` part is the long string: `1FAIpQLSe...`
4. **Replace placeholders in the book:**
   - In `appendices/correct-the-record.qmd`: replace both `YOUR_FORM_ID` instances with the fact-check form ID
   - In `chapters/ch09-voices.qmd`: replace both `YOUR_FORM_ID` instances with the tribute form ID
   - Also **uncomment the iframe lines** (remove the `<!-- ` and ` -->` around them) to embed the forms directly in the book pages
5. **Connect responses to Google Sheets:** In each form → Responses tab → green Sheets icon → create new spreadsheet. This gives you a live spreadsheet of all responses.

---

## SEND THE LINK TO FAMILY (after forms are live)

Draft email (adapt as needed):

> **Subject:** Dad's 80th Birthday Book — We Need Your Help
>
> Hey everyone,
>
> I've been working on a tribute book for Dad's 80th. It covers his whole life — Bayonne, the Air Force, teaching, the restaurant, veterans work, family — everything we could piece together from research.
>
> But here's the thing: we definitely got some stuff wrong, and there's a LOT we don't know. That's where you come in.
>
> **The book (draft):** [PASTE YOUR GITHUB PAGES URL HERE]
>
> **Two things you can do:**
> 1. **Fact-check the book** — we made 67 claims about Dad's life. Mark each one TRUE, FALSE, or I DON'T KNOW: [PASTE FACT-CHECK FORM URL]
> 2. **Write your message for Dad** — a memory, a story, a few words. Whatever you want to say: [PASTE TRIBUTE FORM URL]
>
> Even 5 minutes of your time will make this book way better. And please — don't tell Dad.
>
> Love,
> Greg

---

## Other This-Week Items

- [ ] **Push repo to GitHub** — see Step 1 above
- [ ] **Review the rendered book** — open `_book/index.html`, read all chapters, note issues.
- [ ] **Review "Correct the Record" appendix** — is the tone right? Fun enough for Dad to engage?
- [ ] **Chase "sshhh its a surprise" thread** — follow up on Feb 6 email for tribute messages.
- [ ] **Coordinate with Kathy Pacifico** — she produced the 75th video. Touch base re: 80th.

## Photo Work (drives WS1)

- [ ] **Survey `../Lit-Project/images/`** — flag 30–50 photos for the book by theme (heritage, military, family, career, recent)
- [ ] **Download P1020477.JPG** from Sept 2017 "Look at yourselves!!!!" email via Gmail MCP
- [ ] **Scan the 1987 Red Bank Register article** if anyone has a copy — "Man with Many Missions"
- [ ] **Retrieve Vic's 75th birthday video** from Vimeo for reference

## Information to Gather

- [ ] **Restaurant details** — name, location, years, which son. Ch5 is nearly empty without this.
- [ ] **VVA Chapter 12 founding year** — ask Dad or look through VVA materials.
- [ ] **Ask Dad about Vietnam specifics** — bases, unit, memories. Only if willing. Ch2.
- [ ] **Ask Dad/Mom how they met** — courtship story. Ch3.
- [ ] **JotForm alternative** — Rich knows JotForm (Cicco Devel). Could use instead of Google Forms if preferred. Discuss with Rich.

## Research (can be delegated to Claude)

- [ ] **Subscribe to Ancestry.com** to access: 1940 Census image (4 sisters' names), Mary Chiarolanza obituary (Feb 2008), Victor Sr.'s parents
- [x] ~~Design and draft the birthday tribute document~~ — DONE (Quarto book structure, 10 chapters + 3 appendices)
- [x] ~~Set up GitHub Pages publishing infrastructure~~ — DONE (publish.yml workflow, noindex, form placeholders)
