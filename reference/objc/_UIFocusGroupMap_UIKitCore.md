# `_UIFocusGroupMap`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 6 instance variables, 3 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _environmentToGroupMap;
@"NSMapTable" _identifierToGroupMap;
@"NSMapTable" _identifierToPrimaryItemMap;
@"_UIFocusGroup" _nullGroup;
@"NSArray" _focusGroups;
@"<UICoordinateSpace>" _coordinateSpace;
```

## Properties

```
@property (T@"<UICoordinateSpace>",R,N,V_coordinateSpace) coordinateSpace;
@property (T@"NSArray",R,N,V_focusGroups) focusGroups;
@property (T@"NSArray",R,N) focusItems;
```

## Instance methods

```
-[_UIFocusGroupMap coordinateSpace];
-[_UIFocusGroupMap description];
-[_UIFocusGroupMap copyWithZone:];
-[_UIFocusGroupMap _indexEnvironment:];
-[_UIFocusGroupMap _indexItems:];
-[_UIFocusGroupMap focusGroupForItem:];
-[_UIFocusGroupMap focusGroups];
-[_UIFocusGroupMap focusItems];
-[_UIFocusGroupMap initWithItems:coordinateSpace:];
```
