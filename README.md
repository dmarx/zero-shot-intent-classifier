# Zero-Shot Intent Classifier

This sort of thing used to be non-trivial. I hacked this together probably in like an hour. 

Ho boy, the times: they are a changin.

## What is this?

This is probably going to sound archaic in a few months, but a lot of "home assistant" type devices right now use a technique called "slot filling" under the hood. A component in a slot-filling system is an "intent" classifier. Instead of training one bespoke: if you need one you can probably just use this directly with no or very little modification.

## Setup

1. `git clone <this repo>; cd <this repo>`
2. `pip install -r requirements.txt`
3. Create a file named `.env` containing one line: `OPENAI_API_KEY=...`, replacing `...` with your key.

## Use

    $ python main.py  "becca, how would I drive from my home to SeaTac airport?"
    ## {'intent': 'get_directions', 'arguments': {'start_location': 'home', 'end_location': 'SeaTac airport'}}

## Compiled Prompt

> Act as the intent classification component of a home assistant, similar to Amazon Alexa (except your name is 'Becca', not 'Alexa').  
> Common intents include: play_internet_radio, play_song_by_artist, get_weather, current_time, set_timer, remind_me  
> You receive input in json format: `{"input":...}`  
> You respond in json format: `{"intent":..., "arguments":{ ... }, }}`  
> {"input":`{spoken_request}`}
