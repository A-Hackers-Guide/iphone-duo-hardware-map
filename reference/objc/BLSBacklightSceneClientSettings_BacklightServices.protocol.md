# `BLSBacklightSceneClientSettings` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 7 properties, 7 instance methods, 0 class methods

## Properties

```
@property (TB,R,N) bls_hasDelegate;
@property (TB,R,N) bls_supportsAlwaysOn;
@property (TB,R,N) bls_alwaysOnContentIs1hz;
@property (TB,R,N) bls_optsOutOfProcessAssertions;
@property (TB,R,N) bls_needsFlipbookStateUpdates;
@property (TB,R,N) bls_supportsLowPowerRendering;
@property (TB,R,N) bls_needsLowPowerRenderingStateUpdates;
```

## Instance methods

```
-[BLSBacklightSceneClientSettings bls_hasDelegate];
-[BLSBacklightSceneClientSettings bls_alwaysOnContentIs1hz];
-[BLSBacklightSceneClientSettings bls_needsFlipbookStateUpdates];
-[BLSBacklightSceneClientSettings bls_needsLowPowerRenderingStateUpdates];
-[BLSBacklightSceneClientSettings bls_optsOutOfProcessAssertions];
-[BLSBacklightSceneClientSettings bls_supportsAlwaysOn];
-[BLSBacklightSceneClientSettings bls_supportsLowPowerRendering];
```
