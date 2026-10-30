# `BWVideoPIPOverlayNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 48 instance variables, 3 properties, 25 instance methods, 2 class methods

## Instance variables

```
@"<MTLCommandQueue>" _metalCommandQueue;
^{CGContext=} _bitmapContext;
@"BWScalingSession" _scalingSession;
B _useGPUForDrawing;
f _overCaptureTargetRatio;
B _overCaptureTargetRatioSmoothingEnabled;
i _zoomPIPWidth;
f _overCaptureTargetInterpolationScale;
f _overCaptureTargetRatioInterpolationStart;
f _lastTeleMaxScale;
f _lastTeleMaxScaleZoomFactor;
@"NSDictionary" _baseZoomFactorsByPortType;
f _singleStreamStabilizationHeadroomFraction;
f _singleStreamMinimumScale;
f _frameRate;
B _secondaryCameraStreamingEnabled;
^{opaqueCMSampleBuffer=} _previousAttachedSampleBuffer;
f _reticleLineThickness;
f _pipCornerRadius;
@"CIFilter<CIRoundedRectangleStrokeGenerator>" _drawRectangleFilter;
@"CIFilter<CIBlurredRoundedRectangleGenerator>" _drawDropShadowFilter;
@"CIFilter<CIRoundedRectangleGenerator>" _roundedCornersMaskFilter;
@"CIBlendKernel" _sourceOverBlendKernel;
@"CIContext" _ciContext;
B _gpuPathInitialized;
@"CIColor" _ciReticleColor;
@"<BWVideoPIPOverlayDelegate>" _delegate;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _normalizedOutputRect;
^{opaqueCMSampleBuffer=} _fadeReferenceSampleBuffer;
@"BWRamp" _fadeRamp;
f _fadeInDurationSeconds;
f _fadeOutDurationSeconds;
f _dropShadowWidth;
f _dropShadowBlurSigma;
f _dropShadowAlpha;
B _dropShadowEnabled;
B _releasesResourcesAtEndOfData;
B _smartStyleRenderingEnabled;
B _smartStyleHasBeenAlreadyApplied;
i _smartStyleRenderingMethod;
# _smartStyleClass;
@"<CMISmartStyle>" _currentStyle;
@"<CMISmartStyleProxyRenderer>" _smartStyleProxyRenderer;
^{__CVBuffer=} _smartStyleIntermediateUnstyled;
^{__CVBuffer=} _smartStyleIntermediateStyled;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _smartStyleIntermediateROI;
B _highQualitySamplingEnabled;
B _isDeviceBravoVariant;
```

## Properties

```
@property (TB,N,V_releasesResourcesAtEndOfData) releasesResourcesAtEndOfData;
@property (TB,N,V_smartStyleRenderingEnabled) smartStyleRenderingEnabled;
@property (Tf,R,N,V_fadeOutDurationSeconds) fadeOutDurationSeconds;
```

## Class methods

```
+[BWVideoPIPOverlayNode initialize];
+[BWVideoPIPOverlayNode prewarmCoreImageShaders];
```

## Instance methods

```
-[BWVideoPIPOverlayNode setSmartStyleRenderingEnabled:];
-[BWVideoPIPOverlayNode prepareForCurrentConfigurationToBecomeLive];
-[BWVideoPIPOverlayNode smartStyleRenderingEnabled];
-[BWVideoPIPOverlayNode renderSampleBuffer:forInput:];
-[BWVideoPIPOverlayNode dealloc];
-[BWVideoPIPOverlayNode setReleasesResourcesAtEndOfData:];
-[BWVideoPIPOverlayNode _releaseResources];
-[BWVideoPIPOverlayNode releasesResourcesAtEndOfData];
-[BWVideoPIPOverlayNode _updateCurrentStyle:];
-[BWVideoPIPOverlayNode nodeSubType];
-[BWVideoPIPOverlayNode didSelectFormat:forInput:];
-[BWVideoPIPOverlayNode nodeType];
-[BWVideoPIPOverlayNode _loadAndConfigureSmartStyleProxyRenderer];
-[BWVideoPIPOverlayNode _drawOverlayRects:toPixelBuffer:withinRect:];
-[BWVideoPIPOverlayNode _drawPIPUsingCPUAndMSRToOutputPixelBuffer:attachedPixelBuffer:outputRect:inputRect:normalizedReticleRect:primaryCaptureRect:uprightExifOrientation:];
-[BWVideoPIPOverlayNode _drawPIPUsingGPUToOutputPixelBuffer:attachedPixelBuffer:filters:outputRect:inputRect:normalizedReticleRect:uprightExifOrientation:pipOpacity:];
-[BWVideoPIPOverlayNode _ensureGPUResources];
-[BWVideoPIPOverlayNode _overlayOffsetForPixelBuffer:primaryCaptureRect:];
-[BWVideoPIPOverlayNode _renderAttachedPixelBuffersFromSampleBuffer:toPixelBuffer:];
-[BWVideoPIPOverlayNode _renderSmartStyleToIntermediateBufferWithInputSampleBuffer:pipSourcePixelBuffer:inputRect:outputRect:];
-[BWVideoPIPOverlayNode _reticleCIColorForPixelBuffer:opacity:];
-[BWVideoPIPOverlayNode _strokedRectangleImageWithRect:thickness:c:];
-[BWVideoPIPOverlayNode didReachEndOfDataForInput:];
-[BWVideoPIPOverlayNode fadeOutDurationSeconds];
-[BWVideoPIPOverlayNode initWithDelegate:metalCommandQueue:secondaryCameraStreamingEnabled:secondaryCameraFrameRate:maxLossyCompressionLevel:isDeviceBravoVariant:baseZoomFactorsByPortType:];
```
