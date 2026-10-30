# `SBNonInteractiveDisplayController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBLastInteractedSceneObserver`, `FBSceneDelegate`, `FBSSceneObserver`, `SBCompanionScenePresenting`, `SBNonInteractivePresentationObserver`, `BSInvalidatable`
- 12 instance variables, 9 properties, 26 instance methods, 3 class methods

## Instance variables

```
B _isPerAppSecondDisplayControlling;
@"FBSceneWorkspace" _sceneWorkspace;
@"SBNonInteractivePresentation" _currentPresentation;
@"SBNonInteractiveDisplayPreferences" _currentDisplayPreferences;
@"FBSScene" _hostingScene;
@"FBSDisplayConfiguration" _hostingSceneDisplayConfiguration;
i _hostingSceneDisplayIdentityPid;
@"<SBLastInteractedSceneProviding>" _lastInteractedSceneProvider;
@"<SBNonInteractiveDisplayControllerDelegate>" _delegate;
@"<BSInvalidatable>" _stateCaptureAssertion;
B _companionScenesEnabled;
@"SBCompanionScenePresentation" _companionScenePresentation;
```

## Properties

```
@property (T@"SBNonInteractivePresentation",R,N,G_currentPresentation,V_currentPresentation) currentPresentation;
@property (T@"SBNonInteractiveDisplayPreferences",R,N,G_currentDisplayPreferences) currentDisplayPreferences;
@property (TB,R,N,G_isPerAppSecondDisplayControlling) perAppSecondDisplayControlling;
@property (T@"SBCompanionScenePresentation",R,N,G_companionScenePresentation) companionScenePresentation;
@property (TB,R,N) isRenderingContent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBNonInteractiveDisplayController _defaultDisplayConfigurationRequest];
+[SBNonInteractiveDisplayController _pidForScene:];
+[SBNonInteractiveDisplayController _sceneIdentifierForHostScene:displayIdentity:];
```

## Instance methods

```
-[SBNonInteractiveDisplayController sceneDidDeactivate:withContext:];
-[SBNonInteractiveDisplayController sceneDidInvalidate:withContext:];
-[SBNonInteractiveDisplayController scene:didUpdateSettings:];
-[SBNonInteractiveDisplayController dealloc];
-[SBNonInteractiveDisplayController invalidate];
-[SBNonInteractiveDisplayController description];
-[SBNonInteractiveDisplayController appendDescriptionToStream:];
-[SBNonInteractiveDisplayController lastInteractedSceneProvider:didUpdateLastInteractedScene:];
-[SBNonInteractiveDisplayController isRenderingContent];
-[SBNonInteractiveDisplayController _companionScenePresentation];
-[SBNonInteractiveDisplayController _configurationInitialSceneParameters:deactivationReasons:companionScene:];
-[SBNonInteractiveDisplayController _createNonInteractiveSceneForEligibleScene:withDeactivationReasons:];
-[SBNonInteractiveDisplayController _currentDisplayPreferences];
-[SBNonInteractiveDisplayController _currentNonInteractiveScene];
-[SBNonInteractiveDisplayController _currentPresentation];
-[SBNonInteractiveDisplayController _hostPresentation:];
-[SBNonInteractiveDisplayController _initWithHostingScene:companionScenesEnabled:companionSceneRestrictionCoordinator:displayIdentityPid:lastInteractedSceneProvider:delegate:];
-[SBNonInteractiveDisplayController _isPerAppSecondDisplayControlling];
-[SBNonInteractiveDisplayController _unhostCurrentPresentation];
-[SBNonInteractiveDisplayController _updateCurrentNonInteractiveSceneForEligibleScene:];
-[SBNonInteractiveDisplayController _updateDisplayPreferences:];
-[SBNonInteractiveDisplayController initWithHostingScene:companionSceneRestrictionCoordinator:lastInteractedSceneProvider:delegate:];
-[SBNonInteractiveDisplayController nonInteractivePresentation:didUpdateDisplayPreferences:];
-[SBNonInteractiveDisplayController nonInteractivePresentation:didUpdateWantsControlOfDisplay:];
-[SBNonInteractiveDisplayController presentation:requestsDismissalForCompanionScene:completion:];
-[SBNonInteractiveDisplayController presentation:requestsPresentationForCompanionScene:completion:];
```
