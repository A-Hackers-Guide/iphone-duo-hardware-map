# `_UITabBarContentLayoutManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISearchTabHostedFieldHost`
- 17 instance variables, 14 properties, 53 instance methods, 0 class methods

## Instance variables

```
? host;
? container;
currentDisplayState;
B needsAccessoryDisplayStateUpdate;
morphAnimation;
isUpdatingMorphTransition;
pendingMorphTarget;
hostedSearchFieldConfiguration;
@"_TtC5UIKit27_UITabHostedSearchContainer" searchContainerView;
hostedAccessoryConfiguration;
accessoryContainerView;
d keyboardAdjustment;
B isUpdatingHostedElements;
B isAnimatingBottomAccessory;
B isHostingSearchTextField;
_itemLayout;
B isUpdatingContentLayout;
```

## Properties

```
@property (TB,N,R) isHostingSearchField;
@property (T@"<_UITabBarContentLayoutHost>",N,R,Vhost) host;
@property (T@"UIView",N,W,Vcontainer) container;
@property (TB,N,VneedsAccessoryDisplayStateUpdate) needsAccessoryDisplayStateUpdate;
@property (T@"_TtC5UIKit27_UITabHostedSearchContainer",N,&,VsearchContainerView) searchContainerView;
@property (T@"_TtC5UIKit26_UITabBarAnimationSettings",N,R) animationSettings;
@property (Td,N,VkeyboardAdjustment) keyboardAdjustment;
@property (TB,N,VisUpdatingHostedElements) isUpdatingHostedElements;
@property (TB,N,VisAnimatingBottomAccessory) isAnimatingBottomAccessory;
@property (TB,N,VisHostingSearchTextField) isHostingSearchTextField;
@property (TB,N,R) showsCancelAction;
@property (TB,N,R) isTabBarVertical;
@property (TB,N,VisUpdatingContentLayout) isUpdatingContentLayout;
@property (TB,N,R) isWideOnPhone;
```

## Instance methods

```
-[_UITabBarContentLayoutManager animationSettings];
-[_UITabBarContentLayoutManager initWithLayoutHost:container:];
-[_UITabBarContentLayoutManager isUpdatingContentLayout];
-[_UITabBarContentLayoutManager frameForHostedElement:options:];
-[_UITabBarContentLayoutManager _finalizeMagicMorphAnimationIfNeeded];
-[_UITabBarContentLayoutManager updateLayout];
-[_UITabBarContentLayoutManager updateAccessoryDisplayStyleIfNeeded];
-[_UITabBarContentLayoutManager isUpdatingHostedElements];
-[_UITabBarContentLayoutManager init];
-[_UITabBarContentLayoutManager updateHostedSearchLayoutIfNeeded];
-[_UITabBarContentLayoutManager setNeedsAccessoryDisplayStateUpdate:];
-[_UITabBarContentLayoutManager updateHostedAccessoryWithAnimated:];
-[_UITabBarContentLayoutManager _updateNotificationObserversForSearch];
-[_UITabBarContentLayoutManager _currentSearchFieldConfiguration];
-[_UITabBarContentLayoutManager _removeHostedSearchViewsIfNeeded];
-[_UITabBarContentLayoutManager setIsHostingSearchTextField:];
-[_UITabBarContentLayoutManager setContainer:];
-[_UITabBarContentLayoutManager contentSizeForAllHostedElementsForLayout:];
-[_UITabBarContentLayoutManager tabBarDidChange:];
-[_UITabBarContentLayoutManager setIsUpdatingHostedElements:];
-[_UITabBarContentLayoutManager updateAccessoryDisplayStyle];
-[_UITabBarContentLayoutManager adjustedBoundsForHostedSearchField:prefersFullSizeField:];
-[_UITabBarContentLayoutManager setSearchContainerView:];
-[_UITabBarContentLayoutManager isAnimatingBottomAccessory];
-[_UITabBarContentLayoutManager _searchControllerForHostedSearchField];
-[_UITabBarContentLayoutManager _updateHostedSearchTextFieldIntrinsicHeight:];
-[_UITabBarContentLayoutManager setIsAnimatingBottomAccessory:];
-[_UITabBarContentLayoutManager updateAccessoryLayoutIfNeeded];
-[_UITabBarContentLayoutManager isWideOnPhone];
-[_UITabBarContentLayoutManager layoutContentSizeForAllHostedElements];
-[_UITabBarContentLayoutManager updateContentLayoutWithAnimated:];
-[_UITabBarContentLayoutManager searchContainerView];
-[_UITabBarContentLayoutManager dismissSearchIfNeeded];
-[_UITabBarContentLayoutManager needsAccessoryDisplayStateUpdate];
-[_UITabBarContentLayoutManager isHostingSearchField];
-[_UITabBarContentLayoutManager _updateHostedSearchFieldCancelActionVisibility:];
-[_UITabBarContentLayoutManager keyboardAdjustment];
-[_UITabBarContentLayoutManager setIsUpdatingContentLayout:];
-[_UITabBarContentLayoutManager setBarHidden:animated:];
-[_UITabBarContentLayoutManager isTabBarVertical];
-[_UITabBarContentLayoutManager updateHostedSearchFieldIfNeeded];
-[_UITabBarContentLayoutManager setKeyboardAdjustment:];
-[_UITabBarContentLayoutManager _animateUsing:tracking:animations:completion:];
-[_UITabBarContentLayoutManager _morphToHostedSearchFieldWithActivatesSearchIfPossible:];
-[_UITabBarContentLayoutManager updateHostedElementsAnimated:];
-[_UITabBarContentLayoutManager wantsAccessoryFrame];
-[_UITabBarContentLayoutManager _updateKeyboardInfo:];
-[_UITabBarContentLayoutManager showsCancelAction];
-[_UITabBarContentLayoutManager interPlatterSpacingForHostedSearchFieldWithPrefersFullSizeField:];
-[_UITabBarContentLayoutManager host];
-[_UITabBarContentLayoutManager isHostingSearchTextField];
-[_UITabBarContentLayoutManager presentationContentSizeForAllHostedElements];
-[_UITabBarContentLayoutManager container];
```
