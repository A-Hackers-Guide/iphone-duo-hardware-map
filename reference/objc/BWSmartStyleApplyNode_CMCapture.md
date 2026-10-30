# `BWSmartStyleApplyNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 21 instance variables, 1 properties, 19 instance methods, 1 class methods

## Instance variables

```
i _renderingMethod;
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
f _globalLocalSystemMixFactorDecayRate;
i _mostRecentQuadraBinningFactor;
B _currentRecordingSupportsReversibility;
@"BWPixelBufferPool" _filteredCoefficientsPixelBufferPool;
I _filteredCoefficientsPixelBufferPoolSize;
Q _filterType;
i _maxLossyCompressionLevel;
@"BWFigCaptureISPProcessingSession" _ispSTENProcessingSession;
B _applyDither;
{?="currentTransform"{?="rotationDegrees"i"flipHorizontal"B"flipVertical"B}"lastTransform"{?="rotationDegrees"i"flipHorizontal"B"flipVertical"B}"lastStitcherRampInProgress"B"lastApplyGlobalCoefficients"B"transformChangedSkipFrames"i"savedMaskAgeFrames"i"waitingForFirstMaskAfterPortTypeChange"B"savedMaskPixelBuffer"^{__CVBuffer}"savedMaskCropRect"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"savedMaskTransform"{?="rotationDegrees"i"flipHorizontal"B"flipVertical"B}"savedMaskSwitchingFormatZoomFactor"f"frozenStyle"@"FigCaptureTextureStyle""lastPortType"@"NSString""inactiveFrames"i} _skinSmoothMaskState;
```

## Properties

```
@property (Ti,N,V_maxLossyCompressionLevel) maxLossyCompressionLevel;
```

## Class methods

```
+[BWSmartStyleApplyNode initialize];
```

## Instance methods

```
-[BWSmartStyleApplyNode prepareForCurrentConfigurationToBecomeLive];
-[BWSmartStyleApplyNode renderSampleBuffer:forInput:];
-[BWSmartStyleApplyNode _consumeSampleBufferAttachments:];
-[BWSmartStyleApplyNode setMaxLossyCompressionLevel:];
-[BWSmartStyleApplyNode maxLossyCompressionLevel];
-[BWSmartStyleApplyNode _getSampleBufferPresentationTimeStamp:];
-[BWSmartStyleApplyNode dealloc];
-[BWSmartStyleApplyNode _loadAndConfigureSmartStyleBundleWithSquareAspectRatioConfigEnabled:];
-[BWSmartStyleApplyNode _canRenderWithStyleEngineApplyForInput:];
-[BWSmartStyleApplyNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWSmartStyleApplyNode _updateCurrentStyle:];
-[BWSmartStyleApplyNode nodeSubType];
-[BWSmartStyleApplyNode nodeType];
-[BWSmartStyleApplyNode _loadAndConfigureSmartStyleProxyRenderer];
-[BWSmartStyleApplyNode _updateSupportedPixelFormats];
-[BWSmartStyleApplyNode _applySmartStyleFromSampleBuffer:to:];
-[BWSmartStyleApplyNode _applySmartStyleProxyRenderingWithMethod:fromSampleBuffer:to:];
-[BWSmartStyleApplyNode didReachEndOfDataForInput:];
-[BWSmartStyleApplyNode initWithMetalCommandQueue:renderingMethod:ispSTENProcessingSession:squareAspectRatioConfigEnabled:];
```
