# `SBProximitySensorCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBProximitySensorManagerObserver`, `SBWindowSceneAttachmentObserving`
- 2 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _connectedWindowScenes;
@"NSHashTable" _observers;
```

## Properties

```
@property (TB,R,N,GisObjectInProximity) objectInProximity;
@property (TB,R,N,GisProximityDetectionEnabled) proximityDetectionEnabled;
@property (TB,R,N,GisProximityDetectionPermitted) proximityDetectionPermitted;
@property (TB,R,N,GisGracePeriodDisabled) gracePeriodDisabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBProximitySensorCoordinator removeObserver:];
-[SBProximitySensorCoordinator init];
-[SBProximitySensorCoordinator windowSceneDidDisconnect:];
-[SBProximitySensorCoordinator addObserver:];
-[SBProximitySensorCoordinator windowSceneDidConnect:];
-[SBProximitySensorCoordinator isObjectInProximity];
-[SBProximitySensorCoordinator _notifyObserversEverythingMayHaveChanged];
-[SBProximitySensorCoordinator _proximityEventForDisplay:appliesToWindowScene:];
-[SBProximitySensorCoordinator isGracePeriodDisabled];
-[SBProximitySensorCoordinator isProximityDetectionEnabled];
-[SBProximitySensorCoordinator isProximityDetectionPermitted];
-[SBProximitySensorCoordinator processHIDEvent:];
-[SBProximitySensorCoordinator proximitySensorManager:objectWithinProximityDidChange:];
-[SBProximitySensorCoordinator proximitySensorManager:proximityDetectionEnabledDidChange:];
-[SBProximitySensorCoordinator proximitySensorManager:proximityDetectionPermittedDidChange:];
-[SBProximitySensorCoordinator resetProximityCalibration];
```
