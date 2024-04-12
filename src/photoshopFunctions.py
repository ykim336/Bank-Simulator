import subprocess
import os

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

HELPER_PATH = f":helpers/"

# To use this, you need to make every path and layers a list.
def replaceSmartObject(s3InputPath, s3ReplacementImagePath, s3Preset, smartObjectLayerName, output_path="output", input_path="input", replacement_path="replacement", s3BucketName="customizedblankets4u", awsRegion="us-east-2", file_type="image/jpeg"):
    command = f"replaceSmartObject('{s3InputPath}', '{s3ReplacementImagePath}', '{s3Preset}', '{smartObjectLayerName}', '{output_path}', '{input_path}', '{replacement_path}', '{s3BucketName}', '{awsRegion}', '{file_type}')"
    
    with open("photoshopFunctions.js", "r") as f:
        js_code = f.read()
        with open(f"{HELPER_PATH}photoshopFunctionsHelper.js", "w") as w:
            w.write(js_code + command)

    js_file = f"{HELPER_PATH}photoshopFunctionsHelper.js"
    try:
        subprocess.run(["node", js_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {js_file}: {e}")

def downloadImage(localPath, s3ID, s3Preset, s3BucketName="customizedblankets4u", outputPath="output", awsRegion="us-east-2"):
    command = f"downloadImage({localPath}, '{s3ID}', '{s3Preset}', '{s3BucketName}', '{outputPath}', '{awsRegion}')"
    
    with open("photoshopFunctions.js", "r") as f:
        js_code = f.read()
        with open(f"{HELPER_PATH}photoshopFunctionsHelper.js", "w") as w:
            w.write(js_code + command)

    js_file = f"{HELPER_PATH}photoshopFunctionsHelper.js"
    try:
        subprocess.run(["node", js_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {js_file}: {e}")

def uploadImage(localPath, s3ID, s3Preset, s3BucketName="customizedblankets4u", outputPath="output", awsRegion="us-east-2"):
    command = f"uploadImage({localPath}, '{s3ID}', '{s3Preset}', '{s3BucketName}', '{outputPath}', '{awsRegion}')"
    
    with open("photoshopFunctions.js", "r") as f:
        js_code = f.read()
        with open(f"{HELPER_PATH}photoshopFunctionsHelper.js", "w") as w:
            w.write(js_code + command)

    js_file = f"{HELPER_PATH}photoshopFunctionsHelper.js"
    try:
        subprocess.run(["node", js_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {js_file}: {e}")

def testing_function():
    # INSTRUCTION: Must put s3InputPath and s3ReplacementImagePath as lists. 
    # print("Testing replaceSmartObject Function...")
    # replaceSmartObject("mockup1", "test", "pattern", "Design #1")
    # print("Completed Test for replaceSmartObject...")

    # print("Testing downloadImage Function...")
    # downloadImage([r"C:\Users\kmyn7\Downloads\uuid"], "tests", "mockup1", "customizedblankets4u", "input")
    # print("Completed Test for downloadImage...")

    # print("Testing uploadImage Function...")
    # uploadImage([r"C:\Users\kmyn7\Downloads BLANKETS\FINISHED\Seamless-Kawaii-Cute-Cats-Pattern-8674392\design_test.jpg"], "tests", "mockup2", "customizedblankets4u", "input")
    # print("Completed Test for uploadImage...")
