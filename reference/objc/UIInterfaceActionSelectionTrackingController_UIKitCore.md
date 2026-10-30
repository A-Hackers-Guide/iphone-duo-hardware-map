# `UIInterfaceActionSelectionTrackingController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `UIFocusedInterfaceActionPressDelegate`
- 20 instance variables, 24 properties, 64 instance methods, 0 class methods

## Instance variables

```
B _scrubbingEnabled;
B _selectByPressGestureEnabled;
B _selectionFeedbackEnabled;
B _selectByIndirectPointerTouchEnabled;
B _selectionGestureIsTracking;
@"UIView" _trackableContainerView;
@"UIScrollView" _actionsScrollView;
@"NSArray" _representationViews;
@"UILongPressGestureRecognizer" _selectionGestureRecognizer;
@"_UIInterfaceActionSelectionDelayGestureRecognizer" _selectionDelayGestureRecognizer;
@"UIGestureRecognizer" _systemProvidedGestureRecognizer;
@"NSMutableSet" _viewsRequiringSelectionGestureDisabling;
@"_UIInterfaceActionSelectByPressGestureRecognizer" _selectByPressGestureRecognizer;
@"UISelectionFeedbackGenerator" _selectionRetargetFeedbackGenerator;
@"NSPointerArray" _weakCooperatingSelectionTrackingControllers;
@ _scrollViewWillBeginDraggingNotificationToken;
@ _scrollViewDidEndDraggingNotificationToken;
@ _scrollViewDidEndDeceleratingNotificationToken;
@"UIHoverGestureRecognizer" _hoverGestureRecognizer;
{CGPoint="x"d"y"d} _actionSelectionInitialLocationInContainerView;
```

## Properties

