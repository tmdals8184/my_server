import boto3

def detect_labels_local_file(photo):
    client = boto3.client('rekognition')
   
    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()}) # byte형태의 key값으로

    result = []
    for r in response["Labels"]:
        name = r["Name"]
        confidence = r["Confidence"]
        result.append(f"{name} : {confidence:.2f}%")

    return "<br/>".join(map(str, result))

def compare_faces(sourceFile, targetFile):

    client = boto3.client('rekognition')

    imageSource = open(sourceFile, 'rb')
    imageTarget = open(targetFile, 'rb')

    response = client.compare_faces(SimilarityThreshold=0,
                                    SourceImage={'Bytes': imageSource.read()},
                                    TargetImage={'Bytes': imageTarget.read()})

    result = []
    for faceMatch in response['FaceMatches']:
        similarity = faceMatch['Similarity']
        result.append(f"두 얼굴의 일치율 : {similarity:.2f}")

    imageSource.close()
    imageTarget.close()

    return "<br/>".join(map(str, result))