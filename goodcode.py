def process(d):
    """Process the status of a dictionary and print the corresponding message.
    :param d: Dictionary containing 'status' key."""
    # Status mappings in simple dictionary
    status_message = {
        'active': 'Active',
        'inactive': 'Inactive'
    }
    # Get status from dictionary, default to 'Unknown' if not found
    status = d.get('status', 'unknown')
    # Print corresponding message or 'Unknown' if the status doesn't match
    print(status_message.get(status, 'Unknown'))

