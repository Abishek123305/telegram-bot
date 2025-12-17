MyPrep Assistant – Telegram AI Bot

MyPrep Assistant is an AI-powered Telegram bot designed to help students with exam preparation, resume screening, document summarization, quiz generation, reminders, and OCR-based text extraction — all within Telegram.

Overview

This bot acts as a lightweight academic assistant inside Telegram.
Instead of switching between multiple apps (ChatGPT, weather apps, PDF tools), users can perform all tasks directly in a chat interface.

Features
AI Question Answering

Ask academic or technical questions using /ask <question>

Powered by Groq LLM for fast responses

Weather Information

Get real-time weather updates using /weather <city>

Uses OpenWeather API

Document Summarization (PDF & DOCX)

Upload a PDF or Word document

Bot automatically summarizes the content

Quiz Generator

Upload a PDF or DOCX document

Reply to the document with /quiz

Generates multiple-choice questions for exam preparation

Resume Analyzer (ATS-style)

Upload resume in PDF or DOCX format

Reply with /resume

Provides skill match score and missing keywords based on job role

Smart Reminders

Set reminders using:

/remind <minutes> <task>


Example:

/remind 30 revise dbms

OCR (Image to Text)

Upload an image containing printed text

Extracts readable text using OCR

Best results with clear, printed text (not handwritten)

Technologies Used

Python 3.10+

python-telegram-bot

Groq API (LLM)

OpenWeather API

PyPDF2

python-docx

OpenCV

Tesseract OCR

APScheduler

How to Use (User Flow)
Start the Bot
/start

Ask AI Questions
/ask What is normalization in DBMS?

Get Weather
/weather Vizag

Document Summary

Upload a PDF or DOCX file

Bot automatically replies with a summary

Quiz Generation

Upload a PDF or DOCX file

Reply to that file with:

/quiz

Resume Analysis

Upload resume (PDF or DOCX)

Reply to it with:

/resume

Set Reminder
/remind 10 drink water

OCR

Upload an image containing printed text

Bot extracts and returns the text

Who Benefits From This Bot

Students preparing for exams

Freshers preparing resumes and interviews

Users who prefer Telegram over multiple apps

Lightweight alternative to heavy AI apps

How This Bot Differs From ChatGPT or Gemini

Works entirely inside Telegram

Focused on student workflows (PDFs, quizzes, resumes)

Combines multiple utilities in one place

Faster access with no app switching

Free-tier friendly APIs

Internet Requirement

Yes, the bot requires an internet connection to:

Communicate with Telegram servers

Access AI models

Fetch weather data

Project Status

Core features implemented and working

OCR requires Tesseract installed on system

Suitable for resume and placement discussions

Can be extended further with more AI tools
