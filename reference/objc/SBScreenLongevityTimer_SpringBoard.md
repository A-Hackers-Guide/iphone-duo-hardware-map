# `SBScreenLongevityTimer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 8 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"SBScreenLongevitySettings" _settings;
@"NSTimer" _timer;
d _currentFaceDetectionTimerInterval;
d _startTime;
@"<SBScreenLongevityTimerDelegate>" _delegate;
d _waitInterval;
d _dimInterval;
d _minimalFaceDetectionInterval;
```

## Properties

```
@property (Td,N,V_waitInterval) waitInterval;
@property (Td,N,V_dimInterval) dimInterval;
@property (Td,N,V_minimalFaceDetectionInterval) minimalFaceDetectionInterval;
@property (T@"<SBScreenLongevityTimerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBScreenLongevityTimer elapsedTime];
-[SBScreenLongevityTimer init];
-[SBScreenLongevityTimer dealloc];
-[SBScreenLongevityTimer start];
-[SBScreenLongevityTimer invalidate];
-[SBScreenLongevityTimer setDelegate:];
-[SBScreenLongevityTimer isValid];
-[SBScreenLongevityTimer delegate];
-[SBScreenLongevityTimer setDimInterval:];
-[SBScreenLongevityTimer _isValidCurrentTimer:];
-[SBScreenLongevityTimer dimInterval];
-[SBScreenLongevityTimer dimTimerFired];
-[SBScreenLongevityTimer minimalFaceDetectionInterval];
-[SBScreenLongevityTimer scheduleFaceDetection];
-[SBScreenLongevityTimer setMinimalFaceDetectionInterval:];
-[SBScreenLongevityTimer setWaitInterval:];
-[SBScreenLongevityTimer startFaceDetection];
-[SBScreenLongevityTimer waitInterval];
```
