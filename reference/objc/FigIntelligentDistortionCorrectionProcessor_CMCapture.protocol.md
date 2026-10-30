# `FigIntelligentDistortionCorrectionProcessor` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MetalImageBufferProcessor`
- 0 instance variables, 33 properties, 65 instance methods, 0 class methods

## Properties

```
@property (T@"NSDictionary",&,N) tuningParameters;
@property (T@"NSDictionary",&,N) cameraInfoByPortType;
@property (TB,N) processIntelligentDistortionCorrection;
@property (TB,N) processGeometricDistortionCorrection;
@property (TB,N) useDeepTransferAccommodations;
@property (TB,N) applyResolutionInvariantWarp;
@property (TB,N) applyZoom;
@property (TB,N) applyStereoRectificationHomography;
@property (T{?=[3]},N) stereoRectificationInverseHomography;
@property (TB,N) useBilinearInterpolation;
@property (TB,N) usePrecomputedPolynomialsAndOpticalCenterOffset;
@property (T@"NSData",&,N) gdcForwardPolynomial;
@property (T@"NSData",&,N) gdcInversePolynomial;
@property (T{CGPoint=dd},N) opticalCenterOffset;
@property (T^{__CVBuffer=},N) inputImage;
@property (T^{__CVBuffer=},N) lowResSegmentationMask;
@property (T^{__CVBuffer=},N) outputImage;
@property (T@"NSDictionary",&,N) inputImageMetadataDictionary;
@property (T@"NSArray",&,N) faceObservations;
@property (TB,N) deviceWasStationaryDuringCapture;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) inputImageCropRect;
@property (T{?=ii},N) finalImageDimensions;
@property (TB,N) replicatePixelsOutsideOfFinalImageDimensions;
@property (T,N) inputImageAppliedScalingFactors;
@property (T,N) inputImageAppliedOffsets;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) outputValidBufferRect;
@property (T{?=[3]},R,N) globalTransform;
@property (TB,R,N) globalTransformIsValid;
@property (TB,R,N) zoomWasApplied;
@property (TB,N) withTemporalConsistency;
@property (TI,R,N) makernoteEntry;
@property (Ti,R,N) correctionType;
@property (Ti,R,N) gdcSource;
```

## Instance methods

