from app.services.tree_generate_service import generate_tree
import pageindex.utils as utils

def print_tree_test(doc_id):
    tree_result = generate_tree(doc_id)
    tree = tree_result['result']
    tree_without_text = utils.remove_fields(tree.copy(),fields=["text"])
    utils.print_tree(tree_without_text)