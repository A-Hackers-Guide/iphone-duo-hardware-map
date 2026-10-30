# `WiFiP2PSPITransactionRequestor`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiP2PXPCConnectionDelegate`
- 2 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _openTransactions;
@"WiFiP2PXPCConnection" _xpcConnection;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[WiFiP2PSPITransactionRequestor shared];
```

## Instance methods

```
-[WiFiP2PSPITransactionRequestor startConnectionUsingProxy:completionHandler:];
-[WiFiP2PSPITransactionRequestor init];
-[WiFiP2PSPITransactionRequestor remoteObjectInterface];
-[WiFiP2PSPITransactionRequestor endTransaction:];
-[WiFiP2PSPITransactionRequestor beginTransaction:completionHandler:];
-[WiFiP2PSPITransactionRequestor endTransaction:completionHandler:];
-[WiFiP2PSPITransactionRequestor _removeOpenTransaction:];
-[WiFiP2PSPITransactionRequestor handleConnectionEstablishedWithProxy:];
```
