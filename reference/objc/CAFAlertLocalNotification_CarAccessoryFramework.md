# `CAFAlertLocalNotification`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 19 properties, 34 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) identifierCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleLabelCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleDescriptionCharacteristic;
@property (T@"CAFTrailingButtonCharacteristic",R,N) trailingButtonCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) displayPanelIdentifierCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) displayZoneIdentifierCharacteristic;
@property (T@"CAFSymbolImageWithColorCharacteristic",R,N) symbolNameAndColorCharacteristic;
@property (T@"CAFLocalNotificationUserActionsCharacteristic",R,N) localNotificationUserActionsCharacteristic;
@property (T@"CAFNotificationSeverityCharacteristic",R,N) notificationSeverityCharacteristic;
@property (T@"NSString",R,N) identifier;
@property (T@"NSString",R,N) userVisibleLabel;
@property (T@"NSString",R,N) userVisibleDescription;
@property (T@"CAFTrailingButton",R,N) trailingButton;
@property (T@"NSString",R,N) displayPanelIdentifier;
@property (T@"NSString",R,N) displayZoneIdentifier;
@property (T@"CAFSymbolImageWithColor",R,N) symbolNameAndColor;
@property (T@"CAFLocalNotificationUserActions",R,N) localNotificationUserActions;
@property (TC,R,N) notificationSeverity;
@property (TB,R,N) hasNotificationSeverity;
```

## Class methods

```
+[CAFAlertLocalNotification serviceIdentifier];
+[CAFAlertLocalNotification observerProtocol];
```

## Instance methods

```
-[CAFAlertLocalNotification identifier];
-[CAFAlertLocalNotification removeObserver:];
-[CAFAlertLocalNotification trailingButton];
-[CAFAlertLocalNotification addObserver:];
-[CAFAlertLocalNotification registerObserver:];
-[CAFAlertLocalNotification name];
-[CAFAlertLocalNotification unregisterObserver:];
-[CAFAlertLocalNotification registeredForSymbolNameAndColor];
-[CAFAlertLocalNotification displayPanelIdentifier];
-[CAFAlertLocalNotification displayZoneIdentifier];
-[CAFAlertLocalNotification hasNotificationSeverity];
-[CAFAlertLocalNotification localNotificationUserActions];
-[CAFAlertLocalNotification notificationSeverity];
-[CAFAlertLocalNotification registeredForDisplayPanelIdentifier];
-[CAFAlertLocalNotification registeredForDisplayZoneIdentifier];
-[CAFAlertLocalNotification registeredForIdentifier];
-[CAFAlertLocalNotification registeredForLocalNotificationUserActions];
-[CAFAlertLocalNotification registeredForNotificationSeverity];
-[CAFAlertLocalNotification registeredForTrailingButton];
-[CAFAlertLocalNotification registeredForUserVisibleDescription];
-[CAFAlertLocalNotification registeredForUserVisibleLabel];
-[CAFAlertLocalNotification symbolNameAndColor];
-[CAFAlertLocalNotification userVisibleDescription];
-[CAFAlertLocalNotification userVisibleLabel];
-[CAFAlertLocalNotification _characteristicDidUpdate:fromGroupUpdate:];
-[CAFAlertLocalNotification displayPanelIdentifierCharacteristic];
-[CAFAlertLocalNotification displayZoneIdentifierCharacteristic];
-[CAFAlertLocalNotification identifierCharacteristic];
-[CAFAlertLocalNotification localNotificationUserActionsCharacteristic];
-[CAFAlertLocalNotification notificationSeverityCharacteristic];
-[CAFAlertLocalNotification symbolNameAndColorCharacteristic];
-[CAFAlertLocalNotification trailingButtonCharacteristic];
-[CAFAlertLocalNotification userVisibleDescriptionCharacteristic];
-[CAFAlertLocalNotification userVisibleLabelCharacteristic];
```
