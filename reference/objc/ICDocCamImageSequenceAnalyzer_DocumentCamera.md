# `ICDocCamImageSequenceAnalyzer`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _frameArray;
@"NSObject<OS_dispatch_semaphore>" _frameArraySem;
@"NSObject<OS_dispatch_queue>" _dq;
@"NSDictionary" _sessionOptions;
@? _callback;
@"NSObject<OS_dispatch_semaphore>" _queueSizeSem;
@"VNSequenceRequestHandler" _seqHandler;
B _bRealTime;
B _bSynchronous;
```

## Instance methods

```
-[ICDocCamImageSequenceAnalyzer finish];
-[ICDocCamImageSequenceAnalyzer dealloc];
-[ICDocCamImageSequenceAnalyzer addFrame:metaData:frameOptions:rectangleRequest:pixelFocalLength:cameraIntrinsicData:cropRegionOfInterest:];
-[ICDocCamImageSequenceAnalyzer initWithOptions:callback:];
```
