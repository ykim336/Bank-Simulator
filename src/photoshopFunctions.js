// Import required modules
require("dotenv").config();
let URL = require('url')
let AWS = require('aws-sdk')
const fs = require("fs")

// Load sensitive information from environment variables
const CLIENT_ID = process.env.CLIENT_ID;
const CLIENT_SECRET = process.env.CLIENT_SECRET;
const AWS_ACCESS_KEY_ID = process.env.AWS_ACCESS_KEY_ID;
const AWS_SECRET_ACCESS_KEY = process.env.AWS_SECRET_ACCESS_KEY;

// Authentication configuration
const imsConfig = {
  clientId: CLIENT_ID,
  clientSecret: CLIENT_SECRET
};

// ---------------------------- Functions ---------------------------- //

/* Generates an IMS token for Adobe API authentication.
 * Returns a promise that resolves with the token data. */

async function generateIMSToken() {
  const url = 'https://ims-na1.adobelogin.com/ims/token/v3';
  const options = {
    method: 'POST',
    url: url,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    form: { 
      grant_type: 'client_credentials',
      client_id: imsConfig.clientId,
      client_secret: imsConfig.clientSecret,
      scope: 'openid,AdobeID,read_organizations'
    }
  };
  
  return new Promise((resolve, reject) => {
    request(options, (err, res, body) => {
      if(err || res.statusCode >= 400) {
        reject( err || body )
      }else{
        resolve( body )
      }
    })
  })
}


const request = require('request');
const { error } = require("console");
const endpoint = "https://image.adobe.io/pie/psdService/smartObject"

/* Generates a pre-signed URL for an S3 object.
 * Parameters: bucket name, object key, region, and operation (getObject or putObject)
 * Returns a promise that resolves with the signed URL. */

async function getSignedURL(bucket, destKey, region, op){
  let s3 = new AWS.S3({ accessKeyId: AWS_ACCESS_KEY_ID, secretAccessKey: AWS_SECRET_ACCESS_KEY, region: region, apiVersion: '2006-03-01', signatureVersion: 'v4' })
  let params = {Bucket: bucket, Key: destKey};
  return new Promise((resolve, reject) => {
    s3.getSignedUrl(op, params, (err, url)=>{
      if(err){
        reject(err)
      }else{
        resolve(url)
      }
    });
  })
}

/* Posts a request to the Photoshop API.
 * Parameters: endpoint URL, API key, IMS token, request body
 * Returns a promise that resolves with the API response. */

async function postPhotoshopAPI(endpoint, apiKey, token, requestBody){
  let options = {
    url: endpoint,
    method: 'POST',
    headers: {
      "Authorization": `Bearer ${token}`,
      "x-api-key": apiKey
    },
    json: true,
    body: requestBody
  }

  return new Promise((resolve, reject) => {
    request(options, (err, res, body) => {
      if(err || res.statusCode >= 400) {
        reject( err || body )
      }else{
        resolve( body )
      }
    })
  })
}

/* Polls the status of an ongoing Photoshop API job.
 * Parameters: initial response body, API key, IMS token
 * Returns a promise that resolves with the final job status. */

async function pollStatus(responseBody, apiKey, token){
  let options = {
    url: responseBody._links.self.href,
    method: 'GET',
    headers: {
      "Authorization": `Bearer ${token}`,
      "x-api-key": apiKey
    },
    json: true
  }

  return new Promise((resolve, reject) => {
    let pollFunction = () => {
      request(options, (err, res, body) => {
        console.log(body.jobId, body.outputs[0].status)
        if(err || res.statusCode >= 400) {
          clearInterval(intervalId)
          reject(err || res.statusCode)
        }else if(body.outputs[0].status == 'succeeded' || body.outputs[0].status == 'failed'){
          clearInterval(intervalId)
          resolve( body )
        }
      })
    }
    let intervalId = setInterval(pollFunction, 1000)
  })
}

/* Uploads an image to S3.
 * Parameters: local file path, S3 ID, S3 preset, bucket name, output path, and region
 * Returns a promise that resolves when the upload is complete. */

