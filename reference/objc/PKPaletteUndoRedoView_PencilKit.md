# `PKPaletteUndoRedoView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PKPaletteEdgeLocating`, `PKPaletteViewSizeScaling`
- 14 instance variables, 18 properties, 38 instance methods, 0 class methods

## Instance variables

```
B _undoEnabled;
B _redoEnabled;
Q _edgeLocation;
Q _cornerLocation;
d _scalingFactor;
@"<PKPaletteUndoRedoViewDelegate>" _delegate;
@"PKPaletteButton" _undoButton;
@"PKPaletteButton" _redoButton;
d _interItemSpacing;
@"UIStackView" _stackView;
@"NSLayoutConstraint" _undoButtonWidthConstraint;
@"NSLayoutConstraint" _undoButtonHeightConstraint;
@"NSLayoutConstraint" _redoButtonWidthConstraint;
@"NSLayoutConstraint" _redoButtonHeightConstraint;
```

## Properties

```
@property (T@"UIStackView",&,N,V_stackView) stackView;
@property (T@"PKPaletteButton",&,N,V_undoButton) undoButton;
@property (T@"PKPaletteButton",&,N,V_redoButton) redoButton;
@property (T@"NSLayoutConstraint",&,N,V_undoButtonWidthConstraint) undoButtonWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_undoButtonHeightConstraint) undoButtonHeightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_redoButtonWidthConstraint) redoButtonWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_redoButtonHeightConstraint) redoButtonHeightConstraint;
@property (T@"<PKPaletteUndoRedoViewDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisUndoEnabled,V_undoEnabled) undoEnabled;
@property (TB,N,GisRedoEnabled,V_redoEnabled) redoEnabled;
@property (Td,N,V_interItemSpacing) interItemSpacing;
@property (TQ,N,V_edgeLocation) edgeLocation;
@property (TQ,N,V_cornerLocation) cornerLocation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,N,V_scalingFactor) scalingFactor;
```

## Instance methods

```
-[PKPaletteUndoRedoView setUndoButton:];
-[PKPaletteUndoRedoView redoButton];
-[PKPaletteUndoRedoView intrinsicContentSize];
-[PKPaletteUndoRedoView setRedoButton:];
-[PKPaletteUndoRedoView undoButton];
-[PKPaletteUndoRedoView scalingFactor];
-[PKPaletteUndoRedoView interItemSpacing];
-[PKPaletteUndoRedoView isUndoEnabled];
-[PKPaletteUndoRedoView setDelegate:];
-[PKPaletteUndoRedoView delegate];
-[PKPaletteUndoRedoView stackView];
-[PKPaletteUndoRedoView setScalingFactor:];
-[PKPaletteUndoRedoView setStackView:];
-[PKPaletteUndoRedoView _updateUI];
-[PKPaletteUndoRedoView setInterItemSpacing:];
-[PKPaletteUndoRedoView initWithFrame:];
-[PKPaletteUndoRedoView setUndoEnabled:];
-[PKPaletteUndoRedoView _buttonSize];
-[PKPaletteUndoRedoView updateUI];
-[PKPaletteUndoRedoView setRedoEnabled:];
-[PKPaletteUndoRedoView _installRedoButton];
-[PKPaletteUndoRedoView _installStackView];
-[PKPaletteUndoRedoView _installUndoButton];
-[PKPaletteUndoRedoView cornerLocation];
-[PKPaletteUndoRedoView edgeLocation];
-[PKPaletteUndoRedoView handleRedo:];
-[PKPaletteUndoRedoView handleUndo:];
-[PKPaletteUndoRedoView isRedoEnabled];
-[PKPaletteUndoRedoView redoButtonHeightConstraint];
-[PKPaletteUndoRedoView redoButtonWidthConstraint];
-[PKPaletteUndoRedoView setCornerLocation:];
-[PKPaletteUndoRedoView setEdgeLocation:];
-[PKPaletteUndoRedoView setRedoButtonHeightConstraint:];
-[PKPaletteUndoRedoView setRedoButtonWidthConstraint:];
-[PKPaletteUndoRedoView setUndoButtonHeightConstraint:];
-[PKPaletteUndoRedoView setUndoButtonWidthConstraint:];
-[PKPaletteUndoRedoView undoButtonHeightConstraint];
-[PKPaletteUndoRedoView undoButtonWidthConstraint];
```
