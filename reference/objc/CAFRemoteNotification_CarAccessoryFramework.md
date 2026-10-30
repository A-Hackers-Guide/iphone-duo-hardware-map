# `CAFRemoteNotification`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 18 properties, 33 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) userVisibleLabelCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleDescriptionCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) identifierCharacteristic;
@property (T@"CAFNotificationUserActionsCharacteristic",R,N) notificationUserActionsCharacteristic;
@property (T@"CAFUInt8Characteristic",R,N) userActionCharacteristic;
@property (T@"CAFSymbolImageWithColorCharacteristic",R,N) symbolNameAndColorCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) displayPanelIdentifierCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) displayZoneIdentifierCharacteristic;
@property (T@"NSString",R,N) userVisibleLabel;
@property (T@"NSString",R,N) userVisibleDescription;
@property (T@"NSString",R,N) identifier;
@property (T@"CAFNotificationUserActions",R,N) notificationUserActions;
@property (TC,N) userAction;
@property (T@"CAFUInt8Range",R,N) userActionRange;
@property (T@"CAFSymbolImageWithColor",R,N) symbolNameAndColor;
@property (TB,R,N) hasSymbolNameAndColor;
@property (T@"NSString",R,N) displayPanelIdentifier;
@property (T@"NSString",R,N) displayZoneIdentifier;
```

## Class methods

```
+[CAFRemoteNotification serviceIdentifier];
+[CAFRemoteNotification observerProtocol];
```

## Instance methods

```
-[CAFRemoteNotification identifier];
-[CAFRemoteNotification removeObserver:];
-[CAFRemoteNotification userAction];
-[CAFRemoteNotification addObserver:];
-[CAFRemoteNotification registerObserver:];
-[CAFRemoteNotification name];
-[CAFRemoteNotification unregisterObserver:];
-[CAFRemoteNotification setUserAction:];
-[CAFRemoteNotification registeredForSymbolNameAndColor];
-[CAFRemoteNotification displayPanelIdentifier];
-[CAFRemoteNotification displayZoneIdentifier];
-[CAFRemoteNotification notificationUserActions];
-[CAFRemoteNotification registeredForDisplayPanelIdentifier];
-[CAFRemoteNotification registeredForDisplayZoneIdentifier];
-[CAFRemoteNotification registeredForIdentifier];
-[CAFRemoteNotification registeredForNotificationUserActions];
-[CAFRemoteNotification registeredForUserAction];
-[CAFRemoteNotification registeredForUserVisibleDescription];
-[CAFRemoteNotification registeredForUserVisibleLabel];
-[CAFRemoteNotification symbolNameAndColor];
-[CAFRemoteNotification userVisibleDescription];
-[CAFRemoteNotification userVisibleLabel];
-[CAFRemoteNotification userActionRange];
-[CAFRemoteNotification _characteristicDidUpdate:fromGroupUpdate:];
-[CAFRemoteNotification displayPanelIdentifierCharacteristic];
-[CAFRemoteNotification displayZoneIdentifierCharacteristic];
-[CAFRemoteNotification hasSymbolNameAndColor];
-[CAFRemoteNotification identifierCharacteristic];
-[CAFRemoteNotification notificationUserActionsCharacteristic];
-[CAFRemoteNotification symbolNameAndColorCharacteristic];
-[CAFRemoteNotification userActionCharacteristic];
-[CAFRemoteNotification userVisibleDescriptionCharacteristic];
-[CAFRemoteNotification userVisibleLabelCharacteristic];
```
