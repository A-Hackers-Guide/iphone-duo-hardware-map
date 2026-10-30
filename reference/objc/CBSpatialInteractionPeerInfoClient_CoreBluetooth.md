# `CBSpatialInteractionPeerInfoClient`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
I _peerID;
I _uwbTokenFlags;
@"NSData" _tokenData;
@"NSDictionary" _userInfo;
```

## Properties

```
@property (TI,N,V_peerID) peerID;
@property (T@"NSData",C,N,V_tokenData) tokenData;
@property (T@"NSDictionary",C,N,V_userInfo) userInfo;
@property (TI,N,V_uwbTokenFlags) uwbTokenFlags;
```

## Instance methods

```
-[CBSpatialInteractionPeerInfoClient peerID];
-[CBSpatialInteractionPeerInfoClient userInfo];
-[CBSpatialInteractionPeerInfoClient setUserInfo:];
-[CBSpatialInteractionPeerInfoClient setPeerID:];
-[CBSpatialInteractionPeerInfoClient setTokenData:];
-[CBSpatialInteractionPeerInfoClient tokenData];
-[CBSpatialInteractionPeerInfoClient setUwbTokenFlags:];
-[CBSpatialInteractionPeerInfoClient uwbTokenFlags];
```
