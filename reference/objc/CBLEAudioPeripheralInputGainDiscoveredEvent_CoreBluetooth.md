# `CBLEAudioPeripheralInputGainDiscoveredEvent`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBLEAudioPeripheralUpdateEvent`
- 4 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
C _audioInputType;
C _gainSettingUnit;
c _gainSettingMin;
c _gainSettingMax;
```

## Properties

```
@property (TC,R,N,V_audioInputType) audioInputType;
@property (TC,R,N,V_gainSettingUnit) gainSettingUnit;
@property (Tc,R,N,V_gainSettingMin) gainSettingMin;
@property (Tc,R,N,V_gainSettingMax) gainSettingMax;
```

## Instance methods

```
-[CBLEAudioPeripheralInputGainDiscoveredEvent gainSettingUnit];
-[CBLEAudioPeripheralInputGainDiscoveredEvent audioInputType];
-[CBLEAudioPeripheralInputGainDiscoveredEvent gainSettingMax];
-[CBLEAudioPeripheralInputGainDiscoveredEvent gainSettingMin];
-[CBLEAudioPeripheralInputGainDiscoveredEvent initWithValue:withDescription:andInputType:];
-[CBLEAudioPeripheralInputGainDiscoveredEvent setAudioInputGainSettingInfo:withGainMin:withGainMax:];
```
