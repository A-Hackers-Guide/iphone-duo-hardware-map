# `BWBroadcastVideoSinkNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWSinkNode`
- Protocols: `BWFigVideoCaptureDeviceMaximumFrameRateChangedDelegate`
- 49 instance variables, 4 properties, 21 instance methods, 3 class methods

## Instance variables

```
@"CAContext" _context;
@"CAMetalLayer" _metalLayer;
@"<MTLDevice>" _metalDevice;
@"<MTLCommandQueue>" _commandQueue;
^{__CVBuffer=} _testPatternBuffer;
@"FigCaptureSourceConfiguration" _sourceConfiguration;
q _droppedFrameReplacementPolicy;
q _testPatternToInject;
I _rotationDegrees;
B _mirroringEnabled;
q _maxBufferedFrameCount;
@"FigCaptureAncillaryDataEncoder" _ancillaryDataEncoder;
@"CADisplayLink" _displayLink;
@"NSMutableArray" _frameBuffer;
@"NSMutableArray" _framesScheduledToDisplay;
@"NSObject<OS_dispatch_queue>" _broadcastSinkQueue;
@"FigWeakReference" _broadcastVideoSinkNode;
B _teardownSinkNodeCompleted;
I _displayId;
i _displayChangeNotifyToken;
B _displayLinkCallbackCalled;
d _displayLinkStartTime;
B _suppressDropNotifications;
Q _consecutiveOverflowCallbacks;
Q _consecutiveOverflowThreshold;
Q _consecutiveUnderrunCallbacks;
@"<MTLRenderPipelineState>" _renderPipelineStateYUV;
@"<MTLBuffer>" _vertexBuffer;
@"<MTLSamplerState>" _samplerState;
^{__CVMetalTextureCache=} _textureCache;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _transform;
@"FigWeakReference" _delegate;
^{__CVBuffer=} _lastRenderedFrame;
@"FigWeakReference" _captureDevice;
d _currentDisplayedFrameRate;
d _lastRequestedFrameRate;
d _lastDriftReassertTime;
@"<MTLDevice>" _cachedPipelineDevice;
@"<MTLLibrary>" _cachedShaderLibrary;
@"<MTLBuffer>" _cachedVertexBuffer;
@"<MTLSamplerState>" _cachedSamplerState;
@"NSMutableDictionary" _cachedRenderPipelineStatesByPixelFormat;
B _hasLivePipeConfiguration;
{?="width"i"height"i} _livePipeSourceDimensions;
i _livePipeBitDepth;
d _livePipeFrameRate;
B _livePipeIsFullRange;
B _livePipeIs444;
B _livePipeIsHDRRequired;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWBroadcastVideoSinkNode initialize];
+[BWBroadcastVideoSinkNode createTextureFromCache:pixelBuffer:planeIndex:outTexture:];
+[BWBroadcastVideoSinkNode getColorConversionMatrix:outMatrix:outOffset:];
```

## Instance methods

```
-[BWBroadcastVideoSinkNode setCaptureDevice:];
-[BWBroadcastVideoSinkNode renderSampleBuffer:forInput:];
-[BWBroadcastVideoSinkNode flush];
-[BWBroadcastVideoSinkNode dealloc];
-[BWBroadcastVideoSinkNode setMirroringEnabled:];
-[BWBroadcastVideoSinkNode setRotationDegrees:];
-[BWBroadcastVideoSinkNode didReachEndOfDataForConfigurationID:input:];
-[BWBroadcastVideoSinkNode nodeSubType];
-[BWBroadcastVideoSinkNode setDiscardsSampleData:];
-[BWBroadcastVideoSinkNode setDroppedFrameReplacementPolicy:];
-[BWBroadcastVideoSinkNode setMaxBufferedFrameCount:];
-[BWBroadcastVideoSinkNode setTestPatternToInject:];
-[BWBroadcastVideoSinkNode _desiredBufferDepth];
-[BWBroadcastVideoSinkNode _postDidDropSampleBufferNotificationWithPresentationTimeStamp:dropReason:];
-[BWBroadcastVideoSinkNode _postVideoSettingsDidChangeNotification];
-[BWBroadcastVideoSinkNode _renderBlackFrameToDrawable:];
-[BWBroadcastVideoSinkNode didChangeMaximumFrameRate:];
-[BWBroadcastVideoSinkNode displayLinkCallback:];
-[BWBroadcastVideoSinkNode initWithSinkID:sourceConfiguration:sinkConfiguration:delegate:];
-[BWBroadcastVideoSinkNode processUserAncillaryData:];
-[BWBroadcastVideoSinkNode setVideoCaptureConnectionConfiguration:];
```
