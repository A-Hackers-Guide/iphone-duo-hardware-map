# `PKSelectionGlowRenderer`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKSelectionRendering`
- 11 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"CALayer" _highlightLayer;
@"CALayer" _strokePathsTilesLayer;
@"PKSelectionModificationKnob" _leftKnob;
@"PKSelectionModificationKnob" _rightKnob;
q _knobDragMode;
B _isDraggingKnob;
q _draggedKnobLocation;
@"NSMutableDictionary" _tiles;
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
-[PKSelectionGlowRenderer _accessibilityUserTestingChildren];
-[PKSelectionGlowRenderer _renderLiveSelectionPath:forStrokes:inDrawing:liveScrollOffset:];
-[PKSelectionGlowRenderer _didBeginDraggingSelection];
-[PKSelectionGlowRenderer _didEndDraggingSelection];
-[PKSelectionGlowRenderer _setupSelectionAdornment];
-[PKSelectionGlowRenderer adornmentLayer];
-[PKSelectionGlowRenderer editMenuLocation];
-[PKSelectionGlowRenderer initForLiveSelectionWithRenderingDelegate:];
-[PKSelectionGlowRenderer initWithStrokeSelection:renderingDelegate:];
-[PKSelectionGlowRenderer lassoPath];
```
