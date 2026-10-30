# `BLSHAssertionPausingSceneObserver`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHLocalAssertionAttributeHandlerEntry`, `FBSceneObserver`
- 7 instance variables, 7 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"FBScene" _scene;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _invalidated;
B _paused;
@"<BLSAssertionServiceResponding>" _assertion;
@"<BLSHAssertionAttributeHandlerService>" _service;
@"BLSPauseWhenSceneBackgroundAttribute" _attribute;
```

## Properties

```
@property (T@"BLSPauseWhenSceneBackgroundAttribute",R,W,N,V_attribute) attribute;
@property (T@"<BLSAssertionServiceResponding>",R,W,N,V_assertion) assertion;
@property (T@"<BLSHAssertionAttributeHandlerService>",R,W,N,V_service) service;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHAssertionPausingSceneObserver activateForAttribute:fromAssertion:forService:attributeHandler:];
```

## Instance methods

```
-[BLSHAssertionPausingSceneObserver assertion];
-[BLSHAssertionPausingSceneObserver dealloc];
-[BLSHAssertionPausingSceneObserver sceneDidInvalidate:];
-[BLSHAssertionPausingSceneObserver scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:];
-[BLSHAssertionPausingSceneObserver invalidate];
-[BLSHAssertionPausingSceneObserver service];
-[BLSHAssertionPausingSceneObserver attribute];
-[BLSHAssertionPausingSceneObserver reactivateIfPossible];
```
