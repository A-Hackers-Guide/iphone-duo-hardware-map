# `CAMTransientAssetConvertible` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 17 properties, 17 instance methods, 0 class methods

## Properties

```
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
@property (T{?=qiIq},R,N) duration;
@property (T@"NSString",R,N) irisStillImageUUID;
@property (TB,R,N,GisExpectingPairedVideo) expectingPairedVideo;
@property (T@"NSURL",R,N) irisVideoPersistenceURL;
@property (T{?=qiIq},R,N) irisStillDisplayTime;
```

## Instance methods

```
-[CAMTransientAssetConvertible sessionIdentifier];
-[CAMTransientAssetConvertible isExpectingPairedVideo];
-[CAMTransientAssetConvertible captureDate];
-[CAMTransientAssetConvertible uuid];
-[CAMTransientAssetConvertible finalExpectedPixelSize];
-[CAMTransientAssetConvertible persistenceURL];
-[CAMTransientAssetConvertible burstIdentifier];
-[CAMTransientAssetConvertible mediaSubtypes];
-[CAMTransientAssetConvertible irisStillImageUUID];
-[CAMTransientAssetConvertible duration];
-[CAMTransientAssetConvertible stillImageMetadata];
-[CAMTransientAssetConvertible placeholderImage];
-[CAMTransientAssetConvertible irisVideoPersistenceURL];
-[CAMTransientAssetConvertible numberOfRepresentedAssets];
-[CAMTransientAssetConvertible irisStillDisplayTime];
-[CAMTransientAssetConvertible mediaType];
-[CAMTransientAssetConvertible isTransientAssetTemporaryPlaceholder];
```
