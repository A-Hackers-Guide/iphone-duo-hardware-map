# `CAFTransmissionStatus`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 6 properties, 14 instance methods, 2 class methods

## Properties

```
@property (T@"CAFTransmissionModeCharacteristic",R,N) transmissionModeCharacteristic;
@property (T@"CAFUInt8Characteristic",R,N) gearPositionCharacteristic;
@property (TC,R,N) transmissionMode;
@property (TC,R,N) gearPosition;
@property (T@"CAFUInt8Range",R,N) gearPositionRange;
@property (TB,R,N) gearPositionInvalid;
```

## Class methods

```
+[CAFTransmissionStatus serviceIdentifier];
+[CAFTransmissionStatus observerProtocol];
```

## Instance methods

```
-[CAFTransmissionStatus removeObserver:];
-[CAFTransmissionStatus addObserver:];
-[CAFTransmissionStatus transmissionMode];
-[CAFTransmissionStatus registerObserver:];
-[CAFTransmissionStatus name];
-[CAFTransmissionStatus unregisterObserver:];
-[CAFTransmissionStatus gearPosition];
-[CAFTransmissionStatus registeredForGearPosition];
-[CAFTransmissionStatus registeredForTransmissionMode];
-[CAFTransmissionStatus _characteristicDidUpdate:fromGroupUpdate:];
-[CAFTransmissionStatus gearPositionCharacteristic];
-[CAFTransmissionStatus gearPositionInvalid];
-[CAFTransmissionStatus gearPositionRange];
-[CAFTransmissionStatus transmissionModeCharacteristic];
```
