# `_UISheetInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIScrollViewScrollableAncestor`, `UIPanGestureRecognizerDelegateInternal`, `_UIHyperInteractorDelegate`, `_UIHyperOutOfProcessViewAnimatorDelegate`, `UIInteraction`
- 25 instance variables, 30 properties, 77 instance methods, 0 class methods

## Instance variables

```
d _previousMaxTopOffset;
{?="isUpdatingSheetOffset"b1} _flags;
{?="sheetInteractionShouldInteractWithQuicklyScrollingDescendentScrollView"b1} _delegateFlags;
B _scrollingExpandsToLargerDetentWhenScrolledToEdge;
B _enabled;
B _scrollInteractionEnabled;
B _generatingAnimations;
@? _numberOfDetentsGetter;
@? _detentGetter;
q _indexOfCurrentDetent;
@? _indexOfCurrentDetentGetter;
@? _currentOffsetWasInvalidated;
@? _rubberBandExtentBeyondMinimumOffsetGetter;
@? _rubberBandExtentBeyondMaximumOffsetGetter;
@"<_UISheetInteractionDelegate>" _delegate;
@"UIView" _view;
@"NSMutableArray" _registeredPanGestureRecognizers;
@"UIPanGestureRecognizer" _backgroundGestureRecognizer;
@"_UIHyperInteractor" _interactor;
@"NSMutableArray" _detentPoints;
@"_UIHyperregionUnion" _detentUnion;
@"_UIHyperrectangle" _detentContinuum;
@"_UIHyperAsymmetricExtender" _extender;
@"_UIHyperOutOfProcessViewAnimator" _animator;
@"<NSObject>" _dragSource;
```

## Properties

