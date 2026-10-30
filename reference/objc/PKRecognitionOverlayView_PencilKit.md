# `PKRecognitionOverlayView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CHVisualizationManagerDelegate`
- 2 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"CHVisualizationManager" _visualizationManager;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _drawingTransform;
```

## Properties

```
@property (T{CGAffineTransform=dddddd},N,V_drawingTransform) drawingTransform;
@property (T@"CHVisualizationManager",R,N,V_visualizationManager) visualizationManager;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKRecognitionOverlayView dealloc];
-[PKRecognitionOverlayView drawRect:];
-[PKRecognitionOverlayView hitTest:withEvent:];
-[PKRecognitionOverlayView visualizationManager:needsDisplayInRect:];
-[PKRecognitionOverlayView visualizationManagerNeedsDisplay:];
-[PKRecognitionOverlayView drawingTransform];
-[PKRecognitionOverlayView initWithFrame:visualizationManager:];
-[PKRecognitionOverlayView setDrawingTransform:];
-[PKRecognitionOverlayView visualizationManager];
```
