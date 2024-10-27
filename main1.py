from transformers import pipeline, BitsAndBytesConfig
import torch

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.bfloat16
)

# 13B version can be loaded with llava-hf/llava-1.5-13b-hf
model_id = "llava-hf/llava-1.5-7b-hf"


pipe = pipeline("image-to-text", model=model_id, model_kwargs={"quantization_config": quantization_config})
def update_conversation(new_message, history, image):

    if image is None:
        return "Please upload an image first using the widget on the left"

    conversation_starting_from_image = [[user, assistant] for [user, assistant] in history if not assistant.startswith('Please')]

    prompt = "USER: <image>\n"

    for i in range(len(history)):
        prompt+=history[i][0]+'\nASSISTANT: '+history[i][1]+"\nUSER: "

    prompt = prompt+new_message+'\nASSISTANT: '

    outputs = pipe(image, prompt=prompt, generate_kwargs={"max_new_tokens": 200
                                                          #, "do_sample" : True,
                                                          #"temperature" : 0.7
                                                          })[0]['generated_text']

    return outputs[len(prompt)-6:]
 !gradio deploy
