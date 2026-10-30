# `CAFTurnSignals`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 4 properties, 12 instance methods, 2 class methods

## Properties

```
@property (T@"CAFTurnSignalCharacteristic",R,N) turnSignalLeftCharacteristic;
@property (T@"CAFTurnSignalCharacteristic",R,N) turnSignalRightCharacteristic;
@property (TC,R,N) turnSignalLeft;
@property (TC,R,N) turnSignalRight;
```

## Class methods

```
+[CAFTurnSignals serviceIdentifier];
+[CAFTurnSignals observerProtocol];
```

## Instance methods

```
-[CAFTurnSignals removeObserver:];
-[CAFTurnSignals addObserver:];
-[CAFTurnSignals registerObserver:];
-[CAFTurnSignals name];
-[CAFTurnSignals unregisterObserver:];
-[CAFTurnSignals turnSignalRight];
-[CAFTurnSignals registeredForTurnSignalLeft];
-[CAFTurnSignals registeredForTurnSignalRight];
-[CAFTurnSignals turnSignalLeft];
-[CAFTurnSignals _characteristicDidUpdate:fromGroupUpdate:];
-[CAFTurnSignals turnSignalLeftCharacteristic];
-[CAFTurnSignals turnSignalRightCharacteristic];
```
