# `CADisplayLink`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 17 properties, 33 instance methods, 17 class methods

## Instance variables

```
^v _impl;
```

## Properties

```
@property (T@"CADisplay",R,N) display;
@property (T@,&,N) userInfo;
@property (Tq,N) priority;
@property (Td,R,N) maximumRefreshRate;
@property (Td,R,N) heartbeatRate;
@property (Tq,R,N) minimumFrameDuration;
@property (Tq,R,N) actualFramesPerSecond;
@property (TB,R,N) active;
@property (TI) highFrameRateReason;
@property (Td) localEarlyWakeupOffset;
@property (Td,R,N) timestamp;
@property (Td,R,N) duration;
@property (Td,R,N) targetTimestamp;
@property (TB,N,GisPaused) paused;
@property (Tq,N) frameInterval;
@property (Tq,N) preferredFramesPerSecond;
@property (T{CAFrameRateRange=fff},N) preferredFrameRateRange;
```

## Class methods

```
+[CADisplayLink overrideDisplayLinksForDisplayID:withTimingFromSystemIdentifier:];
+[CADisplayLink displayLinkWithTarget:selector:];
+[CADisplayLink dispatchDeferredDisplayLinks];
+[CADisplayLink displayLinkWithSystemIdentifier:target:selector:];
+[CADisplayLink dispatchDeferredDisplayLinksWithDisplayId:];
+[CADisplayLink displayLinkWithDisplay:target:selector:];
+[CADisplayLink automaticallyNotifiesObserversOfDisplay];
+[CADisplayLink expectedWakeupBeforeCommitDeadline:];
+[CADisplayLink supportsExpectedWakeupBeforeCommitDeadline];
+[CADisplayLink setWillFireHandler:];
+[CADisplayLink notifyDisplayChange:];
+[CADisplayLink willFireInfoVersion];
+[CADisplayLink expectedWakeupBeforeCommitDeadline:forDisplayWithId:];
+[CADisplayLink dispatchDeferredDisplayLink:];
+[CADisplayLink earlyWakeupOffset];
+[CADisplayLink _displayLinkWithDisplay:target:selector:skipsOverrides:];
+[CADisplayLink setEarlyWakeupOffset:];
```

## Instance methods

```
-[CADisplayLink maximumRefreshRate];
-[CADisplayLink setHighFrameRateReason:];
-[CADisplayLink active];
-[CADisplayLink targetTimestamp];
-[CADisplayLink priority];
-[CADisplayLink heartbeatRate];
-[CADisplayLink isPaused];
-[CADisplayLink display];
-[CADisplayLink setFrameInterval:];
-[CADisplayLink updateTimingUsingSystemIdentifier:];
-[CADisplayLink setPreferredFrameRateRange:];
-[CADisplayLink setPriority:];
-[CADisplayLink userInfo];
-[CADisplayLink minimumFrameDuration];
-[CADisplayLink dealloc];
-[CADisplayLink timestamp];
-[CADisplayLink setUserInfo:];
-[CADisplayLink setPreferredFramesPerSecond:];
-[CADisplayLink highFrameRateReason];
-[CADisplayLink preferredFrameRateRange];
-[CADisplayLink duration];
-[CADisplayLink actualFramesPerSecond];
-[CADisplayLink removeFromRunLoop:forMode:];
-[CADisplayLink invalidate];
-[CADisplayLink setPaused:];
-[CADisplayLink frameInterval];
-[CADisplayLink preferredFramesPerSecond];
-[CADisplayLink setHighFrameRateReasons:count:];
-[CADisplayLink _swapToDisplay:];
-[CADisplayLink addToRunLoop:forMode:];
-[CADisplayLink setLocalEarlyWakeupOffset:];
-[CADisplayLink _initWithDisplayLinkItem:];
-[CADisplayLink localEarlyWakeupOffset];
```
