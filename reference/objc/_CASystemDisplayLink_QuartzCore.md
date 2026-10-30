# `_CASystemDisplayLink`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CADisplayLink`
- 11 instance variables, 0 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"CADisplayLink" _innerLink;
@"NSString" _systemIdentifier;
@"_CASystemDisplayLinkDispatcher" _dispatcher;
@"NSRunLoop" _dlRunloop;
@"NSMutableArray" _dlModes;
B _dlPaused;
{CAFrameRateRange="minimum"f"maximum"f"preferred"f} _dlPreferredFrameRateRange;
q _dlPriority;
@ _dlUserInfo;
B _scheduledSelfReference;
[4I] _dlReasons;
```

## Instance methods

```
-[_CASystemDisplayLink maximumRefreshRate];
-[_CASystemDisplayLink setHighFrameRateReason:];
-[_CASystemDisplayLink active];
-[_CASystemDisplayLink targetTimestamp];
-[_CASystemDisplayLink priority];
-[_CASystemDisplayLink heartbeatRate];
-[_CASystemDisplayLink isPaused];
-[_CASystemDisplayLink display];
-[_CASystemDisplayLink setFrameInterval:];
-[_CASystemDisplayLink initWithSystemIdentifier:display:target:selector:];
-[_CASystemDisplayLink updateTimingUsingSystemIdentifier:];
-[_CASystemDisplayLink setPreferredFrameRateRange:];
-[_CASystemDisplayLink setPriority:];
-[_CASystemDisplayLink userInfo];
-[_CASystemDisplayLink minimumFrameDuration];
-[_CASystemDisplayLink dealloc];
-[_CASystemDisplayLink timestamp];
-[_CASystemDisplayLink setUserInfo:];
-[_CASystemDisplayLink setPreferredFramesPerSecond:];
-[_CASystemDisplayLink highFrameRateReason];
-[_CASystemDisplayLink preferredFrameRateRange];
-[_CASystemDisplayLink duration];
-[_CASystemDisplayLink actualFramesPerSecond];
-[_CASystemDisplayLink removeFromRunLoop:forMode:];
-[_CASystemDisplayLink invalidate];
-[_CASystemDisplayLink setPaused:];
-[_CASystemDisplayLink recreateInnerLinkWithDisplay:];
-[_CASystemDisplayLink frameInterval];
-[_CASystemDisplayLink preferredFramesPerSecond];
-[_CASystemDisplayLink setHighFrameRateReasons:count:];
-[_CASystemDisplayLink _updateScheduledSelfReference];
-[_CASystemDisplayLink addToRunLoop:forMode:];
```