```
-[FigIntelligentDistortionCorrectionProcessor setReplicatePixelsOutsideOfFinalImageDimensions:];
-[FigIntelligentDistortionCorrectionProcessor tuningParameters];
-[FigIntelligentDistortionCorrectionProcessor setInputImage:];
-[FigIntelligentDistortionCorrectionProcessor outputImage];
-[FigIntelligentDistortionCorrectionProcessor globalTransform];
-[FigIntelligentDistortionCorrectionProcessor setCameraInfoByPortType:];
-[FigIntelligentDistortionCorrectionProcessor inputImage];
-[FigIntelligentDistortionCorrectionProcessor cameraInfoByPortType];
-[FigIntelligentDistortionCorrectionProcessor setTuningParameters:];
-[FigIntelligentDistortionCorrectionProcessor replicatePixelsOutsideOfFinalImageDimensions];
-[FigIntelligentDistortionCorrectionProcessor setFaceObservations:];
-[FigIntelligentDistortionCorrectionProcessor opticalCenterOffset];
-[FigIntelligentDistortionCorrectionProcessor gdcInversePolynomial];
-[FigIntelligentDistortionCorrectionProcessor inputImageAppliedScalingFactors];
-[FigIntelligentDistortionCorrectionProcessor usePrecomputedPolynomialsAndOpticalCenterOffset];
-[FigIntelligentDistortionCorrectionProcessor lowResSegmentationMask];
-[FigIntelligentDistortionCorrectionProcessor gdcSource];
-[FigIntelligentDistortionCorrectionProcessor deviceWasStationaryDuringCapture];
-[FigIntelligentDistortionCorrectionProcessor setUseBilinearInterpolation:];
-[FigIntelligentDistortionCorrectionProcessor setGdcInversePolynomial:];
-[FigIntelligentDistortionCorrectionProcessor setUsePrecomputedPolynomialsAndOpticalCenterOffset:];
-[FigIntelligentDistortionCorrectionProcessor inputImageCropRect];
-[FigIntelligentDistortionCorrectionProcessor setOutputImage:];
-[FigIntelligentDistortionCorrectionProcessor applyResolutionInvariantWarp];
-[FigIntelligentDistortionCorrectionProcessor setApplyResolutionInvariantWarp:];
-[FigIntelligentDistortionCorrectionProcessor gdcForwardPolynomial];
-[FigIntelligentDistortionCorrectionProcessor determineWorkingBufferRequirements:maximumInputImageWidth:maximumInputImageHeight:maximumSegmentationMaskWidth:maximumSegmentationMaskHeight:];
-[FigIntelligentDistortionCorrectionProcessor processIntelligentDistortionCorrection];
-[FigIntelligentDistortionCorrectionProcessor setStereoRectificationInverseHomography:];
-[FigIntelligentDistortionCorrectionProcessor setInputImageAppliedOffsets:];
-[FigIntelligentDistortionCorrectionProcessor finalImageDimensions];
-[FigIntelligentDistortionCorrectionProcessor inputImageMetadataDictionary];
-[FigIntelligentDistortionCorrectionProcessor processGeometricDistortionCorrection];
-[FigIntelligentDistortionCorrectionProcessor setUseDeepTransferAccommodations:];
-[FigIntelligentDistortionCorrectionProcessor stereoRectificationInverseHomography];
-[FigIntelligentDistortionCorrectionProcessor getParametersListName];
-[FigIntelligentDistortionCorrectionProcessor setLowResSegmentationMask:];
-[FigIntelligentDistortionCorrectionProcessor applyExistingCorrectionToSecondaryAsset:outputPixelBuffer:primaryImageDimensions:];
-[FigIntelligentDistortionCorrectionProcessor globalTransformIsValid];
-[FigIntelligentDistortionCorrectionProcessor setApplyStereoRectificationHomography:];
-[FigIntelligentDistortionCorrectionProcessor applyStereoRectificationHomography];
-[FigIntelligentDistortionCorrectionProcessor faceObservations];
-[FigIntelligentDistortionCorrectionProcessor setGdcForwardPolynomial:];
-[FigIntelligentDistortionCorrectionProcessor useBilinearInterpolation];
-[FigIntelligentDistortionCorrectionProcessor setInputImageCropRect:];
-[FigIntelligentDistortionCorrectionProcessor useDeepTransferAccommodations];
-[FigIntelligentDistortionCorrectionProcessor applyZoom];
-[FigIntelligentDistortionCorrectionProcessor setFinalImageDimensions:];
-[FigIntelligentDistortionCorrectionProcessor applyExistingCorrectionToSecondaryAsset:inputCrop:primaryImageDimensions:inputHorizontalSecondaryToPrimaryScaleFactor:inputVerticalSecondaryToPrimaryScaleFactor:inputHorizontalSecondaryToPrimaryShift:inputVerticalSecondaryToPrimaryShift:outputPixelBuffer:outputHorizontalAdditionalScaleFactor:outputVerticalAdditionalScaleFactor:];
-[FigIntelligentDistortionCorrectionProcessor zoomWasApplied];
-[FigIntelligentDistortionCorrectionProcessor makernoteEntry];
-[FigIntelligentDistortionCorrectionProcessor setProcessIntelligentDistortionCorrection:];
-[FigIntelligentDistortionCorrectionProcessor setProcessGeometricDistortionCorrection:];
-[FigIntelligentDistortionCorrectionProcessor withTemporalConsistency];
-[FigIntelligentDistortionCorrectionProcessor setDeviceWasStationaryDuringCapture:];
-[FigIntelligentDistortionCorrectionProcessor setInputImageMetadataDictionary:];
-[FigIntelligentDistortionCorrectionProcessor correctionType];
-[FigIntelligentDistortionCorrectionProcessor setWithTemporalConsistency:];
-[FigIntelligentDistortionCorrectionProcessor setOpticalCenterOffset:];
-[FigIntelligentDistortionCorrectionProcessor outputValidBufferRect];
-[FigIntelligentDistortionCorrectionProcessor getAdjustedGDCInformation:];
-[FigIntelligentDistortionCorrectionProcessor setInputImageAppliedScalingFactors:];
-[FigIntelligentDistortionCorrectionProcessor setApplyZoom:];
-[FigIntelligentDistortionCorrectionProcessor inputImageAppliedOffsets];
-[FigIntelligentDistortionCorrectionProcessor setSharedMetalBuffer:offset:size:];
```
