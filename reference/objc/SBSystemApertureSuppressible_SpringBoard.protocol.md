# `SBSystemApertureSuppressible` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 1 properties, 16 instance methods, 0 class methods

## Properties

```
@property (TB,?,N,GisSuppressed) suppressed;
```

## Instance methods

```
-[SBSystemApertureSuppressible isSuppressed];
-[SBSystemApertureSuppressible acceptsFullScreenTransitionFromSceneWithIdentifier:ofBundleId:];
-[SBSystemApertureSuppressible shouldSuppressElementWhilePresentingSceneWithIdentifier:];
-[SBSystemApertureSuppressible shouldSuppressElementWhileOnContinuityDisplay];
-[SBSystemApertureSuppressible setSuppressed:];
-[SBSystemApertureSuppressible shouldSuppressElementWhileProximityReaderPresent];
-[SBSystemApertureSuppressible requiresSuppressionFromSystemAperture];
-[SBSystemApertureSuppressible shouldIgnoreSystemChromeSuppressionWhilePresentingAppWithBundleId:];
-[SBSystemApertureSuppressible suppressForReason:];
-[SBSystemApertureSuppressible shouldSuppressElementWhilePresentingAppWithBundleId:];
-[SBSystemApertureSuppressible shouldSuppressElementWhilePresentingNoAppsOrScenes];
-[SBSystemApertureSuppressible shouldSuppressElementWhileOverLiquidDetectionCriticalUI];
-[SBSystemApertureSuppressible shouldSuppressElementWhileOnCoversheet];
-[SBSystemApertureSuppressible shouldSuppressElementWhileOtherElementsPresent];
-[SBSystemApertureSuppressible shouldIgnoreSystemChromeSuppression];
-[SBSystemApertureSuppressible shouldSuppressElementWhileOnAuxiliaryContentCompanionScene];
```
