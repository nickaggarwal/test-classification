import json
import numpy as np
import torch
from transformers import pipeline


class InferlessPythonModel:
    def initialize(self):
        self.generator = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli",
            device=0,
        )

    def infer(self, inputs):
        text = inputs["text"]
        candidate_labels = inputs["candidate_labels"]
        pipeline_output = self.generator(text, candidate_labels)
        return { "output" :  json.dumps(pipeline_output) } 


    def finalize(self):
        self.pipe = None
