# `BLSBacklightSceneSettings` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 8 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,Gbls_isDelegateActive) bls_delegateActive;
@property (T@"BLSBacklightSceneVisualState",R,N) bls_visualState;
@property (T@"NSDate",R,N) bls_presentationDate;
@property (TB,R,N,Gbls_isAlwaysOnEnabledForEnvironment) bls_alwaysOnEnabledForEnvironment;
@property (TQ,R,N) bls_renderSeed;
@property (TB,R,N,Gbls_isLiveUpdating) bls_liveUpdating;
@property (TB,R,N,Gbls_hasUnrestrictedFramerateUpdates) bls_unrestrictedFramerateUpdates;
@property (TQ,R,N) bls_lowPowerRenderingPresentationTime;
```

## Instance methods

```
-[BLSBacklightSceneSettings bls_visualState];
-[BLSBacklightSceneSettings bls_hasUnrestrictedFramerateUpdates];
-[BLSBacklightSceneSettings bls_isAlwaysOnEnabledForEnvironment];
-[BLSBacklightSceneSettings bls_isDelegateActive];
-[BLSBacklightSceneSettings bls_isLiveUpdating];
-[BLSBacklightSceneSettings bls_presentationDate];
-[BLSBacklightSceneSettings bls_lowPowerRenderingPresentationTime];
-[BLSBacklightSceneSettings bls_renderSeed];
```
