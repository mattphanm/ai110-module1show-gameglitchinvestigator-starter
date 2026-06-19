# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
--> Worked fine; broke down after first time playing
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
--> New Game did not refresh previous attempts and did not allow new game to start/inputs
--> Hints always showed "Go Lower" even when not appropriate

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|1| | | |    "Go Lower".        "Go Higher"           None
|NewGame| *refresh/history attempts* |*refresh goes to 0 and only secret changes* | None
|1 1.   | attempts start @ 0 | attempts start @ 1 and doesnt increment on 1st submission | None

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
--> I used OpenAI's Codex as my agent for this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
--> One suggestion that the AI suggested that was correct was logic for each difficulty. It added different features to each difficulty, making it harder/easier depending on chosen. I verfied this through a designer's perspective and also checked logic by seeing if new configurated attempts were changed to match new setting.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
--> One suggestion the AI did and was wrong was the UI. I specified that there was an error with the attempts in the debug log and that first submit did not increment the counter for attempts. The AI reconfigured the whole UI layout without me prompting it. I reprompted, giving it to NOT touch the UI. After new changes, I verified result by checking UI and making sure it matched the original.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
--> I asked AI to implement base test cases and I used pytest to then verified if they passed. I could have written manual, but decided to use AI to write ones that I am sure would pass. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
--> One test I ran manually and through pytest was the "Go Higher" and "Go Lower". Originally when the secret was say 50, and I inputted 30, it said "Go Lower" when it should be saying "Go Higher". The test cases made sure that after the logic is patched, in that example, it would say "Go Higher." This tells me that my code changes are valid and correct + game runs as should.
- Did AI help you design or understand any tests? How?
--> AI did design my tests but did not help me understand it. I understood what each test did and what it should return. AI implemented basic test cases to prove validation of code fixes.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
--> Streamlit reruns the whole Python file from top to bottom whenever the user clicks a button or changes an input, so normal variables can reset unless you save them somewhere. Session state is like a small memory box for the app that keeps important values, like attempts, score, history, and the secret number, across those reruns.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
--> One habit I want to reuse is writing or asking for small tests after fixing a bug, then running pytest to confirm the fix actually works. I also want to keep making clear Git commits after a working repair so my changes are easier to track.
- What is one thing you would do differently next time you work with AI on a coding task?
--> Next time I would give the AI stricter instructions earlier, especially about not changing the UI unless I ask for it. I would also review each suggested change more carefully before accepting it.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
--> This project showed me that AI generated code can be helpful, but it still needs to be tested and checked by a human. AI can speed up debugging, but I should not assume the first answer is correct.