async function uploadImage(localPath, s3ID, s3Preset, s3BucketName="customizedblankets4u", outputPath="output", awsRegion="us-east-2") {
  const credentials = {
    accessKeyId: AWS_ACCESS_KEY_ID,
    secretAccessKey: AWS_SECRET_ACCESS_KEY,
    region: awsRegion
  };
  
  const s3 = new AWS.S3(credentials);
  const remotePath = `${outputPath}/${s3ID}_${s3Preset}.jpg`;
  // Create a writable stream to save the file locally
  const fileStream = fs.createReadStream(localPath[0]);
  
  // Set up parameters for the S3 getObject operation
  const params = {
    Bucket: s3BucketName,
    Key: remotePath,
    Body: fileStream,
    ContentType: 'image/jpeg'
  };

  try {
    // Perform the S3 putObject operation to upload the file
    const data = await s3.upload(params).promise();

    console.log('File uploaded successfully:', data.Location);
  } catch (err) {
    console.error('Error uploading file:', err);
  }
}

/* Downloads an image from S3.
 * Parameters: S3 ID, S3 preset, bucket name, output path, and region
 * Returns a promise that resolves when the download is complete. */

async function downloadImage(localPath, s3ID, s3Preset, s3BucketName="customizedblankets4u", outputPath="output", awsRegion="us-east-2") {
  const credentials = {
    accessKeyId: AWS_ACCESS_KEY_ID,
    secretAccessKey: AWS_SECRET_ACCESS_KEY,
    region: awsRegion
  };
  
  const s3 = new AWS.S3(credentials);
  let remotePath;
  let localPth;

  if (outputPath == "output") {
    remotePath = `${outputPath}/${s3ID}_${s3Preset}.jpeg`;
    localPth = `${localPath[0]}\\${s3ID}_${s3Preset}.jpeg`;
  }
  else {
    remotePath = `${outputPath}/${s3ID}_${s3Preset}.jpg`;
    localPth = `${localPath[0]}/${s3ID}_${s3Preset}.jpg`;
  }

  console.log(remotePath)
  console.log(localPth)
  
  // Create a writable stream to save the file locally
  const fileStream = fs.createWriteStream(localPth);
  
  // Set up parameters for the S3 getObject operation
  const params = {
    Bucket: s3BucketName,
    Key: remotePath,
  };
  
  // Perform the S3 getObject operation and save the file locally
  s3.getObject(params)
    .createReadStream()
    .pipe(fileStream)
    .on('error', (err) => {
      console.error('Error downloading file:', err);
    })
    .on('close', () => {
      console.log('File downloaded successfully:', localPth);
    });
}

/* Replace a smart object in a Photoshop document using the API.
 * Parameters: input path, replacement image path, smart object layer name, bucket name, region, output path, input path, replacement path, and file type */

async function replaceSmartObject(s3InputPath, s3ReplacementImagePath, s3Preset, smartObjectLayerName, output_path="output", input_path="input", replacement_path="replacement", s3BucketName="customizedblankets4u", awsRegion="us-east-2", file_type="image/jpeg"){
  let authDetails = await generateIMSToken();
  let creds = JSON.parse(authDetails);

  // s3OutputPath needs to be defined here!
  let s3OutputPath = `${output_path}/${s3ReplacementImagePath}_${s3InputPath}.jpeg`

  // s3InputPath needs to be defined here!
  s3InputPath = `${input_path}/${s3InputPath}.psd`

  // s3ReplacementImagePath needs to be defined here!
  s3ReplacementImagePath = `${replacement_path}/${s3ReplacementImagePath}_${s3Preset}.jpg`

  console.log("Input Path:",s3InputPath)
  console.log("Replacement Path:",s3ReplacementImagePath)
  console.log("Output Path:",s3OutputPath)

  inputUrl = await getSignedURL(s3BucketName, s3InputPath, awsRegion, 'getObject')
  replacementImageUrl = await getSignedURL(s3BucketName, s3ReplacementImagePath, awsRegion, 'getObject')
  outputUrl = await getSignedURL(s3BucketName, s3OutputPath, awsRegion, 'putObject')
  console.log("Replacing Layer: ", smartObjectLayerName)
  let requestBody = {
    "inputs":[
      {
        "href": inputUrl,
        "storage": "external"
      }
    ],
    "options":{
      "layers":[
        {
          "name": smartObjectLayerName,
          "input": {
            "href": replacementImageUrl,
            "storage": "external"
          }
        }
      ]
    },
    "outputs":[
      {
        "href": outputUrl,
        "storage": "external",
        "type": file_type
      }
    ]
  }

  try {
    let response = await postPhotoshopAPI(endpoint, imsConfig.clientId, creds.access_token, requestBody)
    let status = await pollStatus(response, imsConfig.clientId, creds.access_token)
    console.log(JSON.stringify(status, null, 2))
  } catch(e) {
    console.error(e)
  }
}
