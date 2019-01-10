def numUniqueEmails(emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    ls = []
    for email in emails:
        email = email.split("@")
        local_name = email[0]
        domain_name = email[1]
        if "+" in local_name:
            index = local_name.index("+")
            local_name = local_name[0:index]
            local_name = local_name.replace(".","")
        name = local_name + domain_name
        if name not in ls:
            ls.append(name)
    return len(ls)




