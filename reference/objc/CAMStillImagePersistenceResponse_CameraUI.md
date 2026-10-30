# `CAMStillImagePersistenceResponse`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMPersistenceResponse`
- Protocols: `CAMTransientAssetConvertible`
- 4 instance variables, 23 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _expectingPairedVideo;
@"NSDictionary" _metadata;
@"NSString" _burstIdentifier;
Q _burstRepresentedCount;
```

## Properties

```
@property (T@"NSDictionary",R,C,N,V_metadata) metadata;
@property (T@"NSString",R,C,N,V_burstIdentifier) burstIdentifier;
@property (TQ,R,N,V_burstRepresentedCount) burstRepresentedCount;
@property (TB,R,N,GisExpectingPairedVideo,V_expectingPairedVideo) expectingPairedVideo;
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
-[CAMStillImagePersistenceResponse isExpectingPairedVideo];
-[CAMStillImagePersistenceResponse captureDate];
-[CAMStillImagePersistenceResponse uuid];
-[CAMStillImagePersistenceResponse finalExpectedPixelSize];
-[CAMStillImagePersistenceResponse initWithUUID:captureSession:url:creationDate:scrubberImage:finalExpectedPixelSize:metadata:burstIdentifier:burstRepresentedCount:expectingPairedVideo:coordinationInfo:];
-[CAMStillImagePersistenceResponse burstIdentifier];
-[CAMStillImagePersistenceResponse mediaSubtypes];
-[CAMStillImagePersistenceResponse burstRepresentedCount];
-[CAMStillImagePersistenceResponse irisStillImageUUID];
-[CAMStillImagePersistenceResponse metadata];
-[CAMStillImagePersistenceResponse duration];
-[CAMStillImagePersistenceResponse stillImageMetadata];
-[CAMStillImagePersistenceResponse placeholderImage];
-[CAMStillImagePersistenceResponse irisVideoPersistenceURL];
-[CAMStillImagePersistenceResponse numberOfRepresentedAssets];
-[CAMStillImagePersistenceResponse description];
-[CAMStillImagePersistenceResponse irisStillDisplayTime];
-[CAMStillImagePersistenceResponse mediaType];
-[CAMStillImagePersistenceResponse isTransientAssetTemporaryPlaceholder];
```
