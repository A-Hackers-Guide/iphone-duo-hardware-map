# `BTSDevice`

- Image: [`/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings`](../userland/System__Library__PreferenceBundles__BluetoothSettings.bundle__BluetoothSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 13 properties, 53 instance methods, 0 class methods

## Instance variables

```
B _isChannelSoundingDevice;
@"NSString" _walletPassUID;
@"NSString" _accessorySetupKitDisplayName;
@"NSString" _relatedFutureRadioAddress;
@"NSString" _linkedRadioAddress;
```

## Properties

```
@property (TB,N,GisHealthDevice) healthDevice;
@property (TB,R,N,GisMyDevice) myDevice;
@property (TB,N,GisCTKDDevice) ctkdDevice;
@property (TB,N,GisManagedByWallet) managedByWallet;
@property (TB,N,GisManagedByAliroWallet) managedByAliroWallet;
@property (T@"NSString",C,N,GwalletPassUID,V_walletPassUID) walletPassUID;
@property (TB,N,GdoesSupportBackgroundNI) supportsBackgroundNI;
@property (TB,R,N,GisManagedByDeviceAccess) managedByDeviceAccess;
@property (TB,N,GshouldDenyIncomingClassicConnection) denyIncomingClassicConnection;
@property (T@"NSString",&,N,V_accessorySetupKitDisplayName) accessorySetupKitDisplayName;
@property (T@"NSString",&,N,GrelatedFutureRadioAddress,V_relatedFutureRadioAddress) relatedFutureRadioAddress;
@property (T@"NSString",&,N,GlinkedRadioAddress,V_linkedRadioAddress) linkedRadioAddress;
@property (TB,N,GisChannelSoundingDevice,V_isChannelSoundingDevice) isChannelSoundingDevice;
```

## Instance methods

```
-[BTSDevice connected];
-[BTSDevice connect];
-[BTSDevice isiPad];
-[BTSDevice identifier];
-[BTSDevice compare:];
-[BTSDevice productName];
-[BTSDevice paired];
-[BTSDevice disconnect];
-[BTSDevice hash];
-[BTSDevice isEqual:];
-[BTSDevice name];
-[BTSDevice unpair];
-[BTSDevice isHIDDevice];
-[BTSDevice classicDevice];
-[BTSDevice ancsAuthorized];
-[BTSDevice cloudPaired];
-[BTSDevice doesSupportBackgroundNI];
-[BTSDevice healthDeviceType];
-[BTSDevice isCTKDDevice];
-[BTSDevice isFirmwareUpdateRequiredDevice];
-[BTSDevice isLimitedConnectivityDevice];
-[BTSDevice isManagedByAliroWallet];
-[BTSDevice isManagedByWallet];
-[BTSDevice setANCSAuthorization:];
-[BTSDevice setCtkdDevice:];
-[BTSDevice setManagedByAliroWallet:];
-[BTSDevice setManagedByWallet:];
-[BTSDevice setSupportsBackgroundNI:];
-[BTSDevice setUserSelectedHealthDataSyncConfig:];
-[BTSDevice setWalletPassUID:];
-[BTSDevice supportsANCS];
-[BTSDevice userSelectedHealthDataSyncConfig];
-[BTSDevice walletPassUID];
-[BTSDevice isCarPlayDevice];
-[BTSDevice accessorySetupKitDisplayName];
-[BTSDevice isApplePencil:];
-[BTSDevice isHealthDevice];
-[BTSDevice isManagedByDeviceAccess];
-[BTSDevice isMyDevice];
-[BTSDevice isPSVR2Controller];
-[BTSDevice isTemporaryPairedDevice];
-[BTSDevice linkedRadioAddress];
-[BTSDevice relatedFutureRadioAddress];
-[BTSDevice setAccessorySetupKitDisplayName:];
-[BTSDevice setDenyIncomingClassicConnection:];
-[BTSDevice setHealthDevice:];
-[BTSDevice setLinkedRadioAddress:];
-[BTSDevice setRelatedFutureRadioAddress:];
-[BTSDevice shouldDenyIncomingClassicConnection];
-[BTSDevice isChannelSoundingDevice];
-[BTSDevice isLEAudioSupported];
-[BTSDevice isSpatialController];
-[BTSDevice setIsChannelSoundingDevice:];
```
