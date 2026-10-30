# `TCTextCompositionSmartRepliesCache`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 12 instance methods, 4 class methods

## Instance variables

```
@"_TtC12TextComposer32TCTextCompositionSpotlightReader" _spotlightReader;
B _testingMode;
```

## Class methods

```
+[TCTextCompositionSmartRepliesCache sharedCache];
+[TCTextCompositionSmartRepliesCache messagesSRCache];
+[TCTextCompositionSmartRepliesCache cacheForCompositionMode:];
+[TCTextCompositionSmartRepliesCache mailSRCache];
```

## Instance methods

```
-[TCTextCompositionSmartRepliesCache init];
-[TCTextCompositionSmartRepliesCache _cacheQueue];
-[TCTextCompositionSmartRepliesCache _getObject:cache:];
-[TCTextCompositionSmartRepliesCache _setObject:forKey:cache:];
-[TCTextCompositionSmartRepliesCache bundleIDFrom:];
-[TCTextCompositionSmartRepliesCache cacheKeyFor:threadIdentifier:mode:];
-[TCTextCompositionSmartRepliesCache cacheSmartRepliesResponse:inputContextHistory:threadIdentifier:mode:isExternalAPICall:];
-[TCTextCompositionSmartRepliesCache cachedResponse:threadIdentifier:mode:isExternalAPICall:completionHandler:];
-[TCTextCompositionSmartRepliesCache disableTestingMode];
-[TCTextCompositionSmartRepliesCache enableTestingMode];
-[TCTextCompositionSmartRepliesCache mostRecentMessage:];
-[TCTextCompositionSmartRepliesCache mostRecentMessages:mode:];
```
