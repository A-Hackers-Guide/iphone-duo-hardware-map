# `WiFiAwareDatapathInfo`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiP2PXPCConnectionDelegate`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"WiFiP2PXPCConnection" _xpcConnection;
C _datapathID;
q _role;
@"WiFiMACAddress" _peerMacAddress;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WiFiAwareDatapathInfo handleError:];
-[WiFiAwareDatapathInfo deactivate];
-[WiFiAwareDatapathInfo startConnectionUsingProxy:completionHandler:];
-[WiFiAwareDatapathInfo remoteObjectInterface];
-[WiFiAwareDatapathInfo activate];
-[WiFiAwareDatapathInfo deriveSharedSecretForProtocolName:context:derivationMethod:completion:];
-[WiFiAwareDatapathInfo initWithDatapathID:role:peerMacAddress:];
-[WiFiAwareDatapathInfo performance:];
```
