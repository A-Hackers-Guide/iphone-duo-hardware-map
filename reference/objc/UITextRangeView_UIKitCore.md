# `UITextRangeView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIPointerInteractionDelegate`, `UITextRangeAdjustmentInteractionDelegate`
- 30 instance variables, 33 properties, 113 instance methods, 0 class methods

## Instance variables

```
@"UITextSelectionView" m_selectionView;
@"UIResponder<UITextInput>" m_container;
i m_mode;
@"NSArray" m_rects;
@"NSMutableArray" m_rectViews;
@"UITouch" m_activeTouch;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} m_startEdge;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} m_endEdge;
@"UIView" m_rectContainerView;
@"UISelectionGrabber" m_startGrabber;
@"UISelectionGrabber" m_endGrabber;
B m_animateUpdate;
B m_commandsWereShowing;
B m_willBeginMagnifying;
B m_inGesture;
B m_magnifying;
B m_scrolling;
B m_scaling;
B m_rotating;
B m_inputViewIsChanging;
@"UIPointerInteraction" _pointerInteraction;
B m_isClearingRange;
B m_shouldStayVisible;
B _baseIsStart;
@"UISelectionGrabberCustomPath" _startCustomPath;
@"UISelectionGrabberCustomPath" _endCustomPath;
{CGPoint="x"d"y"d} m_basePoint;
{CGPoint="x"d"y"d} m_extentPoint;
{CGPoint="x"d"y"d} m_initialExtentPoint;
{CGPoint="x"d"y"d} _activeTouchPoint;
```

## Properties

