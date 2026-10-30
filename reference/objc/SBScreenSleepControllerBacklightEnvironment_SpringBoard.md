# `SBScreenSleepControllerBacklightEnvironment`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BLSHBaseSceneHostEnvironment`
- 4 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"SBScreenSleepController" _screenSleepController;
@"NSUUID" _uuid;
@"SBAlwaysOnDefaults" _alwaysOnDefaults;
@"SBAveragePixelLuminanceLimitController" _aplLimitController;
```

## Instance methods

```
-[SBScreenSleepControllerBacklightEnvironment requestDateSpecifiersForDateInterval:previousPresentationDate:shouldReset:completion:];
-[SBScreenSleepControllerBacklightEnvironment requestedFidelityForInactiveContentWithCompletion:];
-[SBScreenSleepControllerBacklightEnvironment _useAlwaysOnBrightnessCurve:withRampDuration:];
-[SBScreenSleepControllerBacklightEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:];
-[SBScreenSleepControllerBacklightEnvironment clientSupportsAlwaysOn];
-[SBScreenSleepControllerBacklightEnvironment initWithScreenSleepController:];
```
