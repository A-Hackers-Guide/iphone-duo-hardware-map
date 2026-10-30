# `CAFMinimalLocalNotification`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 17 properties, 31 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) identifierCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleLabelCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleDescriptionCharacteristic;
@property (T@"CAFTrailingButtonCharacteristic",R,N) trailingButtonCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) displayPanelIdentifierCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) displayZoneIdentifierCharacteristic;
@property (T@"CAFSymbolImageWithColorCharacteristic",R,N) symbolNameAndColorCharacteristic;
@property (T@"CAFNotificationSeverityCharacteristic",R,N) notificationSeverityCharacteristic;
@property (T@"NSString",R,N) identifier;
@property (T@"NSString",R,N) userVisibleLabel;
@property (T@"NSString",R,N) userVisibleDescription;
@property (T@"CAFTrailingButton",R,N) trailingButton;
@property (T@"NSString",R,N) displayPanelIdentifier;
@property (T@"NSString",R,N) displayZoneIdentifier;
@property (T@"CAFSymbolImageWithColor",R,N) symbolNameAndColor;
@property (TC,R,N) notificationSeverity;
@property (TB,R,N) hasNotificationSeverity;
```

## Class methods

```
+[CAFMinimalLocalNotification serviceIdentifier];
+[CAFMinimalLocalNotification observerProtocol];
```

## Instance methods

```
-[CAFMinimalLocalNotification identifier];
-[CAFMinimalLocalNotification removeObserver:];
-[CAFMinimalLocalNotification trailingButton];
-[CAFMinimalLocalNotification addObserver:];
-[CAFMinimalLocalNotification registerObserver:];
-[CAFMinimalLocalNotification name];
-[CAFMinimalLocalNotification unregisterObserver:];
-[CAFMinimalLocalNotification registeredForSymbolNameAndColor];
-[CAFMinimalLocalNotification displayPanelIdentifier];
-[CAFMinimalLocalNotification displayZoneIdentifier];
-[CAFMinimalLocalNotification hasNotificationSeverity];
-[CAFMinimalLocalNotification notificationSeverity];
-[CAFMinimalLocalNotification registeredForDisplayPanelIdentifier];
-[CAFMinimalLocalNotification registeredForDisplayZoneIdentifier];
-[CAFMinimalLocalNotification registeredForIdentifier];
-[CAFMinimalLocalNotification registeredForNotificationSeverity];
-[CAFMinimalLocalNotification registeredForTrailingButton];
-[CAFMinimalLocalNotification registeredForUserVisibleDescription];
-[CAFMinimalLocalNotification registeredForUserVisibleLabel];
-[CAFMinimalLocalNotification symbolNameAndColor];
-[CAFMinimalLocalNotification userVisibleDescription];
-[CAFMinimalLocalNotification userVisibleLabel];
-[CAFMinimalLocalNotification _characteristicDidUpdate:fromGroupUpdate:];
-[CAFMinimalLocalNotification displayPanelIdentifierCharacteristic];
-[CAFMinimalLocalNotification displayZoneIdentifierCharacteristic];
-[CAFMinimalLocalNotification identifierCharacteristic];
-[CAFMinimalLocalNotification notificationSeverityCharacteristic];
-[CAFMinimalLocalNotification symbolNameAndColorCharacteristic];
-[CAFMinimalLocalNotification trailingButtonCharacteristic];
-[CAFMinimalLocalNotification userVisibleDescriptionCharacteristic];
-[CAFMinimalLocalNotification userVisibleLabelCharacteristic];
```
