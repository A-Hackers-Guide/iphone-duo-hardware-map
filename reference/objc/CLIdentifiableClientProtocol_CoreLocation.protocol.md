# `CLIdentifiableClientProtocol` (protocol)

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",&,N) identityToken;
@property (T@"NSData",&,N) storageToken;
@property (T@"CLLocationManager",&,N) manager;
@property (T@?,W,N) weakClient;
```

## Instance methods

```
-[CLIdentifiableClientProtocol storageToken];
-[CLIdentifiableClientProtocol setManager:];
-[CLIdentifiableClientProtocol setStorageToken:];
-[CLIdentifiableClientProtocol setWeakClient:];
-[CLIdentifiableClientProtocol manager];
-[CLIdentifiableClientProtocol identityToken];
-[CLIdentifiableClientProtocol setIdentityToken:];
-[CLIdentifiableClientProtocol weakClient];
-[CLIdentifiableClientProtocol updateIdentityToken:withStorageToken:];
```
