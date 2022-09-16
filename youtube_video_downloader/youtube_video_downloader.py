import pytube
link = input('Enter The Youtube Video URL')
dn = pytube.Youtube(link)
dn.streams.first().download()
print('Your Video Has Been Downloaded', link)