# `SBSystemApertureProximityBacklightPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBDefaultProximityBacklightPolicy`
- Protocols: `_SBSystemApertureProximityTouchHandlingViewDelegate`
- 13 instance variables, 7 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"SBHIDUISensorModeController" _sensorModeController;
@"<BSInvalidatable>" _suppressSystemGestures;
@"UIView" _touchTrackingView;
@"UIView" _touchBlockingView;
Q _numberOfTouchesWhileObjectInProximity;
@"NSTimer" _touchAllowanceGracePeriodTimer;
B _objectThatCanPreventTouchesInProximity;
B _objectInProximityAccordingToProxManager;
B _isTrackingTouchPossiblyInJindoWithObjectInProximity;
B _suppressBacklightChanges;
B _systemApertureBacklightPolicy;
@"<SBSystemApertureProximityBacklightPolicyDelegate>" _delegate;
@"SBProximitySettings" _proximitySettings;
```

## Properties

```
@property (T@"SBProximitySettings",&,N,G_proximitySettings,S_setProximitySettings:,V_proximitySettings) proximitySettings;
@property (T@"<SBSystemApertureProximityBacklightPolicyDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisSystemApertureBacklightPolicy,V_systemApertureBacklightPolicy) systemApertureBacklightPolicy;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemApertureProximityBacklightPolicy dealloc];
-[SBSystemApertureProximityBacklightPolicy initWithConfiguration:];
-[SBSystemApertureProximityBacklightPolicy setDelegate:];
-[SBSystemApertureProximityBacklightPolicy delegate];
-[SBSystemApertureProximityBacklightPolicy isSystemApertureBacklightPolicy];
-[SBSystemApertureProximityBacklightPolicy _isGracePeriodDisabledByEntitledApp];
-[SBSystemApertureProximityBacklightPolicy _nontelephonyTouchAllowanceGracePeriod];
-[SBSystemApertureProximityBacklightPolicy _objectThatCanPreventTouchesWithinProximityDidChange:fromGracePeriod:];
-[SBSystemApertureProximityBacklightPolicy _proximitySettings];
-[SBSystemApertureProximityBacklightPolicy _scheduleBacklightFactorToZeroForTouchWithinSystemAperture];
-[SBSystemApertureProximityBacklightPolicy _setProximitySettings:];
-[SBSystemApertureProximityBacklightPolicy _startCancelingTouches];
-[SBSystemApertureProximityBacklightPolicy _stopCancelingTouches];
-[SBSystemApertureProximityBacklightPolicy didHitAllowedRegion:];
-[SBSystemApertureProximityBacklightPolicy proximityBacklightPolicyTouchHandlingView:shouldConsumeTouchForHitTest:withEvent:];
-[SBSystemApertureProximityBacklightPolicy proximitySensorManager:objectWithinProximityDidChange:];
-[SBSystemApertureProximityBacklightPolicy proximitySensorManager:objectWithinProximityDidChange:detectionMode:];
-[SBSystemApertureProximityBacklightPolicy proximitySensorManager:shouldSuppressBacklightChanges:];
-[SBSystemApertureProximityBacklightPolicy setSystemApertureBacklightPolicy:];
```
