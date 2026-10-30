# `BWStillImageCaptureAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageAnalyticsPayloadCommon`
- 34 instance variables, 31 properties, 68 instance methods, 0 class methods

## Instance variables

```
i _deviceType;
I _processingFlags;
i _shutterLag;
f _zoom;
f _uiZoom;
i _numberOfFacesWithVisionFaceDetection;
f _largestFaceHeight;
f _smallestFaceHeight;
i _numberOfFacesAtEdge;
i _numberOfFacesAtCenter;
@"NSDictionary" _oisRecenteringLoggingData;
i _intelligentDistortionCorrectionStatusCode;
i _intelligentDistortionCorrectionGainMapProcessingStatusCode;
i _intelligentDistortionCorrectionCorrectionType;
i _ispMotionHighPassFilterConvergenceFlags;
I _bitDepth;
I _dngFileSize;
I _photoFileSize;
I _thumbnailImageSize;
I _auxiliaryImagesSize;
I _depthFormatDimensionWidth;
I _depthFormatDimensionHeight;
I _depthPixelFormat;
B _depthDataFiltered;
@"BWStillImageFocusPixelBlurScoreResult" _focusPixelBlurScoreResult;
i _stillImageFusionMode;
I _dngCodecType;
f _dngCodecQuality;
I _numberOfLCBsDetected;
I _numberOfLCBsCorrectedOnIRCF;
I _numberOfLCBsCorrectedOnLens;
B _lcbDetectionCountHistogramSet;
[10I] _lcbDetectionCountHistogram;
i _fusionMode;
```

## Properties

```
@property (Ti,N,V_deviceType) deviceType;
@property (TI,N,V_processingFlags) processingFlags;
@property (Tf,N,V_zoom) zoom;
@property (Tf,N,V_uiZoom) uiZoom;
@property (Ti,N,V_shutterLag) shutterLag;
@property (Ti,N,V_numberOfFacesWithVisionFaceDetection) numberOfFacesWithVisionFaceDetection;
@property (Tf,N,V_largestFaceHeight) largestFaceHeight;
@property (Tf,N,V_smallestFaceHeight) smallestFaceHeight;
@property (Ti,N,V_numberOfFacesAtEdge) numberOfFacesAtEdge;
@property (Ti,N,V_numberOfFacesAtCenter) numberOfFacesAtCenter;
@property (T@"NSDictionary",&,N,V_oisRecenteringLoggingData) oisRecenteringLoggingData;
@property (Ti,N,V_intelligentDistortionCorrectionStatusCode) intelligentDistortionCorrectionStatusCode;
@property (Ti,N,V_intelligentDistortionCorrectionGainMapProcessingStatusCode) intelligentDistortionCorrectionGainMapProcessingStatusCode;
@property (Ti,N,V_intelligentDistortionCorrectionCorrectionType) intelligentDistortionCorrectionCorrectionType;
@property (Ti,N,V_ispMotionHighPassFilterConvergenceFlags) ispMotionHighPassFilterConvergenceFlags;
@property (TI,N,V_bitDepth) bitDepth;
@property (TI,N,V_dngFileSize) dngFileSize;
@property (TI,N,V_photoFileSize) photoFileSize;
@property (TI,N,V_thumbnailImageSize) thumbnailImageSize;
@property (TI,N,V_auxiliaryImagesSize) auxiliaryImagesSize;
@property (TI,N,V_depthFormatDimensionWidth) depthFormatDimensionWidth;
@property (TI,N,V_depthFormatDimensionHeight) depthFormatDimensionHeight;
@property (TI,N,V_depthPixelFormat) depthPixelFormat;
@property (TB,N,V_depthDataFiltered) depthDataFiltered;
@property (T@"BWStillImageFocusPixelBlurScoreResult",&,N,V_focusPixelBlurScoreResult) focusPixelBlurScoreResult;
@property (Ti,N,V_fusionMode) fusionMode;
@property (TI,N,V_dngCodecType) dngCodecType;
@property (Tf,N,V_dngCodecQuality) dngCodecQuality;
@property (TI,N,V_numberOfLCBsDetected) numberOfLCBsDetected;
@property (TI,N,V_numberOfLCBsCorrectedOnIRCF) numberOfLCBsCorrectedOnIRCF;
@property (TI,N,V_numberOfLCBsCorrectedOnLens) numberOfLCBsCorrectedOnLens;
```

## Instance methods

