# `PKAdornmentView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 7 instance variables, 4 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"PKImageView" _strokeSelectionImageView;
B _isInteracting;
@"NSUUID" _adornmentAdditionalStrokesHandle;
@"PKStrokeSelection" _strokeSelection;
@"PKSelectionController" _selectionController;
@"<PKSelectionRendering>" _selectionRenderer;
@"PKStrokeSelectionImage" _strokeSelectionImage;
```

## Properties

```
@property (T@"PKStrokeSelection",&,N,V_strokeSelection) strokeSelection;
@property (T@"PKSelectionController",W,N,V_selectionController) selectionController;
@property (T@"<PKSelectionRendering>",&,N,V_selectionRenderer) selectionRenderer;
@property (T@"PKStrokeSelectionImage",&,N,V_strokeSelectionImage) strokeSelectionImage;
```

## Class methods

```
+[PKAdornmentView classForSelectionType:];
```

## Instance methods

```
-[PKAdornmentView setSelectionController:];
-[PKAdornmentView selectionController];
-[PKAdornmentView pointInside:withEvent:];
-[PKAdornmentView strokeSelection];
-[PKAdornmentView _hideStrokeSelectionImageView:animated:];
-[PKAdornmentView _liftStrokesOutOfTiledView];
-[PKAdornmentView _putStrokesBackIntoTiledViewAnimated:];
-[PKAdornmentView containsPoint:forInputType:];
-[PKAdornmentView hideStrokeImageView];
-[PKAdornmentView initWithFrame:strokeSelection:selectionController:selectionType:];
-[PKAdornmentView selectionRenderer];
-[PKAdornmentView setSelectionRenderer:];
-[PKAdornmentView setStrokeSelection:];
-[PKAdornmentView setStrokeSelectionImage:];
-[PKAdornmentView strokeSelectionImage];
```
