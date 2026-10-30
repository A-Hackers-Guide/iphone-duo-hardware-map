# `SBAssistantGestureManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `SBSystemGestureRecognizerDelegate`, `SBHomeGrabberPointerClickDelegate`, `SBHomeGesturePanGestureRecognizerContextDelegate`, `SBAssistantGestureConfigurationObserving`, `SBFZStackParticipantDelegate`, `PTSettingsKeyObserver`, `SBAssistantSessionObserver`
- 14 instance variables, 16 properties, 72 instance methods, 1 class methods

## Instance variables

```
@"SBSystemAnimationSettings" _settings;
@"UIGestureRecognizer" _statusBarActionGestureRecognizer;
B _allowPencilTouches;
@"<SBAssistantGestureManagerDelegate>" _delegate;
@"SBTransientOverlayViewController" _topmostTransientViewControllerAtPresentation;
@"SBAssistantGestureConfiguration" _gestureConfiguration;
@"SBAssistantWindow" _assistantWindow;
@"SBAssistantContext" _context;
@"SBHomeGesturePanGestureRecognizer" _bottomEdgeDismissGestureRecognizer;
@"UITapGestureRecognizer" _tapToDismissSiriGestureRecognizer;
@"UIPanGestureRecognizer" _panToDismissSiriGestureRecognizer;
@"SBFZStackParticipant" _zStackParticipant;
q _homeAffordanceSuppression;
@"SBPhysicalButtonZStackPolicyAssistant" _physicalButtonPolicyAssistant;
```

## Properties

```
@property (T@"SBAssistantGestureConfiguration",R,N,V_gestureConfiguration) gestureConfiguration;
@property (T@"SBAssistantWindow",R,N,V_assistantWindow) assistantWindow;
@property (T@"SBAssistantContext",R,N,V_context) context;
@property (T@"SBHomeGesturePanGestureRecognizer",&,N,V_bottomEdgeDismissGestureRecognizer) bottomEdgeDismissGestureRecognizer;
@property (T@"UITapGestureRecognizer",&,N,V_tapToDismissSiriGestureRecognizer) tapToDismissSiriGestureRecognizer;
@property (T@"UIPanGestureRecognizer",&,N,V_panToDismissSiriGestureRecognizer) panToDismissSiriGestureRecognizer;
@property (T@"SBFZStackParticipant",&,N,V_zStackParticipant) zStackParticipant;
@property (Tq,N,V_homeAffordanceSuppression) homeAffordanceSuppression;
@property (T@"SBPhysicalButtonZStackPolicyAssistant",&,N,V_physicalButtonPolicyAssistant) physicalButtonPolicyAssistant;
@property (TB,R,N,V_allowPencilTouches) allowPencilTouches;
@property (T@"<SBAssistantGestureManagerDelegate>",W,N,V_delegate) delegate;
@property (T@"SBTransientOverlayViewController",&,N,V_topmostTransientViewControllerAtPresentation) topmostTransientViewControllerAtPresentation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBAssistantGestureManager shouldDismissSiriForGestureTranslation:velocity:];
```

## Instance methods

