from transformers import AutoTokenizer

model_nm = 't5-base'

def tokenize_for_inference(text):
    tokenizer = AutoTokenizer.from_pretrained(model_nm)
    model_inputs = tokenizer(
      text,
      max_length = 512,
      padding=True,
      truncation=True
    )
    return model_inputs['input_ids']
