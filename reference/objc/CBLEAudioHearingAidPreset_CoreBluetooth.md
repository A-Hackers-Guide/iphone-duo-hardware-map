# `CBLEAudioHearingAidPreset`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
C _presetIndex;
B _isWritable;
B _isAvailable;
@"NSString" _presetName;
```

## Properties

```
@property (TC,R,N,V_presetIndex) presetIndex;
@property (T@"NSString",R,&,N,V_presetName) presetName;
@property (TB,R,N,V_isWritable) isWritable;
@property (TB,R,N,V_isAvailable) isAvailable;
```

## Instance methods

```
-[CBLEAudioHearingAidPreset isAvailable];
-[CBLEAudioHearingAidPreset isWritable];
-[CBLEAudioHearingAidPreset presetName];
-[CBLEAudioHearingAidPreset presetIndex];
-[CBLEAudioHearingAidPreset initWithValues:withProperty:withName:];
```
