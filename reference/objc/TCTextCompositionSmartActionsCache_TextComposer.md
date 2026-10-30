# `TCTextCompositionSmartActionsCache`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 14 instance methods, 2 class methods

## Instance variables

```
@? _spotlightReader;
B _testingMode;
```

## Class methods

```
+[TCTextCompositionSmartActionsCache sharedCache];
+[TCTextCompositionSmartActionsCache messagesSmartActionsCache];
```

## Instance methods

```
-[TCTextCompositionSmartActionsCache clearCache];
-[TCTextCompositionSmartActionsCache init];
-[TCTextCompositionSmartActionsCache _cacheQueue];
-[TCTextCompositionSmartActionsCache _defaultSpotlightReader];
-[TCTextCompositionSmartActionsCache _getObject:cache:];
-[TCTextCompositionSmartActionsCache _isCachingSupported:isExternalAPICall:onComposeState:];
-[TCTextCompositionSmartActionsCache _setObject:forKey:cache:];
-[TCTextCompositionSmartActionsCache cacheKeyFor:];
-[TCTextCompositionSmartActionsCache cacheSmartActionResponse:inputContextHistory:mode:onComposeState:isExternalAPICall:];
-[TCTextCompositionSmartActionsCache cachedSmartActionResponse:mode:onComposeState:isExternalAPICall:completionHandler:];
-[TCTextCompositionSmartActionsCache enableTestingMode];
-[TCTextCompositionSmartActionsCache enableTestingModeWithSpotlightReader:];
-[TCTextCompositionSmartActionsCache messagesInLookbackWindow:];
-[TCTextCompositionSmartActionsCache mostRecentMessage:];
```
