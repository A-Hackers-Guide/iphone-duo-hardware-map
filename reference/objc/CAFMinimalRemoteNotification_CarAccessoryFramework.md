# `CAFMinimalRemoteNotification`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 16 properties, 31 instance methods, 2 class methods

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
@property (T@"NSString",R,N) userVisibleLabel;
@property (T@"NSString",R,N) userVisibleDescription;
@property (T@"NSString",R,N) identifier;
@property (T@"CAFSymbolImageWithColor",R,N) symbolNameAndColor;
@property (T@"NSString",R,N) displayPanelIdentifier;
@property (T@"NSString",R,N) displayZoneIdentifier;
@property (T@"CAFTrailingButton",R,N) trailingButton;
@property (TC,N) trailingButtonState;
```

## Class methods

```
+[CAFMinimalRemoteNotification serviceIdentifier];
+[CAFMinimalRemoteNotification observerProtocol];
```

## Instance methods

```
-[CAFMinimalRemoteNotification identifier];
-[CAFMinimalRemoteNotification removeObserver:];
-[CAFMinimalRemoteNotification trailingButton];
-[CAFMinimalRemoteNotification addObserver:];
-[CAFMinimalRemoteNotification registerObserver:];
-[CAFMinimalRemoteNotification name];
-[CAFMinimalRemoteNotification unregisterObserver:];
-[CAFMinimalRemoteNotification registeredForSymbolNameAndColor];
-[CAFMinimalRemoteNotification displayPanelIdentifier];
-[CAFMinimalRemoteNotification displayZoneIdentifier];
-[CAFMinimalRemoteNotification registeredForDisplayPanelIdentifier];
-[CAFMinimalRemoteNotification registeredForDisplayZoneIdentifier];
-[CAFMinimalRemoteNotification registeredForIdentifier];
-[CAFMinimalRemoteNotification registeredForTrailingButton];
-[CAFMinimalRemoteNotification registeredForTrailingButtonState];
-[CAFMinimalRemoteNotification registeredForUserVisibleDescription];
-[CAFMinimalRemoteNotification registeredForUserVisibleLabel];
-[CAFMinimalRemoteNotification setTrailingButtonState:];
-[CAFMinimalRemoteNotification symbolNameAndColor];
-[CAFMinimalRemoteNotification trailingButtonState];
-[CAFMinimalRemoteNotification userVisibleDescription];
-[CAFMinimalRemoteNotification userVisibleLabel];
-[CAFMinimalRemoteNotification _characteristicDidUpdate:fromGroupUpdate:];
-[CAFMinimalRemoteNotification displayPanelIdentifierCharacteristic];
-[CAFMinimalRemoteNotification displayZoneIdentifierCharacteristic];
-[CAFMinimalRemoteNotification identifierCharacteristic];
-[CAFMinimalRemoteNotification symbolNameAndColorCharacteristic];
-[CAFMinimalRemoteNotification trailingButtonCharacteristic];
-[CAFMinimalRemoteNotification trailingButtonStateCharacteristic];
-[CAFMinimalRemoteNotification userVisibleDescriptionCharacteristic];
-[CAFMinimalRemoteNotification userVisibleLabelCharacteristic];
```
