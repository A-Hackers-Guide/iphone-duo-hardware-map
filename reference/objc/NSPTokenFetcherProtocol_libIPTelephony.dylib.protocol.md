# `NSPTokenFetcherProtocol` (protocol)

- Image: [`/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`](../userland/System__Library__PrivateFrameworks__IPTelephony.framework__Support__libIPTelephony.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 7 instance methods, 0 class methods

## Properties

```
@property (TB) systemClient;
@property (T@"NSString",&) auxiliaryAuthenticationCacheKey;
```

## Instance methods

```
-[NSPTokenFetcherProtocol setSystemClient:];
-[NSPTokenFetcherProtocol systemClient];
-[NSPTokenFetcherProtocol auxiliaryAuthenticationCacheKey];
-[NSPTokenFetcherProtocol fetchTokenAndAuxiliaryAuthenticationWithQueue:completionHandler:];
-[NSPTokenFetcherProtocol generateTokenRequestWithQueue:completionHandler:];
-[NSPTokenFetcherProtocol handleTokenResponse:withQueue:completionHandler:];
-[NSPTokenFetcherProtocol setAuxiliaryAuthenticationCacheKey:];
```
