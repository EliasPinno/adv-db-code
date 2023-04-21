class myHashTableBucket:
    class Bucket:
        def __init__(self, bucketSize):
            self.bucketSize = bucketSize
            self.contents = list()
            self.LinkedBucket: Bucket = None
            self.numElems = 0
        
        def addValue(self, value):
            # We need to create a new bucket and put our value in it
            if self.LinkedBucket == None and len(self.contents) >= bucketSize:
                self.LinkedBucket = Bucket(self.bucketSize)
                self.LinkedBucket
            

    def __init__(self, bucketSize, utilization, hashKeySize):
        self.bucketSize = bucketSize
        self.utilization = utilization
        self.hashKeySize = hashKeySize
        self.buckets
    
    



if __name__ == "__main__":
    bucketSize = 2
    hashKeySize = 4
    utilization = 0.85


