# chatBot
Demo ChatBot 

installation:

pip install -r alt_requirements/requirements_full.txt

train:

python -m rasa_nlu.train \
    --config sample_configs/config_spacy.yml \
    --data data/data.json \
    --path projects

utilisation:

curl -X POST localhost:5000/parse -d '{"q":"Hello"}' | python -m json.tool



tutoriel :

https://rasa.com/docs/nlu/0.12.0/tutorial/

https://hackernoon.com/build-simple-chatbot-with-rasa-part-1-f4c6d5bb1aea

https://www.youtube.com/watch?v=xu6D_vLP5vY&t=132s

github

https://gist.github.com/kohn1001

https://github.com/JustinaPetr/Weatherbot_Tutorial


