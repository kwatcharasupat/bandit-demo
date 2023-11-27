import pandas as pd
import os

MODELS = {
    "gt": {
        "name": "Ground Truth",
        "encoder": "",
        "band": "",
        "loss": "",
    },
    "dnr-3s-mus64-l1snr": {
        "name": "BandIt",
        "encoder": "Shared",
        "band": "Music 64",
        "loss": "L1SNR",
    },
    "dnr-3s-vox7-l1snr": {
        "name": "BandIt",
        "encoder": "Shared",
        "band": "Vocals V7",
        "loss": "L1SNR",
    },
    "dnr-3s-vox7-l2snr": {
        "name": "BandIt",
        "encoder": "Shared",
        "band": "Vocals V7",
        "loss": "L2SNR",
    },
    "dnr-bsrnn-lstm12-vox7-l1": {
        "name": "BSRNN",
        "encoder": "Separate",
        "band": "Vocals V7",
        "loss": "L1",
    },
    "dnr-demucs": {
        "name": "Hybrid Demucs (v3)",
        "encoder": "",
        "band": "",
        "loss": "Time L1",
    },
    "dnr-umxhq": {
        "name": "Open-Unmix",
        "encoder": "",
        "band": "",
        "loss": "TF Mag MSE",
    }
}

PAGE_ROOT="https://karnwatcharasupat.github.io/bandit-demo"

def audio_div(model, file, stem):
    html=f'<audio controls="controls"><source src="{PAGE_ROOT}/{model}/{file}/{stem}" autoplay/></audio>'

    # print(html)

    return html

def gen_table(file=159):
    df = pd.DataFrame.from_dict(MODELS, orient="index")

    df["mixture"] = df.index.map(lambda x: audio_div("gt", file, "mix.wav"))

    for stem in ["speech", "music", "effects"]:
        df[stem] = df.index.map(lambda x: audio_div(x, file, stem + ".wav"))

    df = df.rename(columns={k: k.capitalize() for k in df.columns})

    s = df.to_html(escape=False, index=False, border=0, justify="center", table_id=f"table-{file}")

    os.makedirs("html", exist_ok=True)

    with open(f"html/{file}.html", "w") as f:
        f.write(s)

    return s

def gen_tables(n=10, files=None):
    
    if files is None:
        files = os.listdir(os.path.join(os.getcwd(), "gt"))

        files = sorted([f for f in files if os.path.isdir(os.path.join(os.getcwd(), "gt", f))])

        files = files[:n]

    s = ""

    for file in sorted(files):

        s += f"<h2>File: {file}</h2>\n"
        s += gen_table(file)
                           
    with open("html/index.html", "w") as f:
        f.write(s)


if __name__ == "__main__":
    
    import fire

    fire.Fire()