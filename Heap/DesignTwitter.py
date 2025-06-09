import heapq
from typing import List, Optional
class LinkedList:
    class Node:
        def __init__(self, val, timestamp, next=None, prev=None):
            self.val = val
            self.timestamp = timestamp
            self.next = next
            self.prev = prev

    def __init__(self):
        self.head = self.Node(val=None, timestamp=None)
        self.tail = self.Node(val=None, timestamp=None)
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0

    def insertHead(self, val, timestamp):
        nextNode = self.head.next
        newNode = self.Node(val, timestamp)
        self.head.next, newNode.prev = newNode, self.head
        newNode.next = nextNode
        if nextNode is not None:
            nextNode.prev = newNode
        self.size += 1

class Twitter:
 
    def __init__(self):
        self.users = set()
        self.followTable = dict() #{user: set[follow]}
        self.tweetTable = dict() #{userId: tweets} tweetsはLinkedListでheadから最新
        self.timestamp = 0
        self.USER = 0
        self.TWEET = 1

    def addNewUser(self, userId):
        self.users.add(userId)
        self.followTable[userId] = {userId}
        userTweets = LinkedList()
        self.tweetTable[userId] = userTweets

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.addNewUser(userId)
        linkedlist = self.tweetTable[userId]
        linkedlist.insertHead(tweetId, self.timestamp)
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            self.addNewUser(userId)
        numGet = 0
        res = list()
        heap = list()
        followingUsers = self.followTable[userId]
        for followingUser in followingUsers:
            if self.tweetTable[followingUser].size == 0:
                continue
            latestTweet = self.tweetTable[followingUser].head.next
            if latestTweet != self.tweetTable[followingUser].tail:
                heapq.heappush(heap, (-latestTweet.timestamp, latestTweet))

        while heap and numGet < 10:
            _, latestTweet = heapq.heappop(heap)
            res.append(latestTweet.val)
            numGet += 1
            nextTweet = latestTweet.next
            if nextTweet.val:
                heapq.heappush(heap, (-nextTweet.timestamp, nextTweet))
        # print(f"user:{userId}, following:{self.followTable[userId]}\nres:{res}\n")
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.addNewUser(followerId)
        if followeeId not in self.users:
            self.addNewUser(followeeId)
        self.followTable[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followTable[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)