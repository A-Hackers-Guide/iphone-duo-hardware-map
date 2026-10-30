# `BitVector`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
Q _bitsPerBlock;
Q _bitShift;
* _data;
q _numberOfBits;
Q _numberOfBytes;
@"NSData" _bvData;
```

## Properties

```
@property (Tq,R,V_numberOfBits) numberOfBits;
@property (TQ,R,V_numberOfBytes) numberOfBytes;
@property (T@"NSData",R,C,V_bvData) bvData;
```

## Instance methods

```
-[BitVector description];
-[BitVector testAtIndex:];
-[BitVector numberOfBits];
-[BitVector loadData:];
-[BitVector initWithNumberOfBits:];
-[BitVector numberOfBytes];
-[BitVector setAtIndex:];
-[BitVector bvData];
```
