# `SBBannerManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BNPostingPrivate`, `BNPresentingDelegate`, `BNBannerSourceListenerDelegate`, `BNPresentableObserving`, `SBAmbientPresentationObserver`, `SBPlatterHomeGestureManagerDelegate`, `SBWindowLevelAssertionManagerDelegate`, `SBBannerPanGestureSystemDragCancellingDelegate`, `SBPresentableSystemDragCancellationHandler`, `SBFZStackParticipantDelegate`, `SBZStackForegroundScenePolicyAssistantDelegate`, `SBMenuBarManagerObserver`, `_UISceneHingeStateClientObserver`, `SBDisplayContentModeTransitionObserver`, `SBTransientOverlayScenePresenterObserver`, `BNPosting`, `SBButtonEventsHandler`, `SBWindowLevelAssertionProviding`
- 33 instance variables, 6 properties, 141 instance methods, 1 class methods

## Instance variables

```
@"SBBannerAuthority" _bannerAuthority;
@"NSMapTable" _windowScenesToBannerControllers;
@"NSMapTable" _windowScenesToBannerWindows;
@"BNBannerSourceListener" _bannerSourceListener;
@"SBWindowLevelAssertionManager" _windowLevelAssertionManager;
@"NSMapTable" _windowScenesToPanGestures;
@"NSMapTable" _windowScenesToZStackParticipants;
@"NSMapTable" _windowScenesToPhysicalButtonAssistants;
@"NSMutableDictionary" _presentableVCsToCustomTransitioningDelegates;
@"NSMutableArray" _gesturePriorityAssertions;
@"NSMapTable" _gesturePriorityAssertionsToWindowScenes;
@"NSMapTable" _presentablesToGesturePriorityAssertions;
@"NSMapTable" _presentablesToPostingContexts;
@"NSMutableArray" _presentablesToRepostOnUnsuspend;
@"NSMapTable" _windowScenesToPresenterVisibilityGesturePriorityAssertions;
@"NSMutableDictionary" _foregroundScenesToDeferringRules;
@"NSHashTable" _suppressionAssertions;
@"NSHashTable" _transitionObservers;
@"NSMutableSet" _clientSuppressionAssertions;
@"<BSInvalidatable>" _systemStatusBarAssertion;
@"<BSInvalidatable>" _appsStatusBarAssertion;
@"NSMutableSet" _statusBarAssertionReasons;
B _assistantIslandDodgeLatchedOff;
@"SBPlatterHomeGestureManager" _platterHomeGestureManager;
@"NSMapTable" _presentableHomeGestureParticipantsToGesturePriorityAssertions;
@"NSMapTable" _windowScenesToTraitsParticipant;
@"SBTraitsWindowParticipantDelegate" _windowParticipantDelegate;
@"NSMutableSet" _presentablesToRevokeWhenUserInteractionEnd;
@"<BNPresentable>" _presentableForActiveGesture;
@"NSMutableDictionary" _activeSystemApertureFrameInPortraitByDisplay;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _assistantIslandAvoidanceFrame;
B _transientOverlayPresented;
@"<SBPresentableIntercepting>" _presentableInterceptor;
```

## Properties

```
@property (T@"<SBPresentableIntercepting>",W,N,V_presentableInterceptor) presentableInterceptor;
@property (TB,R,N,GisDisplayingBannerInAnyWindowScene) displayingBannerInAnyWindowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBBannerManager _defaultAuthorizedBundleIDs];
```

## Instance methods

