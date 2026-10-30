# `CAMTransientAsset`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PUTransientDisplayAsset`
- 23 instance variables, 48 properties, 46 instance methods, 0 class methods

## Instance variables

```
B _isTemporaryPlaceholder;
B _canPlayPhotoIris;
B _canPlayLoopingVideo;
B _isPhotoIrisPlaceholder;
B _HDR;
B _representsBurst;
S _playbackVariation;
@"NSDate" _localCreationDate;
Q _sensitivityAnalysisState;
@"NSString" _uuid;
Q _mediaType;
Q _mediaSubtypes;
Q _pixelWidth;
Q _pixelHeight;
d _duration;
@"NSDate" _creationDate;
@"NSDate" _modificationDate;
@"NSURL" _persistenceURL;
@"UIImage" _placeholderImage;
@"NSString" _burstIdentifier;
Q _numberOfRepresentedAssets;
{?="value"q"timescale"i"flags"I"epoch"q} _photoIrisStillDisplayTime;
{?="value"q"timescale"i"flags"I"epoch"q} _photoIrisVideoDuration;
```

## Properties

```
@property (T@"NSString",R,N,V_uuid) uuid;
@property (TQ,R,N,V_mediaType) mediaType;
@property (TQ,R,N,V_mediaSubtypes) mediaSubtypes;
@property (Tq,R,N) playbackStyle;
@property (TS,R,N,V_playbackVariation) playbackVariation;
@property (TQ,R,N,V_pixelWidth) pixelWidth;
@property (TQ,R,N,V_pixelHeight) pixelHeight;
@property (T@"CLLocation",R,N) location;
@property (Td,R,N,V_duration) duration;
@property (TB,R,N,GisFavorite) favorite;
@property (T@"NSDate",R,N,V_creationDate) creationDate;
@property (T@"NSDate",R,N,V_modificationDate) modificationDate;
@property (Td,R,N) aspectRatio;
@property (T@"NSString",R,N) localizedGeoDescription;
@property (TB,R,N) isLivePhoto;
@property (TB,R,N,V_canPlayPhotoIris) canPlayPhotoIris;
@property (TB,R,N,V_canPlayLoopingVideo) canPlayLoopingVideo;
@property (TB,R,N,V_isPhotoIrisPlaceholder) isPhotoIrisPlaceholder;
@property (T{?=qiIq},R,N,V_photoIrisStillDisplayTime) photoIrisStillDisplayTime;
@property (T{?=qiIq},R,N,V_photoIrisVideoDuration) photoIrisVideoDuration;
@property (TB,R,N) hasPhotoColorAdjustments;
@property (T@"NSURL",R,C,N,V_persistenceURL) persistenceURL;
@property (T@"UIImage",R,N,V_placeholderImage) placeholderImage;
@property (TB,R,N,GisHDR,V_HDR) HDR;
@property (TB,R,N,V_representsBurst) representsBurst;
@property (T@"NSString",R,C,N,V_burstIdentifier) burstIdentifier;
@property (TQ,R,N,V_numberOfRepresentedAssets) numberOfRepresentedAssets;
@property (TB,R,N,GisHidden) hidden;
@property (T@"NSDate",R,N,V_localCreationDate) localCreationDate;
@property (TB,R,N,V_isTemporaryPlaceholder) isTemporaryPlaceholder;
@property (T@"NSString",R,N) uniformTypeIdentifier;
@property (TQ,R,N) originalFilesize;
@property (TB,R,N) isAnimatedImage;
@property (TB,R,N,GisLivePhoto) livePhoto;
@property (TB,R,N) needsSensitivityProtection;
@property (Tq,R,N) compactSCSensitivityAnalysis;
@property (TQ,R,N,V_sensitivityAnalysisState) sensitivityAnalysisState;
@property (T{?=qiIq},?,R,N) videoKeyFrameSourceTime;
@property (TB,?,R,N) needsDeferredProcessing;
@property (TS,?,R,N) deferredProcessingNeeded;
@property (TB,?,R,N) isGuestAsset;
@property (TB,?,R,N) hasSyndicationInformation;
@property (TB,?,R,N) px_isCloudKitSharedAlbumAsset;
@property (TB,?,R,N) px_isStreamSharedAlbumAsset;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMTransientAsset playbackVariation];
-[CAMTransientAsset pixelWidth];
-[CAMTransientAsset isFavorite];
-[CAMTransientAsset playbackStyle];
-[CAMTransientAsset isHDR];
-[CAMTransientAsset modificationDate];
-[CAMTransientAsset representsBurst];
-[CAMTransientAsset uuid];
-[CAMTransientAsset uniformTypeIdentifier];
-[CAMTransientAsset persistenceURL];
-[CAMTransientAsset init];
-[CAMTransientAsset aspectRatio];
-[CAMTransientAsset initWithUUID:];
-[CAMTransientAsset pixelHeight];
-[CAMTransientAsset location];
-[CAMTransientAsset hasPhotoColorAdjustments];
-[CAMTransientAsset burstIdentifier];
-[CAMTransientAsset photoIrisVideoDuration];
-[CAMTransientAsset mediaSubtypes];
-[CAMTransientAsset localCreationDate];
-[CAMTransientAsset canPlayPhotoIris];
-[CAMTransientAsset isAnimatedImage];
-[CAMTransientAsset creationDate];
-[CAMTransientAsset isPhotoIrisPlaceholder];
-[CAMTransientAsset duration];
-[CAMTransientAsset isContentEqualTo:];
-[CAMTransientAsset placeholderImage];
-[CAMTransientAsset originalFilesize];
-[CAMTransientAsset isHidden];
-[CAMTransientAsset isLivePhoto];
-[CAMTransientAsset isTemporaryPlaceholder];
-[CAMTransientAsset numberOfRepresentedAssets];
-[CAMTransientAsset description];
-[CAMTransientAsset deferredLogInfo];
-[CAMTransientAsset _populateVideoTransientAssetFromConvertible:];
-[CAMTransientAsset localizedGeoDescription];
-[CAMTransientAsset copyWithZone:];
-[CAMTransientAsset canPlayLoopingVideo];
-[CAMTransientAsset compactSCSensitivityAnalysis];
-[CAMTransientAsset mediaType];
-[CAMTransientAsset initWithAsset:uuid:];
-[CAMTransientAsset photoIrisStillDisplayTime];
-[CAMTransientAsset sensitivityAnalysisState];
-[CAMTransientAsset _populateStillImageTransientAssetFromConvertible:];
-[CAMTransientAsset needsSensitivityProtection];
-[CAMTransientAsset initWithAsset:convertible:];
```
