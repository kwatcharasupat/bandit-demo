import os
import shutil
from tqdm import tqdm

stems = ["speech", "music", "effects"]

def reorg(model, original_dir):
    
    model_dirs = {
        stem: os.path.join(original_dir, f"{model}-{stem}") for stem in stems
    }

    new_dir = os.path.join(os.getcwd(), model)

    os.makedirs(new_dir, exist_ok=True)

    files = os.listdir(model_dirs["speech"])

    for file in tqdm(files):
        
        os.makedirs(os.path.join(new_dir, file), exist_ok=True)

        for stem in stems:
            shutil.copy(
                os.path.join(model_dirs[stem], file),
                os.path.join(new_dir, file)
            )



if __name__ == "__main__":
    import fire

    fire.Fire(reorg)
                           

