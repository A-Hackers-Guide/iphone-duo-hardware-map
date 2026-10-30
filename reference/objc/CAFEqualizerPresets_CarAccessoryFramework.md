# `CAFEqualizerPresets`

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
+[CAFEqualizerPresets serviceIdentifier];
+[CAFEqualizerPresets observerProtocol];
```

## Instance methods

```
-[CAFEqualizerPresets removeObserver:];
-[CAFEqualizerPresets addObserver:];
-[CAFEqualizerPresets registerObserver:];
-[CAFEqualizerPresets name];
-[CAFEqualizerPresets unregisterObserver:];
-[CAFEqualizerPresets presetEntryList];
-[CAFEqualizerPresets registeredForPresetEntryList];
-[CAFEqualizerPresets registeredForSelectedPresetEntryIndex];
-[CAFEqualizerPresets selectedPresetEntryIndex];
-[CAFEqualizerPresets setSelectedPresetEntryIndex:];
-[CAFEqualizerPresets _characteristicDidUpdate:fromGroupUpdate:];
-[CAFEqualizerPresets presetEntryListCharacteristic];
-[CAFEqualizerPresets selectedPresetEntryIndexCharacteristic];
-[CAFEqualizerPresets selectedPresetEntryIndexRange];
```
