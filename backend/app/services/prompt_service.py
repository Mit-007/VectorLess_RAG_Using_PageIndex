import json


def search_prompt(query,tree_without_text):
    return f"""
    You are given a question and a tree structure of a document.
    Each node contains a node id, node title, and a corresponding summary.
    Your task is to find all nodes that are likely to contain the answer to the question.

    Question: {query}

    Document tree structure:
    {json.dumps(tree_without_text, indent=2)}

    Return ONLY valid raw JSON.

    strictly Do NOT:
    - use markdown
    - use ```json
    - add explanations
    - add extra text


    Please reply in the following JSON format:
    {{
        "thinking": "<Your thinking process on which nodes are relevant to the question>",
        "node_list": ["node_id_1", "node_id_2", ..., "node_id_n"]
    }}
    Directly return the final RAW JSON structure. Do not output anything else.
    """

def final_prompt(query ,tree ):
    return f"""
    You are an intelligent assistant that answers questions using a hierarchical document tree.

    You will be given:
    1. A user query
    2. A document tree containing:
    - Topic nodes (section titles + short summaries)
    - Detailed text nodes under each topic

    ---

    YOUR TASK:

    Step 1: Topic Filtering (IMPORTANT)
    - First read ONLY the topic-level nodes (titles + summaries).
    - Identify which topics are relevant to the user query.
    - Do NOT read full text nodes initially.

    Step 2: Deep Reading (ONLY if required)
    - If topic summary is not sufficient OR the answer is incomplete,
    then go deeper into the relevant topic’s child text nodes.
    - Avoid reading unrelated branches.

    Step 3: Answer Generation
    - Combine only relevant information.
    - Generate a clear, direct final answer.

    ---

    STRICT RULES:
    - Do NOT read the entire tree blindly
    - Do NOT process unrelated branches
    - Do NOT mention tree structure in output
    - Do NOT say "retrieved data"
    - Do NOT show steps or reasoning
    - Only output final answer

    If the answer is not found in any relevant topic:
    → Say: "The information is not available in the provided document."

    ---

    INPUT FORMAT:

    QUERY:
    {query}

    DOCUMENT TREE:
    {tree}

    ---

    OUTPUT:
    Return ONLY the final answer.
    """