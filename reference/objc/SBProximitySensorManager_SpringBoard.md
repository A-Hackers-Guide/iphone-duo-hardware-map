# `SBProximitySensorManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBUIActiveOrientationObserver`
- 14 instance variables, 9 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _windowScene;
@"NSMutableSet" _clientsWantingDetectionEnabled;
@"NSMutableSet" _clientsWantingGracePeriodDisabled;
@"<SBProximitySensorControlling>" _hidInterface;
@"SBHardwareDefaults" _hardwareDefaults;
@"NSHashTable" _observers;
@"BSCompoundAssertion" _suppressBacklightChangesAssertion;
i _proximityDetectionMode;
B _proximityDetectionEnabled;
B _proximityDetectionPermitted;
B _objectInProximity;
B _objectInCrudeProximity;
i _backboardNotificationToken;
@"SpringBoard" _interfaceOrientationProvider;
```

## Properties

```
@property (TB,N,GisProximityDetectionEnabled,S_setProximityDetectionEnabled:,V_proximityDetectionEnabled) proximityDetectionEnabled;
@property (TB,N,GisProximityDetectionPermitted,S_setProximityDetectionPermitted:,V_proximityDetectionPermitted) proximityDetectionPermitted;
@property (T@"SpringBoard",&,N,G_interfaceOrientationProvider,S_setInterfaceOrientationProvider:,V_interfaceOrientationProvider) interfaceOrientationProvider;
@property (TB,R,N,GisObjectInProximity,V_objectInProximity) objectInProximity;
@property (TB,R,N,GisGracePeriodDisabled) gracePeriodDisabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBProximitySensorManager activeInterfaceOrientationDidChangeToOrientation:willAnimateWithDuration:fromOrientation:];
-[SBProximitySensorManager removeObserver:];
-[SBProximitySensorManager init];
-[SBProximitySensorManager dealloc];
-[SBProximitySensorManager activeInterfaceOrientationWillChangeToOrientation:];
-[SBProximitySensorManager addObserver:];
-[SBProximitySensorManager description];
-[SBProximitySensorManager isObjectInProximity];
-[SBProximitySensorManager _setObjectInProximity:detectionMode:];
-[SBProximitySensorManager _reloadDefaults];
-[SBProximitySensorManager _clientsWantDetectionEnabled];
-[SBProximitySensorManager _destroy];
-[SBProximitySensorManager _disableProx];
-[SBProximitySensorManager _enableProx];
-[SBProximitySensorManager _interfaceOrientationProvider];
-[SBProximitySensorManager _setInterfaceOrientationProvider:];
-[SBProximitySensorManager _setObjectInCrudeProximity:];
-[SBProximitySensorManager _setObjectInProximity:detectionMode:postToApps:];
-[SBProximitySensorManager _setProximityDetectionEnabled:];
-[SBProximitySensorManager _setProximityDetectionPermitted:];
-[SBProximitySensorManager _updateProxState];
-[SBProximitySensorManager client:wantsProximityDetectionEnabled:];
-[SBProximitySensorManager client:wantsProximityDetectionEnabled:disableGracePeriod:];
-[SBProximitySensorManager initWithHIDInterface:hardwareDefaults:interfaceOrientationProvider:windowScene:];
-[SBProximitySensorManager isGracePeriodDisabled];
-[SBProximitySensorManager isProximityDetectionEnabled];
-[SBProximitySensorManager isProximityDetectionPermitted];
-[SBProximitySensorManager processHIDEvent:];
-[SBProximitySensorManager resetProximityCalibration];
-[SBProximitySensorManager suppressBacklightChangesForReason:];
```
