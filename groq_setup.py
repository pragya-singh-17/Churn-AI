import requests
import os

def get_llm_response(data):
    prompt = f"""
        You are a banking data analyst.

        Customer data:
        {data['input']}

        Prediction:
        0 = Not Churn, 1 = Churn
        Model Output: {data['prediction']}
        Churn Probability: {data['probability']}

        STRICT RULES:
        - Give ONLY 3 short bullet points
        - Each point must be 1 line
        - No paragraph
        - No storytelling
        - No assumptions not in data
        - Focus on churn only

        Output format:
        - Insight 1
        - Insight 2
        - Insight 3
        """
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {os.environ.get('GROQ_API_KEY')}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-oss-20b",  
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    
   
    if response.status_code != 200:
        return f"Error: {response.text}"

    return response.json()['choices'][0]['message']['content']



