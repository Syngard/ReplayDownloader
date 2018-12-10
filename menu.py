# Prints a menu and gets user choice for language/quality
def menu_choices(files):
    versions, resolutions = [], []
    for i in files:
        ver = files[i]['versionLibelle']
        if ver not in versions:
            versions.append(ver)
            print(">>>", ver)

    chosen_version = input(">>> Choice : ")

    for i in files:
        res = (str(files[i]['width']),str(files[i]['height']))
        if (files[i]['versionLibelle'] == chosen_version
                        and res not in resolutions):
            resolutions.append(res)
            print(">>>", res[0]+"x"+res[1])

    choosen_res = input(">>> Choice : ").split('x')
    choosen_res = (int(choosen_res[0]), int(choosen_res[1]))

    # Finding the identifier for the right version 
    for i in files:
        if (files[i]['versionLibelle'] == chosen_version and
            (files[i]['width'],files[i]['height']) == choosen_res and
            files[i]['mediaType'] == "mp4"):
            video_id = i
            video_url = files[i]['url']
            break

    print(video_id,":",video_url)
    return video_url
