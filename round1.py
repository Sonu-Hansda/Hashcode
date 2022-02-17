# Initializing all variables

numberOfClient = int(input("Number of client : "))
itemLikes = []
itemDislikes = []

# Collecting the required data

def collectData():
    for client in range(numberOfClient):
        for choices in range(1,2):
            likes = int(input(f"Number of likes of client{client+1} : "))
            for like in range (likes):
                itemLikes.append(input(f'Item client{client+1} like ({like+1}): '))
            dislikes = int(input(f'Number of dislikes of client{client+1}: '))
            for dislike in range(dislikes):
                itemDislikes.append(input(f'Item client{client+1} don\'t like ({dislike+1}):'))

# Prepare recipe

def prepareRecipe():
    if(len(itemDislikes)>0):
        for likedItem in itemLikes:
            for dislikedItem in itemDislikes:
                if(likedItem == dislikedItem):
                    itemLikes.remove(dislikedItem)

# Serve recipe
def serve():
    print(len(itemLikes),end=' ')
    for item in itemLikes:
        print(item,end=' ')

if __name__ == '__main__':
    collectData()
    prepareRecipe()
    serve()