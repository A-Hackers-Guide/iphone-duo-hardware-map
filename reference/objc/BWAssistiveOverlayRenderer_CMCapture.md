# `BWAssistiveOverlayRenderer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 41 instance variables, 3 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
@"<MTLCommandQueue>" _commandQueue;
@"<MTLComputePipelineState>" _compositePipeline;
@"<MTLComputePipelineState>" _peakingOnlyPipeline;
@"<MTLComputePipelineState>" _clippingOnlyPipeline;
^{__CVMetalTextureCache=} _textureCache;
d _exposureClippingThreshold;
d _focusPeakingThreshold;
d _substrateSaturation;
_clippingColor;
_peakingColor;
q _clippingStyle;
d _substrateBrightness;
d _targetSubstrateSaturation;
d _startSubstrateSaturation;
_targetClippingColor;
_startClippingColor;
_targetPeakingColor;
_startPeakingColor;
d _targetSubstrateBrightness;
d _startSubstrateBrightness;
{?="value"q"timescale"i"flags"I"epoch"q} _substrateSaturationStartTime;
{?="value"q"timescale"i"flags"I"epoch"q} _substrateSaturationDuration;
{?="value"q"timescale"i"flags"I"epoch"q} _substrateBrightnessStartTime;
{?="value"q"timescale"i"flags"I"epoch"q} _substrateBrightnessDuration;
{?="value"q"timescale"i"flags"I"epoch"q} _clippingColorStartTime;
{?="value"q"timescale"i"flags"I"epoch"q} _clippingColorDuration;
{?="value"q"timescale"i"flags"I"epoch"q} _peakingColorStartTime;
{?="value"q"timescale"i"flags"I"epoch"q} _peakingColorDuration;
B _substrateSaturationAnimating;
B _substrateBrightnessAnimating;
B _clippingColorAnimating;
B _peakingColorAnimating;
B _prepared;
@"BWVideoFormat" _videoFormat;
^{opaqueCMFormatDescription=} _cachedFormatDescription;
I _cachedPixelFormat;
Q _cachedWidth;
Q _cachedHeight;
AB _invalidated;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _paramsLock;
```

## Properties

```
@property (T@"BWVideoFormat",R,N,V_videoFormat) videoFormat;
@property (TB,R,N,GisPrepared,V_prepared) prepared;
@property (TB,R,N,GisInvalidated) invalidated;
```

## Instance methods

```
-[BWAssistiveOverlayRenderer isPrepared];
-[BWAssistiveOverlayRenderer videoFormat];
-[BWAssistiveOverlayRenderer init];
-[BWAssistiveOverlayRenderer dealloc];
-[BWAssistiveOverlayRenderer isInvalidated];
-[BWAssistiveOverlayRenderer invalidate];
-[BWAssistiveOverlayRenderer setClippingStyle:];
-[BWAssistiveOverlayRenderer _prepareWithMetalCommandQueue:videoFormat:];
-[BWAssistiveOverlayRenderer _updateConvergenceWithPresentationTime:];
-[BWAssistiveOverlayRenderer disableAllOverlaysWithConvergenceTime:];
-[BWAssistiveOverlayRenderer isRenderPathAvailable];
-[BWAssistiveOverlayRenderer prepareWithMetalCommandQueue:videoFormat:];
-[BWAssistiveOverlayRenderer renderSampleBuffer:toOutputPixelBuffer:];
-[BWAssistiveOverlayRenderer setClippingColor:];
-[BWAssistiveOverlayRenderer setClippingColor:convergenceTime:];
-[BWAssistiveOverlayRenderer setClippingThreshold:];
-[BWAssistiveOverlayRenderer setFocusPeakingThreshold:];
-[BWAssistiveOverlayRenderer setPeakingColor:];
-[BWAssistiveOverlayRenderer setPeakingColor:convergenceTime:];
-[BWAssistiveOverlayRenderer setSubstrateBrightness:];
-[BWAssistiveOverlayRenderer setSubstrateBrightness:convergenceTime:];
-[BWAssistiveOverlayRenderer setSubstrateSaturation:];
-[BWAssistiveOverlayRenderer setSubstrateSaturation:convergenceTime:];
```
