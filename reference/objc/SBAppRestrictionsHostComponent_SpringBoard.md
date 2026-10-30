# `SBAppRestrictionsHostComponent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `FBSceneComponent`, `ALRFBScenePreflightObserver`, `SBSafeAreaResolverExtensionDelegate`
- 3 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"FBScene" _fbScene;
@"FBScene" _preflightScene;
@"SBDeviceApplicationSceneHandle" _preflightSceneHandle;
```

## Properties

```
@property (T@"SBDeviceApplicationSceneHandle",R,N,V_preflightSceneHandle) preflightSceneHandle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAppRestrictionsHostComponent scene:clientDidConnect:];
-[SBAppRestrictionsHostComponent shouldApplySafeAreaForScene:];
-[SBAppRestrictionsHostComponent sceneObserverWantsUpdatesFromInactiveScenes];
-[SBAppRestrictionsHostComponent scene:didUpdateSettings:];
-[SBAppRestrictionsHostComponent setScene:];
-[SBAppRestrictionsHostComponent preflightSceneHandle];
-[SBAppRestrictionsHostComponent invalidate];
-[SBAppRestrictionsHostComponent scene:updatedActivePreflightScene:];
-[SBAppRestrictionsHostComponent _configurePreflightSceneHandleIfNecessary];
```
