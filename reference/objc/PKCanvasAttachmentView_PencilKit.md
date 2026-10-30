# `PKCanvasAttachmentView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKAttachmentView`
- 4 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
B __wantsFullyRenderedNotification;
@"PKCanvasView" _canvasView;
d _drawingWidth;
@"NSMutableArray" _fullyRenderedCompletionBlocks;
```

## Properties

```
@property (T@"PKCanvasView",W,N,V_canvasView) canvasView;
@property (TB,N,V__wantsFullyRenderedNotification) _wantsFullyRenderedNotification;
@property (Td,N,V_drawingWidth) drawingWidth;
@property (T@"NSMutableArray",&,N,V_fullyRenderedCompletionBlocks) fullyRenderedCompletionBlocks;
```

## Instance methods

```
-[PKCanvasAttachmentView setCanvasView:];
-[PKCanvasAttachmentView canvasView];
-[PKCanvasAttachmentView _wantsFullyRenderedNotification];
-[PKCanvasAttachmentView drawingDidChangeVisibleStrokes:];
-[PKCanvasAttachmentView disableTileAnimations];
-[PKCanvasAttachmentView drawingTransform];
-[PKCanvasAttachmentView drawingWidth];
-[PKCanvasAttachmentView fullyRendered];
-[PKCanvasAttachmentView fullyRenderedCompletionBlocks];
-[PKCanvasAttachmentView setDrawingWidth:];
-[PKCanvasAttachmentView setFullyRenderedCompletionBlocks:];
-[PKCanvasAttachmentView set_wantsFullyRenderedNotification:];
-[PKCanvasAttachmentView tiledView];
-[PKCanvasAttachmentView wantsFullyRendered];
```