```
@property (T{CGPoint=dd},R,N,V_actionSelectionInitialLocationInContainerView) actionSelectionInitialLocationInContainerView;
@property (T@"UILongPressGestureRecognizer",R,N,V_selectionGestureRecognizer) selectionGestureRecognizer;
@property (T@"_UIInterfaceActionSelectionDelayGestureRecognizer",R,N,V_selectionDelayGestureRecognizer) selectionDelayGestureRecognizer;
@property (T@"UIGestureRecognizer",R,N,V_systemProvidedGestureRecognizer) systemProvidedGestureRecognizer;
@property (T@"NSMutableSet",R,N,V_viewsRequiringSelectionGestureDisabling) viewsRequiringSelectionGestureDisabling;
@property (T@"_UIInterfaceActionSelectByPressGestureRecognizer",&,N,V_selectByPressGestureRecognizer) selectByPressGestureRecognizer;
@property (T@"UISelectionFeedbackGenerator",&,N,V_selectionRetargetFeedbackGenerator) selectionRetargetFeedbackGenerator;
@property (T@"NSPointerArray",&,N,V_weakCooperatingSelectionTrackingControllers) weakCooperatingSelectionTrackingControllers;
@property (T@,&,N,V_scrollViewWillBeginDraggingNotificationToken) scrollViewWillBeginDraggingNotificationToken;
@property (T@,&,N,V_scrollViewDidEndDraggingNotificationToken) scrollViewDidEndDraggingNotificationToken;
@property (T@,&,N,V_scrollViewDidEndDeceleratingNotificationToken) scrollViewDidEndDeceleratingNotificationToken;
@property (T@"UIHoverGestureRecognizer",&,N,V_hoverGestureRecognizer) hoverGestureRecognizer;
@property (TB,N,V_selectionGestureIsTracking) selectionGestureIsTracking;
@property (T@"UIView",W,N,V_trackableContainerView) trackableContainerView;
@property (T@"UIScrollView",W,N,V_actionsScrollView) actionsScrollView;
@property (TB,N,V_scrubbingEnabled) scrubbingEnabled;
@property (TB,N,V_selectByPressGestureEnabled) selectByPressGestureEnabled;
@property (TB,N,V_selectionFeedbackEnabled) selectionFeedbackEnabled;
@property (TB,N,V_selectByIndirectPointerTouchEnabled) selectByIndirectPointerTouchEnabled;
@property (T@"NSArray",&,N,V_representationViews) representationViews;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIInterfaceActionSelectionTrackingController setTrackableContainerView:];
-[UIInterfaceActionSelectionTrackingController gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[UIInterfaceActionSelectionTrackingController selectionGestureIsTracking];
-[UIInterfaceActionSelectionTrackingController selectByPressGestureEnabled];
-[UIInterfaceActionSelectionTrackingController _rolloverActionChanged:];
-[UIInterfaceActionSelectionTrackingController setScrubbingEnabled:];
-[UIInterfaceActionSelectionTrackingController _invokeHandlerForInterfaceAction:];
-[UIInterfaceActionSelectionTrackingController setHoverGestureRecognizer:];
-[UIInterfaceActionSelectionTrackingController setRepresentationViews:];
-[UIInterfaceActionSelectionTrackingController representationViews];
-[UIInterfaceActionSelectionTrackingController selectionGestureRecognizer];
-[UIInterfaceActionSelectionTrackingController scrollViewDidEndDraggingNotificationToken];
-[UIInterfaceActionSelectionTrackingController scrubbingEnabled];
-[UIInterfaceActionSelectionTrackingController setSelectByIndirectPointerTouchEnabled:];
-[UIInterfaceActionSelectionTrackingController viewsRequiringSelectionGestureDisabling];
-[UIInterfaceActionSelectionTrackingController _allGestureRecognizers];
-[UIInterfaceActionSelectionTrackingController actionsScrollView];
-[UIInterfaceActionSelectionTrackingController dealloc];
-[UIInterfaceActionSelectionTrackingController _actionViewIncludingCooperatingActionViewsAtCurrentLocationForGestureRecognizer:];
-[UIInterfaceActionSelectionTrackingController setSelectionGestureIsTracking:];
-[UIInterfaceActionSelectionTrackingController _performRecursivelyWithVisitedCooperatingControllers:block:];
-[UIInterfaceActionSelectionTrackingController selectionDelayGestureRecognizer];
-[UIInterfaceActionSelectionTrackingController setScrollViewWillBeginDraggingNotificationToken:];
-[UIInterfaceActionSelectionTrackingController _registerForScrollViewNotifications];
-[UIInterfaceActionSelectionTrackingController _setSystemProvidedGestureRecognizer:];
-[UIInterfaceActionSelectionTrackingController scrollViewDidEndDeceleratingNotificationToken];
-[UIInterfaceActionSelectionTrackingController systemProvidedGestureRecognizer];
-[UIInterfaceActionSelectionTrackingController deselectAllActions];
-[UIInterfaceActionSelectionTrackingController setSelectionRetargetFeedbackGenerator:];
-[UIInterfaceActionSelectionTrackingController focusedInterfaceAction];
-[UIInterfaceActionSelectionTrackingController initWithTrackableContainerView:actionsScrollView:];
-[UIInterfaceActionSelectionTrackingController scrollViewWillBeginDraggingNotificationToken];
-[UIInterfaceActionSelectionTrackingController setSelectByPressGestureEnabled:];
-[UIInterfaceActionSelectionTrackingController _gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[UIInterfaceActionSelectionTrackingController handlePressedFocusedInterfaceAction:];
-[UIInterfaceActionSelectionTrackingController _handleActionSelectionGestureRecognizer:];
-[UIInterfaceActionSelectionTrackingController _allActionViewsIncludingCooperatingActionViews];
-[UIInterfaceActionSelectionTrackingController setWeakCooperatingSelectionTrackingControllers:];
-[UIInterfaceActionSelectionTrackingController _gestureRecognizer:shouldReceiveTouch:];
-[UIInterfaceActionSelectionTrackingController selectByPressGestureRecognizer];
-[UIInterfaceActionSelectionTrackingController trackableContainerView];
-[UIInterfaceActionSelectionTrackingController setScrollViewDidEndDeceleratingNotificationToken:];
-[UIInterfaceActionSelectionTrackingController _noteScrollView:isUserScrolling:];
-[UIInterfaceActionSelectionTrackingController weakCooperatingSelectionTrackingControllers];
-[UIInterfaceActionSelectionTrackingController _clearSystemProvidedGestureRecognizer];
-[UIInterfaceActionSelectionTrackingController selectionFeedbackEnabled];
-[UIInterfaceActionSelectionTrackingController beginTrackingSessionByTakingOverForSystemProvidedGestureRecognizer:];
-[UIInterfaceActionSelectionTrackingController hoverGestureRecognizer];
-[UIInterfaceActionSelectionTrackingController setCooperatingSelectionTrackingControllers:];
-[UIInterfaceActionSelectionTrackingController setSelectionFeedbackEnabled:];
-[UIInterfaceActionSelectionTrackingController _shouldDisableSelectionTrackingIfScrollingScrollView:];
-[UIInterfaceActionSelectionTrackingController _isPresentedAndVisible];
-[UIInterfaceActionSelectionTrackingController _handleSystemProvidedGestureRecognizer:];
-[UIInterfaceActionSelectionTrackingController _unregisterForScrollViewNotifications];
-[UIInterfaceActionSelectionTrackingController selectByIndirectPointerTouchEnabled];
-[UIInterfaceActionSelectionTrackingController setScrollViewDidEndDraggingNotificationToken:];
-[UIInterfaceActionSelectionTrackingController _actionViewAtCurrentLocationForGestureRecognizer:];
-[UIInterfaceActionSelectionTrackingController _allowSelectionForCurrentGestureLocationWithGestureRecognizer:];
-[UIInterfaceActionSelectionTrackingController actionSelectionInitialLocationInContainerView];
-[UIInterfaceActionSelectionTrackingController setSelectByPressGestureRecognizer:];
-[UIInterfaceActionSelectionTrackingController _initializeSelectionGestureRecognizer];
-[UIInterfaceActionSelectionTrackingController setActionsScrollView:];
-[UIInterfaceActionSelectionTrackingController _interfaceActionOfFocusedRepresentationView];
-[UIInterfaceActionSelectionTrackingController selectionRetargetFeedbackGenerator];
```
