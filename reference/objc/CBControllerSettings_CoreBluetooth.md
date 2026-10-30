# `CBControllerSettings`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`
- 8 instance variables, 8 properties, 20 instance methods, 0 class methods

## Instance variables

```
c _gameControllerAutoSwitchMode;
c _gameControllerUSBBluetoothPairing;
c _hid3ppLELegacyMode;
c _setupAssistantIfNoKeyboard;
c _setupAssistantIfNoPointingDevice;
c _spatialSoundProfileAllowed;
c _bleAdvRSSI;
i _discoverableState;
```

## Properties

```
@property (Ti,N,V_discoverableState) discoverableState;
@property (Tc,N,V_gameControllerAutoSwitchMode) gameControllerAutoSwitchMode;
@property (Tc,N,V_gameControllerUSBBluetoothPairing) gameControllerUSBBluetoothPairing;
@property (Tc,N,V_hid3ppLELegacyMode) hid3ppLELegacyMode;
@property (Tc,N,V_setupAssistantIfNoKeyboard) setupAssistantIfNoKeyboard;
@property (Tc,N,V_setupAssistantIfNoPointingDevice) setupAssistantIfNoPointingDevice;
@property (Tc,N,V_spatialSoundProfileAllowed) spatialSoundProfileAllowed;
@property (Tc,N,V_bleAdvRSSI) bleAdvRSSI;
```

## Instance methods

```
-[CBControllerSettings encodeWithXPCObject:];
-[CBControllerSettings initWithXPCObject:error:];
-[CBControllerSettings descriptionWithLevel:];
-[CBControllerSettings discoverableState];
-[CBControllerSettings setDiscoverableState:];
-[CBControllerSettings description];
-[CBControllerSettings bleAdvRSSI];
-[CBControllerSettings gameControllerAutoSwitchMode];
-[CBControllerSettings gameControllerUSBBluetoothPairing];
-[CBControllerSettings hid3ppLELegacyMode];
-[CBControllerSettings setBleAdvRSSI:];
-[CBControllerSettings setGameControllerAutoSwitchMode:];
-[CBControllerSettings setGameControllerUSBBluetoothPairing:];
-[CBControllerSettings setHid3ppLELegacyMode:];
-[CBControllerSettings setSetupAssistantIfNoKeyboard:];
-[CBControllerSettings setSetupAssistantIfNoPointingDevice:];
-[CBControllerSettings setSpatialSoundProfileAllowed:];
-[CBControllerSettings setupAssistantIfNoKeyboard];
-[CBControllerSettings setupAssistantIfNoPointingDevice];
-[CBControllerSettings spatialSoundProfileAllowed];
```
