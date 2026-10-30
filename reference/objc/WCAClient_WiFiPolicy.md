# `WCAClient`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
q _changeCounter;
@"NSXPCConnection" _connectionToService;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_connectionToService) connectionToService;
```

## Class methods

```
+[WCAClient sharedClient];
```

## Instance methods

```
-[WCAClient init];
-[WCAClient executeFetchRequest:];
-[WCAClient _establishDaemonConnection];
-[WCAClient _invalidateDaemonConnectionIfPossible];
-[WCAClient connectionToService];
-[WCAClient fetchWiFiAssetsFromServer];
-[WCAClient setConnectionToService:];
```
