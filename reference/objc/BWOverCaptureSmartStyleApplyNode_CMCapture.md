# `BWOverCaptureSmartStyleApplyNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 31 instance variables, 2 properties, 26 instance methods, 1 class methods

## Instance variables

```
i _renderingMethod;
f _globalLocalSystemMixFactorDecayRate;
@"<MTLCommandQueue>" _metalCommandQueue;
# _smartStyleClass;
@"<CMISmartStyle>" _currentStyle;
@"<CMISmartStyleProxyRenderer>" _smartStyleProxyRenderer;
# _smartStyleProcessorInputOutputClass;
@"<CMISmartStyleProcessor>" _smartStyleProcessor;
B _firstFrame;
^{opaqueCMSampleBuffer=} _mostRecentCoefficients;
B _applyGlobalMostRecentCoefficients;
f _currentGlobalLocalMixFactor;
f _mostRecentZoomFactor;
f _mostRecentNonDisruptiveSwitchingFormatZoomFactor;
i _mostRecentQuadraBinningFactor;
@"BWVideoFormat" _filterCoefficientsVideoFormatToPrepare;
@"BWPixelBufferPool" _filteredCoefficientsPixelBufferPool;
I _filteredCoefficientsPixelBufferPoolSize;
Q _filterType;
@"BWPixelBufferPool" _unstyledThumbnailPixelBufferPool;
i _maxLossyCompressionLevel;
@"BWFigCaptureISPProcessingSession" _ispSTENProcessingSession;
^{__CVBuffer=} _identityCoefficientsPixelBuffer;
^{__CVBuffer=} _previewThumbnailBuffer;
B _useOptimizedThumbnailGeneration;
@"CMISmartStyleOvercaptureThumbnailGenerator" _overcaptureThumbnailGenerator;
B _didSetTimeToStartStyleEngineBypass;
f _timeToStartStyleEngineBypass;
B _applyDither;
{?="currentTransform"{?="rotationDegrees"i"flipHorizontal"B"flipVertical"B}"lastTransform"{?="rotationDegrees"i"flipHorizontal"B"flipVertical"B}"lastStitcherRampInProgress"B"lastApplyGlobalCoefficients"B"transformChangedSkipFrames"i"savedMaskAgeFrames"i"waitingForFirstMaskAfterPortTypeChange"B"savedMaskPixelBuffer"^{__CVBuffer}"savedMaskCropRect"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"savedMaskTransform"{?="rotationDegrees"i"flipHorizontal"B"flipVertical"B}"savedMaskSwitchingFormatZoomFactor"f"frozenStyle"@"FigCaptureTextureStyle""lastPortType"@"NSString""inactiveFrames"i} _skinSmoothMaskState;
{?="width"i"height"i} _outputDimensions;
```

## Properties

```
@property (Ti,N,V_maxLossyCompressionLevel) maxLossyCompressionLevel;
@property (T{?=ii},N) outputDimensions;
```

## Class methods

```
+[BWOverCaptureSmartStyleApplyNode initialize];
```

## Instance methods

```
-[BWOverCaptureSmartStyleApplyNode prepareForCurrentConfigurationToBecomeLive];
-[BWOverCaptureSmartStyleApplyNode renderSampleBuffer:forInput:];
-[BWOverCaptureSmartStyleApplyNode _consumeSampleBufferAttachments:];
-[BWOverCaptureSmartStyleApplyNode setOutputDimensions:];
-[BWOverCaptureSmartStyleApplyNode _applySmartStyleProxyRenderingWithMethod:onSampleBuffer:];
-[BWOverCaptureSmartStyleApplyNode setMaxLossyCompressionLevel:];
-[BWOverCaptureSmartStyleApplyNode _updateOutputRequirements];
-[BWOverCaptureSmartStyleApplyNode maxLossyCompressionLevel];
-[BWOverCaptureSmartStyleApplyNode _getSampleBufferPresentationTimeStamp:];
-[BWOverCaptureSmartStyleApplyNode dealloc];
-[BWOverCaptureSmartStyleApplyNode _applySmartStyleOnSampleBuffer:];
-[BWOverCaptureSmartStyleApplyNode outputDimensions];
-[BWOverCaptureSmartStyleApplyNode _loadAndConfigureSmartStyleBundleWithSquareAspectRatioConfigEnabled:];
-[BWOverCaptureSmartStyleApplyNode _calculateExtrapolationAndSpotlightZoom:inputCropRectWithinPrimaryCaptureRect:learningROIRect:adjustedPrimaryCaptureRect:adjustedSpotlightZoomRect:];
-[BWOverCaptureSmartStyleApplyNode _canRenderWithStyleEngineApplyForInput:];
-[BWOverCaptureSmartStyleApplyNode _getRotationConfigForPixelBuffer:];
-[BWOverCaptureSmartStyleApplyNode initWithMetalCommandQueue:ispSTENProcessingSession:squareAspectRatioConfigEnabled:];
-[BWOverCaptureSmartStyleApplyNode _computeAffineTransform:mirror:];
-[BWOverCaptureSmartStyleApplyNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWOverCaptureSmartStyleApplyNode didReachEndOfDataForConfigurationID:input:];
-[BWOverCaptureSmartStyleApplyNode _updateCurrentStyle:];
-[BWOverCaptureSmartStyleApplyNode nodeSubType];
-[BWOverCaptureSmartStyleApplyNode _getMirrorConfigForPixelBuffer:];
-[BWOverCaptureSmartStyleApplyNode nodeType];
-[BWOverCaptureSmartStyleApplyNode _loadAndConfigureSmartStyleProxyRenderer];
-[BWOverCaptureSmartStyleApplyNode _updateSupportedPixelFormats];
```
