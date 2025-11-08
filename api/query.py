"""
Vercel serverless function for handling RAG queries
"""
import os
import json
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

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

def handler(request):
    """Handle incoming requests (Vercel format)"""
    # Handle CORS
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
    }
    
    # Handle OPTIONS request
    if request.method == "OPTIONS":
        return {"statusCode": 200, "headers": headers, "body": ""}
    
    try:
        # Get query from request
        if request.method == "GET":
            query = request.args.get("q", "") if hasattr(request, 'args') else ""
        else:
            try:
                body = request.get_json() if hasattr(request, 'get_json') else json.loads(request.body)
                query = body.get("query", "") if body else ""
            except:
                query = ""
        
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
                "body": json.dumps({"error": "Pipeline initialization failed. Please check logs."})
            }
        
        # Generate response
        response = rag_pipeline.generate_response(query)
        
        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps({
                "answer": response["answer"],
                "source": response["source"],
                "is_advice": response.get("is_advice", False)
            })
        }
        
    except Exception as e:
        import traceback
        error_msg = str(e)
        traceback.print_exc()
        return {
            "statusCode": 500,
            "headers": headers,
            "body": json.dumps({"error": error_msg})
        }

# Vercel serverless function entry point
# Vercel automatically calls the handler function
# For explicit export, use: export default handler (but Python doesn't support this)
# Instead, Vercel will auto-detect the handler function

