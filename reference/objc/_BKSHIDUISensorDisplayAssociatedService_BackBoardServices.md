# `_BKSHIDUISensorDisplayAssociatedService`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `BKSHIDUISensorInternalServicing`
- 7 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"_BKSHIDUISensorOverseer" _overseer;
@"NSString" _displayUUID;
@"BSCompoundAssertion" _modeAssertion;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
q _lock_externalReferenceCount;
@"BKSHIDUISensorMode" _lock_prevailingMode;
@"BKSHIDUISensorCharacteristics" _lock_characteristics;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"BKSHIDUISensorCharacteristics",R,N) sensorCharacteristics;
```

## Instance methods

```
-[_BKSHIDUISensorDisplayAssociatedService dealloc];
-[_BKSHIDUISensorDisplayAssociatedService appendDescriptionToStream:];
-[_BKSHIDUISensorDisplayAssociatedService acquireTransactionForReason:];
-[_BKSHIDUISensorDisplayAssociatedService proximityDidUnoccludeAfterWake];
-[_BKSHIDUISensorDisplayAssociatedService recalibrateProximitySensor];
-[_BKSHIDUISensorDisplayAssociatedService requestEstimatedProximityEventWithTimeout:];
-[_BKSHIDUISensorDisplayAssociatedService requestProximityDetectionMode:];
-[_BKSHIDUISensorDisplayAssociatedService requestProximityStatusEventForReason:];
-[_BKSHIDUISensorDisplayAssociatedService requestUISensorMode:];
-[_BKSHIDUISensorDisplayAssociatedService sensorCharacteristics];
-[_BKSHIDUISensorDisplayAssociatedService suppressUISensorChangesForReason:];
```
