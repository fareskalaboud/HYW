# Just Dance AI-Volution

### AI Artathon 2.0 Submission

Our web-based project allows anyone to input any song they wish (as a YouTube link), and our machine learning model will generate dance moves that they follow, competing to imitate the generated model to gain as many points as they can. Our project is inspired by the arcade games Dance Dance revolution and Just Dance. 

### Installation Instructions

#### Notes

Please note our initial respository is at [this link](https://github.com/fareskalaboud/oldHYW/).

#### Pre-Requisites

- Ubuntu or similar (we used Pop! OS)
- NVidia GPU (we used RTX 2060)
- 1080p webcam
- [Learning2Dance](https://github.com/verlab/Learning2Dance_CAG_2020).
- CUDA toolkit version 11.1.1
- cuDNN version 8.1.0
- [nvidia-docker](https://github.com/NVIDIA/nvidia-docker)
#### Run Instructions

- Build the Learning2Dance docker image and place the Learning2Dance folder inside the HYW directory
- Connect the webcam via USB to your machine
- Run this command from inside the HYW directory: `sudo nvidia-docker run -u root -it --device=/dev/video0 --device=/dev/video1 --network host -v $(pwd):/workspace hyw/openpose:v1` 
- You are now inside the workspace of the container. Run `pip install -r requirements.txt`. 
- Run `python3 main.py`
- Enjoy playing and dancing :)
