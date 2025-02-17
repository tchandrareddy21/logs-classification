import pandas as pd
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse
from logger import logging
from exception import  LoggerException
from pipeline.classifier import classify
import io

app = FastAPI()


@app.post("/classify/")
async def classify_logs(file: UploadFile):
    if not file.filename.endswith('.csv'):
        logging.error(f"File type not supported. File must be .csv {file}")
        raise HTTPException(status_code=400, detail="File must be a CSV.")

    try:
        # Read the uploaded CSV
        # df = pd.read_csv(file.file)
        logging.info("Reading file")
        # df = pd.read_csv(io.StringIO(file.file.read().decode("utf-8")))
        content = await file.read()
        df = pd.read_csv(io.StringIO(content.decode("utf-8")))
        if "source" not in df.columns or "log_message" not in df.columns:
            logging.error("Missing source and log_message columns in file.")
            raise HTTPException(status_code=400, detail="CSV must contain 'source' and 'log_message' columns.")

        # Perform classification
        logging.info("Calling classify function.")
        df["target_label"] = classify(list(zip(df["source"], df["log_message"])))
        logging.info("Classified successfully.")

        logging.info(f"Dataframe: {df.to_dict()}")

        # Save the modified file
        output_file = "classified_logs.csv"
        df.to_csv(output_file, index=False)
        logging.info("File saved to classified_logs.csv")
        return FileResponse(output_file, media_type='text/csv')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        file.file.close()