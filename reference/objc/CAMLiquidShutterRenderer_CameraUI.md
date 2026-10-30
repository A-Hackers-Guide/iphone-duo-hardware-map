# `CAMLiquidShutterRenderer`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 13 properties, 31 instance methods, 0 class methods

## Instance variables

```
B _showDragHandle;
B __backgrounded;
d _blurRadius;
d _shadowSize;
@"CAMetalLayer" _metalLayer;
@"<MTLDevice>" __device;
@"<MTLCommandQueue>" __commandQueue;
@"<MTLRenderPipelineState>" __renderPipelineState;
Q __neededRenderID;
Q __lastRenderedID;
{?="r"d"g"d"b"d"a"d} _shadowColor;
{?="position"{CGPoint="x"d"y"d}"size"d"backgroundSize"d"color"{?="r"d"g"d"b"d"a"d}"power"d} _centerShape;
{?="position"{CGPoint="x"d"y"d}"size"d"backgroundSize"d"color"{?="r"d"g"d"b"d"a"d}"power"d} _dragHandleShape;
```

## Properties

```
@property (T@"<MTLDevice>",R,N,V__device) _device;
@property (T@"<MTLCommandQueue>",R,N,V__commandQueue) _commandQueue;
@property (T@"<MTLRenderPipelineState>",R,N,V__renderPipelineState) _renderPipelineState;
@property (TB,N,S_setBackgrounded:,V__backgrounded) _backgrounded;
@property (TQ,N,V__neededRenderID) _neededRenderID;
@property (TQ,N,V__lastRenderedID) _lastRenderedID;
@property (T{?={CGPoint=dd}dd{?=dddd}d},N,V_centerShape) centerShape;
@property (T{?={CGPoint=dd}dd{?=dddd}d},N,V_dragHandleShape) dragHandleShape;
@property (TB,N,V_showDragHandle) showDragHandle;
@property (Td,N,V_blurRadius) blurRadius;
@property (Td,N,V_shadowSize) shadowSize;
@property (T{?=dddd},N,V_shadowColor) shadowColor;
@property (T@"CAMetalLayer",W,N,V_metalLayer) metalLayer;
```

## Instance methods

```
-[CAMLiquidShutterRenderer _applicationDidEnterBackground];
-[CAMLiquidShutterRenderer showDragHandle];
-[CAMLiquidShutterRenderer setShowDragHandle:];
-[CAMLiquidShutterRenderer setCenterShape:];
-[CAMLiquidShutterRenderer dealloc];
-[CAMLiquidShutterRenderer shadowColor];
-[CAMLiquidShutterRenderer setDragHandleShape:];
-[CAMLiquidShutterRenderer blurRadius];
-[CAMLiquidShutterRenderer metalLayer];
-[CAMLiquidShutterRenderer _device];
-[CAMLiquidShutterRenderer dragHandleShape];
-[CAMLiquidShutterRenderer setShadowColor:];
-[CAMLiquidShutterRenderer setBlurRadius:];
-[CAMLiquidShutterRenderer centerShape];
-[CAMLiquidShutterRenderer setShadowSize:];
-[CAMLiquidShutterRenderer shadowSize];
-[CAMLiquidShutterRenderer _applicationWillEnterForeground];
-[CAMLiquidShutterRenderer _neededRenderID];
-[CAMLiquidShutterRenderer _lastRenderedID];
-[CAMLiquidShutterRenderer markNeedsRender];
-[CAMLiquidShutterRenderer _backgrounded];
-[CAMLiquidShutterRenderer _commandQueue];
-[CAMLiquidShutterRenderer _fragmentForShape:scale:];
-[CAMLiquidShutterRenderer _orthographicMatrixWithLeft:right:bottom:top:near:far:];
-[CAMLiquidShutterRenderer _renderPipelineState];
-[CAMLiquidShutterRenderer _setBackgrounded:];
-[CAMLiquidShutterRenderer initWithDevice:commandQueue:pixelFormat:];
-[CAMLiquidShutterRenderer renderIfNecessary];
-[CAMLiquidShutterRenderer setMetalLayer:];
-[CAMLiquidShutterRenderer set_lastRenderedID:];
-[CAMLiquidShutterRenderer set_neededRenderID:];
```
