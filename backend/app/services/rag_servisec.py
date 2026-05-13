import logging
from app.services.tree_generate_service import generate_tree
import pageindex.utils as utils
import json
from app.services.llm_service import call_llm
from app.services.prompt_service import search_prompt,final_prompt
import asyncio
import logging
from app.core.config import DOC_ID

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True 
)

async def query_answer(query):
    
    doc_id=DOC_ID

    tree_result = generate_tree(doc_id)

    tree = tree_result['result']

    tree_without_text = utils.remove_fields(tree.copy(),fields=["text"])

    # # utils.print_tree(tree_without_text)

    search_prompt_templete = search_prompt(query,tree_without_text)

    logging.info("call llm for retrive data ")

    tree_search_result = await call_llm(search_prompt_templete)

    logging.info("finished retrive process")

    node_map = utils.create_node_mapping(tree)

    tree_search_result_json = json.loads(tree_search_result)

    # # utils.print_wrapped(tree_search_result_json['thinking'])

    # print('\nRetrieved Nodes:')
    for node_id in tree_search_result_json["node_list"]:
        node = node_map[node_id]
        print(f"Node ID: {node['node_id']}\t Page: {node['page_index']}\t Title: {node['title']}")

    node_list = json.loads(tree_search_result)["node_list"]

    relevant_content = "\n\n".join(node_map[node_id]["text"] for node_id in node_list)

    # utils.print_wrapped(relevant_content)

    answer_prompt = f"""
    Answer the question based on the context:

    Question: {query}
    Context: {relevant_content}

    Provide a clear, concise answer based only on the context provided.
    """

    logging.info("start answer generation")

    answer = await call_llm(answer_prompt)
    
    return answer




# for single llm call 


# async def query_answer(query):
    
#     doc_id="pi-cmowt00vd05d601qvu5rtmvv9"

#     tree_result = generate_tree(doc_id)

#     tree = tree_result['result']

#     # tree_without_text = utils.remove_fields(tree.copy(),fields=["text"])

#     # # utils.print_tree(tree_without_text)

#     # search_prompt_templete = search_prompt(query,tree_without_text=)

#     logging.info("call llm for retrive data ")

#     # tree_search_result = await call_llm(search_prompt_templete)

#     final_prompt_templete = final_prompt(query,tree)

#     answer = await call_llm(final_prompt_templete)

#     logging.info("finished retrive process")

#     # node_map = utils.create_node_mapping(tree)

#     # tree_search_result_json = json.loads(tree_search_result)

#     # # utils.print_wrapped(tree_search_result_json['thinking'])

#     # print('\nRetrieved Nodes:')
#     # for node_id in tree_search_result_json["node_list"]:
#     #     node = node_map[node_id]
#     #     print(f"Node ID: {node['node_id']}\t Page: {node['page_index']}\t Title: {node['title']}")

#     # node_list = json.loads(tree_search_result)["node_list"]

#     # relevant_content = "\n\n".join(node_map[node_id]["text"] for node_id in node_list)

#     # utils.print_wrapped(relevant_content)

#     # answer_prompt = f"""
#     # Answer the question based on the context:

#     # Question: {query}
#     # Context: {relevant_content}

#     # Provide a clear, concise answer based only on the context provided.
#     # """

#     # logging.info("start answer generation")

#     # answer = await call_llm(answer_prompt)
    
#     return answer