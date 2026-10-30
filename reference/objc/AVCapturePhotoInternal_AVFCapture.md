# `AVCapturePhotoInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 40 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
{?="value"q"timescale"i"flags"I"epoch"q} timestamp;
^{__IOSurface=} photoSurface;
Q photoSurfaceSize;
@"NSString" processedFileType;
^{__CVBuffer=} photoPixelBuffer;
^{__CVBuffer=} previewPixelBuffer;
^{__CVBuffer=} embeddedThumbnailSourcePixelBuffer;
@"NSDictionary" embeddedThumbnailPhotoFormat;
@"NSArray" photoLibraryThumbnails;
@"NSDictionary" metadata;
@"AVCameraCalibrationData" cameraCalibrationData;
@"AVCaptureResolvedPhotoSettings" resolvedSettings;
@"AVCapturePhotoSettings" unresolvedSettings;
@"AVDepthData" depthData;
B didTryToDecodeDepthData;
@"AVPortraitEffectsMatte" portraitEffectsMatte;
B didTryToDecodePortraitEffectsMatte;
@"AVSemanticSegmentationMatte" hairSegmentationMatte;
B didTryToDecodeHairSegmentationMatte;
@"AVSemanticSegmentationMatte" skinSegmentationMatte;
B didTryToDecodeSkinSegmentationMatte;
@"AVSemanticSegmentationMatte" teethSegmentationMatte;
B didTryToDecodeTeethSegmentationMatte;
@"AVSemanticSegmentationMatte" glassesSegmentationMatte;
B didTryToDecodeGlassesSegmentationMatte;
^{__CVBuffer=} constantColorConfidenceMap;
f constantColorCenterWeightedMeanConfidenceLevel;
@"AVCaptureBracketedStillImageSettings" bracketSettings;
Q sequenceCount;
Q photoCount;
@"NSString" underlyingSourceDeviceType;
@"NSString" sourceDeviceType;
^{__IOSurface=} secureSignedRawSurface;
Q secureSignedRawSurfaceSize;
I expectedPhotoProcessingFlags;
I actualPhotoProcessingFlags;
@"AVCapturePhotoPrivateClientMetadata" privateClientMetadata;
@"AVApplePortraitMetadata" portraitMetadata;
@"AVCapturePersonalPhotographerMetadata" personalPhotographerMetadata;
B lensStabilizationSupported;
```
