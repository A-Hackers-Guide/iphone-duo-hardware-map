# `CAMStillImageCaptureResponse`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMCaptureResponse`
- Protocols: `CAMTransientAssetConvertible`
- 14 instance variables, 33 properties, 30 instance methods, 0 class methods

## Instance variables

```
B _expectingPairedVideo;
B _personalPhotographerManualCapture;
@"NSString" _persistenceUUID;
@"NSDate" _captureDate;
@"NSDictionary" _metadata;
@"NSString" _burstIdentifier;
Q _burstRepresentedCount;
@"UIImage" _imageWellImage;
@"UIImage" _textAnalysisImage;
q _captureID;
q _semanticEnhanceScene;
{CGSize="width"d"height"d} _finalExpectedPixelSize;
{?="value"q"timescale"i"flags"I"epoch"q} _captureTimestamp;
{?="value"q"timescale"i"flags"I"epoch"q} _personalPhotographerReplacedTimestamp;
```

## Properties

```
@property (T@"NSString",R,C,N,V_persistenceUUID) persistenceUUID;
@property (T@"NSDate",R,N,V_captureDate) captureDate;
@property (T@"NSDictionary",R,C,N,V_metadata) metadata;
@property (T@"NSString",R,C,N,V_burstIdentifier) burstIdentifier;
@property (TQ,R,N,V_burstRepresentedCount) burstRepresentedCount;
@property (T@"UIImage",R,N,V_imageWellImage) imageWellImage;
@property (T@"UIImage",R,N,V_textAnalysisImage) textAnalysisImage;
@property (TB,R,N) flashFired;
@property (TB,R,N,GisExpectingPairedVideo,V_expectingPairedVideo) expectingPairedVideo;
@property (T{CGSize=dd},R,N,V_finalExpectedPixelSize) finalExpectedPixelSize;
@property (Tq,R,N,V_captureID) captureID;
@property (Tq,R,N,V_semanticEnhanceScene) semanticEnhanceScene;
@property (T{?=qiIq},R,N,V_captureTimestamp) captureTimestamp;
@property (T{?=qiIq},R,N,V_personalPhotographerReplacedTimestamp) personalPhotographerReplacedTimestamp;
@property (TB,R,N,GisPersonalPhotographerDuplicate) personalPhotographerDuplicate;
@property (TB,R,N,GisPersonalPhotographerManualCapture,V_personalPhotographerManualCapture) personalPhotographerManualCapture;
@property (TQ,R,N) mediaType;
@property (TQ,R,N) mediaSubtypes;
@property (T@"NSString",R,N) uuid;
@property (TS,R,N) sessionIdentifier;
@property (T@"NSURL",R,C,N) persistenceURL;
@property (T@"UIImage",R,N) placeholderImage;
@property (TB,R,N,GisTransientAssetTemporaryPlaceholder) transientAssetTemporaryPlaceholder;
@property (T@"NSDictionary",R,C,N) stillImageMetadata;
@property (TQ,R,N) numberOfRepresentedAssets;
@property (T{?=qiIq},R,N) duration;
@property (T@"NSString",R,N) irisStillImageUUID;
@property (T@"NSURL",R,N) irisVideoPersistenceURL;
@property (T{?=qiIq},R,N) irisStillDisplayTime;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMStillImageCaptureResponse captureID];
-[CAMStillImageCaptureResponse isPersonalPhotographerDuplicate];
-[CAMStillImageCaptureResponse persistenceUUID];
-[CAMStillImageCaptureResponse imageWellImage];
-[CAMStillImageCaptureResponse isExpectingPairedVideo];
-[CAMStillImageCaptureResponse flashFired];
-[CAMStillImageCaptureResponse captureDate];
-[CAMStillImageCaptureResponse uuid];
-[CAMStillImageCaptureResponse finalExpectedPixelSize];
-[CAMStillImageCaptureResponse persistenceURL];
-[CAMStillImageCaptureResponse personalPhotographerReplacedTimestamp];
-[CAMStillImageCaptureResponse burstIdentifier];
-[CAMStillImageCaptureResponse mediaSubtypes];
-[CAMStillImageCaptureResponse burstRepresentedCount];
-[CAMStillImageCaptureResponse irisStillImageUUID];
-[CAMStillImageCaptureResponse metadata];
-[CAMStillImageCaptureResponse duration];
-[CAMStillImageCaptureResponse stillImageMetadata];
-[CAMStillImageCaptureResponse placeholderImage];
-[CAMStillImageCaptureResponse irisVideoPersistenceURL];
-[CAMStillImageCaptureResponse numberOfRepresentedAssets];
-[CAMStillImageCaptureResponse description];
-[CAMStillImageCaptureResponse textAnalysisImage];
-[CAMStillImageCaptureResponse irisStillDisplayTime];
-[CAMStillImageCaptureResponse isPersonalPhotographerManualCapture];
-[CAMStillImageCaptureResponse initWithUUID:captureSession:captureDate:metadata:burstIdentifier:burstRepresentedCount:imageWellImage:textAnalysisImage:coordinationInfo:finalExpectedPixelSize:expectingPairedVideo:captureID:semanticEnhanceScene:captureTimestamp:personalPhotographerReplacedTimestamp:personalPhotographerManualCapture:];
-[CAMStillImageCaptureResponse semanticEnhanceScene];
-[CAMStillImageCaptureResponse mediaType];
-[CAMStillImageCaptureResponse isTransientAssetTemporaryPlaceholder];
-[CAMStillImageCaptureResponse captureTimestamp];
```
