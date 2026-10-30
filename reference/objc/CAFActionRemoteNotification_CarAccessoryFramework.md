# `CAFActionRemoteNotification`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 23 properties, 42 instance methods, 2 class methods

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
@property (T@"CAFSymbolNotificationUserActionsCharacteristic",R,N) symbolNotificationUserActionsCharacteristic;
@property (T@"CAFUInt8Characteristic",R,N) userActionCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) showsPrimaryActionHighlightCharacteristic;
@property (T@"NSString",R,N) userVisibleLabel;
@property (T@"NSString",R,N) userVisibleDescription;
@property (T@"NSString",R,N) identifier;
@property (T@"CAFSymbolImageWithColor",R,N) symbolNameAndColor;
@property (T@"NSString",R,N) displayPanelIdentifier;
@property (T@"NSString",R,N) displayZoneIdentifier;
@property (T@"CAFTrailingButton",R,N) trailingButton;
@property (TC,N) trailingButtonState;
@property (T@"CAFSymbolNotificationUserActions",R,N) symbolNotificationUserActions;
@property (TC,N) userAction;
@property (T@"CAFUInt8Range",R,N) userActionRange;
@property (TB,R,N) showsPrimaryActionHighlight;
```

## Class methods

```
+[CAFActionRemoteNotification serviceIdentifier];
+[CAFActionRemoteNotification observerProtocol];
```

## Instance methods

```
-[CAFActionRemoteNotification identifier];
-[CAFActionRemoteNotification removeObserver:];
-[CAFActionRemoteNotification trailingButton];
-[CAFActionRemoteNotification userAction];
-[CAFActionRemoteNotification addObserver:];
-[CAFActionRemoteNotification registerObserver:];
-[CAFActionRemoteNotification name];
-[CAFActionRemoteNotification unregisterObserver:];
-[CAFActionRemoteNotification setUserAction:];
-[CAFActionRemoteNotification registeredForSymbolNameAndColor];
-[CAFActionRemoteNotification displayPanelIdentifier];
-[CAFActionRemoteNotification displayZoneIdentifier];
-[CAFActionRemoteNotification registeredForDisplayPanelIdentifier];
-[CAFActionRemoteNotification registeredForDisplayZoneIdentifier];
-[CAFActionRemoteNotification registeredForIdentifier];
-[CAFActionRemoteNotification registeredForShowsPrimaryActionHighlight];
-[CAFActionRemoteNotification registeredForSymbolNotificationUserActions];
-[CAFActionRemoteNotification registeredForTrailingButton];
-[CAFActionRemoteNotification registeredForTrailingButtonState];
-[CAFActionRemoteNotification registeredForUserAction];
-[CAFActionRemoteNotification registeredForUserVisibleDescription];
-[CAFActionRemoteNotification registeredForUserVisibleLabel];
-[CAFActionRemoteNotification setTrailingButtonState:];
-[CAFActionRemoteNotification showsPrimaryActionHighlight];
-[CAFActionRemoteNotification symbolNameAndColor];
-[CAFActionRemoteNotification symbolNotificationUserActions];
-[CAFActionRemoteNotification trailingButtonState];
-[CAFActionRemoteNotification userVisibleDescription];
-[CAFActionRemoteNotification userVisibleLabel];
-[CAFActionRemoteNotification userActionRange];
-[CAFActionRemoteNotification _characteristicDidUpdate:fromGroupUpdate:];
-[CAFActionRemoteNotification displayPanelIdentifierCharacteristic];
-[CAFActionRemoteNotification displayZoneIdentifierCharacteristic];
-[CAFActionRemoteNotification identifierCharacteristic];
-[CAFActionRemoteNotification showsPrimaryActionHighlightCharacteristic];
-[CAFActionRemoteNotification symbolNameAndColorCharacteristic];
-[CAFActionRemoteNotification symbolNotificationUserActionsCharacteristic];
-[CAFActionRemoteNotification trailingButtonCharacteristic];
-[CAFActionRemoteNotification trailingButtonStateCharacteristic];
-[CAFActionRemoteNotification userActionCharacteristic];
-[CAFActionRemoteNotification userVisibleDescriptionCharacteristic];
-[CAFActionRemoteNotification userVisibleLabelCharacteristic];
```
