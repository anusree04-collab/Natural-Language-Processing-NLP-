TEXT SUMMARIZATION USING SPACY (MINI PROJECCT): 

     This project demonstrates Generic Extractive Text Summarization Using the Spacy NLP library . It explains how raw text is processed and summarized by selecting the most important sentences based on word frequency.

PROJECT OVERVIEW:

         Text summarization is a NLP task that automatically generates a shorter version of a documnet while preserving its key information.
	 
This notebook focuses on:

> Extractive Summarization : selecting important sentences from the original text.
> Generic Summarization : no user query is provided.

 TECHNOLOGIES USED :
 
  1.Python 3
  2.Google colab
  3.spaCy NLP library
  4.spaCy English Language Model(en_core_web_sm)

  HOW IT WORKS(WORKFLOW) :
  
  1.Input text - Raw document is provided as a string
  2.Load spaCy Model - NLP pipeline is intialized
  3.Tokenization - Text is split into words and sentences
  4.Stopword Removal - Common words are ignored
  5.Word Frequency Calculation - Important words are scored
  6.Sentence Scoring - Sentences are ranked
  7.Summary Generation - Top ranked sentences from the summary 
