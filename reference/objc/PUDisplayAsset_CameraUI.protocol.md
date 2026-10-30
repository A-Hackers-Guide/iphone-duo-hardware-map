# `PUDisplayAsset` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `NSCopying`
- 0 instance variables, 37 properties, 39 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) mediaType;
@property (TQ,R,N) mediaSubtypes;
@property (Tq,R,N) playbackStyle;
@property (TS,R,N) playbackVariation;
@property (T@"NSString",R,N) uuid;
@property (TQ,R,N) pixelWidth;
@property (TQ,R,N) pixelHeight;
@property (T@"CLLocation",R,N) location;
@property (Td,R,N) duration;
@property (TB,R,N,GisFavorite) favorite;
@property (TB,R,N,GisHidden) hidden;
@property (T@"NSDate",R,N) creationDate;
@property (T@"NSDate",R,N) localCreationDate;
@property (T@"NSDate",R,N) modificationDate;
@property (Td,R,N) aspectRatio;
@property (T@"NSString",R,N) localizedGeoDescription;
@property (TB,R,N) isTemporaryPlaceholder;
@property (T@"NSString",R,N) uniformTypeIdentifier;
@property (TQ,R,N) originalFilesize;
@property (TB,R,N) isAnimatedImage;
@property (TB,R,N,GisLivePhoto) livePhoto;
@property (TB,R,N) canPlayPhotoIris;
@property (TB,R,N) canPlayLoopingVideo;
@property (TB,R,N) isPhotoIrisPlaceholder;
@property (T{?=qiIq},R,N) photoIrisStillDisplayTime;
@property (T{?=qiIq},R,N) photoIrisVideoDuration;
@property (TB,R,N) hasPhotoColorAdjustments;
@property (TB,R,N) needsSensitivityProtection;
@property (Tq,R,N) compactSCSensitivityAnalysis;
@property (TQ,R,N) sensitivityAnalysisState;
@property (T{?=qiIq},?,R,N) videoKeyFrameSourceTime;
@property (TB,?,R,N) needsDeferredProcessing;
@property (TS,?,R,N) deferredProcessingNeeded;
@property (TB,?,R,N) isGuestAsset;
@property (TB,?,R,N) hasSyndicationInformation;
@property (TB,?,R,N) px_isCloudKitSharedAlbumAsset;
@property (TB,?,R,N) px_isStreamSharedAlbumAsset;
```

## Instance methods

```
-[PUDisplayAsset playbackVariation];
-[PUDisplayAsset pixelWidth];
-[PUDisplayAsset isFavorite];
-[PUDisplayAsset playbackStyle];
-[PUDisplayAsset modificationDate];
-[PUDisplayAsset uuid];
-[PUDisplayAsset uniformTypeIdentifier];
-[PUDisplayAsset aspectRatio];
-[PUDisplayAsset pixelHeight];
-[PUDisplayAsset location];
-[PUDisplayAsset hasPhotoColorAdjustments];
-[PUDisplayAsset photoIrisVideoDuration];
-[PUDisplayAsset mediaSubtypes];
-[PUDisplayAsset localCreationDate];
-[PUDisplayAsset canPlayPhotoIris];
-[PUDisplayAsset isAnimatedImage];
-[PUDisplayAsset creationDate];
-[PUDisplayAsset isPhotoIrisPlaceholder];
-[PUDisplayAsset duration];
-[PUDisplayAsset isContentEqualTo:];
-[PUDisplayAsset originalFilesize];
-[PUDisplayAsset isHidden];
-[PUDisplayAsset isLivePhoto];
-[PUDisplayAsset isTemporaryPlaceholder];
-[PUDisplayAsset localizedGeoDescription];
-[PUDisplayAsset canPlayLoopingVideo];
-[PUDisplayAsset compactSCSensitivityAnalysis];
-[PUDisplayAsset mediaType];
-[PUDisplayAsset photoIrisStillDisplayTime];
-[PUDisplayAsset sensitivityAnalysisState];
-[PUDisplayAsset needsSensitivityProtection];
-[PUDisplayAsset needsDeferredProcessing];
-[PUDisplayAsset deferredProcessingNeeded];
-[PUDisplayAsset contentChangeFromDisplayAsset:];
-[PUDisplayAsset hasSyndicationInformation];
-[PUDisplayAsset isGuestAsset];
-[PUDisplayAsset px_isCloudKitSharedAlbumAsset];
-[PUDisplayAsset px_isStreamSharedAlbumAsset];
-[PUDisplayAsset videoKeyFrameSourceTime];
```
