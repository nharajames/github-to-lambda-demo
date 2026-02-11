import pandas as pd
import json
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        # Log the incoming event
        logger.info(f"Received event: {json.dumps(event)}")

        # Example: if event has 'data', use it; otherwise, use default
        data = event.get('data', {'col1': [1, 2], 'col2': [3, 4]})
        
        # Convert data to DataFrame
        df = pd.DataFrame(data)
        logger.info(f"DataFrame created:\n{df}")

        # Example transformation: add a new column
        df['col3'] = df['col1'] + df['col2']
        logger.info(f"DataFrame after transformation:\n{df}")

        # Return response
        return {
            "statusCode": 200,
            "message": "Lambda executed successfully",
            "data": df.to_dict()
        }

    except Exception as e:
        logger.error(f"Error processing Lambda: {e}")
        return {
            "statusCode": 500,
            "message": f"Lambda execution failed: {e}"
        }
