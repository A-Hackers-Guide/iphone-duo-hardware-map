# `AVCapturePhoto`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 17 properties, 50 instance methods, 2 class methods

## Instance variables

```
@"AVCapturePhotoInternal" _internal;
```

## Properties

```
@property (T@"AVCapturePhotoInternal",R,N,V_internal) internal;
@property (T{?=ii},R,N) dimensions;
@property (T{?=qiIq},R) timestamp;
@property (TB,R,GisRawPhoto) rawPhoto;
@property (T^{__CVBuffer=},R) pixelBuffer;
@property (T^{__CVBuffer=},R) previewPixelBuffer;
@property (T@"NSDictionary",R) embeddedThumbnailPhotoFormat;
@property (T@"AVDepthData",R) depthData;
@property (T@"AVPortraitEffectsMatte",R) portraitEffectsMatte;
@property (T@"NSDictionary",R) metadata;
@property (T@"AVCameraCalibrationData",R) cameraCalibrationData;
@property (T@"AVCaptureResolvedPhotoSettings",R) resolvedSettings;
@property (Tq,R) photoCount;
@property (T@"NSString",R) sourceDeviceType;
@property (T^{__CVBuffer=},R) constantColorConfidenceMap;
@property (Tf,R) constantColorCenterWeightedMeanConfidenceLevel;
@property (TB,R,GisConstantColorFallbackPhoto) constantColorFallbackPhoto;
```

## Class methods

```
+[AVCapturePhoto initialize];
+[AVCapturePhoto AVFileTypeFromFigCaptureStillImageSettingsFileType:codec:unresolvedSettings:];
```

## Instance methods

```
-[AVCapturePhoto pixelBuffer];
-[AVCapturePhoto dimensions];
-[AVCapturePhoto debugDescription];
-[AVCapturePhoto constantColorCenterWeightedMeanConfidenceLevel];
-[AVCapturePhoto embeddedThumbnailPhotoFormat];
-[AVCapturePhoto dealloc];
-[AVCapturePhoto timestamp];
-[AVCapturePhoto _orientation];
-[AVCapturePhoto metadata];
-[AVCapturePhoto sourceDeviceType];
-[AVCapturePhoto photoProcessingFlags];
-[AVCapturePhoto description];
-[AVCapturePhoto resolvedSettings];
-[AVCapturePhoto processedFileType];
-[AVCapturePhoto internal];
-[AVCapturePhoto bracketSettings];
-[AVCapturePhoto livePhotoMovieFileURL];
-[AVCapturePhoto fileDataRepresentation];
-[AVCapturePhoto photoLibraryThumbnails];
-[AVCapturePhoto portraitMetadata];
-[AVCapturePhoto secureSignedPhotoData];
-[AVCapturePhoto cameraCalibrationData];
-[AVCapturePhoto depthData];
-[AVCapturePhoto portraitEffectsMatte];
-[AVCapturePhoto photoCount];
-[AVCapturePhoto CGImageRepresentation];
-[AVCapturePhoto _defaultRawCompressionSettings];
-[AVCapturePhoto _embeddedThumbnailSourcePixelBuffer];
-[AVCapturePhoto _fileDataRepresentationWithReplacementMetadata:replacementEmbeddedThumbnailPhotoFormat:replacementEmbeddedThumbnailPixelBuffer:replacementDepthData:replacementPortraitEffectsMatte:replacementHairSegmentationMatte:replacementSkinSegmentationMatte:replacementTeethSegmentationMatte:replacementGlassesSegmentationMatte:replacementRawCompressionSettings:exceptionReason:];
-[AVCapturePhoto _isCompressedPhoto];
-[AVCapturePhoto _isProRAWPhoto];
-[AVCapturePhoto _isSushiRAWPhoto];
-[AVCapturePhoto _isUncompressedYUVOrRGBPhoto];
-[AVCapturePhoto _maximumAppleProRAWBitDepth];
-[AVCapturePhoto actualPhotoProcessingFlags];
-[AVCapturePhoto constantColorConfidenceMap];
-[AVCapturePhoto expectedPhotoProcessingFlags];
-[AVCapturePhoto fileDataRepresentationWithCustomizer:];
-[AVCapturePhoto fileDataRepresentationWithReplacementMetadata:replacementEmbeddedThumbnailPhotoFormat:replacementEmbeddedThumbnailPixelBuffer:replacementDepthData:];
-[AVCapturePhoto focusPixelBlurScore];
-[AVCapturePhoto initWithTimestamp:photoSurface:photoSurfaceSize:processedFileType:previewPhotoSurface:embeddedThumbnailSourceSurface:photoLibraryThumbnails:metadata:depthDataSurface:depthMetadataDictionary:portraitEffectsMatteSurface:portraitEffectsMatteMetadataDictionary:hairSegmentationMatteSurface:hairSegmentationMatteMetadataDictionary:skinSegmentationMatteSurface:skinSegmentationMatteMetadataDictionary:teethSegmentationMatteSurface:teethSegmentationMatteMetadataDictionary:glassesSegmentationMatteSurface:glassesSegmentationMatteMetadataDictionary:constantColorConfidenceMapSurface:constantColorMetadataDictionary:secureSignedRawSurface:secureSignedRawSurfaceSize:captureRequest:bracketSettings:sequenceCount:photoCount:expectedPhotoProcessingFlags:underlyingSourceDeviceType:sourceDeviceType:];
-[AVCapturePhoto isConstantColorFallbackPhoto];
-[AVCapturePhoto isRawPhoto];
-[AVCapturePhoto lensStabilizationStatus];
-[AVCapturePhoto personalPhotographerMetadata];
-[AVCapturePhoto previewCGImageRepresentation];
-[AVCapturePhoto previewPixelBuffer];
-[AVCapturePhoto privateClientMetadata];
-[AVCapturePhoto semanticSegmentationMatteForType:];
-[AVCapturePhoto sequenceCount];
```
