# `CAFAlertRemoteNotification`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 19 properties, 35 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) userVisibleLabelCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleDescriptionCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) identifierCharacteristic;
@property (T@"CAFSymbolImageWithColorCharacteristic",R,N) symbolNameAndColorCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) displayPanelIdentifierCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) displayZoneIdentifierCharacteristic;
@property (T@"CAFNotificationUserActionsCharacteristic",R,N) notificationUserActionsCharacteristic;
@property (T@"CAFUInt8Characteristic",R,N) userActionCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) showsPrimaryActionHighlightCharacteristic;
@property (T@"NSString",R,N) userVisibleLabel;
@property (T@"NSString",R,N) userVisibleDescription;
@property (T@"NSString",R,N) identifier;
@property (T@"CAFSymbolImageWithColor",R,N) symbolNameAndColor;
@property (T@"NSString",R,N) displayPanelIdentifier;
@property (T@"NSString",R,N) displayZoneIdentifier;
@property (T@"CAFNotificationUserActions",R,N) notificationUserActions;
@property (TC,N) userAction;
@property (T@"CAFUInt8Range",R,N) userActionRange;
@property (TB,R,N) showsPrimaryActionHighlight;
```

## Class methods

```
+[CAFAlertRemoteNotification serviceIdentifier];
+[CAFAlertRemoteNotification observerProtocol];
```

## Instance methods

```
-[CAFAlertRemoteNotification identifier];
-[CAFAlertRemoteNotification removeObserver:];
-[CAFAlertRemoteNotification userAction];
-[CAFAlertRemoteNotification addObserver:];
-[CAFAlertRemoteNotification registerObserver:];
-[CAFAlertRemoteNotification name];
-[CAFAlertRemoteNotification unregisterObserver:];
-[CAFAlertRemoteNotification setUserAction:];
-[CAFAlertRemoteNotification registeredForSymbolNameAndColor];
-[CAFAlertRemoteNotification displayPanelIdentifier];
-[CAFAlertRemoteNotification displayZoneIdentifier];
-[CAFAlertRemoteNotification notificationUserActions];
-[CAFAlertRemoteNotification registeredForDisplayPanelIdentifier];
-[CAFAlertRemoteNotification registeredForDisplayZoneIdentifier];
-[CAFAlertRemoteNotification registeredForIdentifier];
-[CAFAlertRemoteNotification registeredForNotificationUserActions];
-[CAFAlertRemoteNotification registeredForShowsPrimaryActionHighlight];
-[CAFAlertRemoteNotification registeredForUserAction];
-[CAFAlertRemoteNotification registeredForUserVisibleDescription];
-[CAFAlertRemoteNotification registeredForUserVisibleLabel];
-[CAFAlertRemoteNotification showsPrimaryActionHighlight];
-[CAFAlertRemoteNotification symbolNameAndColor];
-[CAFAlertRemoteNotification userVisibleDescription];
-[CAFAlertRemoteNotification userVisibleLabel];
-[CAFAlertRemoteNotification userActionRange];
-[CAFAlertRemoteNotification _characteristicDidUpdate:fromGroupUpdate:];
-[CAFAlertRemoteNotification displayPanelIdentifierCharacteristic];
-[CAFAlertRemoteNotification displayZoneIdentifierCharacteristic];
-[CAFAlertRemoteNotification identifierCharacteristic];
-[CAFAlertRemoteNotification notificationUserActionsCharacteristic];
-[CAFAlertRemoteNotification showsPrimaryActionHighlightCharacteristic];
-[CAFAlertRemoteNotification symbolNameAndColorCharacteristic];
-[CAFAlertRemoteNotification userActionCharacteristic];
-[CAFAlertRemoteNotification userVisibleDescriptionCharacteristic];
-[CAFAlertRemoteNotification userVisibleLabelCharacteristic];
```
