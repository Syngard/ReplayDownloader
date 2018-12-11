# Prints a menu and gets user choice for language/quality
def menu_choices(files, default_ver = None, default_res = None):
    """Select language/resolution from available options
    
    :param files:
        JSON file containing the description for all available versions
    :type files: dict
    
    TODO : Take a default version and a default resolution as parameters
            Select highest res when unspecified

    :rtype: str
    :returns:
        URL of the video file with the choosen options
    """

    versions      = []
    versions_dict = {}
    c             = 1
    for i in files:
        ver = files[i]['versionLibelle']
        if ver not in versions:
            versions.append(ver)
            versions_dict[c] = ver
            print(">>>", c, ':', ver)
            c+=1

    chosen_version = versions_dict[int(input(">>> Choice : "))]

    resolutions      = []
    resolutions_dict = {}
    c                = 1
    for i in files:
        res = (files[i]['width'],files[i]['height'])
        if (
                files[i]['versionLibelle'] == chosen_version and 
                res not in resolutions
            ):

            resolutions.append(res)
            resolutions_dict[c] = res
            print(">>>", c, ':', str(res[0])+"x"+str(res[1]))
            c += 1

    chosen_res = resolutions_dict[int(input(">>> Choice : "))]
    
    # Finding the URL for the right version 
    for i in files:
        if (
                files[i]['versionLibelle'] == chosen_version and
                (files[i]['width'],files[i]['height']) == chosen_res and
                files[i]['mediaType'] == "mp4"
            ):
            
            return files[i]['url']


