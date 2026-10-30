# `SBCompanionSceneHostComponent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `BSDescriptionStreaming`, `_UICompanionSceneInterestHostObserver`, `_UICompanionContainerSceneHostObserver`, `FBSceneComponent`, `SBCompanionSceneHost`
- 6 instance variables, 4 properties, 34 instance methods, 3 class methods

## Instance variables

```
@"NSMutableSet" _lock_registeredPresentations;
@"NSSet" _lock_interestedPresentationModes;
@"NSMapTable" _lock_activePresentationToCompanionSceneMap;
B _isLockInitialized;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"<BSInvalidatable>" _stateCaptureAssertion;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBCompanionSceneHostComponent _companionSceneIdentifierForHostScene:presentation:];
+[SBCompanionSceneHostComponent _setCompanionScenePresentationManager:];
+[SBCompanionSceneHostComponent _setSceneWorkspace:];
```

## Instance methods

```
-[SBCompanionSceneHostComponent registerPresentation:];
-[SBCompanionSceneHostComponent scene:clientDidConnect:];
-[SBCompanionSceneHostComponent sceneDidInvalidate:withContext:];
-[SBCompanionSceneHostComponent companionScenes];
-[SBCompanionSceneHostComponent _lock_companionScenes];
-[SBCompanionSceneHostComponent sceneDidActivate:];
-[SBCompanionSceneHostComponent setScene:];
-[SBCompanionSceneHostComponent _updateCompanionScenesForInterestedModes:registeredPresentations:update:];
-[SBCompanionSceneHostComponent _hostScene:didInvalidateWithContext:];
-[SBCompanionSceneHostComponent _presentation:interestedModes:isConstrainedBySceneUpdate:];
-[SBCompanionSceneHostComponent _companionSceneClientConnected:];
-[SBCompanionSceneHostComponent _companionSceneAttributesForCompanionScenePresentationMode:];
-[SBCompanionSceneHostComponent scene:willUpdateSettings:];
-[SBCompanionSceneHostComponent _scene:didUpdateInterestedAttributes:];
-[SBCompanionSceneHostComponent _unregisterAllPresentations];
-[SBCompanionSceneHostComponent invalidate];
-[SBCompanionSceneHostComponent _updateCompanionScenesForInterestedModes:registeredPresentations:];
-[SBCompanionSceneHostComponent _companionSceneForPresentation:];
-[SBCompanionSceneHostComponent _requestDismissalForCompanionScene:ofPresentation:invalidateCompanionScene:];
-[SBCompanionSceneHostComponent _anyRegisteredPresentationsMayBeConstrainedByUpdate:];
-[SBCompanionSceneHostComponent _unregisterPresentations:];
-[SBCompanionSceneHostComponent _presentationDidUpdate:];
-[SBCompanionSceneHostComponent description];
-[SBCompanionSceneHostComponent appendDescriptionToStream:];
-[SBCompanionSceneHostComponent registeredPresentations];
-[SBCompanionSceneHostComponent unregisterPresentation:];
-[SBCompanionSceneHostComponent _companionScenePresentationModeForCompanionSceneAttributes:];
-[SBCompanionSceneHostComponent _presentationInvalidated:];
-[SBCompanionSceneHostComponent _lock_presentationForCompanionScene:];
-[SBCompanionSceneHostComponent _updateInterestedPresentationModes:];
-[SBCompanionSceneHostComponent _interestedPresentationModesForScene:];
-[SBCompanionSceneHostComponent _scene:didUpdateClientRenderingContent:];
-[SBCompanionSceneHostComponent _availableCompanionSceneAttributesForPresentation:];
-[SBCompanionSceneHostComponent _companionScene:didInvalidateWithContext:];
```
