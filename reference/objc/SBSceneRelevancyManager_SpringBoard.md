# `SBSceneRelevancyManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 3 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"SBSceneRelevancySettings" _settings;
@"<SBSceneRelevancyResolving>" _resolver;
@"NSMapTable" _sceneIdentifierToScore;
@"<BSInvalidatable>" _stateCaptureInvalidatable;
q _firstMaximizedSceneZOrder;
@"NSArray" _zOrderedDeviceApplicationSceneEntities;
@"NSMapTable" _deviceApplicationSceneEntitiesToOcclusionStates;
```

## Properties

```
@property (TQ,R,N) maximumNumberOfVisibleScenesOnStage;
@property (T@"NSArray",R,C,N,V_zOrderedDeviceApplicationSceneEntities) zOrderedDeviceApplicationSceneEntities;
@property (T@"NSMapTable",R,C,N,V_deviceApplicationSceneEntitiesToOcclusionStates) deviceApplicationSceneEntitiesToOcclusionStates;
```

## Instance methods

```
-[SBSceneRelevancyManager dealloc];
-[SBSceneRelevancyManager descriptionWithMultilinePrefix:];
-[SBSceneRelevancyManager description];
-[SBSceneRelevancyManager descriptionBuilderWithMultilinePrefix:];
-[SBSceneRelevancyManager _addStateCaptureHandler];
-[SBSceneRelevancyManager _computeScoreForSceneIdentifier:];
-[SBSceneRelevancyManager configureWithZOrderedDeviceApplicationSceneEntities:deviceApplicationSceneEntitiesToOcclusionStates:firstMaximizedDeviceApplicationSceneEntity:isStageInPeek:];
-[SBSceneRelevancyManager deviceApplicationSceneEntitiesToOcclusionStates];
-[SBSceneRelevancyManager effectForSceneIdentifier:];
-[SBSceneRelevancyManager initWithSceneRelevancySettings:resolver:];
-[SBSceneRelevancyManager maximumNumberOfVisibleScenesOnStage];
-[SBSceneRelevancyManager scoreForSceneIdentifier:];
-[SBSceneRelevancyManager shouldFreezeSceneEntity:];
-[SBSceneRelevancyManager zOrderedDeviceApplicationSceneEntities];
```