```
@property (T@"UIView",W,N,V_view) view;
@property (T@"NSMutableArray",R,N,V_registeredPanGestureRecognizers) registeredPanGestureRecognizers;
@property (T@"UIPanGestureRecognizer",R,N,V_backgroundGestureRecognizer) backgroundGestureRecognizer;
@property (T@"_UIHyperInteractor",R,N,V_interactor) interactor;
@property (T@"NSMutableArray",R,N,V_detentPoints) detentPoints;
@property (T@"_UIHyperregionUnion",R,N,V_detentUnion) detentUnion;
@property (T@"_UIHyperrectangle",R,N,V_detentContinuum) detentContinuum;
@property (T@"_UIHyperAsymmetricExtender",R,N,V_extender) extender;
@property (T@"_UIHyperOutOfProcessViewAnimator",R,N,V_animator) animator;
@property (T@"<NSObject>",&,N,V_dragSource) dragSource;
@property (TB,N,GisGeneratingAnimations,V_generatingAnimations) generatingAnimations;
@property (Tq,N,V_indexOfCurrentDetent) indexOfCurrentDetent;
@property (T@?,C,N,V_numberOfDetentsGetter) numberOfDetentsGetter;
@property (T@?,C,N,V_detentGetter) detentGetter;
@property (T@?,C,N,V_indexOfCurrentDetentGetter) indexOfCurrentDetentGetter;
@property (TB,N,V_scrollingExpandsToLargerDetentWhenScrolledToEdge) scrollingExpandsToLargerDetentWhenScrolledToEdge;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (TB,N,GisScrollInteractionEnabled,V_scrollInteractionEnabled) scrollInteractionEnabled;
@property (TB,R,N,GisDragging) dragging;
@property (T{CGPoint=dd},R,N) currentOffset;
@property (T@?,C,N,V_currentOffsetWasInvalidated) currentOffsetWasInvalidated;
@property (T{CGPoint=dd},R,N) currentVelocity;
@property (T@?,C,N,V_rubberBandExtentBeyondMinimumOffsetGetter) rubberBandExtentBeyondMinimumOffsetGetter;
@property (T@?,C,N,V_rubberBandExtentBeyondMaximumOffsetGetter) rubberBandExtentBeyondMaximumOffsetGetter;
@property (T{CGPoint=dd},R,N) attachmentPoint;
@property (T@"<_UISheetInteractionDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISheetInteraction _animateWithParameters:animations:];
-[_UISheetInteraction _panGestureRecognizer:shouldTryToBeginVerticallyWithEvent:];
-[_UISheetInteraction rubberBandExtentBeyondMinimumOffsetGetter];
-[_UISheetInteraction interactor];
-[_UISheetInteraction _descendentScrollView:shouldPreserveStartOffset:];
-[_UISheetInteraction invalidateRubberBandExtentBeyondMaximumOffset];
-[_UISheetInteraction setScrollInteractionEnabled:];
-[_UISheetInteraction gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[_UISheetInteraction registerPanGestureRecognizer:];
-[_UISheetInteraction isUnconstrainedOffsetBeyondSideOrTopExtentInverted:];
-[_UISheetInteraction _hyperInteractorApplyPresentationPoint:];
-[_UISheetInteraction _shouldInteractWithDescendentScrollView:startOffset:maxTopOffset:];
-[_UISheetInteraction gestureRecognizer:shouldReceiveTouch:];
-[_UISheetInteraction isGeneratingAnimations];
-[_UISheetInteraction scrollingExpandsToLargerDetentWhenScrolledToEdge];
-[_UISheetInteraction sendCurrentOffsetDidChange];
-[_UISheetInteraction init];
-[_UISheetInteraction invalidateDetents];
-[_UISheetInteraction setDetentGetter:];
-[_UISheetInteraction detentGetter];
-[_UISheetInteraction _currentDragPanGesture];
-[_UISheetInteraction numberOfDetentsGetter];
-[_UISheetInteraction detentContinuum];
-[_UISheetInteraction draggingBeganFromSource:withRubberBandCoefficient:];
-[_UISheetInteraction setScrollingExpandsToLargerDetentWhenScrolledToEdge:];
-[_UISheetInteraction setGeneratingAnimations:];
-[_UISheetInteraction animator];
-[_UISheetInteraction setView:];
-[_UISheetInteraction _descendentScrollViewShouldScrollVertically:];
-[_UISheetInteraction currentOffset];
-[_UISheetInteraction setCurrentOffsetWasInvalidated:];
-[_UISheetInteraction handlePan:];
-[_UISheetInteraction extender];
-[_UISheetInteraction updateRegisteredPanGestureRecognizerEnabled:];
-[_UISheetInteraction isScrollInteractionEnabled];
-[_UISheetInteraction draggingCancelledInSource:];
-[_UISheetInteraction isDragging];
-[_UISheetInteraction isEnabled];
-[_UISheetInteraction invalidateIndexOfCurrentDetent];
-[_UISheetInteraction currentOffsetWasInvalidated];
-[_UISheetInteraction rubberBandExtentBeyondMaximumOffsetGetter];
-[_UISheetInteraction view];
-[_UISheetInteraction _descendentScrollViewDidEndDragging:];
-[_UISheetInteraction setDelegate:];
-[_UISheetInteraction _shouldBeFoundByDescendentScrollView:];
-[_UISheetInteraction indexOfCurrentDetent];
-[_UISheetInteraction draggingChangedInSource:withTranslation:velocity:animateChange:];
-[_UISheetInteraction indexOfCurrentDetentGetter];
-[_UISheetInteraction _scrollView:adjustedUnconstrainedOffsetForUnconstrainedOffset:startOffset:horizontalVelocity:verticalVelocity:animator:];
-[_UISheetInteraction setEnabled:];
-[_UISheetInteraction attachmentPoint];
-[_UISheetInteraction willMoveToView:];
-[_UISheetInteraction gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[_UISheetInteraction currentVelocity];
-[_UISheetInteraction _descendentScrollViewShouldMaintainRelativeDistanceFromSafeArea:];
-[_UISheetInteraction delegate];
-[_UISheetInteraction draggingEndedInSource:];
-[_UISheetInteraction _descendentScrollViewDidCancelDragging:];
-[_UISheetInteraction setRubberBandExtentBeyondMinimumOffsetGetter:];
-[_UISheetInteraction unregisterPanGestureRecognizer:];
-[_UISheetInteraction dragSource];
-[_UISheetInteraction _hyperOutOfProcessViewAnimator:getPresentationPointForInterruptedAnimation:];
-[_UISheetInteraction delegateAllowsInteractWithQuicklyScrollingDescendentScrollView];
-[_UISheetInteraction detentUnion];
-[_UISheetInteraction setNumberOfDetentsGetter:];
-[_UISheetInteraction registeredPanGestureRecognizers];
-[_UISheetInteraction _descendentScrollViewShouldScrollHorizontally:];
-[_UISheetInteraction setRubberBandExtentBeyondMaximumOffsetGetter:];
-[_UISheetInteraction backgroundGestureRecognizer];
-[_UISheetInteraction _panGestureRecognizer:shouldTryToBeginHorizontallyWithEvent:];
-[_UISheetInteraction didMoveToView:];
-[_UISheetInteraction setDragSource:];
-[_UISheetInteraction setIndexOfCurrentDetentGetter:];
-[_UISheetInteraction invalidateRubberBandExtentBeyondMinimumOffset];
-[_UISheetInteraction detentPoints];
-[_UISheetInteraction setIndexOfCurrentDetent:];
-[_UISheetInteraction cancelDraggingIfNeeded];
```
