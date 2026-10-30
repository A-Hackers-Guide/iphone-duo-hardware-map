# `SBScreenBrightnessHostComponent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `FBSceneComponent`, `_UISceneRenderingEnvironmentHostObserver`, `SBScreenBrightnessObserving`, `SBHostedScenePolicyHostComponentObserver`, `SBScreenBrightnessHost`
- 4 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _observingHostedScenePolicyHostComponent;
B _isActive;
B _updatesWithSanitizedBrightness;
@"SBScreenBrightnessParticipant" _participant;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBScreenBrightnessHostComponent sceneDidInvalidate:withContext:];
-[SBScreenBrightnessHostComponent deactivate];
-[SBScreenBrightnessHostComponent scene:willUpdateSettings:];
-[SBScreenBrightnessHostComponent sceneHostingPolicyHostComponentDidUpdateHostWindowScene:];
-[SBScreenBrightnessHostComponent _scene:didUpdatePreferredScreenBrightness:];
-[SBScreenBrightnessHostComponent _scene:didUpdatePrefersContentProtection:];
-[SBScreenBrightnessHostComponent _hostWindowScene];
-[SBScreenBrightnessHostComponent _observeHostedScenePolicyHostComponentIfNeeded];
-[SBScreenBrightnessHostComponent _updateParticipantForSettings:];
-[SBScreenBrightnessHostComponent _updateScreenBrightness:];
-[SBScreenBrightnessHostComponent activateWithSanitizedBrightnessUpdates:];
-[SBScreenBrightnessHostComponent brightnessDidChange:];
-[SBScreenBrightnessHostComponent sanitizedBrightnessDidChange:];
```
