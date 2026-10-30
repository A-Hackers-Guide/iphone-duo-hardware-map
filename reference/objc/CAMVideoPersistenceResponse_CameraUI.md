# `CAMVideoPersistenceResponse`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMPersistenceResponse`
- Protocols: `CAMTransientAssetConvertible`
- 4 instance variables, 24 properties, 19 instance methods, 0 class methods

## Instance variables

```
q _captureMode;
@"NSString" _stillPersistenceUUID;
{?="value"q"timescale"i"flags"I"epoch"q} _duration;
{?="value"q"timescale"i"flags"I"epoch"q} _stillDisplayTime;
```

## Properties

```
@property (Tq,R,N,V_captureMode) captureMode;
@property (T{?=qiIq},R,N,V_duration) duration;
@property (T@"NSString",R,C,N,V_stillPersistenceUUID) stillPersistenceUUID;
@property (T{?=qiIq},R,N,V_stillDisplayTime) stillDisplayTime;
@property (TQ,R,N) mediaType;
@property (TQ,R,N) mediaSubtypes;
@property (T@"NSString",R,N) uuid;
@property (TS,R,N) sessionIdentifier;
@property (T@"NSURL",R,C,N) persistenceURL;
@property (T@"NSDate",R,N) captureDate;
@property (T@"UIImage",R,N) placeholderImage;
@property (T{CGSize=dd},R,N) finalExpectedPixelSize;
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
-[CAMVideoPersistenceResponse isExpectingPairedVideo];
-[CAMVideoPersistenceResponse captureDate];
-[CAMVideoPersistenceResponse uuid];
-[CAMVideoPersistenceResponse finalExpectedPixelSize];
-[CAMVideoPersistenceResponse burstIdentifier];
-[CAMVideoPersistenceResponse mediaSubtypes];
-[CAMVideoPersistenceResponse stillPersistenceUUID];
-[CAMVideoPersistenceResponse irisStillImageUUID];
-[CAMVideoPersistenceResponse duration];
-[CAMVideoPersistenceResponse stillImageMetadata];
-[CAMVideoPersistenceResponse placeholderImage];
-[CAMVideoPersistenceResponse irisVideoPersistenceURL];
-[CAMVideoPersistenceResponse stillDisplayTime];
-[CAMVideoPersistenceResponse captureMode];
-[CAMVideoPersistenceResponse numberOfRepresentedAssets];
-[CAMVideoPersistenceResponse irisStillDisplayTime];
-[CAMVideoPersistenceResponse mediaType];
-[CAMVideoPersistenceResponse isTransientAssetTemporaryPlaceholder];
-[CAMVideoPersistenceResponse initWithUUID:captureMode:captureSession:url:creationDate:scrubberImage:finalExpectedPixelSize:duration:stillPersistenceUUID:stillDisplayTime:coordinationInfo:];
```
