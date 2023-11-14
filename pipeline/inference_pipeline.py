from utils.utils import tokenize_for_inference

def infer_model(trainer):
    text = input("Enter the text you want to summarize: ")
    tokenized = tokenize_for_inference(text)
    generated = trainer.model.generate(tokenized, max_length=256)
    
    # Convert the generated output back to text
    summary = trainer.tokenizer.decode(generated.squeeze(), skip_special_tokens=True)
    
    return summary
