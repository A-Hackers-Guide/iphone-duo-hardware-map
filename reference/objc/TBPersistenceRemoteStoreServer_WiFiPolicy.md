# `TBPersistenceRemoteStoreServer`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSXPCStoreServer" _xpcStoreServer;
@"NSURL" _storeURL;
@"NSURL" _modelURL;
@"NSDictionary" _serverOptions;
```

## Properties

```
@property (T@"NSXPCStoreServer",&,N,V_xpcStoreServer) xpcStoreServer;
@property (T@"NSURL",&,N,V_storeURL) storeURL;
@property (T@"NSURL",&,N,V_modelURL) modelURL;
@property (T@"NSDictionary",&,N,V_serverOptions) serverOptions;
```

## Instance methods

```
-[TBPersistenceRemoteStoreServer storeURL];
-[TBPersistenceRemoteStoreServer startListening];
-[TBPersistenceRemoteStoreServer setStoreURL:];
-[TBPersistenceRemoteStoreServer modelURL];
-[TBPersistenceRemoteStoreServer setModelURL:];
-[TBPersistenceRemoteStoreServer initWithStoreURL:modelURL:options:];
-[TBPersistenceRemoteStoreServer serverOptions];
-[TBPersistenceRemoteStoreServer setServerOptions:];
-[TBPersistenceRemoteStoreServer setXpcStoreServer:];
-[TBPersistenceRemoteStoreServer xpcStoreServer];
```
