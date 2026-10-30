# `BTSDeviceClassic`

- Image: [`/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings`](../userland/System__Library__PreferenceBundles__BluetoothSettings.bundle__BluetoothSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BTSDevice`
- 8 instance variables, 1 properties, 44 instance methods, 1 class methods

## Instance variables

```
@"BluetoothDevice" _device;
B ctkdDevice;
B managedByWallet;
B managedByAliroWallet;
B supportsBackgroundNI;
B managedByDeviceAccess;
B denyIncomingClassicConnection;
@"NSString" accessorySetupKitDisplayName;
```

## Properties

```
@property (T@"BluetoothDevice",R,W,N,V_device) device;
```

## Class methods

```
+[BTSDeviceClassic deviceWithDevice:];
```

## Instance methods

```
-[BTSDeviceClassic connected];
-[BTSDeviceClassic connect];
-[BTSDeviceClassic initWithDevice:];
-[BTSDeviceClassic identifier];
-[BTSDeviceClassic device];
-[BTSDeviceClassic productName];
-[BTSDeviceClassic paired];
-[BTSDeviceClassic disconnect];
-[BTSDeviceClassic description];
-[BTSDeviceClassic name];
-[BTSDeviceClassic unpair];
-[BTSDeviceClassic magicPaired];
-[BTSDeviceClassic setUserName:];
-[BTSDeviceClassic isHIDDevice];
-[BTSDeviceClassic classicDevice];
-[BTSDeviceClassic ancsAuthorized];
-[BTSDeviceClassic cloudPaired];
-[BTSDeviceClassic doesSupportBackgroundNI];
-[BTSDeviceClassic healthDeviceType];
-[BTSDeviceClassic isCTKDDevice];
-[BTSDeviceClassic isFirmwareUpdateRequiredDevice];
-[BTSDeviceClassic isLimitedConnectivityDevice];
-[BTSDeviceClassic isManagedByAliroWallet];
-[BTSDeviceClassic isManagedByWallet];
-[BTSDeviceClassic setANCSAuthorization:];
-[BTSDeviceClassic setCtkdDevice:];
-[BTSDeviceClassic setManagedByAliroWallet:];
-[BTSDeviceClassic setManagedByWallet:];
-[BTSDeviceClassic setSupportsBackgroundNI:];
-[BTSDeviceClassic supportsANCS];
-[BTSDeviceClassic userSelectedHealthDataSyncConfig];
-[BTSDeviceClassic walletPassUID];
-[BTSDeviceClassic isCarPlayDevice];
-[BTSDeviceClassic accessorySetupKitDisplayName];
-[BTSDeviceClassic isApplePencil:];
-[BTSDeviceClassic isHealthDevice];
-[BTSDeviceClassic isManagedByDeviceAccess];
-[BTSDeviceClassic isMyDevice];
-[BTSDeviceClassic isPSVR2Controller];
-[BTSDeviceClassic isTemporaryPairedDevice];
-[BTSDeviceClassic setAccessorySetupKitDisplayName:];
-[BTSDeviceClassic setDenyIncomingClassicConnection:];
-[BTSDeviceClassic shouldDenyIncomingClassicConnection];
-[BTSDeviceClassic isSpatialController];
```
