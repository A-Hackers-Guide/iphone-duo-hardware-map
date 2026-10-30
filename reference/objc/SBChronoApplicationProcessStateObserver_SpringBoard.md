# `SBChronoApplicationProcessStateObserver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"CHSInteractionEventService" _service;
@"CHSWidgetExtensionProvider" _extensionProvider;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Class methods

```
+[SBChronoApplicationProcessStateObserver sharedInstance];
```

## Instance methods

```
-[SBChronoApplicationProcessStateObserver init];
-[SBChronoApplicationProcessStateObserver _queue_handleApplicationProcessStateDidChangeIfNecessary:];
-[SBChronoApplicationProcessStateObserver _shouldInformChronoForApplication:];
-[SBChronoApplicationProcessStateObserver applicationProcessStateDidChange:];
```
