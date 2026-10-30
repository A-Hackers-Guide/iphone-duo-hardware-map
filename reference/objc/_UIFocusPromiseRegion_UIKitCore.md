# `_UIFocusPromiseRegion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFocusRegion`
- 3 instance variables, 1 properties, 9 instance methods, 0 class methods

## Instance variables

```
@ _identifier;
Q _fullfillmentCount;
@? _contentFulfillmentHandler;
```

## Properties

```
@property (T@?,C,N,V_contentFulfillmentHandler) contentFulfillmentHandler;
```

## Instance methods

```
-[_UIFocusPromiseRegion isEqual:];
-[_UIFocusPromiseRegion _descriptionBuilder];
-[_UIFocusPromiseRegion _focusRegionWithAdjustedFrame:coordinateSpace:];
-[_UIFocusPromiseRegion _focusableBoundaries];
-[_UIFocusPromiseRegion _nextFocusedItemForFocusMovementRequest:inMap:withSnapshot:];
-[_UIFocusPromiseRegion contentFulfillmentHandler];
-[_UIFocusPromiseRegion initWithFrame:coordinateSpace:];
-[_UIFocusPromiseRegion initWithFrame:coordinateSpace:identifier:];
-[_UIFocusPromiseRegion setContentFulfillmentHandler:];
```