```
-[SBAssistantGestureManager zStackParticipant];
-[SBAssistantGestureManager setZStackParticipant:];
-[SBAssistantGestureManager homeGrabberViewDidReceiveClick:];
-[SBAssistantGestureManager zStackParticipant:updatePreferences:];
-[SBAssistantGestureManager dealloc];
-[SBAssistantGestureManager zStackParticipantDidChange:];
-[SBAssistantGestureManager zStackParticipant:updateZOrderPreferences:];
-[SBAssistantGestureManager settings:changedValueForKey:];
-[SBAssistantGestureManager viewForSystemGestureRecognizer:];
-[SBAssistantGestureManager setDelegate:];
-[SBAssistantGestureManager gestureRecognizerShouldBegin:];
-[SBAssistantGestureManager gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[SBAssistantGestureManager delegate];
-[SBAssistantGestureManager touchInterfaceOrientationForHomeGesturePanGestureRecognizer:];
-[SBAssistantGestureManager context];
-[SBAssistantGestureManager assistantWindow];
-[SBAssistantGestureManager _assistantRootViewController];
-[SBAssistantGestureManager _commonHandlerForSiriDismissalGesture:];
-[SBAssistantGestureManager _configureHomeGesture];
-[SBAssistantGestureManager _configurePanToDismissGestureDependencies];
-[SBAssistantGestureManager _createPanToDismissSiriGestureRecognizer];
-[SBAssistantGestureManager _createTapToDismissSiriGestureRecognizer];
-[SBAssistantGestureManager _didUpdateHomeGestureSharing:];
-[SBAssistantGestureManager _didUpdateShouldDismissForSwipesOutsideContent:];
-[SBAssistantGestureManager _didUpdateShouldDismissForTapsOutsideContent:];
-[SBAssistantGestureManager _didUpdateShouldShowHomeAffordance:];
-[SBAssistantGestureManager _didUpdateSiriHomeAffordanceSuppression:];
-[SBAssistantGestureManager _didUpdateStatusBarActionGestureRecognizer:];
-[SBAssistantGestureManager _didUpdateTouchesPassThroughToSpringBoard:];
-[SBAssistantGestureManager _handleBottomEdgeDismissGesture:];
-[SBAssistantGestureManager _noNewTransientOverlaysPresented];
-[SBAssistantGestureManager _notifyInteractionWithGestureRecognizer:];
-[SBAssistantGestureManager _pannedToDismissSiri:];
-[SBAssistantGestureManager _prototypeSettingsChanged];
-[SBAssistantGestureManager _removeHomeGesture];
-[SBAssistantGestureManager _removeScreenEdgePanGestureRecognizerIfNecessary];
-[SBAssistantGestureManager _resetDismissalSystemGestures];
-[SBAssistantGestureManager _setupSystemDismissalGestures];
-[SBAssistantGestureManager _tappedToDismissSiri:];
-[SBAssistantGestureManager _tearDownDismissalSystemGestures];
-[SBAssistantGestureManager _updateRootViewControllerDimsContentBelow];
-[SBAssistantGestureManager _updateRootViewControllerOwnsHomeGesture];
-[SBAssistantGestureManager _updateRootViewControllerShowsHomeAffordance:];
-[SBAssistantGestureManager _updateZStackParticipantWithReason:];
-[SBAssistantGestureManager allowPencilTouches];
-[SBAssistantGestureManager assistantGestureConfiguration:didUpdateHomeAffordanceSuppression:];
-[SBAssistantGestureManager assistantGestureConfiguration:didUpdateHomeGestureSharing:];
-[SBAssistantGestureManager assistantGestureConfiguration:didUpdateShouldDismissForSwipesOutsideContent:];
-[SBAssistantGestureManager assistantGestureConfiguration:didUpdateShouldDismissForTapsOutsideContent:];
-[SBAssistantGestureManager assistantGestureConfiguration:didUpdateShouldPassTouchesThroughToSpringBoard:];
-[SBAssistantGestureManager assistantGestureConfiguration:didUpdateShouldShowHomeAffordance:];
-[SBAssistantGestureManager assistantGestureConfiguration:didUpdateStatusBarActionGestureRecognizer:];
-[SBAssistantGestureManager assistantSession:didChangePresentationInWindowScene:];
-[SBAssistantGestureManager assistantSession:viewDidAppearInWindowScene:];
-[SBAssistantGestureManager assistantSession:viewDidDisappearInWindowScene:];
-[SBAssistantGestureManager assistantSession:viewWillAppearInWindowScene:];
-[SBAssistantGestureManager assistantSession:viewWillDisappearInWindowScene:];
-[SBAssistantGestureManager bottomEdgeDismissGestureRecognizer];
-[SBAssistantGestureManager gestureConfiguration];
-[SBAssistantGestureManager gesturesImplyFullscreenContent];
-[SBAssistantGestureManager homeAffordanceSuppression];
-[SBAssistantGestureManager initWithAssistantWindow:gestureConfiguration:context:];
-[SBAssistantGestureManager panToDismissSiriGestureRecognizer];
-[SBAssistantGestureManager physicalButtonPolicyAssistant];
-[SBAssistantGestureManager setBottomEdgeDismissGestureRecognizer:];
-[SBAssistantGestureManager setHomeAffordanceSuppression:];
-[SBAssistantGestureManager setPanToDismissSiriGestureRecognizer:];
-[SBAssistantGestureManager setPhysicalButtonPolicyAssistant:];
-[SBAssistantGestureManager setTapToDismissSiriGestureRecognizer:];
-[SBAssistantGestureManager setTopmostTransientViewControllerAtPresentation:];
-[SBAssistantGestureManager tapToDismissSiriGestureRecognizer];
-[SBAssistantGestureManager topmostTransientViewControllerAtPresentation];
```
