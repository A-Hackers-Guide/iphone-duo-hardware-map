# `_UIFocusEnvironmentContainerTuple`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 2 class methods

## Instance variables

```
B _isScrollableContainer;
@"<UIFocusEnvironment>" _owningEnvironment;
@"<UIFocusItemContainer>" _itemContainer;
```

## Properties

```
@property (T@"<UIFocusEnvironment>",R,N,V_owningEnvironment) owningEnvironment;
@property (T@"<UIFocusItemContainer>",R,N,V_itemContainer) itemContainer;
@property (TB,R,N,V_isScrollableContainer) isScrollableContainer;
```

## Class methods

```
+[_UIFocusEnvironmentContainerTuple tupleWithOwningEnvironment:itemContainer:];
+[_UIFocusEnvironmentContainerTuple tupleWithRequiredContainerFromEnvironment:];
```

## Instance methods

```
-[_UIFocusEnvironmentContainerTuple itemContainer];
-[_UIFocusEnvironmentContainerTuple hash];
-[_UIFocusEnvironmentContainerTuple description];
-[_UIFocusEnvironmentContainerTuple isEqual:];
-[_UIFocusEnvironmentContainerTuple initWithOwningEnvironment:itemContainer:];
-[_UIFocusEnvironmentContainerTuple isEqualToEnvironmentContainerTuple:];
-[_UIFocusEnvironmentContainerTuple isScrollableContainer];
-[_UIFocusEnvironmentContainerTuple owningEnvironment];
```
