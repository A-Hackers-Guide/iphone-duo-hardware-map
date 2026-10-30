# `CAMCaptureRequestIntervalometer`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"CAMCaptureRequest" _prototypeRequest;
@"<CAMCaptureRequestIntervalometerDelegate>" _delegate;
d _interval;
d _delay;
q _maximumCount;
q _remaining;
@"CAMPreciseTimer" __timer;
```

## Properties

```
@property (Tq,N,V_remaining) remaining;
@property (T@"CAMPreciseTimer",R,N,V__timer) _timer;
@property (T@"CAMCaptureRequest",C,N,V_prototypeRequest) prototypeRequest;
@property (T@"<CAMCaptureRequestIntervalometerDelegate>",R,W,N,V_delegate) delegate;
@property (Td,R,N,V_interval) interval;
@property (Td,R,N,V_delay) delay;
@property (Tq,R,N,V_maximumCount) maximumCount;
```

## Instance methods

```
-[CAMCaptureRequestIntervalometer _timer];
-[CAMCaptureRequestIntervalometer interval];
-[CAMCaptureRequestIntervalometer init];
-[CAMCaptureRequestIntervalometer delay];
-[CAMCaptureRequestIntervalometer delegate];
-[CAMCaptureRequestIntervalometer remaining];
-[CAMCaptureRequestIntervalometer setRemaining:];
-[CAMCaptureRequestIntervalometer maximumCount];
-[CAMCaptureRequestIntervalometer _generateRequestForDelegate];
-[CAMCaptureRequestIntervalometer initWithDelegate:interval:delay:maximumCount:];
-[CAMCaptureRequestIntervalometer manuallyGenerateRequest];
-[CAMCaptureRequestIntervalometer prototypeRequest];
-[CAMCaptureRequestIntervalometer setPrototypeRequest:];
-[CAMCaptureRequestIntervalometer startGeneratingRequests];
-[CAMCaptureRequestIntervalometer stopGeneratingRequests];
```
