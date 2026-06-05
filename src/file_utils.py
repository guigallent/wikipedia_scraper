def get_urls(leaders_list):
    """
    This function returns a dictionary where each key is a formatted string containing the leader's full name and mandate dates, and the value is the link to their Wikipedia page.
    """
    return {
        f"{leader['first_name']} {leader['last_name']} ({leader.get('start_mandate', 'unknown')} - {leader.get('end_mandate', 'present')})": leader["wikipedia_url"]
        for leader in leaders_list
    }
