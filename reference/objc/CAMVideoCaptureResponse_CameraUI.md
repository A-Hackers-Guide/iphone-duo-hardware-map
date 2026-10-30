# `CAMVideoCaptureResponse`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMCaptureResponse`
- Protocols: `CAMTransientAssetConvertible`
- 13 instance variables, 32 properties, 29 instance methods, 0 class methods

## Instance variables

```
B _slowWriterFrameDrops;
q _captureMode;
@"NSString" _persistenceUUID;
@"NSURL" _localPersistenceURL;
@"NSDate" _captureDate;
q _reason;
d _videoZoomFactor;
@"UIImage" _imageWellImage;
@"UIImage" _previewImage;
@"NSString" _stillPersistenceUUID;
{CGSize="width"d"height"d} _finalExpectedPixelSize;
{?="value"q"timescale"i"flags"I"epoch"q} _duration;
{?="value"q"timescale"i"flags"I"epoch"q} _stillDisplayTime;
```

## Properties

```
@property (Tq,R,N,V_captureMode) captureMode;
@property (T@"NSString",R,C,N,V_persistenceUUID) persistenceUUID;
@property (T@"NSURL",R,C,N,V_localPersistenceURL) localPersistenceURL;
@property (T@"NSDate",R,N,V_captureDate) captureDate;
@property (T{?=qiIq},R,N,V_duration) duration;
@property (Tq,R,N,V_reason) reason;
@property (TB,R,N) stoppedUnexpectedly;
@property (TB,R,N,V_slowWriterFrameDrops) slowWriterFrameDrops;
@property (Td,R,N,V_videoZoomFactor) videoZoomFactor;
@property (T@"UIImage",R,N,V_imageWellImage) imageWellImage;
@property (T@"UIImage",R,N,V_previewImage) previewImage;
@property (T{CGSize=dd},R,N,V_finalExpectedPixelSize) finalExpectedPixelSize;
@property (T@"NSString",R,C,N,V_stillPersistenceUUID) stillPersistenceUUID;
@property (T{?=qiIq},R,N,V_stillDisplayTime) stillDisplayTime;
@property (TQ,R,N) mediaType;
@property (TQ,R,N) mediaSubtypes;
@property (T@"NSString",R,N) uuid;
@property (TS,R,N) sessionIdentifier;
@property (T@"NSURL",R,C,N) persistenceURL;
@property (T@"UIImage",R,N) placeholderImage;
@property (TB,R,N,GisTransientAssetTemporaryPlaceholder) transientAssetTemporaryPlaceholder;
@property (T@"NSDictionary",R,C,N) stillImageMetadata;
@property (T@"NSString",R,C,N) burstIdentifier;
@property (TQ,R,N) numberOfRepresentedAssets;
@property (T@"NSString",R,N) irisStillImageUUID;
@property (TB,R,N,GisExpectingPairedVideo) expectingPairedVideo;
@property (T@"NSURL",R,N) irisVideoPersistenceURL;
@property (T{?=qiIq},R,N) irisStillDisplayTime;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMVideoCaptureResponse videoZoomFactor];
-[CAMVideoCaptureResponse persistenceUUID];
-[CAMVideoCaptureResponse imageWellImage];
-[CAMVideoCaptureResponse slowWriterFrameDrops];
-[CAMVideoCaptureResponse isExpectingPairedVideo];
-[CAMVideoCaptureResponse captureDate];
-[CAMVideoCaptureResponse uuid];
-[CAMVideoCaptureResponse finalExpectedPixelSize];
-[CAMVideoCaptureResponse persistenceURL];
-[CAMVideoCaptureResponse burstIdentifier];
-[CAMVideoCaptureResponse mediaSubtypes];
-[CAMVideoCaptureResponse stillPersistenceUUID];
-[CAMVideoCaptureResponse irisStillImageUUID];
-[CAMVideoCaptureResponse duration];
-[CAMVideoCaptureResponse stoppedUnexpectedly];
-[CAMVideoCaptureResponse previewImage];
-[CAMVideoCaptureResponse stillImageMetadata];
-[CAMVideoCaptureResponse placeholderImage];
-[CAMVideoCaptureResponse irisVideoPersistenceURL];
-[CAMVideoCaptureResponse stillDisplayTime];
-[CAMVideoCaptureResponse captureMode];
-[CAMVideoCaptureResponse numberOfRepresentedAssets];
-[CAMVideoCaptureResponse description];
-[CAMVideoCaptureResponse irisStillDisplayTime];
-[CAMVideoCaptureResponse reason];
-[CAMVideoCaptureResponse mediaType];
-[CAMVideoCaptureResponse isTransientAssetTemporaryPlaceholder];
-[CAMVideoCaptureResponse initWithUUID:captureMode:captureSession:url:captureDate:duration:stillPersistenceUUID:stillDisplayTime:reason:videoZoomFactor:finalExpectedPixelSize:imageWellImage:previewImage:coordinationInfo:slowWriterFrameDrops:];
-[CAMVideoCaptureResponse localPersistenceURL];
```
