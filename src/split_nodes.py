# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#   new_nodes = []
#   for node in old_nodes:
    
#     if node.text_type == "text":
#       text = node.text
#       start_index = text.find(delimiter)
#       if start_index != -1:
#         # get text froom start to start_index ?
#         new_node = TextNode(text[:start_index], "text")
#         new_nodes.append(new_node)
#         # find closing delimiter
#         end_index = text.find(delimiter, start_index + len(delimiter))
#         if end_index == -1:
#           raise Exception("Invalid Markdown: No closing delimiter.")
#         else:
#           # add text between delim as other text type
#           delimited_text = text[start_index + len(delimiter):end_index]
#           new_nodes.append(TextNode(delimited_text, text_type))

#       else:
#         new_nodes.append(node)
#     else:
#       new_nodes.append(node)
#   return new_nodes

  
from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == "text":
            text = node.text
            while delimiter in text:
                start_index = text.find(delimiter)
                if start_index > 0:
                    new_nodes.append(TextNode(text[:start_index], "text"))
                
                end_index = text.find(delimiter, start_index + len(delimiter))
                if end_index == -1:
                    raise ValueError("Invalid Markdown: No closing delimiter.")
                
                delimited_text = text[start_index + len(delimiter):end_index]
                new_nodes.append(TextNode(delimited_text, text_type))
                
                text = text[end_index + len(delimiter):]
            
            if text:
                new_nodes.append(TextNode(text, "text"))
        else:
            new_nodes.append(node)
    return new_nodes