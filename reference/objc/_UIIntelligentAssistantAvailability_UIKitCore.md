# `_UIIntelligentAssistantAvailability`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
B _cachedAvailable;
@"GMAvailabilityObservation" _observation;
```

## Properties

```
@property (TB,R,N,GisAvailable) available;
```

## Class methods

```
+[_UIIntelligentAssistantAvailability sharedAvailability];
```

## Instance methods

```
-[_UIIntelligentAssistantAvailability isAvailable];
-[_UIIntelligentAssistantAvailability init];
-[_UIIntelligentAssistantAvailability dealloc];
-[_UIIntelligentAssistantAvailability _availabilityDidChange];
-[_UIIntelligentAssistantAvailability _computeAvailable];
```
