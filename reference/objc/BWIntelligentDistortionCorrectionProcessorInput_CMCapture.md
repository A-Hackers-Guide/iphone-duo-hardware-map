# `BWIntelligentDistortionCorrectionProcessorInput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerInput`
- 16 instance variables, 15 properties, 32 instance methods, 0 class methods

## Instance variables

```
B _processIntelligentDistortionCorrection;
B _processGeometricDistortionCorrection;
B _applyZoom;
i _resolvedProcessingResolutionFlavor;
^{opaqueCMSampleBuffer=} _image;
B _imageSet;
Q _imageBufferType;
@"<BWIntelligentDistortionCorrectionProcessorInputDelegate>" _delegate;
B _applyStereoRectificationHomography;
B _useBilinearInterpolation;
B _geometricDistortionCorrectionUsePrecomputedPolynomialsAndOpticalCenterOffset;
B _receivedAllInputs;
@"NSData" _geometricDistortionCorrectionForwardPolynomial;
@"NSData" _geometricDistortionCorrectionInversePolynomial;
{CGPoint="x"d"y"d} _geometricDistortionCorrectionOpticalCenterOffset;
{?="columns"[3]} _stereoRectificationInverseHomography;
```

## Properties

```
@property (TB,N,V_receivedAllInputs) receivedAllInputs;
@property (T@"<BWIntelligentDistortionCorrectionProcessorInputDelegate>",&,N,V_delegate) delegate;
@property (TB,N,V_processIntelligentDistortionCorrection) processIntelligentDistortionCorrection;
@property (TB,N,V_processGeometricDistortionCorrection) processGeometricDistortionCorrection;
@property (TB,N,V_applyZoom) applyZoom;
@property (TB,N,V_applyStereoRectificationHomography) applyStereoRectificationHomography;
@property (T{?=[3]},N,V_stereoRectificationInverseHomography) stereoRectificationInverseHomography;
@property (TB,N,V_useBilinearInterpolation) useBilinearInterpolation;
@property (T@"NSData",&,N,V_geometricDistortionCorrectionForwardPolynomial) geometricDistortionCorrectionForwardPolynomial;
@property (T@"NSData",&,N,V_geometricDistortionCorrectionInversePolynomial) geometricDistortionCorrectionInversePolynomial;
@property (T{CGPoint=dd},N,V_geometricDistortionCorrectionOpticalCenterOffset) geometricDistortionCorrectionOpticalCenterOffset;
@property (TB,N,V_geometricDistortionCorrectionUsePrecomputedPolynomialsAndOpticalCenterOffset) geometricDistortionCorrectionUsePrecomputedPolynomialsAndOpticalCenterOffset;
@property (Ti,N,V_resolvedProcessingResolutionFlavor) resolvedProcessingResolutionFlavor;
@property (T^{opaqueCMSampleBuffer=},R,N) image;
@property (TQ,R,N) imageBufferType;
```

## Instance methods

```
-[BWIntelligentDistortionCorrectionProcessorInput addImage:imageBufferType:];
-[BWIntelligentDistortionCorrectionProcessorInput imageBufferType];
-[BWIntelligentDistortionCorrectionProcessorInput setGeometricDistortionCorrectionUsePrecomputedPolynomialsAndOpticalCenterOffset:];
-[BWIntelligentDistortionCorrectionProcessorInput setUseBilinearInterpolation:];
-[BWIntelligentDistortionCorrectionProcessorInput dealloc];
-[BWIntelligentDistortionCorrectionProcessorInput resolvedProcessingResolutionFlavor];
-[BWIntelligentDistortionCorrectionProcessorInput setGeometricDistortionCorrectionInversePolynomial:];
-[BWIntelligentDistortionCorrectionProcessorInput setGeometricDistortionCorrectionOpticalCenterOffset:];
-[BWIntelligentDistortionCorrectionProcessorInput receivedAllInputs];
-[BWIntelligentDistortionCorrectionProcessorInput setReceivedAllInputs:];
-[BWIntelligentDistortionCorrectionProcessorInput processIntelligentDistortionCorrection];
-[BWIntelligentDistortionCorrectionProcessorInput setStereoRectificationInverseHomography:];
-[BWIntelligentDistortionCorrectionProcessorInput processGeometricDistortionCorrection];
-[BWIntelligentDistortionCorrectionProcessorInput setDelegate:];
-[BWIntelligentDistortionCorrectionProcessorInput stereoRectificationInverseHomography];
-[BWIntelligentDistortionCorrectionProcessorInput geometricDistortionCorrectionForwardPolynomial];
-[BWIntelligentDistortionCorrectionProcessorInput geometricDistortionCorrectionInversePolynomial];
-[BWIntelligentDistortionCorrectionProcessorInput setApplyStereoRectificationHomography:];
-[BWIntelligentDistortionCorrectionProcessorInput applyStereoRectificationHomography];
-[BWIntelligentDistortionCorrectionProcessorInput useBilinearInterpolation];
-[BWIntelligentDistortionCorrectionProcessorInput delegate];
-[BWIntelligentDistortionCorrectionProcessorInput applyZoom];
-[BWIntelligentDistortionCorrectionProcessorInput description];
-[BWIntelligentDistortionCorrectionProcessorInput setGeometricDistortionCorrectionForwardPolynomial:];
-[BWIntelligentDistortionCorrectionProcessorInput setProcessIntelligentDistortionCorrection:];
-[BWIntelligentDistortionCorrectionProcessorInput setProcessGeometricDistortionCorrection:];
-[BWIntelligentDistortionCorrectionProcessorInput image];
-[BWIntelligentDistortionCorrectionProcessorInput initWithSettings:portType:];
-[BWIntelligentDistortionCorrectionProcessorInput setResolvedProcessingResolutionFlavor:];
-[BWIntelligentDistortionCorrectionProcessorInput geometricDistortionCorrectionUsePrecomputedPolynomialsAndOpticalCenterOffset];
-[BWIntelligentDistortionCorrectionProcessorInput setApplyZoom:];
-[BWIntelligentDistortionCorrectionProcessorInput geometricDistortionCorrectionOpticalCenterOffset];
```
