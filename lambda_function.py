import pandas as pd

def lambda_handler(event, context):
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done x1.2')
    return {
        "statusCode": 200,
        "message": "Lambda executed successfully",
        "data": df.to_dict()
    }
