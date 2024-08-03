import os

models_list = [
  {
      "model_name": "groq/llama3-70b-8192",
      "litellm_params": { 
          "model": "groq/llama3-70b-8192",
          "api_key": os.getenv("GROQ_API_KEY"),
      }
  },
  {
      "model_name": "groq/llama-3.1-70b-versatile",
      "litellm_params": { 
          "model": "groq/llama-3.1-70b-versatile",
          "api_key": os.getenv("GROQ_API_KEY"),
      }
  },
  {
      "model_name": "gemini/gemini-1.5-flash",
      "litellm_params": { 
          "model": "gemini/gemini-1.5-flash",
          "api_key": os.getenv("GEMINI_API_KEY"),
      }
  }
]