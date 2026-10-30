# `CAFRouteSharing`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 25 properties, 46 instance methods, 2 class methods

## Properties

```
@property (T@"CAFBoolCharacteristic",R,N) applicationEnabledCharacteristic;
@property (T@"CAFSharingStateCharacteristic",R,N) sharingStateCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) userEnabledCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) vehicleEnabledCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleReasonCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) identifierCharacteristic;
@property (T@"CAFRouteLegsCharacteristic",R,N) legsCharacteristic;
@property (T@"CAFUInt32Characteristic",R,N) currentLegIndexCharacteristic;
@property (TB,N) applicationEnabled;
@property (TB,R,N) applicationEnabledInvalid;
@property (TC,N) sharingState;
@property (TB,N) userEnabled;
@property (TB,R,N) userEnabledInvalid;
@property (TB,R,N) vehicleEnabled;
@property (T@"NSString",R,N) userVisibleReason;
@property (T@"NSString",C,N) identifier;
@property (TB,R,N) hasIdentifier;
@property (TB,R,N) identifierInvalid;
@property (T@"CAFRouteLegs",C,N) legs;
@property (TB,R,N) hasLegs;
@property (TB,R,N) legsInvalid;
@property (TI,N) currentLegIndex;
@property (T@"CAFUInt32Range",R,N) currentLegIndexRange;
@property (TB,R,N) hasCurrentLegIndex;
@property (TB,R,N) currentLegIndexInvalid;
```

## Class methods

```
+[CAFRouteSharing serviceIdentifier];
+[CAFRouteSharing observerProtocol];
```

## Instance methods

```
-[CAFRouteSharing identifier];
-[CAFRouteSharing legs];
-[CAFRouteSharing removeObserver:];
-[CAFRouteSharing hasIdentifier];
-[CAFRouteSharing setUserEnabled:];
-[CAFRouteSharing addObserver:];
-[CAFRouteSharing setIdentifier:];
-[CAFRouteSharing registerObserver:];
-[CAFRouteSharing setLegs:];
-[CAFRouteSharing name];
-[CAFRouteSharing unregisterObserver:];
-[CAFRouteSharing userEnabled];
-[CAFRouteSharing currentLegIndex];
-[CAFRouteSharing setCurrentLegIndex:];
-[CAFRouteSharing applicationEnabled];
-[CAFRouteSharing setApplicationEnabled:];
-[CAFRouteSharing setCurrentLegIndexInvalid];
-[CAFRouteSharing setSharingState:];
-[CAFRouteSharing vehicleEnabled];
-[CAFRouteSharing registeredForApplicationEnabled];
-[CAFRouteSharing hasCurrentLegIndex];
-[CAFRouteSharing registeredForCurrentLegIndex];
-[CAFRouteSharing registeredForIdentifier];
-[CAFRouteSharing registeredForLegs];
-[CAFRouteSharing registeredForSharingState];
-[CAFRouteSharing registeredForUserEnabled];
-[CAFRouteSharing registeredForUserVisibleReason];
-[CAFRouteSharing registeredForVehicleEnabled];
-[CAFRouteSharing sharingState];
-[CAFRouteSharing userVisibleReason];
-[CAFRouteSharing userVisibleReasonCharacteristic];
-[CAFRouteSharing hasLegs];
-[CAFRouteSharing _characteristicDidUpdate:fromGroupUpdate:];
-[CAFRouteSharing applicationEnabledCharacteristic];
-[CAFRouteSharing applicationEnabledInvalid];
-[CAFRouteSharing currentLegIndexCharacteristic];
-[CAFRouteSharing currentLegIndexInvalid];
-[CAFRouteSharing currentLegIndexRange];
-[CAFRouteSharing identifierCharacteristic];
-[CAFRouteSharing identifierInvalid];
-[CAFRouteSharing legsCharacteristic];
-[CAFRouteSharing legsInvalid];
-[CAFRouteSharing sharingStateCharacteristic];
-[CAFRouteSharing userEnabledCharacteristic];
-[CAFRouteSharing userEnabledInvalid];
-[CAFRouteSharing vehicleEnabledCharacteristic];
```
