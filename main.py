from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import json

load_dotenv()

INTENTS = [
    "play_internet_radio", 
    "play_song_by_artist",
    "get_weather",
    "current_time",
    "set_timer",
    "remind_me",
]

def build_intent_classifier(intents=INTENTS):
    template = (
        "Act as the intent classification component of a home assistant, similar to Amazon Alexa "
        "(except your name is 'Becca', not 'Alexa').\n"
        f"Common intents include: {', '.join(intents)}, ...\n"
        'You receive input in json format: `{{"input":...}}`\n'
        'You respond in json format: `{{"intent":..., "arguments":{{ ... }}, }}}}`\n\n'
        '{{"input":{spoken_request}}}'
    )

    llm = OpenAI(temperature=0.1)
    prompt = PromptTemplate(
        input_variables=["spoken_request"],
        template=template,
    )
    return LLMChain(llm=llm, prompt=prompt)

def evaluate(chain, text):
    response = chain.run(text)
    return json.loads(response.strip())

if __name__ == '__main__':
    import sys

    # e2e test
    chain = build_intent_classifier()
    if len(sys.argv) > 1:
        text = sys.argv[1]
        response = evaluate(chain, text)
        print(response)
    else:
        text = "becca play kexp"
        response = evaluate(chain, text)
        print(response)
        assert response == {'intent':'play_internet_radio', 'arguments':{'station':'KEXP'}}