```
@property (T@"UISelectionGrabberCustomPath",&,N,V_startCustomPath) startCustomPath;
@property (T@"UISelectionGrabberCustomPath",&,N,V_endCustomPath) endCustomPath;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,Vm_startEdge) startEdge;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,Vm_endEdge) endEdge;
@property (TB,N,Vm_magnifying) magnifying;
@property (TB,N,Vm_isClearingRange) isClearingRange;
@property (TB,N,Vm_shouldStayVisible) shouldStayVisible;
@property (T@"UITextSelectionView",R,N) selectionView;
@property (T@"UIResponder<UITextInput>",R,N) container;
@property (T{CGPoint=dd},R,N,Vm_basePoint) basePoint;
@property (T{CGPoint=dd},R,N,Vm_extentPoint) extentPoint;
@property (Ti,N,Vm_mode) mode;
@property (T@"NSArray",&,N,Vm_rects) rects;
@property (TB,R,N) autoscrolled;
@property (TB,N,Vm_inGesture) inGesture;
@property (TB,N,Vm_scrolling) isScrolling;
@property (TB,N,Vm_rotating) rotating;
@property (TB,N,Vm_scaling) scaling;
@property (TB,N,Vm_inputViewIsChanging) inputViewIsChanging;
@property (TB,N,V_baseIsStart) baseIsStart;
@property (TB,N,Vm_commandsWereShowing) commandsWereShowing;
@property (T@"UISelectionGrabber",&,N,Vm_startGrabber) startGrabber;
@property (T@"UISelectionGrabber",&,N,Vm_endGrabber) endGrabber;
@property (T{CGPoint=dd},N,Vm_initialExtentPoint) initialExtentPoint;
@property (TB,N,Vm_animateUpdate) animateUpdate;
@property (T{CGPoint=dd},R,N,V_activeTouchPoint) activeTouchPoint;
@property (TB,N,Vm_willBeginMagnifying) willBeginMagnifying;
@property (TB,R,N) areSelectionRectsVisible;
@property (TB,R,N,GisDisplayingVerticalSelection) displayingVerticalSelection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UITextRangeView setIsScrolling:];
-[UITextRangeView stopAnimating];
-[UITextRangeView startAnimating];
-[UITextRangeView pointerInteraction:styleForRegion:];
-[UITextRangeView extentPoint];
-[UITextRangeView isScrolling];
-[UITextRangeView basePoint];
-[UITextRangeView selectionView];
-[UITextRangeView setMode:];
-[UITextRangeView gestureRecognizerShouldBegin:];
-[UITextRangeView baseIsStart];
-[UITextRangeView initialExtentPoint];
-[UITextRangeView removeFromSuperview];
-[UITextRangeView mode];
-[UITextRangeView pointerInteraction:regionForRequest:defaultRegion:];
-[UITextRangeView setRotating:];
-[UITextRangeView updateBaseAndExtentPointsFromEdges];
-[UITextRangeView _selectionClipRect];
-[UITextRangeView pointInside:withEvent:];
-[UITextRangeView setBaseIsStart:];
-[UITextRangeView container];
-[UITextRangeView beginMagnifying];
-[UITextRangeView scaling];
-[UITextRangeView textRangeAdjustmentViewForEdge:];
-[UITextRangeView _startEdgeHitRectWithPrecision:];
-[UITextRangeView endEdge];
-[UITextRangeView isClearingRange];
-[UITextRangeView scaleWillChange];
-[UITextRangeView startCustomPath];
-[UITextRangeView textRangeAdjustmentRectForEdge:];
-[UITextRangeView updateRectViews];
-[UITextRangeView _cancelGrabberTransitionOutAnimations:];
-[UITextRangeView _edgeHitRectForEdgeRect:grabber:precision:];
-[UITextRangeView _endEdgeHitRectWithPrecision:];
-[UITextRangeView _endIsHorizontal];
-[UITextRangeView _gestureRecognizerShouldReceiveTouch:];
-[UITextRangeView _setGrabber:bounds:center:];
-[UITextRangeView _startIsHorizontal];
-[UITextRangeView _updateGrabbersVisibility:animated:];
-[UITextRangeView activeTouchPoint];
-[UITextRangeView animateHighlighterDelayedFadeInOnLayer:];
-[UITextRangeView animateHighlighterExpanderAnimation];
-[UITextRangeView animateHighlighterExpanderOnLayer:withOffset:];
-[UITextRangeView animateUpdate];
-[UITextRangeView areSelectionRectsVisible];
-[UITextRangeView autoscrolled];
-[UITextRangeView cancelDelayedActions];
-[UITextRangeView caretRectForTextRangeAdjustmentInteraction:];
-[UITextRangeView clearRangeAnimated:];
-[UITextRangeView commandsWereShowing];
-[UITextRangeView containerCoordinateSpaceForTextRangeAdjustmentInteraction:];
-[UITextRangeView convertFromMagnifierPoint:];
-[UITextRangeView didRotate];
-[UITextRangeView didScroll];
-[UITextRangeView doneMagnifying];
-[UITextRangeView endCustomPath];
-[UITextRangeView endGrabber];
-[UITextRangeView inGesture];
-[UITextRangeView initWithFrame:selectionView:];
-[UITextRangeView inputViewDidChange];
-[UITextRangeView inputViewIsChanging];
-[UITextRangeView inputViewWillChange];
-[UITextRangeView inverseScaleForView:];
-[UITextRangeView isDisplayingVerticalSelection];
-[UITextRangeView loupeOrientationForTextRangeAdjustmentInteraction:];
-[UITextRangeView magnifierPoint];
-[UITextRangeView magnifying];
-[UITextRangeView paddedTextRangeAdjustmentHitRegionForEdge:precision:];
-[UITextRangeView pointCloserToEnd:startEdge:endEdge:];
-[UITextRangeView prepareForMagnification];
-[UITextRangeView rects];
-[UITextRangeView rotating];
-[UITextRangeView scaleDidChange];
-[UITextRangeView setAnimateUpdate:];
-[UITextRangeView setCommandsWereShowing:];
-[UITextRangeView setEndCustomPath:];
-[UITextRangeView setEndEdge:];
-[UITextRangeView setEndGrabber:];
-[UITextRangeView setInGesture:];
-[UITextRangeView setInitialExtentPoint:];
-[UITextRangeView setInputViewIsChanging:];
-[UITextRangeView setIsClearingRange:];
-[UITextRangeView setMagnifierOrientation];
-[UITextRangeView setMagnifying:];
-[UITextRangeView setRects:];
-[UITextRangeView setScaling:];
-[UITextRangeView setShouldStayVisible:];
-[UITextRangeView setStartCustomPath:];
-[UITextRangeView setStartEdge:];
-[UITextRangeView setStartGrabber:];
-[UITextRangeView setWillBeginMagnifying:];
-[UITextRangeView shouldHitTestGrabbers];
-[UITextRangeView shouldShowGrabbers];
-[UITextRangeView shouldStayVisible];
-[UITextRangeView startEdge];
-[UITextRangeView startGrabber];
-[UITextRangeView textRangeAdjustmentInteraction:didBeginAtPoint:];
-[UITextRangeView textRangeAdjustmentInteraction:didEndAtPoint:];
-[UITextRangeView textRangeAdjustmentInteraction:prepareForInvalidation:];
-[UITextRangeView textRangeAdjustmentInteraction:selectionMoved:withTouchPoint:];
-[UITextRangeView textRangeAdjustmentInteraction:shouldBeginAtPoint:];
-[UITextRangeView textRangeAdjustmentInteraction:shouldDisplayLoupeForTouchType:];
-[UITextRangeView textRangeAdjustmentInteractionShouldApplyTouchOffset:];
-[UITextRangeView textRangeAdjustmentInteractionWasCancelled:];
-[UITextRangeView updateAfterEffectiveModeChange];
-[UITextRangeView updateBaseIsStartWithDocumentPoint:];
-[UITextRangeView updateDots];
-[UITextRangeView updateEdges];
-[UITextRangeView updateGrabbers];
-[UITextRangeView updateSelectionWithDocumentPoint:];
-[UITextRangeView willBeginMagnifying];
-[UITextRangeView willRotate];
-[UITextRangeView willScroll];
```
