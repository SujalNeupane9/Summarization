from transformers import AutoTokenizer

model_nm = 't5-small'

def tokenize_for_inference(text):
    model_inputs = tokenizer(
      x['document'],
      max_length = 512,
      padding=True,
      truncation=True
    )
    return model_inputs['input_ids']