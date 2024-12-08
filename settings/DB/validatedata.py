def validate_data(data, schema):
    """
    Validate data against a schema.

    :param data: dict - The input data to validate.
    :param schema: dict - The schema defining required fields and types.
    :return: tuple (bool, str) - (Validation success, Message/Error).
    """
    for field, rules in schema.items():
        # Check if the field is required and present
        if rules.get("required") and field not in data:
            return False, f"'{field}' is required."
        
        # Check type if the field exists
        if field in data and not isinstance(data[field], rules["type"]):
            return False, f"'{field}' must be of type {rules['type'].__name__}."
    
    return True, "Validation passed."
