# `CAMVideoCaptureResult`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 14 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _slowWriterFrameDrops;
@"NSURL" _localDestinationURL;
@"NSURL" _filteredLocalDestinationURL;
{?="width"i"height"i} _dimensions;
@"NSArray" _metadata;
d _videoZoomFactor;
q _reason;
^{__CVBuffer=} _videoPreviewPixelBuffer;
@"NSDate" _captureDate;
@"CAMCaptureCoordinationInfo" _coordinationInfo;
@"NSError" _error;
{?="value"q"timescale"i"flags"I"epoch"q} _duration;
{?="value"q"timescale"i"flags"I"epoch"q} _stillDisplayTime;
```

## Properties

```
@property (T@"NSURL",R,N,V_localDestinationURL) localDestinationURL;
@property (T@"NSURL",R,N,V_filteredLocalDestinationURL) filteredLocalDestinationURL;
@property (T{?=qiIq},R,N,V_duration) duration;
@property (T{?=qiIq},R,N,V_stillDisplayTime) stillDisplayTime;
@property (T{?=ii},R,N,V_dimensions) dimensions;
@property (T@"NSArray",R,C,N,V_metadata) metadata;
@property (Td,R,N,V_videoZoomFactor) videoZoomFactor;
@property (Tq,R,N,V_reason) reason;
@property (TB,R,N) stoppedUnexpectedly;
@property (TB,R,N,V_slowWriterFrameDrops) slowWriterFrameDrops;
@property (T^{__CVBuffer=},R,N,V_videoPreviewPixelBuffer) videoPreviewPixelBuffer;
@property (T@"NSDate",R,N,V_captureDate) captureDate;
@property (T@"CAMCaptureCoordinationInfo",R,N,V_coordinationInfo) coordinationInfo;
@property (T@"NSError",R,N,V_error) error;
```

## Instance methods

```
-[CAMVideoCaptureResult videoZoomFactor];
-[CAMVideoCaptureResult dimensions];
-[CAMVideoCaptureResult slowWriterFrameDrops];
-[CAMVideoCaptureResult captureDate];
-[CAMVideoCaptureResult filteredLocalDestinationURL];
-[CAMVideoCaptureResult dealloc];
-[CAMVideoCaptureResult videoPreviewPixelBuffer];
-[CAMVideoCaptureResult error];
-[CAMVideoCaptureResult metadata];
-[CAMVideoCaptureResult duration];
-[CAMVideoCaptureResult stoppedUnexpectedly];
-[CAMVideoCaptureResult stillDisplayTime];
-[CAMVideoCaptureResult reason];
-[CAMVideoCaptureResult coordinationInfo];
-[CAMVideoCaptureResult initWithURL:filteredLocalDestinationURL:duration:stillDisplayTime:dimensions:metadata:videoZoomFactor:reason:videoPreviewPixelBuffer:coordinationInfo:error:slowWriterFrameDrops:];
-[CAMVideoCaptureResult localDestinationURL];
```
