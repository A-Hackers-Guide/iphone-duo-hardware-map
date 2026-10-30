# `BLSBacklightSceneUpdate`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
@? _sceneContentsUpdatedBlock;
@? _performBacklightRampBlock;
@? _sceneContentsAnimationCompleteBlock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_sceneContentsUpdated;
B _lock_didStartBacklightRamp;
B _lock_animationComplete;
B _isUpdateToDateSpecifier;
@"BLSBacklightSceneUpdateContext" _context;
@"<BLSBacklightSceneEnvironment_Private>" _environment;
```

## Properties

```
@property (TB,R,N,V_isUpdateToDateSpecifier) isUpdateToDateSpecifier;
@property (T@"<BLSBacklightSceneEnvironment_Private>",R,W,N,V_environment) environment;
@property (T@"BLSBacklightSceneUpdateContext",R,N,V_context) context;
@property (TB,R,N,GareSceneContentsUpdated) sceneContentsUpdated;
@property (TB,R,N) didStartBacklightRamp;
@property (TB,R,N,GisAnimationComplete) animationComplete;
```

## Instance methods

```
-[BLSBacklightSceneUpdate performBacklightRampWithDuration:];
-[BLSBacklightSceneUpdate debugDescription];
-[BLSBacklightSceneUpdate initForEnvironment:visualState:previousVisualState:frameSpecifier:animated:triggerEvent:touchTargetable:isUpdateToDateSpecifier:sceneContentsUpdated:performBacklightRamp:sceneContentsAnimationComplete:];
-[BLSBacklightSceneUpdate isUpdateToDateSpecifier];
-[BLSBacklightSceneUpdate didStartBacklightRamp];
-[BLSBacklightSceneUpdate sceneContentsDidUpdate];
-[BLSBacklightSceneUpdate sceneContentsAnimationDidComplete];
-[BLSBacklightSceneUpdate hash];
-[BLSBacklightSceneUpdate description];
-[BLSBacklightSceneUpdate areSceneContentsUpdated];
-[BLSBacklightSceneUpdate setReplacedSceneUpdate:];
-[BLSBacklightSceneUpdate isAnimationComplete];
-[BLSBacklightSceneUpdate context];
-[BLSBacklightSceneUpdate isEqual:];
-[BLSBacklightSceneUpdate environment];
```