```
-[SBBannerManager _bannerWindowForWindowScene:creatingIfNecessary:];
-[SBBannerManager _panGestureInWindowScene:creatingIfNecessary:];
-[SBBannerManager acquireWindowLevelAssertionWithPriority:windowLevel:windowScene:reason:];
-[SBBannerManager _systemApertureInsetsDidChange:];
-[SBBannerManager _updateDeferringRulesForWindowScene:activeForegroundScenes:];
-[SBBannerManager _updateGesturePriorityForGestureRecognizerInWindowScene:];
-[SBBannerManager _zStackParticipantForWindowScene:];
-[SBBannerManager _activeSystemApertureFrameInPortraitForWindow:];
-[SBBannerManager windowLevelAssertionManager:didUpdateAssertionsForWindowScene:];
-[SBBannerManager _presenterForWindowScene:];
-[SBBannerManager _updateWindowLevelForScene:];
-[SBBannerManager handleVolumeDownButtonPress];
-[SBBannerManager _shouldHideStatusBarForPresentable:];
-[SBBannerManager transientOverlayScenePresenter:didDismissViewController:wasTopmostPresentation:];
-[SBBannerManager platterHomeGestureManager:orderedParticipants:];
-[SBBannerManager _insetForAvoidanceFrame:currentInsets:window:bannerFrame:loggingName:];
-[SBBannerManager removeTransitionObserver:];
-[SBBannerManager revokePresentablesWithIdentification:reason:options:animated:userInfo:error:];
-[SBBannerManager bannerSourceListener:newBannerSourceListenerPresentableForBannerSpecification:serviceDomain:scene:readyCompletion:];
-[SBBannerManager preferredBannerAlignmentForPresenter:];
-[SBBannerManager foregroundSceneZStackPolicyAssistantDidChange:forReason:];
-[SBBannerManager transientOverlayScenePresenter:willPresentViewController:];
-[SBBannerManager _assistantIslandAvoidanceFrameForWindow:];
-[SBBannerManager zStackParticipant:updatePreferences:];
-[SBBannerManager userInterfaceStyleTransitionAnimationSettingsForPresentable:forTransitionToStyle:];
-[SBBannerManager handleHomeButtonLongPress];
-[SBBannerManager _acquireGestureRecognizerPriorityAssertionWithPriority:windowScene:reason:];
-[SBBannerManager _logGesturePriorityStateForWindowScene:reasonSuffix:];
-[SBBannerManager _presenterForPresentable:];
-[SBBannerManager init];
-[SBBannerManager addTransitionObserver:];
-[SBBannerManager bannerContainmentFrameForPresenter:idealWidth:];
-[SBBannerManager _updateExclusiveBannerRegionForWindowScene:reason:];
-[SBBannerManager displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBBannerManager bannerPanGestureRecognizer:shouldDisableTouchCancellationForTouch:event:];
-[SBBannerManager dismissAllBannersInWindowScene:animated:reason:];
-[SBBannerManager layoutManagerInWindowScene:];
-[SBBannerManager menuBarDidBecomeVisible:forManager:];
-[SBBannerManager menuWillPresentForMenuBarManager:];
-[SBBannerManager isDisplayingFullScreenBannerInWindowScene:];
-[SBBannerManager postPresentable:withOptions:userInfo:error:];
-[SBBannerManager _platterHomeGestureManager];
-[SBBannerManager presenter:willPresentPresentable:withTransitionCoordinator:userInfo:];
-[SBBannerManager ambientPresentationController:willUpdatePresented:];
-[SBBannerManager handleVoiceCommandButtonPress];
-[SBBannerManager displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBBannerManager _bannerControllerForWindowScene:];
-[SBBannerManager handleHeadsetButtonPress:];
-[SBBannerManager _updateTransientOverlayPresence];
-[SBBannerManager _regularDeviceUseableFrameForWindow:scene:];
-[SBBannerManager bannerSourceListener:addExtensionIfNeededForScene:userInfo:];
-[SBBannerManager bannerSourceListener:didUpdateInitialSceneSettingsWithParameters:];
-[SBBannerManager handleLockButtonPress];
-[SBBannerManager zStackParticipantDidChange:];
-[SBBannerManager hingeStateComponent:didUpdateFromState:toState:];
-[SBBannerManager pointInsideBanner:inWindowScene:];
-[SBBannerManager handleHomeButtonPressInWindowScene:];
-[SBBannerManager presenter:willTransitionToSize:withTransitionCoordinator:];
-[SBBannerManager handleVolumeUpButtonPress];
-[SBBannerManager zStackParticipant:updateZOrderPreferences:];
-[SBBannerManager newBannerControllerForWindowScene:];
-[SBBannerManager _windowSceneForPresenter:];
-[SBBannerManager _windowSceneForZStackParticipant:];
-[SBBannerManager acquireGestureRecognizerPriorityAssertionForPresentable:priority:reason:];
-[SBBannerManager _windowForPresenter:];
-[SBBannerManager handleHomeButtonDoublePress];
-[SBBannerManager bannerSourceListener:didUpdateInitialSceneSettings:];
-[SBBannerManager bannerSourceListener:sceneSpecificationForBannerSceneWithIdentifier:forProcess:userInfo:];
-[SBBannerManager _bannerWindowForWindowScene:];
-[SBBannerManager _handleButtonEventWithTest:handler:];
-[SBBannerManager _contentViewControllerForWindowScene:];
-[SBBannerManager platterHomeGestureManager:gestureRecognizerPriorityAssertionForParticipant:reason:];
-[SBBannerManager bannerSourceListenerShouldEnablePresentableContextInterface:];
-[SBBannerManager _setUpBannerAvoidance];
-[SBBannerManager presenter:gestureRecognizer:locationForTouch:inView:];
-[SBBannerManager presenter:gestureRecognizer:translationInView:];
-[SBBannerManager presenter:willDismissPresentable:withTransitionCoordinator:userInfo:];
-[SBBannerManager revokePresentablesWithIdentification:reason:options:userInfo:error:];
-[SBBannerManager userInteractionWillBeginForBannerForPresentable:];
-[SBBannerManager setPresentableInterceptor:];
-[SBBannerManager _hideStatusBarIfNecessaryForPresentable:];
-[SBBannerManager userInteractionDidEndForBannerForPresentable:];
-[SBBannerManager _panGestureInWindowScene:];
-[SBBannerManager _shouldRevokePresentablesWithIdentification:reason:options:userInfo:error:];
-[SBBannerManager _activeSystemApertureTopInsetForWindow:];
-[SBBannerManager _isPresentableHUD:];
-[SBBannerManager bannerSourceListener:layoutDescriptionWithError:];
-[SBBannerManager bannerSourceListener:recommendsSuspending:forReason:revokingCurrent:error:];
-[SBBannerManager _homeGestureContextForPresentable:windowScene:];
-[SBBannerManager _setWindowScene:forGestureRecognizerPriorityAssertion:];
-[SBBannerManager presenter:gestureRecognizer:velocityInView:];
-[SBBannerManager presenter:minimumPreferredEdgeInsetsForBannerFrame:];
-[SBBannerManager windowSceneForPresentable:];
-[SBBannerManager _invalidatePresenterVisibilityGestureRecognizerPriorityAssertionForWindowScene:];
-[SBBannerManager _unregisterHomeGestureContextForPresentable:];
-[SBBannerManager _updatePolicyAssistantForWindowScene:];
-[SBBannerManager _enumerateObserversRespondingToSelector:usingBlock:];
-[SBBannerManager _windowSceneForBannerController:];
-[SBBannerManager _zStackPolicyAssistantForParticipant:];
-[SBBannerManager bannerPanGestureRecognizer:shouldCancelSystemDragGestureWithTouches:event:];
-[SBBannerManager bannerSourceListener:requestsRevokingPresentablesWithIdentification:reason:animated:userInfo:error:];
-[SBBannerManager bannerWindowInWindowScene:];
-[SBBannerManager dismissAllBannersInAllWindowScenesAnimated:reason:];
-[SBBannerManager dismissAllBannersInWindowScene:animated:reason:keepPostingContextForRepost:];
-[SBBannerManager _needsToAddExtensionForSceneWithUserInfo:];
-[SBBannerManager _assistantIslandFrameDidChange:];
-[SBBannerManager platterHomeGestureManager:zStackParticipantIdentifierForParticipant:];
-[SBBannerManager presentableInterceptor];
-[SBBannerManager _apertureAvoidanceFrameForWindow:];
-[SBBannerManager _avoidableObstacleFramesForWindow:];
-[SBBannerManager postPresentable:withOptions:reason:animated:userInfo:error:];
-[SBBannerManager setSuspended:forReason:];
-[SBBannerManager _isPresentableNotice:];
-[SBBannerManager _bannerAlignmentForWindow:scene:];
-[SBBannerManager _handleButtonEventWithWindowScene:test:handler:];
-[SBBannerManager _menuBarTopInsetForPresenter:];
-[SBBannerManager _revealStatusBarIfNecessaryForPresentable:];
-[SBBannerManager _statusBarAssertionReasonForPresentable:];
-[SBBannerManager bannerSourceListener:presentationSize:containerSize:error:];
-[SBBannerManager presenter:gestureRecognizer:locationForEvent:inView:];
-[SBBannerManager presentableDidDisappearAsBanner:withReason:];
-[SBBannerManager _updateZStackPolicyAssistantForWindowScene:reasonSuffix:transitionCoordinator:];
-[SBBannerManager acquireBannerSuppressionAssertionForReason:];
-[SBBannerManager presenter:presentable:willTransitionToSize:withTransitionCoordinator:];
-[SBBannerManager isDisplayingBannerInAnyWindowScene];
-[SBBannerManager registerAuthority:forRequesterIdentifier:];
-[SBBannerManager bannerSourceListener:requestsPostingPresentable:options:userInfo:error:];
-[SBBannerManager _usesPadLayoutBehaviorForWindow:];
-[SBBannerManager _invalidatePreferredMinimumTopInsetInteractive:];
-[SBBannerManager _acquirePresenterVisibilityGestureRecognizerPriorityAssertionForWindowScene:];
-[SBBannerManager _zStackParticipantForAssistant:];
-[SBBannerManager _zStackPolicyAssistantForWindowScene:];
-[SBBannerManager _layoutDescriptionWithBounds:inWindowScene:];
-[SBBannerManager isDisplayingBannerInWindowScene:];
-[SBBannerManager cancelSystemDragForPresentable:];
-[SBBannerManager panGestureRecognizerForPresenter:];
-[SBBannerManager platterHomeGestureManager:windowForParticipant:];
-[SBBannerManager handleHomeButtonPress];
-[SBBannerManager presenterRelinquishesVisibility:];
-[SBBannerManager platterHomeGestureManager:participantOwningHomeGestureDidChange:];
-[SBBannerManager presenterRequestsVisibility:];
```
