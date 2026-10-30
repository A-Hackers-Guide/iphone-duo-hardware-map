# `CBFrameLink`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBClockSource`
- 6 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"NSObject<OS_dispatch_queue>" _queue;
@"CADisplayLink" _displayLink;
@? _frameNotificationBlock;
@"CBSharedFrameLinkRunLoop" _runLoopRef;
Q _frameSignpostID;
```

## Properties

```
@property (TQ,V_frameSignpostID) frameSignpostID;
@property (TQ,R,N) nextFrameTimestamp;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBFrameLink initWithDisplay:];
-[CBFrameLink pause];
-[CBFrameLink copyStatusInfo];
-[CBFrameLink isPaused];
-[CBFrameLink dealloc];
-[CBFrameLink setPreferredFramesPerSecond:];
-[CBFrameLink invalidate];
-[CBFrameLink resume];
-[CBFrameLink frameSignpostID];
-[CBFrameLink frameSync:];
-[CBFrameLink nextFrameTimestamp];
-[CBFrameLink scheduleWithDispatchQueue:];
-[CBFrameLink setFrameNotificationBlock:];
-[CBFrameLink setFrameSignpostID:];
```
