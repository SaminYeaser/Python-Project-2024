import json

fileName = 'youtube.txt'


def loadData():
    try:
        with open(fileName, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return 'List Is Empty'
    
def save(videos):
    with open(fileName, 'w') as file:
        json.dump(videos, file)


def listAllVideos(videos):
    print('*' * 60)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} -> the duration is: {video['time']}")
    print('*' * 60)

def addVideo(video):
    name = input('Video Name: ')
    time = input('video Time: ')
    video.append({
        'name': name,
        'time': time
    })
    save(video)


def updateVideo(video):
    index = int(input('Which video you want to edit: '))
    print(video)
    if 1 <= index <= len(video):
        newName = input('Enter new name: ')
        newDuration = input('Enter new duration: ')
        video[index - 1]['name'] = newName
        video[index - 1]['time'] = newDuration
        save(video)
        listAllVideos(video)
    else:
        print('Invalid Data!')
    print('video edited!')

def deleteVideo(video):
    index = int(input('Which video you want to delete: '))

    if 1 <= index <= len(video):
        del video[index - 1]
        save(video)
        listAllVideos(video)

def main():
    videos = loadData()
    while True:
        print("\n Youtube Manager")
        print("1. List all favourite video")
        print("2. Add a youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        choice = input('Enter your choice: ')
        # print(videos)

        match choice: 
            case '1':
                listAllVideos(videos)
            case '2':
                addVideo(videos)
            case '3':
                updateVideo(videos)
            case '4':
                deleteVideo(videos)
            case '5':
                break
            case _:
                print('Invalid Choice')

if __name__ == '__main__':
    main()