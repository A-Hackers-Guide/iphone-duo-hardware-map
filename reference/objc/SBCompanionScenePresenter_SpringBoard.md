# `SBCompanionScenePresenter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `FBSSceneObserver`, `BSInvalidatable`, `SBCompanionScenePresenting`
- 12 instance variables, 19 properties, 41 instance methods, 3 class methods

## Instance variables

```
B _active;
B _valid;
@"SBWindowScene" _windowScene;
@"SBCompanionScenePresentation" _presentation;
@"NSHashTable" _observers;
@"TRAParticipant" _traitsParticipant;
@"SBTraitsSceneParticipantDelegate" _traitsSceneParticipantDelegate;
@"SBTraitsSingleSceneWindow" _hostingWindow;
@"NSMutableOrderedSet" _viewControllers;
@"<BSInvalidatable>" _stateCaptureAssertion;
@"<BSInvalidatable>" _subduedGlassAssertion;
@"SBCompanionSceneRestrictionCoordinator" _restrictionCoordinator;
```

## Properties

```
@property (TB,N,GisValid,V_valid) valid;
@property (T@"NSHashTable",R,N,V_observers) observers;
@property (T@"TRAParticipant",R,N,V_traitsParticipant) traitsParticipant;
@property (T@"SBTraitsSceneParticipantDelegate",R,N,V_traitsSceneParticipantDelegate) traitsSceneParticipantDelegate;
@property (T@"SBTraitsSingleSceneWindow",R,N,V_hostingWindow) hostingWindow;
@property (T@"NSMutableOrderedSet",&,N,V_viewControllers) viewControllers;
@property (T@"<BSInvalidatable>",&,N,V_stateCaptureAssertion) stateCaptureAssertion;
@property (T@"<BSInvalidatable>",&,N,V_subduedGlassAssertion) subduedGlassAssertion;
@property (T@"SBCompanionSceneRestrictionCoordinator",R,N,V_restrictionCoordinator) restrictionCoordinator;
@property (T@"NSSet",C,N) availableCompanionModes;
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (TB,N,GisActive,V_active) active;
@property (T@"SBCompanionScenePresentation",R,N,V_presentation) presentation;
@property (TB,R,N) isHostingCompanionScene;
@property (TB,R,N) ignoresOrientationLock;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBCompanionScenePresenter defaultLifecycleConstraints];
+[SBCompanionScenePresenter defaultSupportedOrientations];
+[SBCompanionScenePresenter presenterWithWindowScene:restrictionCoordinator:sensorActivityDataProvider:];
```

## Instance methods

```
-[SBCompanionScenePresenter presentation];
-[SBCompanionScenePresenter removeObserver:];
-[SBCompanionScenePresenter scene:didUpdateSettings:];
-[SBCompanionScenePresenter dealloc];
-[SBCompanionScenePresenter setValid:];
-[SBCompanionScenePresenter setActive:];
-[SBCompanionScenePresenter addObserver:];
-[SBCompanionScenePresenter invalidate];
-[SBCompanionScenePresenter setViewControllers:];
-[SBCompanionScenePresenter hostingWindow];
-[SBCompanionScenePresenter isValid];
-[SBCompanionScenePresenter description];
-[SBCompanionScenePresenter appendDescriptionToStream:];
-[SBCompanionScenePresenter viewControllers];
-[SBCompanionScenePresenter observers];
-[SBCompanionScenePresenter isActive];
-[SBCompanionScenePresenter windowScene];
-[SBCompanionScenePresenter traitsParticipant];
-[SBCompanionScenePresenter _enumerateObservers:];
-[SBCompanionScenePresenter _notifyObserversOfHostingChange];
-[SBCompanionScenePresenter _currentCompanionSceneViewController];
-[SBCompanionScenePresenter _initWithPresentationIdentifier:windowScene:supportedModes:restrictionCoordinator:lifecycleConstraints:];
-[SBCompanionScenePresenter _makeHostingWindow];
-[SBCompanionScenePresenter _presentCompanionSceneViewController:];
-[SBCompanionScenePresenter _updateAvailableCompanionModesForActive:];
-[SBCompanionScenePresenter _updateHostWindowHidden:];
-[SBCompanionScenePresenter _updateTraitsSceneParticipantDelegateForScene:];
-[SBCompanionScenePresenter _viewControllerForCompanionSceneIdentityToken:];
-[SBCompanionScenePresenter availableCompanionModes];
-[SBCompanionScenePresenter ignoresOrientationLock];
-[SBCompanionScenePresenter isHostingCompanionScene];
-[SBCompanionScenePresenter presentation:requestsDismissalForCompanionScene:completion:];
-[SBCompanionScenePresenter presentation:requestsPresentationForCompanionScene:completion:];
-[SBCompanionScenePresenter restrictionCoordinator];
-[SBCompanionScenePresenter setAvailableCompanionModes:];
-[SBCompanionScenePresenter setStateCaptureAssertion:];
-[SBCompanionScenePresenter setSubduedGlassAssertion:];
-[SBCompanionScenePresenter stateCaptureAssertion];
-[SBCompanionScenePresenter subduedGlassAssertion];
-[SBCompanionScenePresenter supportedOrientationsForClientHandle:];
-[SBCompanionScenePresenter traitsSceneParticipantDelegate];
```
