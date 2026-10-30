# `CAFAutomakerSettingsRemoteNotification`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 18 properties, 34 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) userVisibleLabelCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleDescriptionCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) identifierCharacteristic;
@property (T@"CAFSymbolImageWithColorCharacteristic",R,N) symbolNameAndColorCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) displayPanelIdentifierCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) displayZoneIdentifierCharacteristic;
@property (T@"CAFTrailingButtonCharacteristic",R,N) trailingButtonCharacteristic;
@property (T@"CAFButtonActionCharacteristic",R,N) trailingButtonStateCharacteristic;
@property (T@"CAFArrayCharacteristic",R,N) automakerSettingsNotificationButtonsCharacteristic;
@property (T@"NSString",R,N) userVisibleLabel;
@property (T@"NSString",R,N) userVisibleDescription;
@property (T@"NSString",R,N) identifier;
@property (T@"CAFSymbolImageWithColor",R,N) symbolNameAndColor;
@property (T@"NSString",R,N) displayPanelIdentifier;
@property (T@"NSString",R,N) displayZoneIdentifier;
@property (T@"CAFTrailingButton",R,N) trailingButton;
@property (TC,N) trailingButtonState;
@property (T@"NSArray",R,N) automakerSettingsNotificationButtons;
```

## Class methods

```
+[CAFAutomakerSettingsRemoteNotification serviceIdentifier];
+[CAFAutomakerSettingsRemoteNotification observerProtocol];
```

## Instance methods

```
-[CAFAutomakerSettingsRemoteNotification identifier];
-[CAFAutomakerSettingsRemoteNotification removeObserver:];
-[CAFAutomakerSettingsRemoteNotification trailingButton];
-[CAFAutomakerSettingsRemoteNotification addObserver:];
-[CAFAutomakerSettingsRemoteNotification registerObserver:];
-[CAFAutomakerSettingsRemoteNotification name];
-[CAFAutomakerSettingsRemoteNotification unregisterObserver:];
-[CAFAutomakerSettingsRemoteNotification registeredForSymbolNameAndColor];
-[CAFAutomakerSettingsRemoteNotification automakerSettingsNotificationButtons];
-[CAFAutomakerSettingsRemoteNotification displayPanelIdentifier];
-[CAFAutomakerSettingsRemoteNotification displayZoneIdentifier];
-[CAFAutomakerSettingsRemoteNotification registeredForAutomakerSettingsNotificationButtons];
-[CAFAutomakerSettingsRemoteNotification registeredForDisplayPanelIdentifier];
-[CAFAutomakerSettingsRemoteNotification registeredForDisplayZoneIdentifier];
-[CAFAutomakerSettingsRemoteNotification registeredForIdentifier];
-[CAFAutomakerSettingsRemoteNotification registeredForTrailingButton];
-[CAFAutomakerSettingsRemoteNotification registeredForTrailingButtonState];
-[CAFAutomakerSettingsRemoteNotification registeredForUserVisibleDescription];
-[CAFAutomakerSettingsRemoteNotification registeredForUserVisibleLabel];
-[CAFAutomakerSettingsRemoteNotification setTrailingButtonState:];
-[CAFAutomakerSettingsRemoteNotification symbolNameAndColor];
-[CAFAutomakerSettingsRemoteNotification trailingButtonState];
-[CAFAutomakerSettingsRemoteNotification userVisibleDescription];
-[CAFAutomakerSettingsRemoteNotification userVisibleLabel];
-[CAFAutomakerSettingsRemoteNotification _characteristicDidUpdate:fromGroupUpdate:];
-[CAFAutomakerSettingsRemoteNotification automakerSettingsNotificationButtonsCharacteristic];
-[CAFAutomakerSettingsRemoteNotification displayPanelIdentifierCharacteristic];
-[CAFAutomakerSettingsRemoteNotification displayZoneIdentifierCharacteristic];
-[CAFAutomakerSettingsRemoteNotification identifierCharacteristic];
-[CAFAutomakerSettingsRemoteNotification symbolNameAndColorCharacteristic];
-[CAFAutomakerSettingsRemoteNotification trailingButtonCharacteristic];
-[CAFAutomakerSettingsRemoteNotification trailingButtonStateCharacteristic];
-[CAFAutomakerSettingsRemoteNotification userVisibleDescriptionCharacteristic];
-[CAFAutomakerSettingsRemoteNotification userVisibleLabelCharacteristic];
```
