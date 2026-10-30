# `BrightnessSequenceQueue`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
d _timeFactor;
d _sequenceStartTime;
Q _currentUpdateID;
@"NSArray" _flipbook;
```

## Properties

```
@property (Td,V_sequenceStartTime) sequenceStartTime;
@property (TB,R) isDone;
@property (TQ,R,V_currentUpdateID) currentUpdateID;
@property (T@"NSArray",R,V_flipbook) flipbook;
```

## Instance methods

```
-[BrightnessSequenceQueue dealloc];
-[BrightnessSequenceQueue flipbook];
-[BrightnessSequenceQueue isDone];
-[BrightnessSequenceQueue currentUpdateID];
-[BrightnessSequenceQueue absoluteTimestampForUpdate:];
-[BrightnessSequenceQueue initWithArrayOfUpdates:];
-[BrightnessSequenceQueue nextUpdate];
-[BrightnessSequenceQueue sequenceStartTime];
-[BrightnessSequenceQueue setSequenceStartTime:];
```
