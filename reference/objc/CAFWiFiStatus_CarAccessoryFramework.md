# `CAFWiFiStatus`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 11 properties, 22 instance methods, 2 class methods

## Properties

```
@property (T@"CAFModuleStatusCharacteristic",R,N) moduleStatusCharacteristic;
@property (T@"CAFUInt8Characteristic",R,N) signalBarsCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) contentURLActionCharacteristic;
@property (T@"CAFButtonActionCharacteristic",R,N) buttonActionCharacteristic;
@property (TC,R,N) moduleStatus;
@property (TC,R,N) signalBars;
@property (T@"CAFUInt8Range",R,N) signalBarsRange;
@property (T@"NSString",R,N) contentURLAction;
@property (TB,R,N) hasContentURLAction;
@property (TC,N) buttonAction;
@property (TB,R,N) hasButtonAction;
```

## Class methods

```
+[CAFWiFiStatus serviceIdentifier];
+[CAFWiFiStatus observerProtocol];
```

## Instance methods

```
-[CAFWiFiStatus signalBars];
-[CAFWiFiStatus removeObserver:];
-[CAFWiFiStatus addObserver:];
-[CAFWiFiStatus registerObserver:];
-[CAFWiFiStatus name];
-[CAFWiFiStatus unregisterObserver:];
-[CAFWiFiStatus buttonAction];
-[CAFWiFiStatus setButtonAction:];
-[CAFWiFiStatus hasButtonAction];
-[CAFWiFiStatus contentURLAction];
-[CAFWiFiStatus moduleStatus];
-[CAFWiFiStatus registeredForButtonAction];
-[CAFWiFiStatus registeredForContentURLAction];
-[CAFWiFiStatus registeredForModuleStatus];
-[CAFWiFiStatus registeredForSignalBars];
-[CAFWiFiStatus signalBarsRange];
-[CAFWiFiStatus _characteristicDidUpdate:fromGroupUpdate:];
-[CAFWiFiStatus buttonActionCharacteristic];
-[CAFWiFiStatus contentURLActionCharacteristic];
-[CAFWiFiStatus hasContentURLAction];
-[CAFWiFiStatus moduleStatusCharacteristic];
-[CAFWiFiStatus signalBarsCharacteristic];
```
