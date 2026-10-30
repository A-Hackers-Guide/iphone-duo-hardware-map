# `UIPopoverController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDimmingViewDelegate`, `UIGestureRecognizerDelegatePrivate`, `UIAppearanceContainer`
- 49 instance variables, 25 properties, 135 instance methods, 7 class methods

## Instance variables

```
@ _delegate;
@"UIViewController" _contentViewController;
@"UIViewController" _splitParentController;
@"_UIPopoverView" _popoverView;
@"UIDimmingView" _dimmingView;
@"UIView" _layoutConstraintView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _targetRectInEmbeddingView;
@"UIBarButtonItem" _targetBarButtonItem;
Q _requestedArrowDirections;
Q _currentArrowDirection;
q _popoverBackgroundStyle;
@"UIColor" _backgroundColor;
@"_UIPopoverLayoutInfo" _preferredLayoutInfo;
# _popoverBackgroundViewClass;
{CGSize="width"d"height"d} _popoverContentSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _targetRectInDimmingView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _embeddedTargetRect;
q _popoverControllerStyle;
B _ignoresKeyboardNotifications;
@"UIView" _currentPresentationView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _currentPresentationRectInView;
Q _originalArrowDirections;
I draggingChildScrollViewCount;
@ _target;
q _didFinish;
@"UIViewController" _modalPresentationFromViewController;
@"UIViewController" _modalPresentationToViewController;
Q _toViewAutoResizingMask;
@"UIViewController" _slidingViewController;
@"UIView" _presentingView;
Q _presentationEdge;
q _presentationDirection;
i _presentationState;
B _didPresentInActiveSequence;
Q _slideTransitionCount;
@"UIPanGestureRecognizer" _vendedGestureRecognizer;
@"UIPanGestureRecognizer" _dimmingViewGestureRecognizer;
@"UIPopoverController" _retainedSelf;
@"NSArray" _passthroughViews;
{?="isPresentingModalViewController"b1"isPresentingActionSheet"b1"wasIgnoringDimmingViewTouchesBeforeScrolling"b1"isInTextEffectsWindow"b1"isEmbeddingInView"b1"embeddedPresentationBounces"b1"isWaitingToPresentShimmedPopover"b1} _popoverControllerFlags;
B _dismissesOnRotation;
B _showsTargetRect;
B _showsOrientationMarker;
B _showsPresentationArea;
B _retainsSelfWhilePresented;
B _allowsPopoverPresentationToAdapt;
Q _popoverArrowDirection;
@"UIPopoverPresentationController" _presentationController;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _popoverLayoutMargins;
```

## Properties

```
@property (TQ,N,V_popoverArrowDirection) popoverArrowDirection;
@property (T@"UIDimmingView",&,N,V_dimmingView) dimmingView;
@property (TB,N,V_dismissesOnRotation) dismissesOnRotation;
@property (T@"_UIPopoverLayoutInfo",&,N,V_preferredLayoutInfo) preferredLayoutInfo;
@property (T@"UIView",W,N,G_presentingView,S_setPresentingView:,V_presentingView) presentingView;
@property (TQ,N,G_presentationEdge,S_setPresentationEdge:,V_presentationEdge) presentationEdge;
@property (TB,D,N,S_setIgnoresKeyboardNotifications:) _ignoresKeyboardNotifications;
@property (T@"UIPopoverPresentationController",&,N,G_presentationController,S_setPresentationController:,V_presentationController) presentationController;
@property (TB,N,V_showsTargetRect) showsTargetRect;
@property (TB,N,V_showsOrientationMarker) showsOrientationMarker;
@property (TB,N,V_showsPresentationArea) showsPresentationArea;
@property (TB,N,G_retainsSelfWhilePresented,S_setRetainsSelfWhilePresented:,V_retainsSelfWhilePresented) retainsSelfWhilePresented;
@property (TB,N,G_allowsPopoverPresentationToAdapt,S_setAllowsPopoverPresentationToAdapt:,V_allowsPopoverPresentationToAdapt) allowsPopoverPresentationToAdapt;
@property (T@"<UIPopoverControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"UIViewController",&,N) contentViewController;
@property (T{CGSize=dd},N) popoverContentSize;
@property (TB,R,N,GisPopoverVisible) popoverVisible;
@property (T@"NSArray",C,N) passthroughViews;
@property (T@"UIColor",C,N) backgroundColor;
@property (T{UIEdgeInsets=dddd},N,V_popoverLayoutMargins) popoverLayoutMargins;
@property (T#,&,N,V_popoverBackgroundViewClass) popoverBackgroundViewClass;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIPopoverController _defaultPopoverLayoutMarginsForPopoverControllerStyle:andContentViewController:];
+[UIPopoverController _forceAttemptsToAvoidKeyboard];
+[UIPopoverController _popoverViewClass];
+[UIPopoverController _popoversDisabled];
+[UIPopoverController _setForceModernPopoverUse:];
+[UIPopoverController _showTargetRectPref];
+[UIPopoverController _useLegacyPopoverControllers];
```

