# `ICDocCamPhotoCaptureDelegate`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVCapturePhotoCaptureDelegate`
- 10 instance variables, 14 properties, 31 instance methods, 0 class methods

## Instance variables

```
B _constantColorDeliveredFallBackPhoto;
B _constantColorDeliveredOriginalPhoto;
f _highestSharpness;
f _constantColorCenterWeightedMeanConfidenceLevel;
@"AVCapturePhotoSettings" _requestedPhotoSettings;
@"NSDictionary" _metaData;
^{__CVBuffer=} _pbRef;
@"NSMutableDictionary" _imageAttributes;
@? _willCapturePhotoAnimation;
@? _completed;
```

## Properties

```
@property (T@"AVCapturePhotoSettings",&,N,V_requestedPhotoSettings) requestedPhotoSettings;
@property (T@"NSDictionary",&,N,V_metaData) metaData;
@property (T^{__CVBuffer=},N,V_pbRef) pbRef;
@property (Tf,N,V_highestSharpness) highestSharpness;
@property (T@"NSMutableDictionary",&,N,V_imageAttributes) imageAttributes;
@property (Tf,N,V_constantColorCenterWeightedMeanConfidenceLevel) constantColorCenterWeightedMeanConfidenceLevel;
@property (TB,N,V_constantColorDeliveredFallBackPhoto) constantColorDeliveredFallBackPhoto;
@property (TB,N,V_constantColorDeliveredOriginalPhoto) constantColorDeliveredOriginalPhoto;
@property (T@?,C,N,V_willCapturePhotoAnimation) willCapturePhotoAnimation;
@property (T@?,C,N,V_completed) completed;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ICDocCamPhotoCaptureDelegate setCompleted:];
-[ICDocCamPhotoCaptureDelegate completed];
-[ICDocCamPhotoCaptureDelegate setMetaData:];
-[ICDocCamPhotoCaptureDelegate captureOutput:willBeginCaptureForResolvedSettings:];
-[ICDocCamPhotoCaptureDelegate constantColorCenterWeightedMeanConfidenceLevel];
-[ICDocCamPhotoCaptureDelegate metaData];
-[ICDocCamPhotoCaptureDelegate captureOutput:didFinishRecordingLivePhotoMovieForEventualFileAtURL:resolvedSettings:];
-[ICDocCamPhotoCaptureDelegate dealloc];
-[ICDocCamPhotoCaptureDelegate captureOutput:didFinishProcessingPhoto:error:];
-[ICDocCamPhotoCaptureDelegate captureOutput:didFinishCaptureForResolvedSettings:error:];
-[ICDocCamPhotoCaptureDelegate didFinish];
-[ICDocCamPhotoCaptureDelegate setConstantColorCenterWeightedMeanConfidenceLevel:];
-[ICDocCamPhotoCaptureDelegate captureOutput:willCapturePhotoForResolvedSettings:];
-[ICDocCamPhotoCaptureDelegate captureOutput:didFinishProcessingLivePhotoToMovieFileAtURL:duration:photoDisplayTime:resolvedSettings:error:];
-[ICDocCamPhotoCaptureDelegate captureOutput:didFinishProcessingPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:];
-[ICDocCamPhotoCaptureDelegate imageAttributes];
-[ICDocCamPhotoCaptureDelegate constantColorDeliveredFallBackPhoto];
-[ICDocCamPhotoCaptureDelegate constantColorDeliveredOriginalPhoto];
-[ICDocCamPhotoCaptureDelegate highestSharpness];
-[ICDocCamPhotoCaptureDelegate initWithRequestedPhotoSettings:willCapturePhotoAnimation:completed:];
-[ICDocCamPhotoCaptureDelegate pbRef];
-[ICDocCamPhotoCaptureDelegate requestedPhotoSettings];
-[ICDocCamPhotoCaptureDelegate setConstantColorDeliveredFallBackPhoto:];
-[ICDocCamPhotoCaptureDelegate setConstantColorDeliveredOriginalPhoto:];
-[ICDocCamPhotoCaptureDelegate setHighestSharpness:];
-[ICDocCamPhotoCaptureDelegate setImageAttributes:];
-[ICDocCamPhotoCaptureDelegate setPbRef:];
-[ICDocCamPhotoCaptureDelegate setRequestedPhotoSettings:];
-[ICDocCamPhotoCaptureDelegate setWillCapturePhotoAnimation:];
-[ICDocCamPhotoCaptureDelegate sharpnessForImageBuffer:];
-[ICDocCamPhotoCaptureDelegate willCapturePhotoAnimation];
```
