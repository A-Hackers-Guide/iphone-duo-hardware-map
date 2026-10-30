# `PKPaintAreaViewSurface`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKControllerDelegate`, `PKMetalRendererControllerDelegate`
- 20 instance variables, 19 properties, 36 instance methods, 0 class methods

## Instance variables

```
@"PKController" _drawingController;
@"NSMutableArray" _textureSet;
{CGSize="width"d"height"d} _pixelSize;
{CGPoint="x"d"y"d} _oldEraseLocation;
@"CIContext" _imageContext;
@"<MTLDevice>" _device;
B _isDrawing;
B _waitingForStrokeToEnd;
B _isErasingObjects;
B _isMipmapped;
@"NSMutableArray" _strokesToErase;
@"NSMutableSet" _strokeIDsToErase;
@"PKPaintAreaView" _paintAreaView;
@"<PKPaintSurface>" _surface;
d _textureScale;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@"<PKDrawingUUID>" _drawingUUID;
{CGSize="width"d"height"d} _drawingSize;
{CGPoint="x"d"y"d} _previousPoint;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _strokeTransform;
```

## Properties

```
@property (TB,N,V_isDrawing) isDrawing;
@property (TB,R,N,V_waitingForStrokeToEnd) waitingForStrokeToEnd;
@property (TB,R,N,V_isErasingObjects) isErasingObjects;
@property (T@"NSMutableArray",R,N,V_strokesToErase) strokesToErase;
@property (T@"NSMutableSet",R,N,V_strokeIDsToErase) strokeIDsToErase;
@property (T@"PKController",R,N,V_drawingController) drawingController;
@property (T@"PKPaintAreaView",W,N,V_paintAreaView) paintAreaView;
@property (T@"<PKPaintSurface>",R,N,V_surface) surface;
@property (T{CGSize=dd},R,N,V_drawingSize) drawingSize;
@property (Td,R,N,V_textureScale) textureScale;
@property (T{CGAffineTransform=dddddd},R,N,V_strokeTransform) strokeTransform;
@property (TB,R,N,V_isMipmapped) isMipmapped;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_dispatchQueue) dispatchQueue;
@property (T@"<PKDrawingUUID>",R,N,V_drawingUUID) drawingUUID;
@property (T{CGPoint=dd},N,V_previousPoint) previousPoint;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKPaintAreaViewSurface dispatchQueue];
-[PKPaintAreaViewSurface setPreviousPoint:];
-[PKPaintAreaViewSurface surface];
-[PKPaintAreaViewSurface previousPoint];
-[PKPaintAreaViewSurface dealloc];
-[PKPaintAreaViewSurface isErasingObjects];
-[PKPaintAreaViewSurface isDrawing];
-[PKPaintAreaViewSurface strokeTransform];
-[PKPaintAreaViewSurface eraserCancelled];
-[PKPaintAreaViewSurface drawingCancelled];
-[PKPaintAreaViewSurface eraseStrokesForPoint:prevPoint:];
-[PKPaintAreaViewSurface strokeIDsToErase];
-[PKPaintAreaViewSurface drawingChanged:];
-[PKPaintAreaViewSurface _didFinishErasingStrokes:];
-[PKPaintAreaViewSurface strokesToErase];
-[PKPaintAreaViewSurface setIsDrawing:];
-[PKPaintAreaViewSurface drawingSize];
-[PKPaintAreaViewSurface CIImageFromTexture:];
-[PKPaintAreaViewSurface _setupPKController];
-[PKPaintAreaViewSurface dispatchSyncOnSurfaceQueue:];
-[PKPaintAreaViewSurface drawingBegan:activeInputProperties:inputType:];
-[PKPaintAreaViewSurface drawingController];
-[PKPaintAreaViewSurface drawingEndedWithDetectedShape:completionBlock:];
-[PKPaintAreaViewSurface drawingUUID];
-[PKPaintAreaViewSurface eraserBeganAtLocation:];
-[PKPaintAreaViewSurface eraserEnded];
-[PKPaintAreaViewSurface eraserMovedToLocation:];
-[PKPaintAreaViewSurface initWithPaintSurface:dispatchQueue:device:];
-[PKPaintAreaViewSurface isMipmapped];
-[PKPaintAreaViewSurface metalRendererController:didCommitRenderingIntoTexture:];
-[PKPaintAreaViewSurface nextTextureTargetForMetalRendererController:];
-[PKPaintAreaViewSurface paintAreaView];
-[PKPaintAreaViewSurface setPaintAreaView:];
-[PKPaintAreaViewSurface textureScale];
-[PKPaintAreaViewSurface vsync:];
-[PKPaintAreaViewSurface waitingForStrokeToEnd];
```
