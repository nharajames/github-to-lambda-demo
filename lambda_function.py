import json
import pandas as pd

def lambda_handler(event, context):
    try:
        # Expecting event to contain a list of records
        # Example: {"data": [{"name": "John", "age": 25}, ...]}
        
        data = event.get("data", [])
        
        if not data:
            return {
                "statusCode": 400,
                "error": "No data provided to me",
                "message": "Please provide 'data' as a list of records"
            }

        # Create DataFrame
        df = pd.DataFrame(data)

        # Example processing: calculate average age if column exists
        result = {}

        if "age" in df.columns:
            result["average_age"] = df["age"].mean()

        result["row_count"] = len(df)
        result["columns"] = list(df.columns)

        return {
            "statusCode": 200,
            "error": None,
            "message": "Data processed successfully",
            "result": result
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "error": "ProcessingError",
            "message": str(e)
        }
