# `BloomFilter`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"BitVector" _bitVector;
Q _numberOfBits;
Q _numberHashes;
I _seed;
Q _expectedNumberOfItems;
d _falsePositiveRate;
```

## Properties

```
@property (TI,R,V_seed) seed;
@property (TQ,R,V_expectedNumberOfItems) expectedNumberOfItems;
@property (Td,R,V_falsePositiveRate) falsePositiveRate;
```

## Class methods

```
+[BloomFilter supportsSecureCoding];
```

## Instance methods

```
-[BloomFilter seed];
-[BloomFilter add:];
-[BloomFilter encodeWithCoder:];
-[BloomFilter initWithCoder:];
-[BloomFilter contains:];
-[BloomFilter expectedNumberOfItems];
-[BloomFilter falsePositiveRate];
-[BloomFilter _loadBitVectorData:];
-[BloomFilter initWithExpectedNumberOfItems:falsePositiveRate:seed:];
```
