# `CBClockSource` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 1 properties, 8 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) nextFrameTimestamp;
```

## Instance methods

```
-[CBClockSource pause];
-[CBClockSource copyStatusInfo];
-[CBClockSource setPreferredFramesPerSecond:];
-[CBClockSource invalidate];
-[CBClockSource resume];
-[CBClockSource nextFrameTimestamp];
-[CBClockSource scheduleWithDispatchQueue:];
-[CBClockSource setFrameNotificationBlock:];
```
