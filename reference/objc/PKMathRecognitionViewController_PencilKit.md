# `PKMathRecognitionViewController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKHoverControllerDelegate`, `PKCalculateScrubberControllerDelegate`, `PKMathContextMenuControllerDelegate`, `PKMathRecognitionControllerDelegate`, `PKOverlayDrawingControllerDelegate`, `UIEditMenuInteractionDelegate`, `UIPopoverPresentationControllerDelegate`
- 35 instance variables, 8 properties, 63 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _currentMathItemsLookup;
@"NSMutableDictionary" _currentResultsLookup;
@"NSMutableDictionary" _currentResultsAttributionLookup;
@"NSMutableDictionary" _currentResultsDrawings;
@"UIView" _mathFloatingLabelView;
@"UIViewController" _typesetViewController;
@"PKToolPicker" _activeToolPickerForPresentedViewController;
@"<PKCalculateScrubberController>" _scrubberController;
B _shouldAutohideScrubber;
@"NSUUID" _uuidForLatestLiveVariableExpression;
@"PKLiveMathVariable" _liveVariable;
@"PKMathRecognitionToken" _currentMenuToken;
B _menuIsVisible;
B _disableAlternatives;
B _disableErrors;
@"NSString" _solveResult;
@"NSUUID" _popoverHintItemUUID;
@"NSUUID" _addGraphItemUUID;
@"NSUUID" _solveItemUUID;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _currentViewBounds;
@"NSMutableSet" _expressionsWithActiveAnimations;
@"NSMutableSet" _expressionsWeCreatedGraphsFor;
@"NSUUID" _mathAnimationAdditionalStrokesHandle;
{?="delegateSupportsUpdateFrameForContainer"b1"delegateSupportsExpressionIdentifiersForExistingGraphNearLocation"b1"delegateSupportsExpressionIdentifiersForCompatibleGraphNearLocation"b1"delegateSupportsAddGraphForExpression"b1"delegateSupportsLatestEndOfStrokeTimestamp"b1"delegateSupportsCoordinateSpaceForDrawing"b1"delegateSupportsSetHiddenStrokes"b1"delegateSupportsReplaceStrokesWithStrokes"b1"delegateSupportsUpdatedResult"b1"delegateSupportsCreateScrubberController"b1"delegateSupportsCreateTypesetViewController"b1"delegateSupportsCreateTypesetImage"b1"delegateSupportsCreateTypesetImageFromUUID"b1"delegateSupportsSetShouldSolve"b1"delegateSupportsSetShouldSolveUndoable"b1"delegateSupportsAnySetShouldSolve"b1"delegateSupportsSelectStrokes"b1"delegateSupportsTimestampForLatestUserInteraction"b1"delegateSupportsWillPresentPopoverUI"b1"delegateSupportsDidDismissPopoverUI"b1"delegateSupportsResultForLocale"b1} _delegateFlags;
@"PKHoverController" _hoverController;
B _shouldCacheDrawingForResults;
q _solvingStyle;
d _canvasWidth;
@"UIViewController" _viewControllerForPresentingUI;
@"<PKMathRecognitionViewControllerDelegate>" _delegate;
@"UIView" _parentView;
@"PKMathRecognitionController" _controller;
@"PKOverlayDrawingController" _overlayDrawingController;
@"UIEditMenuInteraction" _alternativedEditMenuInteraction;
@"PKMathContextMenuController" _contextMenuController;
```

## Properties

```
@property (Tq,N,V_solvingStyle) solvingStyle;
@property (TB,N,V_shouldCacheDrawingForResults) shouldCacheDrawingForResults;
@property (Td,N,V_canvasWidth) canvasWidth;
@property (T@"UIViewController",W,N,V_viewControllerForPresentingUI) viewControllerForPresentingUI;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKMathRecognitionViewController adaptivePresentationStyleForPresentationController:traitCollection:];
-[PKMathRecognitionViewController adaptivePresentationStyleForPresentationController:];
-[PKMathRecognitionViewController presentationControllerDidDismiss:];
-[PKMathRecognitionViewController editMenuInteraction:willPresentMenuForConfiguration:animator:];
-[PKMathRecognitionViewController dealloc];
-[PKMathRecognitionViewController layoutSubviews];
-[PKMathRecognitionViewController editMenuInteraction:willDismissMenuForConfiguration:animator:];
-[PKMathRecognitionViewController hitTest:];
-[PKMathRecognitionViewController editMenuInteraction:menuForConfiguration:suggestedActions:];
-[PKMathRecognitionViewController removedFromView];
-[PKMathRecognitionViewController contextMenuControllerDidFinish:];
-[PKMathRecognitionViewController didBeginDrawing];
-[PKMathRecognitionViewController dismissPopovers];
-[PKMathRecognitionViewController setCanvasWidth:];
-[PKMathRecognitionViewController _updateDrawingOverlayCache];
-[PKMathRecognitionViewController adjustedSelectedStrokes:selectionPath:];
-[PKMathRecognitionViewController canvasWidth];
-[PKMathRecognitionViewController contextMenuController:addGraphForItemUUID:addToExisting:graphableVariable:];
-[PKMathRecognitionViewController contextMenuController:dismissErrorForItem:token:];
-[PKMathRecognitionViewController contextMenuController:imageForItemUUID:];
-[PKMathRecognitionViewController contextMenuController:removeResultForItemUUID:];
-[PKMathRecognitionViewController contextMenuController:resultAttributionForItemUUID:];
-[PKMathRecognitionViewController contextMenuController:resultDrawingForItemUUID:];
-[PKMathRecognitionViewController contextMenuController:resultForItemUUID:];
-[PKMathRecognitionViewController contextMenuController:solveItemUUID:];
-[PKMathRecognitionViewController contextMenuControllerDrawing:];
-[PKMathRecognitionViewController contextMenuControllerDrawingTransform:];
-[PKMathRecognitionViewController didEraseStrokes:];
-[PKMathRecognitionViewController eraserMovedToLocation:];
-[PKMathRecognitionViewController handleSingleTapAtDrawingLocation:];
-[PKMathRecognitionViewController handleSingleTapAtDrawingLocation:fromTapStroke:];
-[PKMathRecognitionViewController hideMathFloatingLabelView];
-[PKMathRecognitionViewController hideScrubber];
-[PKMathRecognitionViewController hoverController:holdGestureMeanInputPoint:latestInputPoint:];
-[PKMathRecognitionViewController initWithController:view:delegate:];
-[PKMathRecognitionViewController mathRecognitionController:didEraseStrokesInExpressions:];
-[PKMathRecognitionViewController mathRecognitionController:didUpdateExpressions:newItems:removedItems:mathItems:];
-[PKMathRecognitionViewController mathRecognitionController:solveStateChangedForExpressions:mathItems:];
-[PKMathRecognitionViewController mathRecognitionControllerTimestampForLatestUserInteraction:];
-[PKMathRecognitionViewController mathResult:itemUUID:];
-[PKMathRecognitionViewController mathResultAttributionImage:darkModeImage:string:date:itemUUID:];
-[PKMathRecognitionViewController openPopoverForAddingGraph];
-[PKMathRecognitionViewController openPopoverForHint];
-[PKMathRecognitionViewController overlayController:imageViewForStrokes:completion:];
-[PKMathRecognitionViewController overlayController:willUpdateView:animationDuration:];
-[PKMathRecognitionViewController overlayControllerDrawingTransform:];
-[PKMathRecognitionViewController overlayViews];
-[PKMathRecognitionViewController redrawSubviews];
-[PKMathRecognitionViewController regenerateResultsIfNecessary];
-[PKMathRecognitionViewController registerRecentlyCreatedLocalStroke:];
-[PKMathRecognitionViewController resultViewForItemUUID:];
-[PKMathRecognitionViewController scrubberController:valueDidChange:];
-[PKMathRecognitionViewController scrubberControllerDidDismiss:];
-[PKMathRecognitionViewController setItemAttributes:forItemUUID:];
-[PKMathRecognitionViewController setShouldCacheDrawingForResults:];
-[PKMathRecognitionViewController setSolvingStyle:];
-[PKMathRecognitionViewController setTokens:forItem:];
-[PKMathRecognitionViewController setTokens:forItemUUID:graphable:];
-[PKMathRecognitionViewController setTokens:forItemUUID:graphable:graphableVariables:];
-[PKMathRecognitionViewController setViewControllerForPresentingUI:];
-[PKMathRecognitionViewController shouldCacheDrawingForResults];
-[PKMathRecognitionViewController solvingStyle];
-[PKMathRecognitionViewController viewControllerForPresentingUI];
```
