# `ASOctaneServer`

- Image: [`/System/Library/PrivateFrameworks/ASOctaneSupport.framework/ASOctaneSupport`](../userland/System__Library__PrivateFrameworks__ASOctaneSupport.framework__ASOctaneSupport.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSXPCConnection" _connectionToService;
```

## Class methods

```
+[ASOctaneServer shared];
```

## Instance methods

```
-[ASOctaneServer init];
-[ASOctaneServer _remoteObjectProxyWithErrorHandler:];
-[ASOctaneServer _synchronousRemoteObjectProxy:];
-[ASOctaneServer deleteAllTransactionsForBundleID:];
-[ASOctaneServer generateSKANPostbackSignature:];
-[ASOctaneServer getEncodedTransactionsForBundleID:withReply:];
-[ASOctaneServer getStringValueForIdentifier:forBundleID:];
-[ASOctaneServer validateSKAdNetworkSignature:withPublicKey:source:andParameters:forBundleID:];
```
