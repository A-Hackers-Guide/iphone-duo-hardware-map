# `SBFlexibleWindowingAutoLayoutGroup`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
Q _hash;
@"NSArray" _cached_displayItemsInGroup;
@"NSArray" _itemsInGroup;
d _intersectionHeight;
{CGPoint="x"d"y"d} _resizeGrabberPosition;
```

## Properties

```
@property (T@"NSArray",R,N,V_itemsInGroup) itemsInGroup;
@property (T@"NSArray",R,N,V_cached_displayItemsInGroup) displayItemsInGroup;
@property (T{CGPoint=dd},R,N,V_resizeGrabberPosition) resizeGrabberPosition;
@property (Td,R,N,V_intersectionHeight) intersectionHeight;
```

## Instance methods

```
-[SBFlexibleWindowingAutoLayoutGroup succinctDescriptionBuilder];
-[SBFlexibleWindowingAutoLayoutGroup descriptionWithMultilinePrefix:];
-[SBFlexibleWindowingAutoLayoutGroup succinctDescription];
-[SBFlexibleWindowingAutoLayoutGroup hash];
-[SBFlexibleWindowingAutoLayoutGroup description];
-[SBFlexibleWindowingAutoLayoutGroup copyWithZone:];
-[SBFlexibleWindowingAutoLayoutGroup isEqual:];
-[SBFlexibleWindowingAutoLayoutGroup initWithItems:];
-[SBFlexibleWindowingAutoLayoutGroup descriptionBuilderWithMultilinePrefix:];
-[SBFlexibleWindowingAutoLayoutGroup _copyWithClass:];
-[SBFlexibleWindowingAutoLayoutGroup displayItemsInGroup];
-[SBFlexibleWindowingAutoLayoutGroup intersectionHeight];
-[SBFlexibleWindowingAutoLayoutGroup itemsInGroup];
-[SBFlexibleWindowingAutoLayoutGroup resizeGrabberPosition];
```
