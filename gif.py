# -*- coding: utf-8 -*-
"""GIF.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1N3xxvtgqDoM6iYL76GeP9mblUEq9tqkq
"""

!pip install diffusers transformers accelerate torch
import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video

pipe = DiffusionPipeline.from_pretrained("damo-vilab/text-to-video-ms-1.7b", torch_dtype=torch.float16, variant="fp16")
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe.enable_model_cpu_offload()
pipe.enable_vae_slicing()

prompt = "Panda eating bamboo"
video_frames = pipe(prompt, num_inference_steps=50).frames
video_frames=video_frames.squeeze(0)

video_path = export_to_video(video_frames)

from moviepy.editor import *
clip=VideoFileClip(video_path)
clip.write_gif("output.gif", fps=8)