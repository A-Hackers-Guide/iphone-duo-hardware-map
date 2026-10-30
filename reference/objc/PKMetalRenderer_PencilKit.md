# `PKMetalRenderer`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 76 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
@"PKMetalRenderState" _currentRenderState;
Q _currentCacheSize;
@"<MTLDevice>" _device;
@"<MTLCommandQueueSPI>" _commandQueue;
{RendererFramebuffer="framebuffer"@"PKMetalFramebuffer""isNonPurgeable"B"mustBeCleared"B} _originalBackFramebuffer;
{RendererFramebuffer="framebuffer"@"PKMetalFramebuffer""isNonPurgeable"B"mustBeCleared"B} _sixChannelMultiplyFramebuffer;
B _shouldClearOriginalBackFramebuffer;
{?="red"d"green"d"blue"d"alpha"d} _originalBackClearColor;
[2{RendererFramebuffer="framebuffer"@"PKMetalFramebuffer""isNonPurgeable"B"mustBeCleared"B}] _paintFramebuffer;
[2{RendererFramebuffer="framebuffer"@"PKMetalFramebuffer""isNonPurgeable"B"mustBeCleared"B}] _paintAccumulationFramebuffer;
@"PKMetalFramebuffer" _paintFramebufferMask;
@"PKMetalFramebuffer" _maskMSAAFramebuffer;
@"PKMetalResourceHandler" _resourceHandler;
[2@"PKMetalFramebuffer"] _dummyPaintFramebuffer;
@"PKMetalFramebuffer" _dummyColorFramebuffer;
{CGSize="width"d"height"d} _drawingPixelSize;
^{CGColor=} _backgroundColor;
{CGSize="width"d"height"d} _actualSize;
d _fromStrokeSpaceScale;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _strokeTransform;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _viewScissor;
B _lastPointForEraserIsValid;
{_PKStrokePoint="timestamp"d"location"{CGPoint="x"d"y"d}"radius"d"aspectRatio"d"edgeWidth"d"force"d"azimuth"d"altitude"d"opacity"d"radius2"d"threshold"d"elevation"d} _lastPointForEraser;
@"<MTLTexture>" _paperTexture;
{CGSize="width"d"height"d} _paperTextureSize;
Q _originalBackPixelFormat;
Q _paintAndParticlePixelFormat;
B _sixChannelCanvasHasContentTexture;
B _wantsExtendedDynamicRangeContent;
{vector<PKMetalParticleStrokePoint, std::allocator<PKMetalParticleStrokePoint>>="__begin_"^{PKMetalParticleStrokePoint}"__end_"^{PKMetalParticleStrokePoint}""{?="__cap_"^{PKMetalParticleStrokePoint}}} _particleStrokePointBuffer;
{vector<PKMetalPaintStrokePoint, std::allocator<PKMetalPaintStrokePoint>>="__begin_"^{PKMetalPaintStrokePoint}"__end_"^{PKMetalPaintStrokePoint}""{?="__cap_"^{PKMetalPaintStrokePoint}}} _paintStrokePointBuffer;
{vector<PKMetalSDFPenStrokePoint, std::allocator<PKMetalSDFPenStrokePoint>>="__begin_"^{PKMetalSDFPenStrokePoint}"__end_"^{PKMetalSDFPenStrokePoint}""{?="__cap_"^{PKMetalSDFPenStrokePoint}}} _sdfPenStrokePointBuffer;
{vector<PKMetalLiveStrokePaintStrokePoint, std::allocator<PKMetalLiveStrokePaintStrokePoint>>="__begin_"^{PKMetalLiveStrokePaintStrokePoint}"__end_"^{PKMetalLiveStrokePaintStrokePoint}""{?="__cap_"^{PKMetalLiveStrokePaintStrokePoint}}} _liveStrokeStrokePointBuffer;
{shared_ptr<std::vector<(anonymous namespace)::StrokeVertex>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} _sharedStrokeVertexBuffer;
{shared_ptr<std::vector<PKMetalSDFStrokeVertex>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} _sharedSDFStrokeVertexBuffer;
{vector<(anonymous namespace)::AnimatingStroke, std::allocator<(anonymous namespace)::AnimatingStroke>>="__begin_"^{AnimatingStroke}"__end_"^{AnimatingStroke}""{?="__cap_"^{AnimatingStroke}}} _animatingStrokes;
@"PKStroke" _activeCombinedStroke;
@"NSArray" _activeCombinedAlternativeStrokes;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _paintFramebufferDirtyRect;
@"<MTLBuffer>" _randomNumberBuffer;
Q _renderMaskMSAASampleCount;
B _needRestartWorkaroundForOldIntelDrivers;
B _useComputeRenderCaches;
@"PKMetalResourceHandlerBuffer" _computeVertexBuffer;
q _sixChannelBlendingMode;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _drawableDirtyRect;
@"MTKTextureLoader" _textureLoader;
{vector<_PKStrokePoint, std::allocator<_PKStrokePoint>>="__begin_"^{_PKStrokePoint}"__end_"^{_PKStrokePoint}""{?="__cap_"^{_PKStrokePoint}}} previewStrokePoints;
{PKShaderPipelineConfig="framebufferPixelFormats"[8C]} _defaultNonSixChannelPipelineConfig;
{PKShaderPipelineConfig="framebufferPixelFormats"[8C]} _defaultSixChannelPipelineConfig;
{PKShaderPipelineConfig="framebufferPixelFormats"[8C]} _singleFramebufferPipelineConfig;
{?=""(?="point"{CGPoint="x"d"y"d}"location"{CGPoint="x"d"y"d})"force"d"azimuth"d"altitude"d"velocity"d"directionAngle"d"zPosition"d"timestamp"d"predicted"B"estimationUpdateIndex"q"length"d"distance"d"hasEstimatedAltitudeAndAzimuth"B"rollAngle"d"estimatedActiveInputProperties"q"estimatedActiveInputPropertiesExpectingUpdates"q} _latestInputPoint;
B _renderDebugColorForSynthesizedStrokes;
{RendererFramebuffer="framebuffer"@"PKMetalFramebuffer""isNonPurgeable"B"mustBeCleared"B} _addLayerFramebuffer;
{RendererFramebuffer="framebuffer"@"PKMetalFramebuffer""isNonPurgeable"B"mustBeCleared"B} _multiplyLayerFramebuffer;
B _solidColorBackboard;
B _oneRenderPassForLiveRendering;
B _fadeOutStrokesMode;
B _liveStrokeMode;
B _edgeMask;
B _invertColors;
B _drawBitmapEraserMask;
B _allowBrushIndicator;
B _combineStrokesAllowed;
Q _pixelFormat;
@"PKLinedPaper" _linedPaper;
^{CGColor=} _liveRenderingOverrideColor;
d _contentZoomScale;
d _backboardPaperMultiply;
d _inputScale;
d _eraserIndicatorAlpha;
d _previewStrokeAlpha;
d _previewStrokeMaxPoints;
d _liveStrokeElapsedTime;
{CGSize="width"d"height"d} _liveStrokeMaxSize;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _paperTransform;
```

## Instance methods

```
-[PKMetalRenderer dealloc];
```
