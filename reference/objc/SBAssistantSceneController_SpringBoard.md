# `SBAssistantSceneController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAssistantObserver`, `SBLayoutStateTransitionObserver`, `SBAssistantSceneControlling`, `CSCoverSheetOverlaying`
- 6 instance variables, 20 properties, 45 instance methods, 0 class methods

## Instance variables

```
B _homeAffordanceDoubleTapGestureEnabled;
B _observingLayoutStateTransitions;
q _lastKnownInterfaceOrientation;
@"SBWindowScene" _windowScene;
@"SBAssistantController" _assistantController;
@"NSHashTable" _observers;
```

## Properties

```
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (T@"SBAssistantController",R,N,V_assistantController) assistantController;
@property (T@"NSHashTable",R,N,V_observers) observers;
@property (TB,N,GisObservingLayoutStateTransitions,V_observingLayoutStateTransitions) observingLayoutStateTransitions;
@property (Tq,N,V_lastKnownInterfaceOrientation) lastKnownInterfaceOrientation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N,GisSystemAssistantExperienceAvailable) systemAssistantExperienceAvailable;
@property (TB,R,N,GisSystemAssistantExperienceEnabled) systemAssistantExperienceEnabled;
@property (TB,R,N,GisSystemAssistantExperiencePersistentSiriEnabled) systemAssistantExperiencePersistentSiriEnabled;
@property (TB,R,N,GisLinwoodDismissalEnabled) linwoodDismissalEnabled;
@property (TB,R,N,GisHomeAffordanceDoubleTapGestureEnabled,V_homeAffordanceDoubleTapGestureEnabled) homeAffordanceDoubleTapGestureEnabled;
@property (TB,R,N,GisVisualSearchEnabled) visualSearchEnabled;
@property (TB,R,N,GisVisible) visible;
@property (TB,R,N,GisOccludingSystemContent) occludingSystemContent;
@property (T@"SBAssistantSessionPresentationContext",R,N) presentationContext;
@property (T@"SBWindow",R,N) window;
@property (T@"SBAssistantRootViewController",R,N) assistantRootViewController;
```

## Instance methods

```
-[SBAssistantSceneController layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:];
-[SBAssistantSceneController assistantDidChangeSystemAssistantExperienceEnablement:];
-[SBAssistantSceneController assistantRootViewController];
-[SBAssistantSceneController assistantDidDisappear:windowScene:];
-[SBAssistantSceneController dismissOverlayForDashBoardAnimated:];
-[SBAssistantSceneController assistantDidChangeHomeAffordanceDoubleTapGestureEnablement:];
-[SBAssistantSceneController isLinwoodDismissalEnabled];
-[SBAssistantSceneController removeObserver:];
-[SBAssistantSceneController _endObservingLayoutStateTransitionsIfNeeded];
-[SBAssistantSceneController isSystemAssistantExperiencePersistentSiriEnabled];
-[SBAssistantSceneController presentationContext];
-[SBAssistantSceneController isSystemAssistantExperienceEnabled];
-[SBAssistantSceneController isObservingLayoutStateTransitions];
-[SBAssistantSceneController _disablesHomeAffordanceDoubleTapGestureInLandscape];
-[SBAssistantSceneController assistantWillDisappear:windowScene:];
-[SBAssistantSceneController isVisible];
-[SBAssistantSceneController window];
-[SBAssistantSceneController _beginObservingLayoutStateTransitionsIfNeeded];
-[SBAssistantSceneController _notifiesAssistantOfApplicationTransitions];
-[SBAssistantSceneController _setHomeAffordanceDoubleTapGestureEnabled:withReason:];
-[SBAssistantSceneController dismissAssistantViewIfNecessaryWithAnimation:completion:];
-[SBAssistantSceneController assistantController];
-[SBAssistantSceneController _reevaluateHomeAffordanceDoubleTapGestureEnablement];
-[SBAssistantSceneController addObserver:];
-[SBAssistantSceneController invalidate];
-[SBAssistantSceneController assistantDidChangeSystemAssistantExperiencePersistentSiriEnablement:];
-[SBAssistantSceneController setObservingLayoutStateTransitions:];
-[SBAssistantSceneController layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:];
-[SBAssistantSceneController assistantDidChangePresentation:windowScene:];
-[SBAssistantSceneController dismissAssistantViewIfNecessary];
-[SBAssistantSceneController assistantDidAppear:windowScene:];
-[SBAssistantSceneController dismissAssistantViewIfNecessaryForGestureTranslation:velocity:];
-[SBAssistantSceneController isHomeAffordanceDoubleTapGestureEnabled];
-[SBAssistantSceneController _lastKnownInterfaceOrientationIsLandscape];
-[SBAssistantSceneController setLastKnownInterfaceOrientation:];
-[SBAssistantSceneController isSystemAssistantExperienceAvailable];
-[SBAssistantSceneController observers];
-[SBAssistantSceneController commandeerCaptureDropletPreludeForVisionInvocation:];
-[SBAssistantSceneController windowScene];
-[SBAssistantSceneController dismissAssistantViewIfNecessaryWithAnimation:];
-[SBAssistantSceneController initWithWindowScene:assistantController:];
-[SBAssistantSceneController isVisualSearchEnabled];
-[SBAssistantSceneController lastKnownInterfaceOrientation];
-[SBAssistantSceneController assistantWillAppear:windowScene:];
-[SBAssistantSceneController isOccludingSystemContent];
```
