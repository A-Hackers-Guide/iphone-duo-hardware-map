# `CBDisplayClockSourceAdapter`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBClockSource`
- 4 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
^{__Display=} _display;
f _preferredFramesPerSecond;
B _running;
Q _nextFrameTimestamp;
```

## Properties

```
@property (TQ,R,N,V_nextFrameTimestamp) nextFrameTimestamp;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBDisplayClockSourceAdapter pause];
-[CBDisplayClockSourceAdapter copyStatusInfo];
-[CBDisplayClockSourceAdapter setPreferredFramesPerSecond:];
-[CBDisplayClockSourceAdapter invalidate];
-[CBDisplayClockSourceAdapter resume];
-[CBDisplayClockSourceAdapter initWithDisplayRef:];
-[CBDisplayClockSourceAdapter nextFrameTimestamp];
-[CBDisplayClockSourceAdapter scheduleWithDispatchQueue:];
-[CBDisplayClockSourceAdapter setFrameNotificationBlock:];
```
