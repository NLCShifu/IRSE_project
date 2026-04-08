from diagrams import Cluster, Diagram
from diagrams.programming.language import Python
from diagrams.generic.storage import Storage
from diagrams.generic.compute import Rack

with Diagram("Naive RAG Architecture", show=False, direction="LR"):
    user_query = Rack("User Query")

    with Cluster("Information Retrieval (IR) Subsystem"):
        encoder = Python("Encoding Function (fQ)")
        vector_db = Storage("Encoded Corpus (fD(D))")
        retriever = Python("Similarity Search (S)")
        
    with Cluster("LM Subsystem"):
        formatter = Python("Prompt Formatter (I)")
        llm = Rack("Mistral-7B-Instruct")

    user_query >> encoder >> retriever
    vector_db >> retriever >> formatter
    user_query >> formatter >> llm