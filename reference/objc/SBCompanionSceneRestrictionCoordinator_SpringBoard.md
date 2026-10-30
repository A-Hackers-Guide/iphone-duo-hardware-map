# `SBCompanionSceneRestrictionCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `BSInvalidatable`
- 2 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSMapTable" _presentationModeToRestrictorMap;
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
+[SBCompanionSceneRestrictionCoordinator _defaultCompanionScenePresentationModeToPossibleRestrictionsMap];
```

## Instance methods

```
-[SBCompanionSceneRestrictionCoordinator init];
-[SBCompanionSceneRestrictionCoordinator dealloc];
-[SBCompanionSceneRestrictionCoordinator invalidate];
-[SBCompanionSceneRestrictionCoordinator description];
-[SBCompanionSceneRestrictionCoordinator appendDescriptionToStream:];
-[SBCompanionSceneRestrictionCoordinator _currentRestrictionForPresentationMode:];
-[SBCompanionSceneRestrictionCoordinator _initWithPresentationModeToPossibleRestrictionsMapping:];
-[SBCompanionSceneRestrictionCoordinator acquireAssertionForPresentationRestriction:];
-[SBCompanionSceneRestrictionCoordinator addObserver:forPresentationModes:];
-[SBCompanionSceneRestrictionCoordinator isAnyPresentationModeRestricted:];
-[SBCompanionSceneRestrictionCoordinator isPresentationModeRestricted:];
-[SBCompanionSceneRestrictionCoordinator removeObserver:forPresentationModes:];
```
