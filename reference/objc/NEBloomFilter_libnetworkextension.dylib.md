# `NEBloomFilter`

- Image: [`/usr/lib/libnetworkextension.dylib`](../userland/usr__lib__libnetworkextension.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 7 properties, 20 instance methods, 7 class methods

## Instance variables

```
I _numberOfItems;
I _numberOfBits;
I _numberOfHashes;
I _murmurSeed;
d _falsePositiveTolerance;
@"NSData" _tag;
@"NSData" _bitVectorBuffer;
@"NEBitVector" _bitVector;
```

## Properties

```
@property (TI,N,V_numberOfItems) numberOfItems;
@property (Td,N,V_falsePositiveTolerance) falsePositiveTolerance;
@property (TI,N,V_numberOfBits) numberOfBits;
@property (TI,N,V_numberOfHashes) numberOfHashes;
@property (TI,N,V_murmurSeed) murmurSeed;
@property (T@"NSData",&,N,V_tag) tag;
@property (T@"NSData",&,N,V_bitVectorBuffer) bitVectorBuffer;
```

## Class methods

```
+[NEBloomFilter getNumberOfHashes:numberOfBits:];
+[NEBloomFilter containsWithBitmap:numberOfBits:numberOfHashes:murmurSeed:value:];
+[NEBloomFilter getFalsePositiveProbability:numberOfBits:numberOfHashes:];
+[NEBloomFilter getNumberOfBits:falsePositiveTolerance:];
+[NEBloomFilter insertWithBitmap:numberOfBits:numberOfHashes:murmurSeed:value:];
+[NEBloomFilter mmapFromFile:bloomFilter:];
+[NEBloomFilter mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:tag:];
```

## Instance methods

```
-[NEBloomFilter numberOfItems];
-[NEBloomFilter setTag:];
-[NEBloomFilter falsePositiveTolerance];
-[NEBloomFilter tag];
-[NEBloomFilter contains:];
-[NEBloomFilter initFromFile:];
-[NEBloomFilter setNumberOfItems:];
-[NEBloomFilter insert:];
-[NEBloomFilter bitVectorBuffer];
-[NEBloomFilter getFilterTag];
-[NEBloomFilter initWithData:numberOfBits:numberOfHashes:murmurSeed:mmapFilename:tag:];
-[NEBloomFilter initWithNumberOfItems:falsePositiveTolerance:];
-[NEBloomFilter murmurSeed];
-[NEBloomFilter numberOfBits];
-[NEBloomFilter numberOfHashes];
-[NEBloomFilter setBitVectorBuffer:];
-[NEBloomFilter setFalsePositiveTolerance:];
-[NEBloomFilter setMurmurSeed:];
-[NEBloomFilter setNumberOfBits:];
-[NEBloomFilter setNumberOfHashes:];
```
