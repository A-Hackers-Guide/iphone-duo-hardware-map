# `UITabBarControllerSidebar`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 13 properties, 33 instance methods, 0 class methods

## Instance variables

```
{?="availabilityDidChange"b1"visibilityWillChange"b1"itemForRequest"b1"updateItem"b1"leadingSwipeActions"b1"trailingSwipeActions"b1"contextMenuConfiguration"b1"willBeginDisplayingTab"b1"didEndDisplayingTab"b1"itemsForBeginningSession"b1"itemsForAddingToSession"b1"operationForAcceptingIntoAction"b1"acceptItemsIntoAction"b1"_spi_sessionPropertiesForSession"b1"_spi_operationForInsertingIntoGroup"b1"_spi_insertIntoGroup"b1"_spi_availabilityDidChange"b1} _delegateImplements;
{?="hasCustomBottomBarView"b1"currentVisibilityAppliedByUser"b1"preferredPlacement"b2"isAvailable"b1} _sidebarFlags;
@"NSArray" _toolbarItems;
B _hidden;
@"UITabBarController" _tabBarController;
@"_UITabOutlineView" _outlineView;
@"<UIContentConfiguration>" _headerContentConfiguration;
@"<UIContentConfiguration>" _footerContentConfiguration;
@"UIView" _bottomBarView;
@"<UITabBarControllerSidebarDelegate>" _delegate;
q _preferredLayout;
@"UIDeferredMenuElement" _navigationOverflowItems;
@"_UITabSidebarTransaction" __activeTransaction;
@"<_UITabOutlineViewDelegate>" __sidebarViewDelegate;
@"UIVisualEffect" __overrideBackgroundEffect;
@"UIView<_UITabContentProviding>" __sidebarView;
```

## Properties

```
@property (T@"_UITabOutlineView",R,N,V_outlineView) _outlineView;
@property (T@"UITab<_UITabGroup>",&,N,S_setDisplayedGroup:) _displayedGroup;
@property (T@"UIView<_UITabContentProviding>",&,N,V__sidebarView) _sidebarView;
@property (TB,N,S_setPrefersTabBarPresentation:) _prefersTabBarPresentation;
@property (T@"<UITabBarControllerSidebarDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N) isAvailable;
@property (Tq,N) preferredPlacement;
@property (TB,N,GisHidden,V_hidden) hidden;
@property (Tq,N,V_preferredLayout) preferredLayout;
@property (T@"UIDeferredMenuElement",&,N,V_navigationOverflowItems) navigationOverflowItems;
@property (T@"<UIContentConfiguration>",C,N,V_headerContentConfiguration) headerContentConfiguration;
@property (T@"<UIContentConfiguration>",C,N,V_footerContentConfiguration) footerContentConfiguration;
@property (T@"UIView",&,N,V_bottomBarView) bottomBarView;
```

## Instance methods

```
-[UITabBarControllerSidebar _isVisible];
-[UITabBarControllerSidebar isAvailable];
-[UITabBarControllerSidebar setHidden:];
-[UITabBarControllerSidebar preferredLayout];
-[UITabBarControllerSidebar _delegate];
-[UITabBarControllerSidebar setDelegate:];
-[UITabBarControllerSidebar isHidden];
-[UITabBarControllerSidebar delegate];
-[UITabBarControllerSidebar _setVisible:];
-[UITabBarControllerSidebar setPreferredLayout:];
-[UITabBarControllerSidebar preferredPlacement];
-[UITabBarControllerSidebar _displayedGroup];
-[UITabBarControllerSidebar _makeFirstResponderForTab:];
-[UITabBarControllerSidebar _outlineView];
-[UITabBarControllerSidebar _prefersTabBarPresentation];
-[UITabBarControllerSidebar _resignFirstResponder];
-[UITabBarControllerSidebar _setDisplayedGroup:];
-[UITabBarControllerSidebar _setPrefersTabBarPresentation:];
-[UITabBarControllerSidebar _sidebarView];
-[UITabBarControllerSidebar _sidebarViewStyle];
-[UITabBarControllerSidebar _updateInitialSidebarVisibilityIfPossible];
-[UITabBarControllerSidebar bottomBarView];
-[UITabBarControllerSidebar footerContentConfiguration];
-[UITabBarControllerSidebar headerContentConfiguration];
-[UITabBarControllerSidebar navigationOverflowItems];
-[UITabBarControllerSidebar reconfigureItemForTab:];
-[UITabBarControllerSidebar scrollToTarget:animated:];
-[UITabBarControllerSidebar setBottomBarView:];
-[UITabBarControllerSidebar setFooterContentConfiguration:];
-[UITabBarControllerSidebar setHeaderContentConfiguration:];
-[UITabBarControllerSidebar setNavigationOverflowItems:];
-[UITabBarControllerSidebar setPreferredPlacement:];
-[UITabBarControllerSidebar set_sidebarView:];
```
