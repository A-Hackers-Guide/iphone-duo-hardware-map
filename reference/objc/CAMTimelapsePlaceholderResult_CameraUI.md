# `CAMTimelapsePlaceholderResult`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMTransientAssetConvertible`
- 9 instance variables, 29 properties, 27 instance methods, 0 class methods

## Instance variables

```
S _sessionIdentifier;
@"NSString" _assetUUID;
@"NSDate" _creationDate;
q _captureOrientation;
q _captureDevice;
d _timelapseDuration;
^v _previewImageSurface;
@"NSURL" _localPrivateMetadataFileURL;
{CGSize="width"d"height"d} _videoDimensions;
```

## Properties

```
@property (T@"NSString",R,C,N,V_assetUUID) assetUUID;
@property (TS,R,N,V_sessionIdentifier) sessionIdentifier;
@property (T@"NSDate",R,C,N,V_creationDate) creationDate;
@property (Tq,R,N,V_captureOrientation) captureOrientation;
@property (Tq,R,N,V_captureDevice) captureDevice;
@property (T{CGSize=dd},R,N,V_videoDimensions) videoDimensions;
@property (Td,R,N,V_timelapseDuration) timelapseDuration;
@property (T^v,R,N,V_previewImageSurface) previewImageSurface;
@property (T@"NSURL",R,C,N,V_localPrivateMetadataFileURL) localPrivateMetadataFileURL;
@property (TQ,R,N) mediaType;
@property (TQ,R,N) mediaSubtypes;
@property (T@"NSString",R,N) uuid;
@property (T@"NSURL",R,C,N) persistenceURL;
@property (T@"NSDate",R,N) captureDate;
@property (T@"UIImage",R,N) placeholderImage;
@property (T{CGSize=dd},R,N) finalExpectedPixelSize;
@property (TB,R,N,GisTransientAssetTemporaryPlaceholder) transientAssetTemporaryPlaceholder;
@property (T@"NSDictionary",R,C,N) stillImageMetadata;
@property (T@"NSString",R,C,N) burstIdentifier;
@property (TQ,R,N) numberOfRepresentedAssets;
@property (T{?=qiIq},R,N) duration;
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
-[CAMTimelapsePlaceholderResult sessionIdentifier];
-[CAMTimelapsePlaceholderResult isExpectingPairedVideo];
-[CAMTimelapsePlaceholderResult captureDate];
-[CAMTimelapsePlaceholderResult videoDimensions];
-[CAMTimelapsePlaceholderResult uuid];
-[CAMTimelapsePlaceholderResult finalExpectedPixelSize];
-[CAMTimelapsePlaceholderResult persistenceURL];
-[CAMTimelapsePlaceholderResult captureDevice];
-[CAMTimelapsePlaceholderResult burstIdentifier];
-[CAMTimelapsePlaceholderResult dealloc];
-[CAMTimelapsePlaceholderResult mediaSubtypes];
-[CAMTimelapsePlaceholderResult assetUUID];
-[CAMTimelapsePlaceholderResult creationDate];
-[CAMTimelapsePlaceholderResult irisStillImageUUID];
-[CAMTimelapsePlaceholderResult duration];
-[CAMTimelapsePlaceholderResult stillImageMetadata];
-[CAMTimelapsePlaceholderResult placeholderImage];
-[CAMTimelapsePlaceholderResult irisVideoPersistenceURL];
-[CAMTimelapsePlaceholderResult localPrivateMetadataFileURL];
-[CAMTimelapsePlaceholderResult numberOfRepresentedAssets];
-[CAMTimelapsePlaceholderResult irisStillDisplayTime];
-[CAMTimelapsePlaceholderResult mediaType];
-[CAMTimelapsePlaceholderResult isTransientAssetTemporaryPlaceholder];
-[CAMTimelapsePlaceholderResult captureOrientation];
-[CAMTimelapsePlaceholderResult initWithAssetUUID:captureSession:creationDate:captureOrientation:captureDevice:videoDimensions:duration:previewImageSurface:localPrivateMetadataFileURL:];
-[CAMTimelapsePlaceholderResult previewImageSurface];
-[CAMTimelapsePlaceholderResult timelapseDuration];
```
