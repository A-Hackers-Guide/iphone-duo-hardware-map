# `PKLassoRenderer`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKSelectionRendering`
- 7 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"CAShapeLayer" _lassoLayer;
@"CAShapeLayer" _whiteLassoLayer;
{CGPoint="x"d"y"d} _editMenuLocation;
@"UIBezierPath" _lassoPath;
@"PKStrokeSelection" _strokeSelection;
@"<PKSelectionRenderingDelegate>" _renderingDelegate;
@? _calculateSelectionHullBlock;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKLassoRenderer dealloc];
-[PKLassoRenderer _accessibilityUserTestingChildren];
-[PKLassoRenderer _renderLiveSelectionPath:forStrokes:inDrawing:liveScrollOffset:];
-[PKLassoRenderer _didBeginDraggingSelection];
-[PKLassoRenderer _didEndDraggingSelection];
-[PKLassoRenderer _setupSelectionAdornment];
-[PKLassoRenderer _updateLassoForAccessibility:];
-[PKLassoRenderer adornmentLayer];
-[PKLassoRenderer editMenuLocation];
-[PKLassoRenderer initForLiveSelectionWithRenderingDelegate:];
-[PKLassoRenderer initWithStrokeSelection:renderingDelegate:];
-[PKLassoRenderer lassoPath];
```
