# `CAFSeatBelt`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- Protocols: `CAFPositionedRequired`
- 0 instance variables, 14 properties, 20 instance methods, 3 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) vehicleLayoutKeyCharacteristic;
@property (T@"CAFSeatOccupancyCharacteristic",R,N) seatOccupancyCharacteristic;
@property (T@"CAFLockStateCharacteristic",R,N) buckleStateCharacteristic;
@property (T@"CAFSeatBeltIndicatorCharacteristic",R,N) seatBeltIndicatorCharacteristic;
@property (T@"NSString",R,N) vehicleLayoutKey;
@property (TC,R,N) seatOccupancy;
@property (TB,R,N) hasSeatOccupancy;
@property (TC,R,N) buckleState;
@property (TB,R,N) hasBuckleState;
@property (TC,R,N) seatBeltIndicator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAFSeatBelt serviceIdentifier];
+[CAFSeatBelt indexBy];
+[CAFSeatBelt observerProtocol];
```

## Instance methods

```
-[CAFSeatBelt removeObserver:];
-[CAFSeatBelt addObserver:];
-[CAFSeatBelt registerObserver:];
-[CAFSeatBelt name];
-[CAFSeatBelt unregisterObserver:];
-[CAFSeatBelt buckleState];
-[CAFSeatBelt hasBuckleState];
-[CAFSeatBelt hasSeatOccupancy];
-[CAFSeatBelt registeredForBuckleState];
-[CAFSeatBelt registeredForSeatBeltIndicator];
-[CAFSeatBelt registeredForSeatOccupancy];
-[CAFSeatBelt registeredForVehicleLayoutKey];
-[CAFSeatBelt seatBeltIndicator];
-[CAFSeatBelt seatOccupancy];
-[CAFSeatBelt vehicleLayoutKey];
-[CAFSeatBelt seatBeltIndicatorCharacteristic];
-[CAFSeatBelt _characteristicDidUpdate:fromGroupUpdate:];
-[CAFSeatBelt buckleStateCharacteristic];
-[CAFSeatBelt seatOccupancyCharacteristic];
-[CAFSeatBelt vehicleLayoutKeyCharacteristic];
```
