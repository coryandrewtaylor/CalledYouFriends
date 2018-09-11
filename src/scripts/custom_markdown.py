def convert(doc, lookup):
    """
    Given a lookup dict, replace custom Markdown elements in a document
    with their standard equivalents.
    
    Parameters
    ----------
    doc : str
        Document whose custom Markdown will be standardized.
    lookup : dict
        Lookup dict that drives this function. Should take the form
        `{'custom_element': 'standard_element'}`.
    
    Returns
    -------
    str
        Input document with standardized Markdown elements.
    
    """
    for tag in lookup:
        doc = doc.replace(tag, lookup[tag])

    return doc
