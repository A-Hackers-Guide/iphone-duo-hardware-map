# `CBLEAudioHearingAidUpdateEvent`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBLEAudioPeripheralUpdateEvent`
- 2 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _presetResults;
@"CBLEAudioHearingAidPreset" _activePreset;
```

## Properties

```
@property (T@"NSMutableArray",C,N,V_presetResults) presetResults;
@property (T@"CBLEAudioHearingAidPreset",C,N,V_activePreset) activePreset;
```

## Instance methods

```
-[CBLEAudioHearingAidUpdateEvent initWithEventType:];
-[CBLEAudioHearingAidUpdateEvent activePreset];
-[CBLEAudioHearingAidUpdateEvent presetResults];
-[CBLEAudioHearingAidUpdateEvent initWithValue:withValue:];
-[CBLEAudioHearingAidUpdateEvent setActivePreset:];
-[CBLEAudioHearingAidUpdateEvent setPresetResults:];
```
