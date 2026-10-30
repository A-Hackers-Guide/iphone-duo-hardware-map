# `PKSelectionHighlightRenderer`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKSelectionRendering`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"CAShapeLayer" _highlightLayer;
@"UIBezierPath" _lassoPath;
@"PKStrokeSelection" _strokeSelection;
@"<PKSelectionRenderingDelegate>" _renderingDelegate;
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
-[PKSelectionHighlightRenderer _accessibilityUserTestingChildren];
-[PKSelectionHighlightRenderer _renderLiveSelectionPath:forStrokes:inDrawing:liveScrollOffset:];
-[PKSelectionHighlightRenderer _didBeginDraggingSelection];
-[PKSelectionHighlightRenderer _didEndDraggingSelection];
-[PKSelectionHighlightRenderer _setupSelectionAdornment];
-[PKSelectionHighlightRenderer adornmentLayer];
-[PKSelectionHighlightRenderer editMenuLocation];
-[PKSelectionHighlightRenderer initForLiveSelectionWithRenderingDelegate:];
-[PKSelectionHighlightRenderer initWithStrokeSelection:renderingDelegate:];
-[PKSelectionHighlightRenderer lassoPath];
```
