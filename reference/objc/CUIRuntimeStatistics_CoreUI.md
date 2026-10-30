# `CUIRuntimeStatistics`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 0 properties, 9 instance methods, 2 class methods

## Instance variables

```
Aq _wasted_size;
Aq _total_size;
Aq _shortCircuitImageLookup;
Aq _total_lookup;
Aq _total_probes;
Aq _total_initial_lookups;
Aq _missed_lookup;
@"NSObject<OS_dispatch_queue>" _queue;
i _notify_token;
```

## Class methods

```
+[CUIRuntimeStatistics generateLog];
+[CUIRuntimeStatistics sharedRuntimeStatistics];
```

## Instance methods

```
-[CUIRuntimeStatistics init];
-[CUIRuntimeStatistics dealloc];
-[CUIRuntimeStatistics incrementStaticsInitialLookup];
-[CUIRuntimeStatistics incrementStatisticDidShortCircuitImageLookup];
-[CUIRuntimeStatistics shortCircuitImageLookup];
-[CUIRuntimeStatistics incrementStatisticLookup];
-[CUIRuntimeStatistics incrementStaticsProbe];
-[CUIRuntimeStatistics addStatisticAllocatedImageSize:roundedSize:];
-[CUIRuntimeStatistics incrementMissedLookup];
```
