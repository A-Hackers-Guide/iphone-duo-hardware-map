# `CHDefaultHapticDeviceCapability`

- Image: [`/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`](../userland/System__Library__Frameworks__CoreHaptics.framework__CoreHaptics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CHHapticDeviceCapability`
- 2 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _supportsHaptics;
B _supportsAudio;
```

## Properties

```
@property (TQ,R) maximumNumberOfHapticChannels;
@property (TQ,R) maximumNumberOfAudioChannels;
@property (TB,R) supportsHaptics;
@property (TB,R) supportsAudio;
```

## Instance methods

```
-[CHDefaultHapticDeviceCapability maximumNumberOfHapticChannels];
-[CHDefaultHapticDeviceCapability attributesForEventParameter:eventType:error:];
-[CHDefaultHapticDeviceCapability init];
-[CHDefaultHapticDeviceCapability supportsAudio];
-[CHDefaultHapticDeviceCapability initPrivate];
-[CHDefaultHapticDeviceCapability supportsHaptics];
-[CHDefaultHapticDeviceCapability defaultValueForDynamicParameter:];
-[CHDefaultHapticDeviceCapability attributesForDynamicParameter:error:];
-[CHDefaultHapticDeviceCapability minimumValueForEventParameter:];
-[CHDefaultHapticDeviceCapability defaultValueForEventParameter:eventType:];
-[CHDefaultHapticDeviceCapability maximumValueForDynamicParameter:];
-[CHDefaultHapticDeviceCapability maximumNumberOfAudioChannels];
-[CHDefaultHapticDeviceCapability maximumValueForEventParameter:];
-[CHDefaultHapticDeviceCapability minimumValueForDynamicParameter:];
```
