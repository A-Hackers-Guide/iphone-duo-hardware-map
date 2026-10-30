# `PKSqueezePaletteViewUndoRedoLayout`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKSqueezePaletteViewLayout`
- 15 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSLayoutConstraint" _undoButtonCenterXConstraint;
@"NSLayoutConstraint" _undoButtonCenterYConstraint;
@"NSLayoutConstraint" _redoButtonCenterXConstraint;
@"NSLayoutConstraint" _redoButtonCenterYConstraint;
d _undoButtonAngle;
d _redoButtonAngle;
d _interItemSpace;
B _didTransitionToExpandedLayout;
@"UILongPressGestureRecognizer" _undoButtonLongPressGestureRecognizer;
@"UILongPressGestureRecognizer" _redoButtonLongPressGestureRecognizer;
@"PKSqueezePaletteView" _paletteView;
@"<PKSqueezePaletteViewUndoRedoLayoutDelegate>" _delegate;
d _startAngle;
@"UIButton" _undoButton;
@"UIButton" _redoButton;
```

## Properties

```
@property (T@"PKSqueezePaletteView",W,N,V_paletteView) paletteView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKSqueezePaletteViewUndoRedoLayout setupUI];
-[PKSqueezePaletteViewUndoRedoLayout updateUI];
-[PKSqueezePaletteViewUndoRedoLayout setPaletteView:];
-[PKSqueezePaletteViewUndoRedoLayout _didTapRedoButton:];
-[PKSqueezePaletteViewUndoRedoLayout _didTapUndoButton:];
-[PKSqueezePaletteViewUndoRedoLayout _handleRedoButtonLongPressGestureRecognizer:];
-[PKSqueezePaletteViewUndoRedoLayout _handleUndoButtonLongPressGestureRecognizer:];
-[PKSqueezePaletteViewUndoRedoLayout handlePencilInteractionDidTap:];
-[PKSqueezePaletteViewUndoRedoLayout paletteView];
-[PKSqueezePaletteViewUndoRedoLayout willTransitionToLayout:];
```
