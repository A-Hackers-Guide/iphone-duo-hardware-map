# `PKController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _renderedStrokes;
@"NSMutableArray" _mutableRenderedStrokes;
@"PKMetalConfig" _metalConfig;
B _sixChannelBlending;
@"NSMutableArray" _liveDrawingUndoCommands;
B _liveInteraction;
B _drawBitmapEraserMask;
B _onDrawingQueue;
@"NSObject<PKControllerDelegate>" _delegate;
@"PKMetalRendererController" _rendererController;
@"PKDrawing" _drawing;
@"NSObject<OS_dispatch_semaphore>" _interactSemaphore;
@"NSObject<OS_dispatch_queue>" _interactQueue;
@"NSObject<OS_dispatch_queue>" _drawingQueue;
@"NSObject<OS_dispatch_queue>" _backgroundQueue;
```

## Instance methods

```
-[PKController init];
```
