# Just Dance AI-Volution

### AI Artathon 2.0 Submission

Inspired by the arcade games Dance Dance Revolution and Just Dance, our web-based project allows anyone to input any song they wish (using YouTube), and our deep learning (DL) model will generate dance moves for them to follow. Not only does the game take the song as input, but it also processes a live video stream of the user dancing, using another DL model to detect their pose, with the goal of creating an interactive game, where they imitate the AI-generated dance moves or challenge friends to score points.

### Installation Instructions

1. `docker build -t openpose -f openpose-Dockerfile .`
2. `docker run opepose`
3. `docker build -t hyw/openpose:v0 Dockerfile .`

#### Notes

Please note our initial respository is at [this link](https://github.com/fareskalaboud/oldHYW/). We removed all the heavy files to keep the repository lightweight.

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
- Run this command from inside the HYW directory: `sudo nvidia-docker run -u root -it --device=/dev/video0 --device=/dev/video1 --network host -v $(pwd):/workspace hyw/openpose:v0` 
- Run `python3 main.py`
- Enjoy playing and dancing :)
