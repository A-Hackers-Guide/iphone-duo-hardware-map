# `_UIFocusRegionContainerProxy`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIFocusRegionContainer`
- 4 instance variables, 18 properties, 30 instance methods, 0 class methods

## Instance variables

```
B _allowsLazyLoading;
B _shouldCreateRegionForOwningItem;
B _shouldCreateRegionForGuideBehavior;
@"_UIFocusEnvironmentContainerTuple" _environmentContainer;
```

## Properties

```
@property (T@"_UIFocusEnvironmentContainerTuple",&,N,V_environmentContainer) environmentContainer;
@property (TB,N,V_allowsLazyLoading) allowsLazyLoading;
@property (TB,N,V_shouldCreateRegionForOwningItem) shouldCreateRegionForOwningItem;
@property (TB,N,V_shouldCreateRegionForGuideBehavior) shouldCreateRegionForGuideBehavior;
@property (T@"<UIFocusEnvironment>",R,N) owningEnvironment;
@property (TB,?,R,N,G_isEligibleForFocusInteraction) eligibleForFocusInteraction;
@property (TB,?,R,N,G_isEligibleForFocusOcclusion) eligibleForFocusOcclusion;
@property (Tq,?,R,N,G_preferredFocusMovementStyle) preferredFocusMovementStyle;
@property (T@"NSArray",?,R,C,N,G_linearFocusMovementSequences) linearFocusMovementSequences;
@property (T@"NSArray",R,C,N) preferredFocusEnvironments;
@property (T@"<UIFocusEnvironment>",R,W,N) parentFocusEnvironment;
@property (T@"<UIFocusItemContainer>",R,N) focusItemContainer;
@property (T@"UIView",?,R,W,N) preferredFocusedView;
@property (T@"NSString",?,R,C,N) focusGroupIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIFocusRegionContainerProxy _isEligibleForFocusInteraction];
-[_UIFocusRegionContainerProxy _didUpdateFocusInContext:];
-[_UIFocusRegionContainerProxy updateFocusIfNeeded];
-[_UIFocusRegionContainerProxy _preferredFocusRegionCoordinateSpace];
-[_UIFocusRegionContainerProxy didUpdateFocusInContext:withAnimationCoordinator:];
-[_UIFocusRegionContainerProxy setNeedsFocusUpdate];
-[_UIFocusRegionContainerProxy parentFocusEnvironment];
-[_UIFocusRegionContainerProxy focusItemContainer];
-[_UIFocusRegionContainerProxy hash];
-[_UIFocusRegionContainerProxy _isEligibleForFocusOcclusion];
-[_UIFocusRegionContainerProxy description];
-[_UIFocusRegionContainerProxy preferredFocusEnvironments];
-[_UIFocusRegionContainerProxy isEqual:];
-[_UIFocusRegionContainerProxy shouldUpdateFocusInContext:];
-[_UIFocusRegionContainerProxy shouldCreateRegionForOwningItem];
-[_UIFocusRegionContainerProxy _clippingRectInCoordinateSpace:];
-[_UIFocusRegionContainerProxy _focusSystem];
-[_UIFocusRegionContainerProxy _itemContainer];
-[_UIFocusRegionContainerProxy _searchForFocusRegionsInContext:];
-[_UIFocusRegionContainerProxy _ui_isUIFocusRegionContainerProxy];
-[_UIFocusRegionContainerProxy allowsLazyLoading];
-[_UIFocusRegionContainerProxy environmentContainer];
-[_UIFocusRegionContainerProxy initWithEnvironmentContainer:];
-[_UIFocusRegionContainerProxy initWithOwningEnvironment:itemContainer:];
-[_UIFocusRegionContainerProxy owningEnvironment];
-[_UIFocusRegionContainerProxy setAllowsLazyLoading:];
-[_UIFocusRegionContainerProxy setEnvironmentContainer:];
-[_UIFocusRegionContainerProxy setShouldCreateRegionForGuideBehavior:];
-[_UIFocusRegionContainerProxy setShouldCreateRegionForOwningItem:];
-[_UIFocusRegionContainerProxy shouldCreateRegionForGuideBehavior];
```
