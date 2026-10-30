# `AVURLAssetInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
@"AVAssetInspectorLoader" loader;
@"AVAssetClientURLRequestHelper" URLRequestHelper;
@"AVAssetCustomURLBridgeForNSURLProtocol" customURLBridgeForNSURLProtocol;
@"AVAssetCustomURLAuthentication" customURLAuthenticationUsingKeychain;
@"NSURL" URL;
@"NSArray" tracks;
@"AVAssetResourceLoader" resourceLoader;
@"AVDispatchOnce" makeOneResourceLoaderOnly;
@"AVAssetCache" assetCache;
@"AVDispatchOnce" makeOneAssetDownloadCacheOnly;
@"NSObject<OS_dispatch_queue>" tracksAccessQueue;
@"NSDictionary" initializationOptions;
B hasInstanceIdentifierMapping;
B requiresSecurityScopeRelease;
B allowsExpensiveNetworkAccess;
B allowsConstrainedNetworkAccess;
@"AVWeakReference" sessionReference;
```
