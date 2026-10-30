# `AVAssetCustomURLAuthentication`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 3 instance methods, 2 class methods

## Instance variables

```
^{OpaqueFigCustomURLHandler=} _handler;
@"NSObject<OS_dispatch_queue>" _callbackQueue;
```

## Class methods

```
+[AVAssetCustomURLAuthentication copyKeychainCredentialForUrl:];
+[AVAssetCustomURLAuthentication sendAuthResponse:requestID:disposition:credential:authHandler:];
```

## Instance methods

```
-[AVAssetCustomURLAuthentication dealloc];
-[AVAssetCustomURLAuthentication initWithFigAsset:];
-[AVAssetCustomURLAuthentication _handleAuthChallenge:requestID:canHandleRequestOut:];
```