## Instance methods

```
-[UIPopoverController adaptivePresentationStyleForPresentationController:traitCollection:];
-[UIPopoverController adaptivePresentationStyleForPresentationController:];
-[UIPopoverController setContentViewController:];
-[UIPopoverController dimmingView];
-[UIPopoverController dimmingViewWasTapped:];
-[UIPopoverController init];
-[UIPopoverController contentViewController];
-[UIPopoverController dealloc];
-[UIPopoverController _gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[UIPopoverController setBackgroundColor:];
-[UIPopoverController setDimmingView:];
-[UIPopoverController setDelegate:];
-[UIPopoverController popoverPresentationController:willRepositionPopoverToRect:inView:];
-[UIPopoverController passthroughViews];
-[UIPopoverController _setGesturesEnabled:];
-[UIPopoverController popoverPresentationControllerShouldDismissPopover:];
-[UIPopoverController initWithContentViewController:];
-[UIPopoverController delegate];
-[UIPopoverController backgroundColor];
-[UIPopoverController _gestureRecognizerShouldBegin:];
-[UIPopoverController _gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[UIPopoverController _dimmingView];
-[UIPopoverController popoverPresentationControllerDidDismissPopover:];
-[UIPopoverController _presentingView];
-[UIPopoverController setPopoverContentSize:animated:];
-[UIPopoverController _incrementSlideTransitionCount:];
-[UIPopoverController _stopWatchingForWindowRotations];
-[UIPopoverController _swipe:];
-[UIPopoverController showsTargetRect];
-[UIPopoverController _adjustPopoverForNewContentSizeFromViewController:allowShrink:];
-[UIPopoverController _allowsFocusBehindDimmingView];
-[UIPopoverController _allowsPopoverPresentationToAdapt];
-[UIPopoverController _attemptsToAvoidKeyboard];
-[UIPopoverController _beginMapsTransitionToNewViewController:arrowDirections:slideDuration:expandDuration:];
-[UIPopoverController _beginMapsTransitionToNewViewController:newTargetRect:inView:arrowDirections:slideDuration:expandDuration:];
-[UIPopoverController _canRepresentAutomatically];
-[UIPopoverController _centerPointForScale:frame:anchor:];
-[UIPopoverController _commonPresentPopoverFromRect:inView:permittedArrowDirections:animated:];
-[UIPopoverController _completionBlockForDismissalWhenNotifyingDelegate:];
-[UIPopoverController _containedViewControllerModalStateChanged];
-[UIPopoverController _currentPopoverContentSize];
-[UIPopoverController _defaultChromeViewClass];
-[UIPopoverController _dismissPopoverAnimated:stateOnly:notifyDelegate:];
-[UIPopoverController _dismissalAnimationDuration];
-[UIPopoverController _embedsInView];
-[UIPopoverController _gestureRecognizerForPresentationFromEdge:];
-[UIPopoverController _hostingWindowDidRotate:];
-[UIPopoverController _hostingWindowWillRotate:];
-[UIPopoverController _ignoresKeyboardNotifications];
-[UIPopoverController _initWithContentViewController:popoverControllerStyle:];
-[UIPopoverController _invalidateLayoutInfo];
-[UIPopoverController _isDismissing];
-[UIPopoverController _isPresenting];
-[UIPopoverController _keyboardStateChanged:];
-[UIPopoverController _layoutDimmingViewForInterfaceOrientationOfHostingWindow:];
-[UIPopoverController _layoutInfoForCurrentKeyboardState];
-[UIPopoverController _layoutInfoForCurrentKeyboardStateAndHostingWindow:];
-[UIPopoverController _layoutInfoFromLayoutInfo:forCurrentKeyboardStateAndHostingWindow:];
-[UIPopoverController _managingSplitViewController];
-[UIPopoverController _manuallyHandlesContentViewControllerAppearanceCalls];
-[UIPopoverController _modalAnimationFinishedEndIgnoringInteractiveEvents:];
-[UIPopoverController _modalTransition:fromViewController:toViewController:target:didFinish:];
-[UIPopoverController _moveAwayFromTheKeyboard:];
-[UIPopoverController _newViewControllerWasPushed:];
-[UIPopoverController _performHierarchyCheckOnViewController:];
-[UIPopoverController _popoverBackgroundStyle];
-[UIPopoverController _popoverControllerStyle];
-[UIPopoverController _popoverLayoutInfoForChromeClass:];
-[UIPopoverController _postludeForDismissal];
-[UIPopoverController _presentPopoverBySlidingIn:fromEdge:ofView:animated:stateOnly:notifyDelegate:];
-[UIPopoverController _presentPopoverFromEdge:ofView:animated:];
-[UIPopoverController _presentPopoverFromRect:embeddedInView:usingViewForLayoutConstraints:permittedArrowDirections:];
-[UIPopoverController _presentPopoverFromRect:embeddedInView:usingViewForLayoutConstraints:permittedArrowDirections:animate:];
-[UIPopoverController _presentShimmedPopoverFromRect:inView:permittedArrowDirections:animated:];
-[UIPopoverController _presentationAnimationDuration];
-[UIPopoverController _presentationController];
-[UIPopoverController _presentationEdge];
-[UIPopoverController _presentationState];
-[UIPopoverController _resetSlideTransitionCount];
-[UIPopoverController _retainsSelfWhilePresented];
-[UIPopoverController _scrollViewDidEndDragging:];
-[UIPopoverController _scrollViewWillBeginDragging:];
-[UIPopoverController _setAllowsPopoverPresentationToAdapt:];
-[UIPopoverController _setContentViewController:backgroundStyle:animated:];
-[UIPopoverController _setIgnoresKeyboardNotifications:];
-[UIPopoverController _setManagingSplitViewController:];
-[UIPopoverController _setPopoverBackgroundStyle:];
-[UIPopoverController _setPopoverView:];
-[UIPopoverController _setPresentationController:];
-[UIPopoverController _setPresentationEdge:];
-[UIPopoverController _setPresentationState:];
-[UIPopoverController _setPresentingView:];
-[UIPopoverController _setRetainsSelfWhilePresented:];
-[UIPopoverController _setSplitParentController:];
-[UIPopoverController _setupPresentationController];
-[UIPopoverController _shimPopoverPresentationController];
-[UIPopoverController _shimPresentSlidingPopoverAnimated:];
-[UIPopoverController _slideTransitionCount];
-[UIPopoverController _splitParentController];
-[UIPopoverController _startWatchingForKeyboardNotificationsIfNecessary];
-[UIPopoverController _startWatchingForNavigationControllerNotifications:];
-[UIPopoverController _startWatchingForScrollViewNotifications];
-[UIPopoverController _startWatchingForWindowRotations];
-[UIPopoverController _stopWatchingForKeyboardNotifications];
-[UIPopoverController _stopWatchingForNavigationControllerNotifications:];
-[UIPopoverController _stopWatchingForNotifications];
-[UIPopoverController _stopWatchingForScrollViewNotifications];
-[UIPopoverController _transitionFromViewController:toViewController:animated:];
-[UIPopoverController _updateDimmingViewTransformForInterfaceOrientationOfHostingWindow:];
-[UIPopoverController dismissPopoverAnimated:];
-[UIPopoverController dismissesOnRotation];
-[UIPopoverController isPopoverVisible];
-[UIPopoverController isPresentingOrDismissing];
-[UIPopoverController popoverArrowDirection];
-[UIPopoverController popoverBackgroundViewClass];
-[UIPopoverController popoverContentSize];
-[UIPopoverController popoverLayoutMargins];
-[UIPopoverController popoverView];
-[UIPopoverController preferredLayoutInfo];
-[UIPopoverController presentPopoverFromBarButtonItem:permittedArrowDirections:animated:];
-[UIPopoverController presentPopoverFromRect:inView:permittedArrowDirections:animated:];
-[UIPopoverController setContentViewController:animated:];
-[UIPopoverController setDismissesOnRotation:];
-[UIPopoverController setPassthroughViews:];
-[UIPopoverController setPopoverArrowDirection:];
-[UIPopoverController setPopoverBackgroundViewClass:];
-[UIPopoverController setPopoverContentSize:];
-[UIPopoverController setPopoverFrame:animated:];
-[UIPopoverController setPopoverLayoutMargins:];
-[UIPopoverController setPreferredLayoutInfo:];
-[UIPopoverController setShowsOrientationMarker:];
-[UIPopoverController setShowsPresentationArea:];
-[UIPopoverController setShowsTargetRect:];
-[UIPopoverController showsOrientationMarker];
-[UIPopoverController showsPresentationArea];
```
