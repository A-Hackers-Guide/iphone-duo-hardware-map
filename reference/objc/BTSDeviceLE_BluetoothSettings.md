# `BTSDeviceLE`

- Image: [`/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings`](../userland/System__Library__PreferenceBundles__BluetoothSettings.bundle__BluetoothSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BTSDevice`
- Protocols: `NSStreamDelegate`
- 12 instance variables, 7 properties, 57 instance methods, 1 class methods

## Instance variables

```
@"CBPeripheral" _peripheral;
@"CBCentralManager" _centralManager;
B healthDevice;
B ctkdDevice;
B managedByWallet;
B managedByAliroWallet;
B supportsBackgroundNI;
B managedByDeviceAccess;
B denyIncomingClassicConnection;
@"DADevice" _underlyingDADevice;
@"CBL2CAPChannel" _channelSoundingL2CAP;
@"NSMutableArray" _channelSoundingTXQueue;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_channelSoundingTXQueue) channelSoundingTXQueue;
@property (T@"DADevice",&,N,V_underlyingDADevice) underlyingDADevice;
@property (T@"CBL2CAPChannel",&,N,V_channelSoundingL2CAP) channelSoundingL2CAP;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BTSDeviceLE deviceWithPeripheral:manager:];
```

## Instance methods

```
-[BTSDeviceLE connected];
-[BTSDeviceLE connect];
-[BTSDeviceLE identifier];
-[BTSDeviceLE productName];
-[BTSDeviceLE paired];
-[BTSDeviceLE disconnect];
-[BTSDeviceLE description];
-[BTSDeviceLE stream:handleEvent:];
-[BTSDeviceLE name];
-[BTSDeviceLE unpair];
-[BTSDeviceLE setUserName:];
-[BTSDeviceLE setUnderlyingDADevice:];
-[BTSDeviceLE underlyingDADevice];
-[BTSDeviceLE isHIDDevice];
-[BTSDeviceLE classicDevice];
-[BTSDeviceLE ancsAuthorized];
-[BTSDeviceLE cloudPaired];
-[BTSDeviceLE doesSupportBackgroundNI];
-[BTSDeviceLE healthDeviceType];
-[BTSDeviceLE isCTKDDevice];
-[BTSDeviceLE isFirmwareUpdateRequiredDevice];
-[BTSDeviceLE isLimitedConnectivityDevice];
-[BTSDeviceLE isManagedByAliroWallet];
-[BTSDeviceLE isManagedByWallet];
-[BTSDeviceLE setANCSAuthorization:];
-[BTSDeviceLE setCtkdDevice:];
-[BTSDeviceLE setManagedByAliroWallet:];
-[BTSDeviceLE setManagedByWallet:];
-[BTSDeviceLE setSupportsBackgroundNI:];
-[BTSDeviceLE setUserSelectedHealthDataSyncConfig:];
-[BTSDeviceLE supportsANCS];
-[BTSDeviceLE userSelectedHealthDataSyncConfig];
-[BTSDeviceLE walletPassUID];
-[BTSDeviceLE isCarPlayDevice];
-[BTSDeviceLE initWithPeripheral:manager:];
-[BTSDeviceLE isApplePencil:];
-[BTSDeviceLE isHealthDevice];
-[BTSDeviceLE isManagedByDeviceAccess];
-[BTSDeviceLE isMyDevice];
-[BTSDeviceLE isPSVR2Controller];
-[BTSDeviceLE isTemporaryPairedDevice];
-[BTSDeviceLE linkedRadioAddress];
-[BTSDeviceLE relatedFutureRadioAddress];
-[BTSDeviceLE setDenyIncomingClassicConnection:];
-[BTSDeviceLE setHealthDevice:];
-[BTSDeviceLE shouldDenyIncomingClassicConnection];
-[BTSDeviceLE supportsCTKD];
-[BTSDeviceLE channelSoundingL2CAP];
-[BTSDeviceLE channelSoundingTXQueue];
-[BTSDeviceLE closeChannelSoundingL2CAP];
-[BTSDeviceLE isLEAudioSupported];
-[BTSDeviceLE isSpatialController];
-[BTSDeviceLE openChannelSoundingL2CAP];
-[BTSDeviceLE sendChannelSoundingResults:];
-[BTSDeviceLE sendNextChannelSoundingMessage];
-[BTSDeviceLE setChannelSoundingL2CAP:];
-[BTSDeviceLE setChannelSoundingTXQueue:];
```
