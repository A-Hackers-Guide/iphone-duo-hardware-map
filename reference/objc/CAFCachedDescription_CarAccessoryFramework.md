# `CAFCachedDescription`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _lazyRefreshDescription;
B _needsRefresh;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _cacheLock;
@"<CAFCacheableDescription>" _cacheable;
@"NSString" _cachedDescription;
```

## Properties

```
@property (T@"<CAFCacheableDescription>",W,N,V_cacheable) cacheable;
@property (T{os_unfair_lock_s=I},N,V_cacheLock) cacheLock;
@property (T@"NSString",&,N,V_cachedDescription) cachedDescription;
@property (TB,N,V_needsRefresh) needsRefresh;
@property (TB,N,V_lazyRefreshDescription) lazyRefreshDescription;
```

## Instance methods

```
-[CAFCachedDescription cacheable];
-[CAFCachedDescription cacheLock];
-[CAFCachedDescription cachedDescription];
-[CAFCachedDescription setNeedsRefresh:];
-[CAFCachedDescription needsRefresh];
-[CAFCachedDescription setCacheable:];
-[CAFCachedDescription setCachedDescription:];
-[CAFCachedDescription description];
-[CAFCachedDescription setCacheLock:];
-[CAFCachedDescription _lock_refreshDescriptionIfNeeded];
-[CAFCachedDescription initWithCacheable:];
-[CAFCachedDescription initWithCacheable:lazyRefreshDescription:];
-[CAFCachedDescription lazyRefreshDescription];
-[CAFCachedDescription setLazyRefreshDescription:];
-[CAFCachedDescription setNeedsRefreshDescription];
```
