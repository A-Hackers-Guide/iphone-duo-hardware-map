# `AVCaptureResolvedPhotoSettingsInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 35 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
q uniqueID;
{?="width"i"height"i} photoDimensions;
{?="width"i"height"i} rawPhotoDimensions;
{?="width"i"height"i} previewDimensions;
{?="width"i"height"i} embeddedThumbnailDimensions;
{?="width"i"height"i} rawEmbeddedThumbnailDimensions;
B livePhotoMovieEnabled;
{?="width"i"height"i} livePhotoMovieDimensions;
{?="width"i"height"i} portraitEffectsMatteDimensions;
{?="width"i"height"i} hairSegmentationMatteDimensions;
{?="width"i"height"i} skinSegmentationMatteDimensions;
{?="width"i"height"i} teethSegmentationMatteDimensions;
{?="width"i"height"i} glassesSegmentationMatteDimensions;
{?="width"i"height"i} spatialOverCapturePhotoDimensions;
B turboModeEnabled;
B flashEnabled;
B redEyeReductionEnabled;
B HDREnabled;
B adjustedPhotoFiltersEnabled;
B EV0PhotoDeliveryEnabled;
B stillImageStabilizationEnabled;
B virtualDeviceFusionEnabled;
B squareCropEnabled;
{?="width"i"height"i} deferredPhotoProxyDimensions;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} photoProcessingTimeRange;
B contentAwareDistortionCorrectionEnabled;
B spatialPhotoCaptureEnabled;
@"NSArray" photoManifest;
@"NSString" livePhotoAssetIdentifier;
Q digitalFlashUserInterfaceHints;
@"NSArray" digitalFlashUserInterfaceRGBEstimate;
B captureBeforeResolvingSettingsEnabled;
@"AVSemanticStyle" semanticStyle;
B secureSigningPhotoCaptureEnabled;
@"AVCapturePersonalPhotographerDuplicateInfo" personalPhotographerDuplicateInfo;
```

## Instance methods

```
-[AVCaptureResolvedPhotoSettingsInternal dealloc];
```
