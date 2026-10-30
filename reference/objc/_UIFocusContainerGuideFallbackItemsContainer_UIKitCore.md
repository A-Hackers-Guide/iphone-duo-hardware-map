# `_UIFocusContainerGuideFallbackItemsContainer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIFocusEnvironment`, `UIFocusItemContainer`
- 2 instance variables, 11 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<UIFocusEnvironment>" _parentFocusEnvironment;
@"NSArray" _childItems;
```

## Properties

```
@property (T@"<UIFocusEnvironment>",R,W,N,V_parentFocusEnvironment) parentFocusEnvironment;
@property (T@"NSArray",R,N,V_childItems) childItems;
@property (T@"NSArray",R,C,N) preferredFocusEnvironments;
@property (T@"<UIFocusItemContainer>",R,N) focusItemContainer;
@property (T@"UIView",?,R,W,N) preferredFocusedView;
@property (T@"NSString",?,R,C,N) focusGroupIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<UICoordinateSpace>",R,N) coordinateSpace;
```

## Instance methods

```
-[_UIFocusContainerGuideFallbackItemsContainer updateFocusIfNeeded];
-[_UIFocusContainerGuideFallbackItemsContainer coordinateSpace];
-[_UIFocusContainerGuideFallbackItemsContainer focusItemsInRect:];
-[_UIFocusContainerGuideFallbackItemsContainer didUpdateFocusInContext:withAnimationCoordinator:];
-[_UIFocusContainerGuideFallbackItemsContainer setNeedsFocusUpdate];
-[_UIFocusContainerGuideFallbackItemsContainer parentFocusEnvironment];
-[_UIFocusContainerGuideFallbackItemsContainer focusItemContainer];
-[_UIFocusContainerGuideFallbackItemsContainer preferredFocusEnvironments];
-[_UIFocusContainerGuideFallbackItemsContainer shouldUpdateFocusInContext:];
-[_UIFocusContainerGuideFallbackItemsContainer childItems];
-[_UIFocusContainerGuideFallbackItemsContainer initWithParentEnvironment:childItems:];
```
