## Step-by-step BMAD POC in Cursor

Below is a practical step-by-step guide to run a small BMAD POC inside Cursor. The goal is to use Cursor as the environment where the AI plays the BMAD roles and builds a simple web application.

**Example application**: TaskLite – a minimal task manager web app  
**Stack**: FastAPI + simple HTML

---

## 1. Install Cursor

Download and install Cursor from `https://cursor.sh`.

**Steps**

- Install Cursor.
- Start the application.
- Sign in.
- Enable the AI features:
    - Open Settings and check:
        - AI features enabled.
        - Model selected (GPT-4.1 / Claude / similar).

---

## 2. Clone the BMAD repository

Open a terminal and run:

```bash
git clone https://github.com/bmad-code-org/BMAD-METHOD.git
```

Then open the project in Cursor:

- `File` → `Open Folder` → select `BMAD-METHOD`.
- Cursor will now index the repository. Wait until indexing finishes.

---

## 3. Create a new POC folder

Inside the repository, create a folder for your experiment, for example:

- `/bmad-poc-tasklite`

Create these files inside that folder:

- `product.md`
- `architecture.md`
- `tasks.md`

This helps the AI keep context.

---

## 4. Start the Product Manager agent

Open the Cursor Chat panel.

- Shortcut: `Cmd + L`

Paste this prompt:

```text
You are acting as the Product Manager in the BMAD method.

Goal:
Create a simple MVP web application called TaskLite.

Requirements:
Users can add tasks
Users can see a task list
Users can mark tasks as completed

Constraints:
Backend FastAPI
Storage SQLite or in memory
Frontend simple HTML

Output:
1 Product brief
2 Feature list
3 Acceptance criteria

Write the output into product.md
```

Cursor will generate the document.  
Accept the change.

---

## 5. Run the Architect agent

Open the chat again and prompt:

```text
Act as the Software Architect in the BMAD method.

Read product.md and design a minimal architecture.

Provide:

1 System architecture
2 API endpoints
3 Data model
4 Project folder structure

Write the result into architecture.md
```

Cursor will generate something like:

- FastAPI backend
- SQLite database

**Endpoints**

- `POST /tasks`
- `GET /tasks`
- `PUT /tasks/{id}`

**Data model**

- `Task`
    - `id`
    - `title`
    - `completed`

---

## 6. Ask the Developer agent to create the project

Now instruct Cursor to generate the code.

Prompt:

```text
Act as the Developer agent.

Read architecture.md and implement the application.

Create a minimal FastAPI project with:

app.py
database.py
models.py
templates/index.html

Requirements:
Tasks can be created
Tasks can be listed
Tasks can be marked completed

Generate the full code.
```

Cursor will create the files.  
Approve the changes.

---

## 7. Create a Python environment

Open the Cursor terminal:

- `Terminal` → `New Terminal`

Run:

```bash
python3 -m venv venv
```

Activate it:

- **Mac / Linux**

  ```bash
  source venv/bin/activate
  ```

- **Windows**

  ```bash
  venv\Scripts\activate
  ```

Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy jinja2
pip install python-multipart
```

---

## 8. Run the application

Start the server:

```bash
uvicorn app:app --reload
```

Open the browser:

- `http://127.0.0.1:8000`

Or the API docs:

- `http://127.0.0.1:8000/docs`

You now have a running AI-generated application.

---

## 9. Run the QA agent

Now test the BMAD loop.

Open Cursor chat again and prompt:

```text
Act as the QA engineer in the BMAD method.

Analyze the codebase.

Create:

1 Test strategy
2 5 test cases
3 Example pytest tests for the API endpoints
```

Cursor will generate:

- Test plan
- API tests

Approve and create a folder:

- `tests/`

---

## BMAD Test Architect
Then in your IDE chat, start TEA flow with:
/bmad:tea:automate





## BMAD Test Architect UI Tests
Act as murat the BMAD Test Architect.
Create a set of tests for validating every UI use case.
For each usecase create a set  of T1T5 test scenarios according to TestDesignTechnique-T1T5.md
Create only the title of the test cases according to the T1T5 syntax.
Give every test scenario a risk score.
Store the outcome in test-cases-UI.md

## 10. Run the BMAD improvement loop

Now simulate the Measure–Analyze–Decide part.

Prompt:

```text
Act as a BMAD reviewer.

Evaluate the project.

Provide:

1 architectural weaknesses
2 security issues
3 missing validation
4 improvements
```

Cursor will propose improvements.  
Example:

- Add request validation
- Add error handling
- Add logging

Implement the improvements.

---

## 11. Commit the POC

Initialize git:

```bash
git init
git add .
git commit -m "BMAD POC TaskLite"
```

---

## What this POC demonstrates

You tested the agentic workflow:

- Product → Architect → Developer → QA → Reviewer

This is exactly the BMAD method loop.

---

## A powerful trick used in real teams

Instead of running each role manually, you can run one orchestration prompt.

Example:

```text
Simulate the BMAD workflow.

Step 1 Product Manager defines the product
Step 2 Architect designs the system
Step 3 Developer implements the code
Step 4 QA writes tests

Build a minimal task manager web application using FastAPI.

Show each step clearly.
```

Cursor will execute the entire workflow.

If you want, I can also show you a much better BMAD POC that builds a full web app in about 10 minutes using Cursor agents, which is how many AI engineering teams currently experiment with agentic development.

## Testdesign with T1T5 approach
Act as the QA engineer in the BMAD method.

Analyze the codebase.

Create:

For every API a set of POISED Test according to POISED-TestCases.md and T1T5-TestDesign.md

STore the ourcome into POISED-T1T5-TestDesign.md
