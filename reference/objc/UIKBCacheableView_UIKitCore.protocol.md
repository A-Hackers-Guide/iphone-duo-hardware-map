# `UIKBCacheableView` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 7 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,N) cacheKey;
@property (TB,R,N) cacheDeferable;
@property (Td,R,N) cachedWidth;
@property (TB,R,N) keepNonPersistent;
@property (TB,R,N) displaysColorImage;
@property (Tq,R,N) assetIdiom;
@property (Tq,?,R,N) cacheDeferPriority;
```

## Instance methods

```
-[UIKBCacheableView assetIdiom];
-[UIKBCacheableView cachedWidth];
-[UIKBCacheableView cacheKey];
-[UIKBCacheableView keepNonPersistent];
-[UIKBCacheableView displaysColorImage];
-[UIKBCacheableView cacheKeysForRenderFlags:];
-[UIKBCacheableView cacheDeferable];
-[UIKBCacheableView drawContentsOfRenderers:];
-[UIKBCacheableView cacheDeferPriority];
```
