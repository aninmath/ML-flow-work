
import os
import dagshub.auth
import dagshub

# Add your token to the DagsHub client cache

os.environ['DAGSHUB_TOKEN'] = '32ae467abca7407408fa331319b54eaf2a1dc984'

# Initialize DagsHub with MLflow integration
dagshub.init(
    repo_owner='aninmath',
    repo_name='ML-flow-work',
    mlflow=True
)
