# `FaceDetectionANSTRGBObserverImpl`

- Image: [`/usr/lib/libBasebandManagerICE.dylib`](../userland/usr__lib__libBasebandManagerICE.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVCaptureMetadataOutputObjectsDelegate`
- 17 instance variables, 4 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"CMCaptureFrameReceiver" fFrameReceiver;
{function<void (FaceDetectionANSTRGBDelegate::FaceDetectionInfo)>="__f_"{__value_func<void (FaceDetectionANSTRGBDelegate::FaceDetectionInfo)>="__buf_"(type="__data"[24C])"__f_"^v}} fCallback;
^{dispatch_queue_s=} fQueue;
B fKeyPathOn;
@"NSDate" fPreviousTime;
@"AVCaptureSession" fAVCaptureSession;
@"AVCaptureMetadataOutput" fAVCaptureMetadataOutput;
@"AVCaptureDeviceInput" fAVCaptureInput;
@"AVCaptureDevice" fDevice;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} fMetadataOutputRectangleOfInterest;
{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}} fCam1Defaults;
{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}} fCam2Defaults;
{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}} fCam1Override;
{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}} fCam2Override;
f fCurrentDistance;
B fFrontCameraState;
B fIsStopped;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FaceDetectionANSTRGBObserverImpl observeValueForKeyPath:ofObject:change:context:];
-[FaceDetectionANSTRGBObserverImpl stop];
-[FaceDetectionANSTRGBObserverImpl dealloc];
-[FaceDetectionANSTRGBObserverImpl start];
-[FaceDetectionANSTRGBObserverImpl registerHandler:];
-[FaceDetectionANSTRGBObserverImpl init:];
-[FaceDetectionANSTRGBObserverImpl captureOutput:didOutputMetadataObjects:fromConnection:];
-[FaceDetectionANSTRGBObserverImpl cameraTypeFromPort:];
-[FaceDetectionANSTRGBObserverImpl computeDistanceDeltaBucket:threshold:];
-[FaceDetectionANSTRGBObserverImpl getCurrentDistance];
-[FaceDetectionANSTRGBObserverImpl getFaceDetectionDistanceMaxForCamera:];
-[FaceDetectionANSTRGBObserverImpl getFaceDetectionDistanceMinForCamera:];
-[FaceDetectionANSTRGBObserverImpl handleNewFrameSenderEndpoints:];
-[FaceDetectionANSTRGBObserverImpl isFrontCameraOn:];
-[FaceDetectionANSTRGBObserverImpl notifyClient:frontCameraOn:sourceFromCMCapture:camera:];
-[FaceDetectionANSTRGBObserverImpl setFaceDetectionDistanceMax:forCamera:];
-[FaceDetectionANSTRGBObserverImpl setFaceDetectionDistanceMin:forCamera:];
-[FaceDetectionANSTRGBObserverImpl thresholdForCamera:];
```
