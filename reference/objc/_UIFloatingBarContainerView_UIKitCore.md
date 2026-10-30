# `_UIFloatingBarContainerView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PTSettingsKeyObserver`, `_UIBarButtonItemGroupOwner`
- 10 instance variables, 11 properties, 35 instance methods, 0 class methods

## Instance variables

```
changeObservers;
@"_UIScrollPocketContainerInteraction" bottomScrollPocketContainerInteraction;
@"_UIScrollPocketContainerInteraction" verticalScrollPocketContainerInteraction;
@"_UIScrollPocketBarInteraction" scrollPocketBarInteraction;
model;
hostingView;
@"_TtC5UIKit34ToolbarPointerInteractionAssistant" pointerAssistant;
@"_TtC5UIKit32ToolbarAccessibilityHUDAssistant" axHUDAssistant;
@"_TtC5UIKit24ToolbarKeyboardAssistant" keyboardAssistant;
$__lazy_storage_$_verticalPocketAssistant;
```

## Properties

```
@property (T@"_UIScrollPocketContainerInteraction",N,&,VbottomScrollPocketContainerInteraction) bottomScrollPocketContainerInteraction;
@property (T@"_UIScrollPocketContainerInteraction",N,&,VverticalScrollPocketContainerInteraction) verticalScrollPocketContainerInteraction;
@property (T@"_UIScrollPocketBarInteraction",N,&,VscrollPocketBarInteraction) scrollPocketBarInteraction;
@property (T@"_TtC5UIKit34ToolbarPointerInteractionAssistant",N,R,VpointerAssistant) pointerAssistant;
@property (T@"_TtC5UIKit32ToolbarAccessibilityHUDAssistant",N,R,VaxHUDAssistant) axHUDAssistant;
@property (T@"_TtC5UIKit24ToolbarKeyboardAssistant",N,R,VkeyboardAssistant) keyboardAssistant;
@property (Td,N) dimmingLevel;
@property (TQ,N) edgesRequiringContentMargin;
@property (TQ,N) adjacentBarEdges;
@property (T@"UIBarButtonItem",N,R) overflowBarButtonItem;
@property (TB,N,R) supportsExternalContent;
```

## Instance methods

```
-[_UIFloatingBarContainerView _groupDidUpdateVisibility:];
-[_UIFloatingBarContainerView _groupDidUpdateItems:removedItems:];
-[_UIFloatingBarContainerView _groupDidUpdateRepresentative:fromRepresentative:];
-[_UIFloatingBarContainerView _groupDidUpdatePlatterizationPreference:];
-[_UIFloatingBarContainerView didMoveToWindow];
-[_UIFloatingBarContainerView setEdgesRequiringContentMargin:];
-[_UIFloatingBarContainerView setAdjacentBarEdges:];
-[_UIFloatingBarContainerView setBarCompressionBehavior:];
-[_UIFloatingBarContainerView removeChangeObserver:];
-[_UIFloatingBarContainerView axHUDAssistant];
-[_UIFloatingBarContainerView layoutSubviews];
-[_UIFloatingBarContainerView pointerAssistant];
-[_UIFloatingBarContainerView hitTest:withEvent:];
-[_UIFloatingBarContainerView keyboardAssistant];
-[_UIFloatingBarContainerView verticalScrollPocketContainerInteraction];
-[_UIFloatingBarContainerView setScrollPocketBarInteraction:];
-[_UIFloatingBarContainerView settings:changedValueForKey:];
-[_UIFloatingBarContainerView adjacentBarEdges];
-[_UIFloatingBarContainerView setDimmingLevel:];
-[_UIFloatingBarContainerView supportsExternalContent];
-[_UIFloatingBarContainerView setPocketReplaySourceView:];
-[_UIFloatingBarContainerView removeNavigationBarRepresentation];
-[_UIFloatingBarContainerView dimmingLevel];
-[_UIFloatingBarContainerView bottomScrollPocketContainerInteraction];
-[_UIFloatingBarContainerView setVerticalScrollPocketContainerInteraction:];
-[_UIFloatingBarContainerView overflowBarButtonItem];
-[_UIFloatingBarContainerView setBottomScrollPocketContainerInteraction:];
-[_UIFloatingBarContainerView addChangeObserver:];
-[_UIFloatingBarContainerView initWithCoder:];
-[_UIFloatingBarContainerView edgesRequiringContentMargin];
-[_UIFloatingBarContainerView scrollPocketBarInteraction];
-[_UIFloatingBarContainerView setTabBarItemGroups:animated:];
-[_UIFloatingBarContainerView initWithFrame:];
-[_UIFloatingBarContainerView setScrollPocketCollectorInteraction:];
-[_UIFloatingBarContainerView removeContributionFromNavigationController:];
```
