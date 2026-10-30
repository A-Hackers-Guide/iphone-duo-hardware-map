# `BLSHEngineRenderFlipbookSessionDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `BLSHFlipbookPowerSavingProviding`
- 0 instance variables, 2 properties, 5 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisUsingPseudoFlipbook) usePseudoFlipbook;
@property (TB,R,N,GflipbookUsesLowPowerRendering) flipbookUsesLowPowerRendering;
```

## Instance methods

```
-[BLSHEngineRenderFlipbookSessionDelegate flipbookUsesLowPowerRendering];
-[BLSHEngineRenderFlipbookSessionDelegate renderFramesSession:beganRenderingSpecifier:timedOutEnvironments:];
-[BLSHEngineRenderFlipbookSessionDelegate renderFramesSession:failedToRenderSpecifier:error:timedOutEnvironments:];
-[BLSHEngineRenderFlipbookSessionDelegate isUsingPseudoFlipbook];
-[BLSHEngineRenderFlipbookSessionDelegate renderFramesSession:didRenderFrame:timedOutEnvironments:];
```
