# `SBHUDController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_SBHUDHostViewControllerDelegate`, `SBFZStackParticipantDelegate`, `PTSettingsKeyObserver`, `BSDescriptionProviding`, `UIViewControllerTransitioningDelegate`, `SBHUDControlling`
- 8 instance variables, 10 properties, 40 instance methods, 1 class methods

## Instance variables

```
@"SBHUDCoordinator" _coordinator;
@"NSCountedSet" _hudHiddenAssertions;
@"<BSInvalidatable>" _stateCaptureHandle;
@"SBWindowScene" _windowScene;
@"SBFZStackParticipant" _zStackParticipant;
@"UIWindow" _HUDWindow;
@"_SBHUDHostViewController" _hudViewController;
@"SBHUDSettings" _settings;
```

## Properties

```
@property (T@"SBFZStackParticipant",R,N,V_zStackParticipant) zStackParticipant;
@property (T@"UIWindow",R,N,V_HUDWindow) HUDWindow;
@property (T@"_SBHUDHostViewController",R,N,V_hudViewController) hudViewController;
@property (T@"SBHUDSettings",R,N,V_settings) settings;
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) anyHUDsVisible;
```

## Class methods

```
+[SBHUDController _defaultCrossfadeAnimatorForHUDController:];
```

## Instance methods

```
-[SBHUDController zStackParticipant];
-[SBHUDController animationControllerForDismissedController:];
-[SBHUDController animationControllerForPresentedController:presentingController:sourceController:];
-[SBHUDController zStackParticipant:updatePreferences:];
-[SBHUDController succinctDescriptionBuilder];
-[SBHUDController settings];
-[SBHUDController dealloc];
-[SBHUDController zStackParticipantDidChange:];
-[SBHUDController descriptionWithMultilinePrefix:];
-[SBHUDController zStackParticipant:updateZOrderPreferences:];
-[SBHUDController settings:changedValueForKey:];
-[SBHUDController succinctDescription];
-[SBHUDController _setupStateCapture];
-[SBHUDController description];
-[SBHUDController _tearDown];
-[SBHUDController windowSceneDidConnect:];
-[SBHUDController windowScene];
-[SBHUDController descriptionBuilderWithMultilinePrefix:];
-[SBHUDController _dismissHUD:animated:];
-[SBHUDController _presentHUD:animated:];
-[SBHUDController HUDSessionForViewController:identifier:];
-[SBHUDController HUDWindow];
-[SBHUDController _createHUDWindowIfNeeded];
-[SBHUDController _finishedTransitionForHUD:intendedState:finalState:];
-[SBHUDController _hideWindowIfPossible];
-[SBHUDController _notificationFiredToDismissHUDs:];
-[SBHUDController acquireHUDHiddenAssertionForIdentifier:withReason:];
-[SBHUDController anyHUDsVisible];
-[SBHUDController dismissHUDs:];
-[SBHUDController hudViewController];
-[SBHUDController hudViewController:didDismissHUD:];
-[SBHUDController hudViewController:didPresentHUD:];
-[SBHUDController hudViewController:willDismissHUD:];
-[SBHUDController hudViewController:willPresentHUD:];
-[SBHUDController initWithWindowScene:hudCoordinator:];
-[SBHUDController knownHUDControllerForIdentifier:];
-[SBHUDController knownHUDs];
-[SBHUDController presentedHUDControllerForIdentifier:];
-[SBHUDController presentedHUDs];
-[SBHUDController presentingHUDs];
```
