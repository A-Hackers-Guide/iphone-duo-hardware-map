# `CAFLocalNotification`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 6 properties, 15 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) identifierCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) displayPanelIdentifierCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) displayZoneIdentifierCharacteristic;
@property (T@"NSString",R,N) identifier;
@property (T@"NSString",R,N) displayPanelIdentifier;
@property (T@"NSString",R,N) displayZoneIdentifier;
```

## Class methods

```
+[CAFLocalNotification serviceIdentifier];
+[CAFLocalNotification observerProtocol];
```

## Instance methods

```
-[CAFLocalNotification identifier];
-[CAFLocalNotification removeObserver:];
-[CAFLocalNotification addObserver:];
-[CAFLocalNotification registerObserver:];
-[CAFLocalNotification name];
-[CAFLocalNotification unregisterObserver:];
-[CAFLocalNotification displayPanelIdentifier];
-[CAFLocalNotification displayZoneIdentifier];
-[CAFLocalNotification registeredForDisplayPanelIdentifier];
-[CAFLocalNotification registeredForDisplayZoneIdentifier];
-[CAFLocalNotification registeredForIdentifier];
-[CAFLocalNotification _characteristicDidUpdate:fromGroupUpdate:];
-[CAFLocalNotification displayPanelIdentifierCharacteristic];
-[CAFLocalNotification displayZoneIdentifierCharacteristic];
-[CAFLocalNotification identifierCharacteristic];
```
