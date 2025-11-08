"""
Netlify serverless function for handling RAG queries
"""
import os
import json
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent.parent))

try:
    from rag_pipeline import RAGPipeline
except ImportError:
    # Handle import errors gracefully
    RAGPipeline = None

# Initialize pipeline (cached across invocations)
pipeline = None

def init_pipeline():
    """Initialize RAG pipeline (cached)"""
    global pipeline
    if pipeline is None:
        try:
            if RAGPipeline is None:
                return None
            pipeline = RAGPipeline()
        except Exception as e:
            print(f"Error initializing pipeline: {e}")
            import traceback
            traceback.print_exc()
            return None
    return pipeline

def handler(event, context):
    """Handle incoming requests"""
    # Handle CORS
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
    }
    
    # Handle OPTIONS request
    if event["httpMethod"] == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": headers,
            "body": ""
        }
    
    try:
        # Get query from request
        if event["httpMethod"] == "GET":
            query = event.get("queryStringParameters", {}).get("q", "")
        else:
            body = json.loads(event.get("body", "{}"))
            query = body.get("query", "")
        
        if not query:
            return {
                "statusCode": 400,
                "headers": headers,
                "body": json.dumps({"error": "Query parameter is required"})
            }
        
        # Initialize pipeline
        rag_pipeline = init_pipeline()
        if rag_pipeline is None:
            return {
                "statusCode": 500,
                "headers": headers,
                "body": json.dumps({"error": "Pipeline initialization failed. Please ensure OPENAI_API_KEY is set and vector store is initialized."})
            }
        
        # Generate response
        response = rag_pipeline.generate_response(query)
        
        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps({
                "answer": response["answer"],
                "source": response["source"],
                "is_advice": response["is_advice"]
            })
        }
        
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": headers,
            "body": json.dumps({"error": str(e)})
        }

