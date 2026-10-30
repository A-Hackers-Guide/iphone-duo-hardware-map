# `PKMetalRendererController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKRendererVSyncControllerDelegate`
- 68 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"PKMetalConfig" _metalConfig;
B _synchronous;
@"NSObject<OS_dispatch_queue>" _renderQueue;
Ai _cancelLongRunningRenderingCount;
Ai _cancelAllRendering;
@"NSObject<OS_dispatch_semaphore>" _canBeginRenderSemaphore;
{atomic_flag="_Value"AB} _readyToBeginRender;
Ad _lastFrameDuration;
AQ _lastPresentationTime;
Ad _skipRendersUntilTime;
B _vSyncControllerIsActive;
@"PKRendererVSyncController" _currentVSyncController;
Ai _queuedRenders;
@"NSMutableArray" _postPresentCallbacks;
B _isTorndown;
{CGSize="width"d"height"d} _pixelSize;
{CGSize="width"d"height"d} _actualSize;
q _presentationCount;
{PKRunningStat="isAngle"B"numValues"q"numValuesOverLimit"q"oldM"d"newM"d"oldS"d"newS"d"minValue"d"maxValue"d"limit"d"lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} _strokeLatencyStat;
{PKRunningStat="isAngle"B"numValues"q"numValuesOverLimit"q"oldM"d"newM"d"oldS"d"newS"d"minValue"d"maxValue"d"limit"d"lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} _predictedTouchesLatencyStat;
@"<MTLTexture>" _currentTextureTarget;
@"<CAMetalDrawable>" _currentDrawable;
@"<MTLTexture>" _currentMultiplyTextureTarget;
@"<CAMetalDrawable>" _currentMultiplyDrawable;
^{CGImage=} _paperTextureImage;
{CGPoint="x"d"y"d} _canvasOffset;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _strokeTransformForRenderQueue;
@? _canvasOffsetBlock;
@"NSArray" _liveStrokeStrokes;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _liveStrokeStrokesAnimationBounds;
B _dirtyRectMightBeInvalid;
B _renderingForPreview;
@"NSString" _currentInkIdentifier;
d _timestampForDrawingBegan;
@"NSObject<OS_dispatch_semaphore>" _updateCycleSemaphore;
@"NSObject<OS_dispatch_semaphore>" _updateCycleRendererReadySemaphore;
B _isPDFCanvasForAnalytics;
Q _extendedRangePixelFormat;
B _sixChannelUsesWideGamut;
B _liveStrokeMode;
B _fadeOutStrokesMode;
B _invertColors;
B _wantsExtendedDynamicRangeContent;
B _drawBitmapEraserMask;
B _combineStrokesAllowed;
B _allowBrushIndicator;
@"<PKMetalRendererControllerDelegate>" _delegate;
Q _pixelFormat;
Q _sixChannelMetalLayerPixelFormat;
d _contentZoomScale;
@"PKStrokeGenerator" _inputController;
@"PKLinedPaper" _linedPaper;
d _liveStrokeElapsedTime;
d _liveStrokeDuration;
d __latestLatency;
@"NSString" _vSyncDeviceName;
@"CAMetalLayer" _presentationLayer;
@"CAMetalLayer" _multiplyPresentationLayer;
q _sixChannelBlendingMode;
Q _previewStrokeMaxPoints;
d _previewStrokeAlpha;
@"PKMetalRenderer" _renderer;
d _inputScale;
{CGSize="width"d"height"d} _liveStrokeMaxSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _viewScissor;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _strokeTransform;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _paperTransform;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _renderTransform;
```

## Instance methods

```
-[PKMetalRendererController dealloc];
-[PKMetalRendererController signalVSyncSemaphore:presentationTime:];
```
