# `CAFCellularStatus`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 14 properties, 26 instance methods, 2 class methods

## Properties

```
@property (T@"CAFModuleStatusCharacteristic",R,N) moduleStatusCharacteristic;
@property (T@"CAFUInt8Characteristic",R,N) signalBarsCharacteristic;
@property (T@"CAFCellularTypeCharacteristic",R,N) cellularTypeCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) contentURLActionCharacteristic;
@property (T@"CAFButtonActionCharacteristic",R,N) buttonActionCharacteristic;
@property (TC,R,N) moduleStatus;
@property (TC,R,N) signalBars;
@property (T@"CAFUInt8Range",R,N) signalBarsRange;
@property (TC,R,N) cellularType;
@property (TB,R,N) hasCellularType;
@property (T@"NSString",R,N) contentURLAction;
@property (TB,R,N) hasContentURLAction;
@property (TC,N) buttonAction;
@property (TB,R,N) hasButtonAction;
```

## Class methods

```
+[CAFCellularStatus serviceIdentifier];
+[CAFCellularStatus observerProtocol];
```

## Instance methods

```
-[CAFCellularStatus signalBars];
-[CAFCellularStatus removeObserver:];
-[CAFCellularStatus addObserver:];
-[CAFCellularStatus registerObserver:];
-[CAFCellularStatus name];
-[CAFCellularStatus unregisterObserver:];
-[CAFCellularStatus buttonAction];
-[CAFCellularStatus setButtonAction:];
-[CAFCellularStatus hasButtonAction];
-[CAFCellularStatus hasCellularType];
-[CAFCellularStatus cellularType];
-[CAFCellularStatus contentURLAction];
-[CAFCellularStatus moduleStatus];
-[CAFCellularStatus registeredForButtonAction];
-[CAFCellularStatus registeredForCellularType];
-[CAFCellularStatus registeredForContentURLAction];
-[CAFCellularStatus registeredForModuleStatus];
-[CAFCellularStatus registeredForSignalBars];
-[CAFCellularStatus signalBarsRange];
-[CAFCellularStatus _characteristicDidUpdate:fromGroupUpdate:];
-[CAFCellularStatus buttonActionCharacteristic];
-[CAFCellularStatus cellularTypeCharacteristic];
-[CAFCellularStatus contentURLActionCharacteristic];
-[CAFCellularStatus hasContentURLAction];
-[CAFCellularStatus moduleStatusCharacteristic];
-[CAFCellularStatus signalBarsCharacteristic];
```
