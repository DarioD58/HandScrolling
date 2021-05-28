from FileScroller import FileScroller
from TrackHand import HandTracking
from FileScroller import FileScroller

if __name__ == '__main__':
    handTracker = HandTracking()
    fileScroller = FileScroller()
    handTracker.attach(fileScroller)
    handTracker.trackHands()