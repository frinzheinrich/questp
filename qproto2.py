import boto3
import json
import time

# Setting up S3 bucket and file
s3_bucket = 'django-quest-bucket'
document_name = 'UK-visa-application-form-Sample-1.pdf'
output_json_file = 'textract_results.json'

# Initialize Textract client
textract = boto3.client('textract', region_name='ap-southeast-1')

# Start the document text detection job
response = textract.start_document_analysis(
    DocumentLocation={
        'S3Object': {
            'Bucket': s3_bucket,
            'Name': document_name
        }
    },
    FeatureTypes=['FORMS', 'TABLES']
)

# Get the Job ID
job_id = response['JobId']
print(f"Job ID: {job_id}")

# Poll the job status
while True:
    response = textract.get_document_analysis(JobId=job_id)
    status = response['JobStatus']

    if status in ['SUCCEEDED', 'FAILED']:
        break

    print("Waiting for the job to complete...")
    time.sleep(5)  # Time

# Check if the job was successful
if status == 'SUCCEEDED':
    # Initialize pagination and result storage
    next_token = None
    all_blocks = []

    while True:
        if next_token:
            response = textract.get_document_analysis(JobId=job_id, NextToken=next_token)
        else:
            response = textract.get_document_analysis(JobId=job_id)

        # Collect blocks
        blocks = response.get('Blocks', [])
        all_blocks.extend(blocks)

        # Check for pagination
        next_token = response.get('NextToken')
        if not next_token:
            break

    # Save results to a JSON file
    with open(output_json_file, 'w') as json_file:
        json.dump(all_blocks, json_file, indent=4)

    print(f"Results saved to {output_json_file}")

else:
    print("Document analysis failed.")
