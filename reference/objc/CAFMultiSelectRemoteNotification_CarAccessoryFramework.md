# `CAFMultiSelectRemoteNotification`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 20 properties, 38 instance methods, 2 class methods

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
@property (T@"CAFSelectableNotificationEntryListCharacteristic",R,N) selectableNotificationEntriesCharacteristic;
@property (T@"CAFArrayCharacteristic",R,N) selectedEntryIndicesCharacteristic;
@property (T@"NSString",R,N) userVisibleLabel;
@property (T@"NSString",R,N) userVisibleDescription;
@property (T@"NSString",R,N) identifier;
@property (T@"CAFSymbolImageWithColor",R,N) symbolNameAndColor;
@property (T@"NSString",R,N) displayPanelIdentifier;
@property (T@"NSString",R,N) displayZoneIdentifier;
@property (T@"CAFTrailingButton",R,N) trailingButton;
@property (TC,N) trailingButtonState;
@property (T@"CAFSelectableNotificationEntryList",R,N) selectableNotificationEntries;
@property (T@"NSArray",C,N) selectedEntryIndices;
```

## Class methods

```
+[CAFMultiSelectRemoteNotification serviceIdentifier];
+[CAFMultiSelectRemoteNotification observerProtocol];
```

## Instance methods

```
-[CAFMultiSelectRemoteNotification identifier];
-[CAFMultiSelectRemoteNotification removeObserver:];
-[CAFMultiSelectRemoteNotification trailingButton];
-[CAFMultiSelectRemoteNotification addObserver:];
-[CAFMultiSelectRemoteNotification registerObserver:];
-[CAFMultiSelectRemoteNotification name];
-[CAFMultiSelectRemoteNotification unregisterObserver:];
-[CAFMultiSelectRemoteNotification registeredForSymbolNameAndColor];
-[CAFMultiSelectRemoteNotification displayPanelIdentifier];
-[CAFMultiSelectRemoteNotification displayZoneIdentifier];
-[CAFMultiSelectRemoteNotification registeredForDisplayPanelIdentifier];
-[CAFMultiSelectRemoteNotification registeredForDisplayZoneIdentifier];
-[CAFMultiSelectRemoteNotification registeredForIdentifier];
-[CAFMultiSelectRemoteNotification registeredForSelectableNotificationEntries];
-[CAFMultiSelectRemoteNotification registeredForSelectedEntryIndices];
-[CAFMultiSelectRemoteNotification registeredForTrailingButton];
-[CAFMultiSelectRemoteNotification registeredForTrailingButtonState];
-[CAFMultiSelectRemoteNotification registeredForUserVisibleDescription];
-[CAFMultiSelectRemoteNotification registeredForUserVisibleLabel];
-[CAFMultiSelectRemoteNotification selectableNotificationEntries];
-[CAFMultiSelectRemoteNotification selectedEntryIndices];
-[CAFMultiSelectRemoteNotification setSelectedEntryIndices:];
-[CAFMultiSelectRemoteNotification setTrailingButtonState:];
-[CAFMultiSelectRemoteNotification symbolNameAndColor];
-[CAFMultiSelectRemoteNotification trailingButtonState];
-[CAFMultiSelectRemoteNotification userVisibleDescription];
-[CAFMultiSelectRemoteNotification userVisibleLabel];
-[CAFMultiSelectRemoteNotification _characteristicDidUpdate:fromGroupUpdate:];
-[CAFMultiSelectRemoteNotification displayPanelIdentifierCharacteristic];
-[CAFMultiSelectRemoteNotification displayZoneIdentifierCharacteristic];
-[CAFMultiSelectRemoteNotification identifierCharacteristic];
-[CAFMultiSelectRemoteNotification selectableNotificationEntriesCharacteristic];
-[CAFMultiSelectRemoteNotification selectedEntryIndicesCharacteristic];
-[CAFMultiSelectRemoteNotification symbolNameAndColorCharacteristic];
-[CAFMultiSelectRemoteNotification trailingButtonCharacteristic];
-[CAFMultiSelectRemoteNotification trailingButtonStateCharacteristic];
-[CAFMultiSelectRemoteNotification userVisibleDescriptionCharacteristic];
-[CAFMultiSelectRemoteNotification userVisibleLabelCharacteristic];
```
