# Single Laptop Shop

This repository is a small shop that (almost) sells a laptop.

## Install the project and run the main file

> This section must be written according to the curriculum approach to project management (venv or something like this).

## Your Task Context

> Data is the New Oil

The shop owner has read a new book about data and metrics and wants to apply new knowledge to improve sales. For this purpose, he wants to know how many users visit the laptop page. A counter was implemented, but we forgot about how to expose data to the owner and how he can reset it.

### Acceptance Criteria

In main.py file, you should implement two new functions (in our case, let's name its "pages"):
1. Page that shows the visitors count (check the function at line 41);
2. Page that resets the visitors count (check the function at line 50).

The first page should return a simple HTML page consisting of a level one header and div element with text like "Visitor count: n.". Remember that the page should not change the `counter` field.

The second page you are implementing should try to reset the counter (set to 0). If the counter is more than 0, the page should reset it and return an HTML page with the red text "The counter has been reset." If the counter is eq 0, the page should return an HTML page with the text "There is nothing to reset yet!"

## How to test the project

Run the project and then open...

### The main page

Open http://localhost:5000/

### The metrics page

Open http://localhost:5000/metrics

### The metrics reset page

Open http://localhost:5000/metrics/reset
