# `AVAssetResourceLoaderRemoteHandlerContext`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_xpc_object>" _endpoint;
Q _customURLHandlerObjectID;
Q _authHandlerObjectID;
Q _contentKeySessionHandlerObjectID;
```

## Properties

```
@property (T@"NSObject<OS_xpc_object>",R,N,V_endpoint) endpoint;
@property (TQ,R,N,V_customURLHandlerObjectID) customURLHandlerObjectID;
@property (TQ,R,N,V_authHandlerObjectID) authHandlerObjectID;
@property (TQ,R,N,V_contentKeySessionHandlerObjectID) contentKeySessionHandlerObjectID;
```

## Class methods

```
+[AVAssetResourceLoaderRemoteHandlerContext supportsSecureCoding];
```

## Instance methods

```
-[AVAssetResourceLoaderRemoteHandlerContext dealloc];
-[AVAssetResourceLoaderRemoteHandlerContext endpoint];
-[AVAssetResourceLoaderRemoteHandlerContext encodeWithCoder:];
-[AVAssetResourceLoaderRemoteHandlerContext initWithCoder:];
-[AVAssetResourceLoaderRemoteHandlerContext authHandlerObjectID];
-[AVAssetResourceLoaderRemoteHandlerContext contentKeySessionHandlerObjectID];
-[AVAssetResourceLoaderRemoteHandlerContext customURLHandlerObjectID];
-[AVAssetResourceLoaderRemoteHandlerContext initWithEndpoint:customURLHandlerObjectID:authHandlerObjectID:contentKeySessionHandlerObjectID:];
```
