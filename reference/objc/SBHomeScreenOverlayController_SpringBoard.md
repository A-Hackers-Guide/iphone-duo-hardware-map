# `SBHomeScreenOverlayController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBarSwipeAffordanceDelegate`, `SBBarSwipeAffordanceObserver`, `SBHomeScreenOverlayViewControllerDelegate`, `UIGestureRecognizerDelegate`, `SBFOverlayControlling`, `SBFIdleTimerBehaviorProviding`, `CSExternalBehaviorProviding`, `CSExternalEventHandling`, `BSDescriptionProviding`, `SBFOverlayDismissalDelegate`, `SBHVisibleContentPresenter`
- 20 instance variables, 42 properties, 115 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"NSCountedSet" _reasonsToDisablePanGestureRecognizer;
@"SBFFrameRateAssertion" _frameRateAssertion;
B _dismissing;
B _animatingPresentationProgress;
B _overlayAppearing;
B _overlayDisappearing;
@"<SBFOverlayDismissalDelegate>" _dismissalDelegate;
@"<SBHomeScreenOverlayControllerDelegate>" _delegate;
@"UITapGestureRecognizer" _dismissTapGestureRecognizer;
@"SBFWindow" _window;
@"SBBarSwipeAffordanceViewController" _homeAffordanceViewController;
@"SBHomeScreenOverlayViewController" _overlayViewController;
@"<BSInvalidatable>" _displayLayoutAssertion;
Q _screenEdgeSystemGestureType;
@"UIPanGestureRecognizer" _dismissPanGestureRecognizer;
Q _indirectScreenEdgeSystemGestureType;
Q _scrunchSystemGestureType;
@"UIViewController" _existingAvocadoVC;
d _initialPresentationProgress;
```

## Properties

```
@property (T@"SBFWindow",R,N,V_window) window;
@property (T@"SBBarSwipeAffordanceViewController",R,N,V_homeAffordanceViewController) homeAffordanceViewController;
@property (T@"SBHomeScreenOverlayViewController",R,N,V_overlayViewController) overlayViewController;
@property (T@"<BSInvalidatable>",&,N,V_displayLayoutAssertion) displayLayoutAssertion;
@property (TB,N,GisDismissing,V_dismissing) dismissing;
@property (TQ,R,N,V_screenEdgeSystemGestureType) screenEdgeSystemGestureType;
@property (T@"UIPanGestureRecognizer",&,N,V_dismissPanGestureRecognizer) dismissPanGestureRecognizer;
@property (TQ,R,N,V_indirectScreenEdgeSystemGestureType) indirectScreenEdgeSystemGestureType;
@property (TQ,R,N,V_scrunchSystemGestureType) scrunchSystemGestureType;
@property (TB,N,GisAnimatingPresentationProgress,V_animatingPresentationProgress) animatingPresentationProgress;
@property (TB,N,GisOverlayAppearing,V_overlayAppearing) overlayAppearing;
@property (TB,N,GisOverlayDisappearing,V_overlayDisappearing) overlayDisappearing;
@property (T@"UIViewController",W,N,V_existingAvocadoVC) existingAvocadoVC;
@property (Td,N,V_initialPresentationProgress) initialPresentationProgress;
@property (TB,N) shouldUseReducedMotionAnimation;
@property (T@"<SBHomeScreenOverlayControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"UIViewController<SBHLibraryViewControllerPresenter><SBHWidgetSheetViewControllerPresenter>",R,N) viewController;
@property (T@"UIViewController<SBHVisibleContentPresenter>",&,N) leadingSidebarViewController;
@property (T@"UIViewController<SBHVisibleContentPresenter>",&,N) trailingSidebarViewController;
@property (T@"UIViewController",R,N) activeSidebarViewController;
@property (T@"UITapGestureRecognizer",R,N,V_dismissTapGestureRecognizer) dismissTapGestureRecognizer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,R,N) contentWidth;
@property (Td,N) presentationProgress;
@property (TB,R,N,GisPresented) presented;
@property (T@"<SBFOverlayDismissalDelegate>",W,N,V_dismissalDelegate) dismissalDelegate;
@property (Td,R,N) leadingViewScrollFraction;
@property (Tq,R,N) idleTimerDuration;
@property (Tq,R,N) idleTimerMode;
@property (Tq,R,N) idleWarnMode;
@property (Td,?,R,N) customIdleExpirationTimeout;
@property (Td,?,R,N) customIdleWarningTimeout;
@property (Tq,R,N) scrollingStrategy;
@property (Tq,R,N) notificationBehavior;
@property (TQ,R,N) restrictedCapabilities;
@property (Tq,R,N) proximityDetectionMode;
@property (T@"NSString",R,C,N) coverSheetIdentifier;
@property (Tq,R,N) participantState;
@property (TQ,N) contentVisibility;
```

## Instance methods

```
-[SBHomeScreenOverlayController dismissAnimated:completionHandler:];
-[SBHomeScreenOverlayController presentAnimated:completionHandler:];
-[SBHomeScreenOverlayController isPresented];
-[SBHomeScreenOverlayController handleEvent:];
-[SBHomeScreenOverlayController wouldHandleButtonEvent:];
-[SBHomeScreenOverlayController displayLayoutAssertion];
-[SBHomeScreenOverlayController _setDisplayLayoutElementActive:];
-[SBHomeScreenOverlayController conformsToCSBehaviorProviding];
-[SBHomeScreenOverlayController gestureRecognizer:shouldReceiveTouch:];
-[SBHomeScreenOverlayController succinctDescriptionBuilder];
-[SBHomeScreenOverlayController barSwipeAffordanceView:systemGestureTypeForType:];
-[SBHomeScreenOverlayController dealloc];
-[SBHomeScreenOverlayController idleTimerDuration];
-[SBHomeScreenOverlayController proximityDetectionMode];
-[SBHomeScreenOverlayController window];
-[SBHomeScreenOverlayController descriptionWithMultilinePrefix:];
-[SBHomeScreenOverlayController homeGesturePerformedForBarSwipeAffordanceView:];
-[SBHomeScreenOverlayController viewController];
-[SBHomeScreenOverlayController succinctDescription];
-[SBHomeScreenOverlayController setDelegate:];
-[SBHomeScreenOverlayController setPresentationProgress:];
-[SBHomeScreenOverlayController isDismissing];
-[SBHomeScreenOverlayController gestureRecognizerShouldBegin:];
-[SBHomeScreenOverlayController contentVisibility];
-[SBHomeScreenOverlayController scrollingStrategy];
-[SBHomeScreenOverlayController notificationBehavior];
-[SBHomeScreenOverlayController homeAffordanceViewController];
-[SBHomeScreenOverlayController setContentVisibility:];
-[SBHomeScreenOverlayController _setHidden:];
-[SBHomeScreenOverlayController presentAnimated:];
-[SBHomeScreenOverlayController delegate];
-[SBHomeScreenOverlayController dismissTapGestureRecognizer];
-[SBHomeScreenOverlayController description];
-[SBHomeScreenOverlayController contentWidth];
-[SBHomeScreenOverlayController conformsToCSExternalBehaviorProviding];
-[SBHomeScreenOverlayController setDismissing:];
-[SBHomeScreenOverlayController conformsToCSEventHandling];
-[SBHomeScreenOverlayController idleTimerMode];
-[SBHomeScreenOverlayController coverSheetIdentifier];
-[SBHomeScreenOverlayController setDisplayLayoutAssertion:];
-[SBHomeScreenOverlayController idleWarnMode];
-[SBHomeScreenOverlayController participantState];
-[SBHomeScreenOverlayController updateExtraButtonVisibilityAnimated:];
-[SBHomeScreenOverlayController restrictedCapabilities];
-[SBHomeScreenOverlayController descriptionBuilderWithMultilinePrefix:];
-[SBHomeScreenOverlayController overlayViewController];
-[SBHomeScreenOverlayController _rootViewController];
-[SBHomeScreenOverlayController dismissalDelegate];
-[SBHomeScreenOverlayController setDismissalDelegate:];
-[SBHomeScreenOverlayController dismissPanGestureRecognizer];
-[SBHomeScreenOverlayController initWithListLayoutProvider:];
-[SBHomeScreenOverlayController presentationProgress];
-[SBHomeScreenOverlayController setPresentationProgress:interactive:animated:completionHandler:];
-[SBHomeScreenOverlayController addHomeScreenOverlayObserver:];
-[SBHomeScreenOverlayController finalPresentationProgressForTranslation:velocity:initialPresentationProgress:fromLeading:];
-[SBHomeScreenOverlayController interceptDismissalGestureForOverlayController:];
-[SBHomeScreenOverlayController layerPresentationProgress];
-[SBHomeScreenOverlayController leadingViewScrollFraction];
-[SBHomeScreenOverlayController overlayControllerRequestsDismissal:];
-[SBHomeScreenOverlayController presentationProgressForTranslation:initialPresentationProgress:fromLeading:];
-[SBHomeScreenOverlayController setLeadingViewScrollFraction:animated:];
-[SBHomeScreenOverlayController setPresentationProgress:fromLeading:interactive:animated:completionHandler:];
-[SBHomeScreenOverlayController isAnimatingPresentationProgress];
-[SBHomeScreenOverlayController setInitialPresentationProgress:];
-[SBHomeScreenOverlayController homeScreenOverlayViewWantsWidgetEditingViewControllerPresented:];
-[SBHomeScreenOverlayController setDismissPanGestureRecognizer:];
-[SBHomeScreenOverlayController shouldUseReducedMotionAnimation];
-[SBHomeScreenOverlayController _addSystemGestureRecognizer];
-[SBHomeScreenOverlayController _configureDismissGestureRecognizer];
-[SBHomeScreenOverlayController _directionCoefficient];
-[SBHomeScreenOverlayController _dismissLevelAnimated:completionHandler:];
-[SBHomeScreenOverlayController _dismissScrollGestureBegan:];
-[SBHomeScreenOverlayController _dismissScrollGestureChanged:];
-[SBHomeScreenOverlayController _dismissScrollGestureEndedOrCancelled:];
-[SBHomeScreenOverlayController _enumerateHomeScreenOverlayObserversUsingBlock:];
-[SBHomeScreenOverlayController _removeSystemGestureRecognizer];
-[SBHomeScreenOverlayController _setHitTestingDisabled:];
-[SBHomeScreenOverlayController activeSidebarViewController];
-[SBHomeScreenOverlayController addReasonToDisableDismissGestureRecognizer:];
-[SBHomeScreenOverlayController animatePresentationProgress:withGestureLiftOffVelocity:completionHandler:];
-[SBHomeScreenOverlayController backgroundViewForEditingDoneButtonForHomeScreenOverlayViewController:];
-[SBHomeScreenOverlayController cleanUpAfterSettingPresentationProgress:];
-[SBHomeScreenOverlayController dismissScrollGestureUpdated:];
-[SBHomeScreenOverlayController dismissTapGestureUpdated:];
-[SBHomeScreenOverlayController dismissUsingViewControllerTransitionCoordinator:];
-[SBHomeScreenOverlayController existingAvocadoVC];
-[SBHomeScreenOverlayController homeScreenOverlayViewController:setSuppressesEditingStateForListView:];
-[SBHomeScreenOverlayController homeScreenOverlayViewControllerRequestsDismissal:];
-[SBHomeScreenOverlayController homeScreenOverlayViewWantsToEndEditing:];
-[SBHomeScreenOverlayController indirectScreenEdgeSystemGestureType];
-[SBHomeScreenOverlayController initWithListLayoutProvider:windowLevel:windowScene:traitsRole:zStackParticipantIdentifier:screenEdgeSystemGestureType:indirectScreenEdgeSystemGestureType:scrunchSystemGestureType:secure:];
-[SBHomeScreenOverlayController initialPresentationProgress];
-[SBHomeScreenOverlayController isEditingForHomeScreenOverlayViewController:];
-[SBHomeScreenOverlayController isOverlayAppearing];
-[SBHomeScreenOverlayController isOverlayDisappearing];
-[SBHomeScreenOverlayController leadingSidebarViewController];
-[SBHomeScreenOverlayController prepareToSetPresentationProgress:fromPresentationProgress:];
-[SBHomeScreenOverlayController presentAnimated:fromLeading:];
-[SBHomeScreenOverlayController presentAnimated:fromLeading:completionHandler:];
-[SBHomeScreenOverlayController removeHomeScreenOverlayObserver:];
-[SBHomeScreenOverlayController removeReasonToDisableDismissGestureRecognizer:];
-[SBHomeScreenOverlayController screenEdgeSystemGestureType];
-[SBHomeScreenOverlayController scrunchSystemGestureType];
-[SBHomeScreenOverlayController setAnimatingPresentationProgress:];
-[SBHomeScreenOverlayController setExistingAvocadoVC:];
-[SBHomeScreenOverlayController setLeadingSidebarViewController:];
-[SBHomeScreenOverlayController setOverlayAppearing:];
-[SBHomeScreenOverlayController setOverlayDisappearing:];
-[SBHomeScreenOverlayController setPresentationProgress:fromLeading:];
-[SBHomeScreenOverlayController setShouldUseReducedMotionAnimation:];
-[SBHomeScreenOverlayController setTrailingSidebarViewController:];
-[SBHomeScreenOverlayController showsAddWidgetButtonWhileEditingForHomeScreenOverlayViewController:];
-[SBHomeScreenOverlayController showsDoneButtonWhileEditingForHomeScreenOverlayViewController:];
-[SBHomeScreenOverlayController testScrollView];
-[SBHomeScreenOverlayController trailingSidebarViewController];
```
