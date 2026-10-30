# `CAFPicker`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 13 properties, 26 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) identifierCharacteristic;
@property (T@"CAFEntryListCharacteristic",R,N) entryListCharacteristic;
@property (T@"CAFUInt8Characteristic",R,N) selectedEntryIndexCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) userSelectionEnabledCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) displayPanelIdentifierCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) displayZoneIdentifierCharacteristic;
@property (T@"NSString",R,N) identifier;
@property (T@"CAFEntryList",R,N) entryList;
@property (TC,N) selectedEntryIndex;
@property (T@"CAFUInt8Range",R,N) selectedEntryIndexRange;
@property (TB,R,N) userSelectionEnabled;
@property (T@"NSString",R,N) displayPanelIdentifier;
@property (T@"NSString",R,N) displayZoneIdentifier;
```

## Class methods

```
+[CAFPicker serviceIdentifier];
+[CAFPicker observerProtocol];
```

## Instance methods

```
-[CAFPicker identifier];
-[CAFPicker removeObserver:];
-[CAFPicker addObserver:];
-[CAFPicker registerObserver:];
-[CAFPicker name];
-[CAFPicker unregisterObserver:];
-[CAFPicker userSelectionEnabled];
-[CAFPicker entryList];
-[CAFPicker registeredForSelectedEntryIndex];
-[CAFPicker displayPanelIdentifier];
-[CAFPicker displayZoneIdentifier];
-[CAFPicker registeredForDisplayPanelIdentifier];
-[CAFPicker registeredForDisplayZoneIdentifier];
-[CAFPicker registeredForEntryList];
-[CAFPicker registeredForIdentifier];
-[CAFPicker registeredForUserSelectionEnabled];
-[CAFPicker selectedEntryIndex];
-[CAFPicker setSelectedEntryIndex:];
-[CAFPicker _characteristicDidUpdate:fromGroupUpdate:];
-[CAFPicker displayPanelIdentifierCharacteristic];
-[CAFPicker displayZoneIdentifierCharacteristic];
-[CAFPicker entryListCharacteristic];
-[CAFPicker identifierCharacteristic];
-[CAFPicker selectedEntryIndexCharacteristic];
-[CAFPicker selectedEntryIndexRange];
-[CAFPicker userSelectionEnabledCharacteristic];
```