```
-[BWStillImageCaptureAnalyticsPayload setDepthPixelFormat:];
-[BWStillImageCaptureAnalyticsPayload bitDepth];
-[BWStillImageCaptureAnalyticsPayload depthPixelFormat];
-[BWStillImageCaptureAnalyticsPayload setDeviceType:];
-[BWStillImageCaptureAnalyticsPayload fusionMode];
-[BWStillImageCaptureAnalyticsPayload setShutterLag:];
-[BWStillImageCaptureAnalyticsPayload setZoom:];
-[BWStillImageCaptureAnalyticsPayload largestFaceHeight];
-[BWStillImageCaptureAnalyticsPayload setDngCodecType:];
-[BWStillImageCaptureAnalyticsPayload eventDictionary];
-[BWStillImageCaptureAnalyticsPayload setAuxiliaryImagesSize:];
-[BWStillImageCaptureAnalyticsPayload intelligentDistortionCorrectionGainMapProcessingStatusCode];
-[BWStillImageCaptureAnalyticsPayload numberOfLCBsCorrectedOnIRCF];
-[BWStillImageCaptureAnalyticsPayload setUiZoom:];
-[BWStillImageCaptureAnalyticsPayload init];
-[BWStillImageCaptureAnalyticsPayload setNumberOfFacesAtEdge:];
-[BWStillImageCaptureAnalyticsPayload deviceType];
-[BWStillImageCaptureAnalyticsPayload setDngCodecQuality:];
-[BWStillImageCaptureAnalyticsPayload setDepthFormatDimensionHeight:];
-[BWStillImageCaptureAnalyticsPayload setOisRecenteringLoggingData:];
-[BWStillImageCaptureAnalyticsPayload setNumberOfLCBsCorrectedOnIRCF:];
-[BWStillImageCaptureAnalyticsPayload dealloc];
-[BWStillImageCaptureAnalyticsPayload setNumberOfLCBsCorrectedOnLens:];
-[BWStillImageCaptureAnalyticsPayload reset];
-[BWStillImageCaptureAnalyticsPayload setIntelligentDistortionCorrectionGainMapProcessingStatusCode:];
-[BWStillImageCaptureAnalyticsPayload dngFileSize];
-[BWStillImageCaptureAnalyticsPayload oisRecenteringLoggingData];
-[BWStillImageCaptureAnalyticsPayload setFocusPixelBlurScoreResult:];
-[BWStillImageCaptureAnalyticsPayload dngCodecQuality];
-[BWStillImageCaptureAnalyticsPayload intelligentDistortionCorrectionStatusCode];
-[BWStillImageCaptureAnalyticsPayload setNumberOfFacesWithVisionFaceDetection:];
-[BWStillImageCaptureAnalyticsPayload numberOfFacesWithVisionFaceDetection];
-[BWStillImageCaptureAnalyticsPayload smallestFaceHeight];
-[BWStillImageCaptureAnalyticsPayload zoom];
-[BWStillImageCaptureAnalyticsPayload setLCBDetectionCountHistogram:];
-[BWStillImageCaptureAnalyticsPayload eventName];
-[BWStillImageCaptureAnalyticsPayload photoFileSize];
-[BWStillImageCaptureAnalyticsPayload setSmallestFaceHeight:];
-[BWStillImageCaptureAnalyticsPayload setFusionMode:];
-[BWStillImageCaptureAnalyticsPayload numberOfFacesAtEdge];
-[BWStillImageCaptureAnalyticsPayload focusPixelBlurScoreResult];
-[BWStillImageCaptureAnalyticsPayload setIntelligentDistortionCorrectionStatusCode:];
-[BWStillImageCaptureAnalyticsPayload setThumbnailImageSize:];
-[BWStillImageCaptureAnalyticsPayload numberOfLCBsDetected];
-[BWStillImageCaptureAnalyticsPayload processingFlags];
-[BWStillImageCaptureAnalyticsPayload numberOfFacesAtCenter];
-[BWStillImageCaptureAnalyticsPayload setDepthFormatDimensionWidth:];
-[BWStillImageCaptureAnalyticsPayload intelligentDistortionCorrectionCorrectionType];
-[BWStillImageCaptureAnalyticsPayload auxiliaryImagesSize];
-[BWStillImageCaptureAnalyticsPayload ispMotionHighPassFilterConvergenceFlags];
-[BWStillImageCaptureAnalyticsPayload setPhotoFileSize:];
-[BWStillImageCaptureAnalyticsPayload setNumberOfFacesAtCenter:];
-[BWStillImageCaptureAnalyticsPayload setBitDepth:];
-[BWStillImageCaptureAnalyticsPayload setDepthDataFiltered:];
-[BWStillImageCaptureAnalyticsPayload depthFormatDimensionHeight];
-[BWStillImageCaptureAnalyticsPayload shutterLag];
-[BWStillImageCaptureAnalyticsPayload setProcessingFlags:];
-[BWStillImageCaptureAnalyticsPayload thumbnailImageSize];
-[BWStillImageCaptureAnalyticsPayload setLargestFaceHeight:];
-[BWStillImageCaptureAnalyticsPayload uiZoom];
-[BWStillImageCaptureAnalyticsPayload setDngFileSize:];
-[BWStillImageCaptureAnalyticsPayload setIspMotionHighPassFilterConvergenceFlags:];
-[BWStillImageCaptureAnalyticsPayload dngCodecType];
-[BWStillImageCaptureAnalyticsPayload setNumberOfLCBsDetected:];
-[BWStillImageCaptureAnalyticsPayload setIntelligentDistortionCorrectionCorrectionType:];
-[BWStillImageCaptureAnalyticsPayload numberOfLCBsCorrectedOnLens];
-[BWStillImageCaptureAnalyticsPayload depthFormatDimensionWidth];
-[BWStillImageCaptureAnalyticsPayload depthDataFiltered];
```
