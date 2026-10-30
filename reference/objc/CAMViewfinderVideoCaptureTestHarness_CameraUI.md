# `CAMViewfinderVideoCaptureTestHarness`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMPerformanceTestHarness`
- Protocols: `CAMViewfinderViewControllerVideoCaptureRequestTestingDelegate`
- 7 instance variables, 11 properties, 18 instance methods, 0 class methods

## Instance variables

```
B __captureCTMVideo;
@? _startVideoHandler;
@? _endVideoHandler;
@"CAMViewfinderViewController" __viewfinderViewController;
d __videoDurationInSeconds;
d __initialDelayInSeconds;
d __postDelayInSeconds;
```

## Properties

```
@property (T@"CAMViewfinderViewController",&,N,V__viewfinderViewController) _viewfinderViewController;
@property (Td,R,N,V__videoDurationInSeconds) _videoDurationInSeconds;
@property (Td,R,N,V__initialDelayInSeconds) _initialDelayInSeconds;
@property (Td,R,N,V__postDelayInSeconds) _postDelayInSeconds;
@property (TB,R,N,V__captureCTMVideo) _captureCTMVideo;
@property (T@?,C,N,V_startVideoHandler) startVideoHandler;
@property (T@?,C,N,V_endVideoHandler) endVideoHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMViewfinderVideoCaptureTestHarness endVideoHandler];
-[CAMViewfinderVideoCaptureTestHarness _captureCTMVideo];
-[CAMViewfinderVideoCaptureTestHarness _endCaptureWithError:];
-[CAMViewfinderVideoCaptureTestHarness _initialDelayInSeconds];
-[CAMViewfinderVideoCaptureTestHarness _postDelayInSeconds];
-[CAMViewfinderVideoCaptureTestHarness _startCapture];
-[CAMViewfinderVideoCaptureTestHarness _videoDurationInSeconds];
-[CAMViewfinderVideoCaptureTestHarness _viewfinderViewController];
-[CAMViewfinderVideoCaptureTestHarness initWithTestName:viewfinderViewController:videoDurationInSeconds:initialDelayInSeconds:postDelayInSeconds:captureCTMVideo:];
-[CAMViewfinderVideoCaptureTestHarness setEndVideoHandler:];
-[CAMViewfinderVideoCaptureTestHarness setStartVideoHandler:];
-[CAMViewfinderVideoCaptureTestHarness set_viewfinderViewController:];
-[CAMViewfinderVideoCaptureTestHarness startTesting];
-[CAMViewfinderVideoCaptureTestHarness startVideoHandler];
-[CAMViewfinderVideoCaptureTestHarness stillImageRequestsWillRequestCTMVideoCaptureEndForViewfinderViewController:];
-[CAMViewfinderVideoCaptureTestHarness stillImageRequestsWillRequestCTMVideoCaptureStartForViewfinderViewController:];
-[CAMViewfinderVideoCaptureTestHarness viewfinderViewController:didReceiveVideoRequestDidCompleteCapture:withResponse:error:];
-[CAMViewfinderVideoCaptureTestHarness viewfinderViewController:didReceiveVideoRequestDidStartCapturing:];
```
