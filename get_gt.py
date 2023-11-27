import os
import shutil
from tqdm import tqdm

stems = ["speech", "music", "effects", "mixture"]

stem_names = {
    "speech": "speech",
    "music": "music",
    "effects": "sfx",
    "mixture": "mix",
}

def copy(gt_dir):
    
    files = os.listdir(gt_dir)
    files = [f for f in files if os.path.isdir(os.path.join(gt_dir, f))]

    new_dir = os.path.join(os.getcwd(), "gt")

    for file in tqdm(files):
        
        os.makedirs(os.path.join(new_dir, file), exist_ok=True)

        for stem in stems:
            shutil.copy(
                os.path.join(gt_dir, file, stem_names[stem] + ".wav"),
                os.path.join(new_dir, file, stem + ".wav")
            )



if __name__ == "__main__":
    import fire

    fire.Fire(copy)
                           

