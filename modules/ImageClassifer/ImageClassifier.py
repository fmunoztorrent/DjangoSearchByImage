# Google APIs
from google.cloud import vision
# import validators
import io
import os

class ImageClassifier():

    LABEL_SCORE_THRESHOLD = 0.6
    WEB_ENTITIES_SCORE_THRESHOLD = 0.7
    IMAGE_CLASSIFICATION_RESULT = {}

    def __init__(self, image_url, resource_type='url'):
        self.image_url = image_url
        self.resource_type = resource_type
        self.classify()

    def classify(self):

        """Detects labels in the file located in Google Cloud Storage or on the Web."""
        client = vision.ImageAnnotatorClient()

        if self.resource_type == 'url':
            image = vision.types.Image()
            image.source.image_uri = self.image_url

        elif self.resource_type == 'filesystem':

            with io.open(self.image_url, 'rb') as image_file:
                content = image_file.read()
                image = vision.types.Image(content=content)

        # Getting data #


        # Labels
        response_labels = client.label_detection(image=image)
        labels = response_labels.label_annotations

        # Web
        response_web = client.web_detection(image=image).web_detection
        web_entities = response_web.web_entities

        image_labels = []
        for label in labels:
            if label.score > self.LABEL_SCORE_THRESHOLD:
                image_labels.append({
                    "description": str(label.description),
                    "score": float(label.score),
                })


        entites_web = []
        for web_entity in web_entities:
                
            if web_entity.score > self.WEB_ENTITIES_SCORE_THRESHOLD:
                entites_web.append({
                    "description": str(web_entity.description),
                    "score": float(web_entity.score),
                })
    

        self.IMAGE_CLASSIFICATION_RESULT = {
            "labels" : image_labels,
            "entities" : entites_web,
            "objects" : []
        }


    def image_data(self):
        return self.IMAGE_CLASSIFICATION_RESULT
