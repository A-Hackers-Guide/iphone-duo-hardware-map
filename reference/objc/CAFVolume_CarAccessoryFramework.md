# `CAFVolume`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 12 properties, 25 instance methods, 3 class methods

## Properties

```
@property (T@"CAFVolumeTypeCharacteristic",R,N) volumeTypeCharacteristic;
@property (T@"CAFUInt8Characteristic",R,N) volumeCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleLabelCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) muteCharacteristic;
@property (TC,R,N) volumeType;
@property (TC,N) volume;
@property (T@"CAFUInt8Range",R,N) volumeRange;
@property (TB,R,N) volumeDisabled;
@property (T@"NSString",R,N) userVisibleLabel;
@property (TB,R,N) hasUserVisibleLabel;
@property (TB,N) mute;
@property (TB,R,N) hasMute;
```

## Class methods

```
+[CAFVolume serviceIdentifier];
+[CAFVolume observerProtocol];
+[CAFVolume typeComparator];
```

## Instance methods

```
-[CAFVolume mute];
-[CAFVolume volume];
-[CAFVolume removeObserver:];
-[CAFVolume setVolume:];
-[CAFVolume addObserver:];
-[CAFVolume registerObserver:];
-[CAFVolume name];
-[CAFVolume unregisterObserver:];
-[CAFVolume setMute:];
-[CAFVolume volumeType];
-[CAFVolume hasMute];
-[CAFVolume registeredForMute];
-[CAFVolume registeredForUserVisibleLabel];
-[CAFVolume registeredForVolume];
-[CAFVolume registeredForVolumeType];
-[CAFVolume userVisibleLabel];
-[CAFVolume volumeDisabled];
-[CAFVolume volumeRange];
-[CAFVolume _characteristicDidUpdate:fromGroupUpdate:];
-[CAFVolume hasUserVisibleLabel];
-[CAFVolume muteCharacteristic];
-[CAFVolume typeCompare:];
-[CAFVolume userVisibleLabelCharacteristic];
-[CAFVolume volumeCharacteristic];
-[CAFVolume volumeTypeCharacteristic];
```
