# `BKDirectTouchState`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`, `BSInvalidatable`
- 34 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"BKIOHIDService" _service;
@"NSString" _displayUUID;
@"BKHIDDirectTouchEventProcessor" _eventProcessor;
@"BKDirectTouchStateHitTester" _hitTester;
@"BSCompoundAssertion" _suppressTouchesAssertion;
@"BKDirectTouchPerDisplayInfo" _displayInfo;
@"<BKHIDEventHitTestDispatcher>" _dispatcher;
@"BKTouchDeliveryPolicyServer" _touchDeliveryPolicyServer;
@"BKTouchDeliveryObservationManager" _touchDeliveryObservationManager;
@"NSMutableArray" _touchLifecycleObservers;
@"BKTouchAnnotationController" _annotationController;
@"<BKHIDEventDeliveryManagerProviding>" _deliveryManagerProvider;
@"BKHIDEventDeliveryManager" _deliveryManager;
@"<BKOrientationProvider>" _orientationProvider;
d _initialTouchTimestamp;
q _activeModifiers;
@"BKTouchContactSet" _contacts;
@"BSMutableIntegerMap" _destinationsByTargetID;
@"BSMutableIntegerMap" _contactsByTargetID;
@"BSMutableIntegerMap" _centroidPerUserIdentifier;
@"NSMutableSet" _latentSystemGestureDestinations;
q _interfaceOrientation;
d _lastSystemGestureTouchTimestamp;
d _initialTouchStreamTouchTimestamp;
@"NSArray" _hitTestRegions;
@"BKDirectTouchUpdateEvents" _updateEvents;
d _maximumPositionZ;
f _maxForce;
B _determinedMaxForce;
B _supportsPreciseLocations;
B _displayIntegrated;
B _builtIn;
B _waitingForAllTouchesUp;
B _hoverDisabled;
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
-[BKDirectTouchState init];
-[BKDirectTouchState appendDescriptionToFormatter:];
-[BKDirectTouchState invalidate];
-[BKDirectTouchState description];
```
