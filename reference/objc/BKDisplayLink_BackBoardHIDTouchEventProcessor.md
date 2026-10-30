# `BKDisplayLink`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 10 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
# _displayLinkClass;
@"CADisplay" _display;
@ _target;
: _action;
@"NSRunLoop" _runLoop;
@"NSThread" _thread;
@"CADisplayLink" _thread_displayLink;
B _thread_invalid;
B _paused;
@"NSString" _displayUUID;
```

## Properties

```
@property (T@"NSString",C,N,V_displayUUID) displayUUID;
@property (TB,N,GisPaused) paused;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKDisplayLink isPaused];
-[BKDisplayLink displayUUID];
-[BKDisplayLink dealloc];
-[BKDisplayLink setDisplayUUID:];
-[BKDisplayLink invalidate];
-[BKDisplayLink setPaused:];
-[BKDisplayLink _thread_displayLinkFired];
-[BKDisplayLink _thread_invalidate];
-[BKDisplayLink _thread_setPaused:];
-[BKDisplayLink _thread_startRunLoop];
-[BKDisplayLink initWithDisplayLinkClass:display:target:action:];
```
