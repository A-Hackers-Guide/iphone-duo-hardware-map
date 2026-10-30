# `SBCompanionScenePresentation`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `BSDescriptionStreaming`, `SBCompanionSceneRestrictionCoordinatorObserver`, `BSInvalidatable`
- 8 instance variables, 9 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"<SBCompanionScenePresenting>" _presenter;
@"SBCompanionSceneRestrictionCoordinator" _restrictionCoordinator;
@"NSSet" _availableModes;
@"NSMutableSet" _hostScenes;
@"<BSInvalidatable>" _stateCaptureAssertion;
@"NSString" _identifier;
@"NSSet" _supportedModes;
@"SBCompanionScenePresentationContext" _context;
```

## Properties

```
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T@"NSSet",R,C,N,V_supportedModes) supportedModes;
@property (T@"NSSet",C,N) availableModes;
@property (T@"NSSet",R,N) restrictedModes;
@property (T@"SBCompanionScenePresentationContext",C,N,V_context) context;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBCompanionScenePresentation availableModes];
-[SBCompanionScenePresentation identifier];
-[SBCompanionScenePresentation supportedModes];
-[SBCompanionScenePresentation invalidate];
-[SBCompanionScenePresentation setContext:];
-[SBCompanionScenePresentation hash];
-[SBCompanionScenePresentation description];
-[SBCompanionScenePresentation appendDescriptionToStream:];
-[SBCompanionScenePresentation copyWithZone:];
-[SBCompanionScenePresentation context];
-[SBCompanionScenePresentation restrictedModes];
-[SBCompanionScenePresentation updateContextWithSceneSettings:];
-[SBCompanionScenePresentation _isHostSceneRegistered:];
-[SBCompanionScenePresentation _iterateAllHostedSceneCompanionSceneHostComponents:];
-[SBCompanionScenePresentation _notifyCompanionSceneCreation:];
-[SBCompanionScenePresentation _notifyObserversForPresentationRestrictionUpdates];
-[SBCompanionScenePresentation _registerHostScene:];
-[SBCompanionScenePresentation _requestDismissalForCompanionScene:completion:];
-[SBCompanionScenePresentation _requestPresentationForCompanionScene:completion:];
-[SBCompanionScenePresentation _unregisterHostScene:];
-[SBCompanionScenePresentation _willRequestDismissalForCompanionScene:];
-[SBCompanionScenePresentation companionSceneRestrictionCoordinator:didBeginRestrictingPresentationMode:];
-[SBCompanionScenePresentation companionSceneRestrictionCoordinator:didEndRestrictingPresentationMode:];
-[SBCompanionScenePresentation initWithIdentifier:presenter:supportedModes:availableModes:restrictionCoordinator:context:];
-[SBCompanionScenePresentation registerHostScene:];
-[SBCompanionScenePresentation registeredHostScenes];
-[SBCompanionScenePresentation setAvailableModes:];
-[SBCompanionScenePresentation unregisterHostScene:];
-[SBCompanionScenePresentation updateContextWithLifecycleConstraints:];
```
