# `CAMetalDisplayLink`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
^v _impl;
@"<CAMetalDisplayLinkDelegate>" _delegate;
```

## Properties

```
@property (T@"<CAMetalDisplayLinkDelegate>",W,N,V_delegate) delegate;
@property (Tf,N) preferredFrameLatency;
@property (T{CAFrameRateRange=fff},N) preferredFrameRateRange;
@property (TB,N,GisPaused) paused;
```

## Instance methods

```
-[CAMetalDisplayLink isPaused];
-[CAMetalDisplayLink setPreferredFrameRateRange:];
-[CAMetalDisplayLink dealloc];
-[CAMetalDisplayLink preferredFrameRateRange];
-[CAMetalDisplayLink removeFromRunLoop:forMode:];
-[CAMetalDisplayLink invalidate];
-[CAMetalDisplayLink setPaused:];
-[CAMetalDisplayLink setDelegate:];
-[CAMetalDisplayLink delegate];
-[CAMetalDisplayLink addToRunLoop:forMode:];
-[CAMetalDisplayLink _initWithMetalLinkItem:];
-[CAMetalDisplayLink initWithMetalLayer:];
-[CAMetalDisplayLink preferredFrameLatency];
-[CAMetalDisplayLink setPreferredFrameLatency:];
```
