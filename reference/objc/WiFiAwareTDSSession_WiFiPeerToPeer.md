# `WiFiAwareTDSSession`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiP2PXPCConnectionDelegate`, `WiFiAwareTDSXPCDelegate`
- 4 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"WiFiP2PXPCConnection" _xpcConnection;
@"NSObject<OS_os_log>" _logger;
@"WiFiAwareTDSConfig" _tdsConfig;
@"<WiFiAwareTDSDelegate>" _delegate;
```

## Properties

```
@property (T@"WiFiAwareTDSConfig",&,N,V_tdsConfig) tdsConfig;
@property (T@"<WiFiAwareTDSDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WiFiAwareTDSSession handleError:];
-[WiFiAwareTDSSession deactivate];
-[WiFiAwareTDSSession startConnectionUsingProxy:completionHandler:];
-[WiFiAwareTDSSession remoteObjectInterface];
-[WiFiAwareTDSSession exportedInterface];
-[WiFiAwareTDSSession timedOut];
-[WiFiAwareTDSSession setDelegate:];
-[WiFiAwareTDSSession exportedObject];
-[WiFiAwareTDSSession activate];
-[WiFiAwareTDSSession delegate];
-[WiFiAwareTDSSession initWithTDSConfig:delegate:];
-[WiFiAwareTDSSession matchFound:transportState:];
-[WiFiAwareTDSSession pairedMatchFound:transportState:];
-[WiFiAwareTDSSession setTdsConfig:];
-[WiFiAwareTDSSession tdsConfig];
```
