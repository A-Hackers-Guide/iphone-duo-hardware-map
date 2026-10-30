# `CAFSingleSelectRemoteNotification`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 21 properties, 39 instance methods, 2 class methods

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
@property (T@"CAFUInt8Characteristic",R,N) selectedEntryIndexCharacteristic;
@property (T@"NSString",R,N) userVisibleLabel;
@property (T@"NSString",R,N) userVisibleDescription;
@property (T@"NSString",R,N) identifier;
@property (T@"CAFSymbolImageWithColor",R,N) symbolNameAndColor;
@property (T@"NSString",R,N) displayPanelIdentifier;
@property (T@"NSString",R,N) displayZoneIdentifier;
@property (T@"CAFTrailingButton",R,N) trailingButton;
@property (TC,N) trailingButtonState;
@property (T@"CAFSelectableNotificationEntryList",R,N) selectableNotificationEntries;
@property (TC,N) selectedEntryIndex;
@property (T@"CAFUInt8Range",R,N) selectedEntryIndexRange;
```

## Class methods

```
+[CAFSingleSelectRemoteNotification serviceIdentifier];
+[CAFSingleSelectRemoteNotification observerProtocol];
```

## Instance methods

```
-[CAFSingleSelectRemoteNotification identifier];
-[CAFSingleSelectRemoteNotification removeObserver:];
-[CAFSingleSelectRemoteNotification trailingButton];
-[CAFSingleSelectRemoteNotification addObserver:];
-[CAFSingleSelectRemoteNotification registerObserver:];
-[CAFSingleSelectRemoteNotification name];
-[CAFSingleSelectRemoteNotification unregisterObserver:];
-[CAFSingleSelectRemoteNotification registeredForSelectedEntryIndex];
-[CAFSingleSelectRemoteNotification registeredForSymbolNameAndColor];
-[CAFSingleSelectRemoteNotification displayPanelIdentifier];
-[CAFSingleSelectRemoteNotification displayZoneIdentifier];
-[CAFSingleSelectRemoteNotification registeredForDisplayPanelIdentifier];
-[CAFSingleSelectRemoteNotification registeredForDisplayZoneIdentifier];
-[CAFSingleSelectRemoteNotification registeredForIdentifier];
-[CAFSingleSelectRemoteNotification registeredForSelectableNotificationEntries];
-[CAFSingleSelectRemoteNotification registeredForTrailingButton];
-[CAFSingleSelectRemoteNotification registeredForTrailingButtonState];
-[CAFSingleSelectRemoteNotification registeredForUserVisibleDescription];
-[CAFSingleSelectRemoteNotification registeredForUserVisibleLabel];
-[CAFSingleSelectRemoteNotification selectableNotificationEntries];
-[CAFSingleSelectRemoteNotification selectedEntryIndex];
-[CAFSingleSelectRemoteNotification setSelectedEntryIndex:];
-[CAFSingleSelectRemoteNotification setTrailingButtonState:];
-[CAFSingleSelectRemoteNotification symbolNameAndColor];
-[CAFSingleSelectRemoteNotification trailingButtonState];
-[CAFSingleSelectRemoteNotification userVisibleDescription];
-[CAFSingleSelectRemoteNotification userVisibleLabel];
-[CAFSingleSelectRemoteNotification _characteristicDidUpdate:fromGroupUpdate:];
-[CAFSingleSelectRemoteNotification displayPanelIdentifierCharacteristic];
-[CAFSingleSelectRemoteNotification displayZoneIdentifierCharacteristic];
-[CAFSingleSelectRemoteNotification identifierCharacteristic];
-[CAFSingleSelectRemoteNotification selectableNotificationEntriesCharacteristic];
-[CAFSingleSelectRemoteNotification selectedEntryIndexCharacteristic];
-[CAFSingleSelectRemoteNotification selectedEntryIndexRange];
-[CAFSingleSelectRemoteNotification symbolNameAndColorCharacteristic];
-[CAFSingleSelectRemoteNotification trailingButtonCharacteristic];
-[CAFSingleSelectRemoteNotification trailingButtonStateCharacteristic];
-[CAFSingleSelectRemoteNotification userVisibleDescriptionCharacteristic];
-[CAFSingleSelectRemoteNotification userVisibleLabelCharacteristic];
```
