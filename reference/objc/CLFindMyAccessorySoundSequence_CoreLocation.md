# `CLFindMyAccessorySoundSequence`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 10 instance methods, 4 class methods

## Instance variables

```
@"NSMutableData" _encodedSequence;
Q _type;
```

## Properties

```
@property (T@"NSData",R) encodedSequence;
@property (TQ,R,V_type) type;
```

## Class methods

```
+[CLFindMyAccessorySoundSequence supportsSecureCoding];
+[CLFindMyAccessorySoundSequence defaultSequence];
+[CLFindMyAccessorySoundSequence rangingSequence];
+[CLFindMyAccessorySoundSequence shortSequence];
```

## Instance methods

```
-[CLFindMyAccessorySoundSequence init];
-[CLFindMyAccessorySoundSequence initWithType:];
-[CLFindMyAccessorySoundSequence dealloc];
-[CLFindMyAccessorySoundSequence type];
-[CLFindMyAccessorySoundSequence encodeWithCoder:];
-[CLFindMyAccessorySoundSequence initWithCoder:];
-[CLFindMyAccessorySoundSequence copyWithZone:];
-[CLFindMyAccessorySoundSequence encodedSequence];
-[CLFindMyAccessorySoundSequence addSoundBlockWithAsset:loopCount:duration:];
-[CLFindMyAccessorySoundSequence initWithType:encodedSequence:];
```
