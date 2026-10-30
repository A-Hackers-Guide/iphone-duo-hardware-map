# `CAFSoundDistributionPresets`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 5 properties, 14 instance methods, 2 class methods

## Properties

```
@property (T@"CAFPresetEntryListCharacteristic",R,N) presetEntryListCharacteristic;
@property (T@"CAFUInt8Characteristic",R,N) selectedPresetEntryIndexCharacteristic;
@property (T@"CAFPresetEntryList",R,N) presetEntryList;
@property (TC,N) selectedPresetEntryIndex;
@property (T@"CAFUInt8Range",R,N) selectedPresetEntryIndexRange;
```

## Class methods

```
+[CAFSoundDistributionPresets serviceIdentifier];
+[CAFSoundDistributionPresets observerProtocol];
```

## Instance methods

```
-[CAFSoundDistributionPresets removeObserver:];
-[CAFSoundDistributionPresets addObserver:];
-[CAFSoundDistributionPresets registerObserver:];
-[CAFSoundDistributionPresets name];
-[CAFSoundDistributionPresets unregisterObserver:];
-[CAFSoundDistributionPresets presetEntryList];
-[CAFSoundDistributionPresets registeredForPresetEntryList];
-[CAFSoundDistributionPresets registeredForSelectedPresetEntryIndex];
-[CAFSoundDistributionPresets selectedPresetEntryIndex];
-[CAFSoundDistributionPresets setSelectedPresetEntryIndex:];
-[CAFSoundDistributionPresets _characteristicDidUpdate:fromGroupUpdate:];
-[CAFSoundDistributionPresets presetEntryListCharacteristic];
-[CAFSoundDistributionPresets selectedPresetEntryIndexCharacteristic];
-[CAFSoundDistributionPresets selectedPresetEntryIndexRange];
```
