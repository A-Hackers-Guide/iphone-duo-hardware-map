# `CAFChargingStatus`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 9 properties, 18 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) chargingModeIdentifierCharacteristic;
@property (T@"CAFChargingStateCharacteristic",R,N) chargingStateCharacteristic;
@property (T@"CAFPortSideIndicatorCharacteristic",R,N) portSideIndicatorCharacteristic;
@property (T@"NSString",R,N) chargingModeIdentifier;
@property (TB,R,N) hasChargingModeIdentifier;
@property (TC,R,N) chargingState;
@property (TB,R,N) hasChargingState;
@property (TC,R,N) portSideIndicator;
@property (TB,R,N) hasPortSideIndicator;
```

## Class methods

```
+[CAFChargingStatus serviceIdentifier];
+[CAFChargingStatus observerProtocol];
```

## Instance methods

```
-[CAFChargingStatus removeObserver:];
-[CAFChargingStatus addObserver:];
-[CAFChargingStatus registerObserver:];
-[CAFChargingStatus name];
-[CAFChargingStatus unregisterObserver:];
-[CAFChargingStatus chargingState];
-[CAFChargingStatus hasChargingState];
-[CAFChargingStatus chargingModeIdentifier];
-[CAFChargingStatus hasPortSideIndicator];
-[CAFChargingStatus portSideIndicator];
-[CAFChargingStatus registeredForChargingModeIdentifier];
-[CAFChargingStatus registeredForChargingState];
-[CAFChargingStatus registeredForPortSideIndicator];
-[CAFChargingStatus portSideIndicatorCharacteristic];
-[CAFChargingStatus _characteristicDidUpdate:fromGroupUpdate:];
-[CAFChargingStatus chargingModeIdentifierCharacteristic];
-[CAFChargingStatus chargingStateCharacteristic];
-[CAFChargingStatus hasChargingModeIdentifier];
```
