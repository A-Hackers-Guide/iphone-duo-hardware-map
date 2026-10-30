# `WiFiAwareDevicesStore`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiAwarePairedDevicesXPCDelegate`, `WiFiP2PXPCConnectionDelegate`
- 2 instance variables, 5 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"WiFiP2PXPCConnection" _xpcConnection;
@"<WiFiAwareDevicesStoreDelegate>" _delegate;
```

## Properties

```
@property (T@"<WiFiAwareDevicesStoreDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WiFiAwareDevicesStore deactivate];
-[WiFiAwareDevicesStore startConnectionUsingProxy:completionHandler:];
-[WiFiAwareDevicesStore init];
-[WiFiAwareDevicesStore remoteObjectInterface];
-[WiFiAwareDevicesStore exportedInterface];
-[WiFiAwareDevicesStore setDelegate:];
-[WiFiAwareDevicesStore exportedObject];
-[WiFiAwareDevicesStore activate];
-[WiFiAwareDevicesStore delegate];
-[WiFiAwareDevicesStore queryPairedDevicesInfo:];
-[WiFiAwareDevicesStore removeAllPairedDevices];
-[WiFiAwareDevicesStore removeAllPairedDevicesFor:completionHandler:];
-[WiFiAwareDevicesStore authorizeNewPairedDeviceFor:pairingKeyStoreID:storageClass:lifetime:client:completionHandler:];
-[WiFiAwareDevicesStore authorizeNewPairedDeviceFor:pairingKeyStoreID:storageClass:lifetime:client:error:];
-[WiFiAwareDevicesStore deauthorizePairedDeviceFor:withDeviceID:remove:];
-[WiFiAwareDevicesStore deauthorizePairedDeviceFor:withDeviceID:remove:completionHandler:];
-[WiFiAwareDevicesStore pairedDeviceAdded:];
-[WiFiAwareDevicesStore pairedDeviceChanged:];
-[WiFiAwareDevicesStore pairedDeviceRemoved:];
-[WiFiAwareDevicesStore reauthorizePairedDeviceFor:withDeviceID:];
-[WiFiAwareDevicesStore reauthorizePairedDeviceFor:withDeviceID:completionHandler:];
-[WiFiAwareDevicesStore removeAllPairedDevices:];
-[WiFiAwareDevicesStore removeAllPairedDevicesFor:];
-[WiFiAwareDevicesStore removePairedDeviceFor:withDeviceID:];
-[WiFiAwareDevicesStore removePairedDeviceFor:withDeviceID:completionHandler:];
-[WiFiAwareDevicesStore uninstallPairedDeviceFor:withDeviceID:];
-[WiFiAwareDevicesStore uninstallPairedDeviceFor:withDeviceID:completionHandler:];
-[WiFiAwareDevicesStore updatePairedDeviceNameFor:withDeviceID:toNewName:];
-[WiFiAwareDevicesStore updatePairedDeviceNameFor:withDeviceID:toNewName:completionHandler:];
```
