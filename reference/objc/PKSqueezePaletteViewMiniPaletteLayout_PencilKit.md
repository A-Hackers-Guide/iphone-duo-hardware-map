# `PKSqueezePaletteViewMiniPaletteLayout`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `PKSqueezePaletteViewExpandedToolsLayoutDelegate`, `PKSqueezePaletteDrawingToolDelegate`, `PKSqueezePaletteViewUndoRedoLayoutDelegate`, `PKSqueezePaletteViewLayout`
- 42 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"PKSqueezePaletteViewUndoRedoLayout" _undoRedoLayout;
d _interButtonSpace;
d _beforeToolSpace;
d _interToolSpace;
d _afterToolSpace;
@"PKFloatArray" _toolAngles;
@"PKFloatArray" _toolAnglesBeforePanning;
@"NSArray" _toolCenterXConstraints;
@"NSArray" _toolCenterYConstraints;
{CGSize="width"d"height"d} _buttonSize;
d _toolWidth;
d _multicolorButtonAngle;
d _moreButtonAngle;
@"UIPanGestureRecognizer" _panGestureRecognizer;
{CGPoint="x"d"y"d} _startPanGestureLocation;
d _startPanGestureAngleOnArc;
d _endPanGestureAngleOnArc;
@"PKViewWithHitTestHandler" _toolsContentView;
@"CAShapeLayer" _toolsContentClippingShapeMask;
@"PKSqueezePaletteClipIndicatorView" _clipIndicatorView;
B _clipIndicatorViewVisible;
d _initialUndoButtonAngle;
d _initialRedoButtonAngle;
d _initialMulticolorButtonAngle;
d _initialMoreButtonAngle;
@"NSLayoutConstraint" _multicolorButtonCenterXConstraint;
@"NSLayoutConstraint" _multicolorButtonCenterYConstraint;
@"NSLayoutConstraint" _moreButtonCenterXConstraint;
@"NSLayoutConstraint" _moreButtonCenterYConstraint;
d _toolsContentClippingIndicatorAngle;
d _initialToolsContentClippingIndicatorAngle;
d _startAngle;
@"PKSqueezePaletteViewSwitchToEraserAction" _switchToEraserAction;
@"PKSqueezePaletteView" _paletteView;
@"UIButton" _undoButton;
@"UIButton" _redoButton;
@"NSArray" _drawingTools;
Q _selectedToolIndex;
Q _eraserToolIndex;
Q _visibleToolsCount;
@"PKSqueezePaletteMulticolorSwatchButton" _multicolorButton;
@"UIButton" _moreButton;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"PKSqueezePaletteView",W,N,V_paletteView) paletteView;
```

## Instance methods

```
-[PKSqueezePaletteViewMiniPaletteLayout gestureRecognizer:shouldReceiveTouch:];
-[PKSqueezePaletteViewMiniPaletteLayout _handlePanGesture:];
-[PKSqueezePaletteViewMiniPaletteLayout setupUI];
-[PKSqueezePaletteViewMiniPaletteLayout updateUI];
-[PKSqueezePaletteViewMiniPaletteLayout setPaletteView:];
-[PKSqueezePaletteViewMiniPaletteLayout _didTapDrawingTool:];
-[PKSqueezePaletteViewMiniPaletteLayout _didTapMoreButton:];
-[PKSqueezePaletteViewMiniPaletteLayout _didTapMulticolorButton:];
-[PKSqueezePaletteViewMiniPaletteLayout colorAppearanceDidChange];
-[PKSqueezePaletteViewMiniPaletteLayout expandedToolsLayout:canSelectTool:atIndex:];
-[PKSqueezePaletteViewMiniPaletteLayout expandedToolsLayout:didChangeDrawingTools:];
-[PKSqueezePaletteViewMiniPaletteLayout expandedToolsLayout:didChangeSelectedToolIndex:];
-[PKSqueezePaletteViewMiniPaletteLayout handlePencilInteractionDidTap:];
-[PKSqueezePaletteViewMiniPaletteLayout paletteView];
-[PKSqueezePaletteViewMiniPaletteLayout toolAngle:];
-[PKSqueezePaletteViewMiniPaletteLayout undoRedoLayoutStartAngle:];
-[PKSqueezePaletteViewMiniPaletteLayout willTransitionToLayout:];
```
