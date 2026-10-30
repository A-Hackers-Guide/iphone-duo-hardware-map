# `NSPTokenFetcherImpl`

- Image: [`/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`](../userland/System__Library__PrivateFrameworks__IPTelephony.framework__Support__libIPTelephony.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSPTokenFetcherProtocol`
- 1 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSPPrivateAccessTokenFetcher" _fetcher;
```

## Properties

```
@property (TB) systemClient;
@property (T@"NSString",&) auxiliaryAuthenticationCacheKey;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[NSPTokenFetcherImpl setSystemClient:];
-[NSPTokenFetcherImpl systemClient];
-[NSPTokenFetcherImpl auxiliaryAuthenticationCacheKey];
-[NSPTokenFetcherImpl fetchTokenAndAuxiliaryAuthenticationWithQueue:completionHandler:];
-[NSPTokenFetcherImpl generateTokenRequestWithQueue:completionHandler:];
-[NSPTokenFetcherImpl handleTokenResponse:withQueue:completionHandler:];
-[NSPTokenFetcherImpl setAuxiliaryAuthenticationCacheKey:];
-[NSPTokenFetcherImpl initWithFetcher:];
```
