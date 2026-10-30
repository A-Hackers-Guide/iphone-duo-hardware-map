# `UITab`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIPopoverPresentationControllerSourceItem_Internal`
- 20 instance variables, 26 properties, 90 instance methods, 0 class methods

## Instance variables

```
@? _viewControllerProvider;
B _springLoaded;
B _enabled;
B _hidden;
B _hiddenByDefault;
B _allowsHiding;
@"UIViewController" _viewController;
@"NSArray" _displayedViewControllers;
@"NSString" _accessibilityIdentifier;
@"_UITabModel" _tabModel;
@"NSString" _identifier;
@"NSString" _title;
@"UIImage" _image;
@"UIImage" _selectedImage;
@"NSString" _subtitle;
@"NSString" _badgeValue;
q _preferredPlacement;
@ _userInfo;
@"UITabGroup" _parent;
@"<_UITabAlternateRepresentation>" __compactRepresentation;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"_UITabModel",W,N,S_setTabModel:,V_tabModel) _tabModel;
@property (T@"UITabBarItem",R,N) _linkedTabBarItem;
@property (T@"NSArray",&,N,S_setDisplayedViewControllers:,V_displayedViewControllers) _displayedViewControllers;
@property (TB,N,GisDisabled) disabled;
@property (T@"<_UITabAlternateRepresentation>",&,N,S_setCompactRepresentation:,V__compactRepresentation) _compactRepresentation;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (T@"NSString",C,N,V_title) title;
@property (T@"UIImage",&,N,V_image) image;
@property (T@"UIImage",&,N,V_selectedImage) selectedImage;
@property (T@"NSString",C,N,V_subtitle) subtitle;
@property (T@"NSString",C,N,V_badgeValue) badgeValue;
@property (Tq,N,V_preferredPlacement) preferredPlacement;
@property (T@,&,N,V_userInfo) userInfo;
@property (T@"UITabGroup",R,W,N,V_parent) parent;
@property (T@"UITabBarController",R,N) tabBarController;
@property (T@"UIViewController",R,N,V_viewController) viewController;
@property (T@"UITabGroup",R,N) managingTabGroup;
@property (TB,N,GisHidden,V_hidden) hidden;
@property (TB,N,GisHiddenByDefault,V_hiddenByDefault) hiddenByDefault;
@property (TB,N,V_allowsHiding) allowsHiding;
@property (TB,R,N) hasVisiblePlacement;
```

## Instance methods

```
-[UITab setSpringLoaded:];
-[UITab _displayedViewController];
-[UITab setAccessibilityAttributedValue:];
-[UITab setAccessibilityAttributedHint:];
-[UITab badgeValue];
-[UITab _existingDisplayedViewController];
-[UITab _updateView];
-[UITab setBadgeValue:];
-[UITab isSpringLoaded];
-[UITab managingTabGroup];
-[UITab _isElement];
-[UITab _filledVariantImage];
-[UITab setAccessibilityAttributedLabel:];
-[UITab subtitle];
-[UITab setHidden:];
-[UITab identifier];
-[UITab initWithTitle:image:identifier:viewControllerProvider:];
-[UITab _filledVariantSelectedImage];
-[UITab userInfo];
-[UITab _nearestViewController];
-[UITab _updateDescriptionWithBuilder:recursive:];
-[UITab setUserInfo:];
-[UITab _frameInCoordinateSpace:window:];
-[UITab setSubtitle:];
-[UITab _isCustomizable];
-[UITab isDisabled];
-[UITab _prefersZoomTransitionsForPopoverPresentationController:];
-[UITab setAccessibilityIdentifier:];
-[UITab _recursiveDescription];
-[UITab tabBarController];
-[UITab viewController];
-[UITab _sourceRectForPresentationInWindow:];
-[UITab _sourceViewForPresentationInWindow:];
-[UITab isEnabled];
-[UITab _canBeReordered];
-[UITab parent];
-[UITab _isMoreTab];
-[UITab _isGroup];
-[UITab accessibilityIdentifier];
-[UITab isHidden];
-[UITab _isSearchTab];
-[UITab title];
-[UITab setEnabled:];
-[UITab setAccessibilityValue:];
-[UITab selectedImage];
-[UITab hash];
-[UITab description];
-[UITab _visibilityDidChange];
-[UITab setTitle:];
-[UITab setSelectedImage:];
-[UITab _setParent:];
-[UITab image];
-[UITab setAccessibilityLabel:];
-[UITab _isSidebarDestination];
-[UITab _overrideTabBarItem];
-[UITab setAccessibilityHint:];
-[UITab isEqual:];
-[UITab _resolvedTabBarItemSourceItemForPopoverPresentationControllerSourceItem];
-[UITab preferredPlacement];
-[UITab setDisabled:];
-[UITab _isBridgedItem];
-[UITab _didChangeTabModel:];
-[UITab frameInView:];
-[UITab setImage:];
-[UITab _compactRepresentation];
-[UITab _contentDidChange];
-[UITab _customizabilityDidChange];
-[UITab _descriptionWithRecursion:];
-[UITab _displayedViewControllers];
-[UITab _hasCustomizablePlacement];
-[UITab _hasParent];
-[UITab _isAncestorOfTab:];
-[UITab _isUniquelySPI];
-[UITab _linkedTabBarItem];
-[UITab _parentGroup];
-[UITab _resetViewController];
-[UITab _setCompactRepresentation:];
-[UITab _setDisplayedViewControllers:];
-[UITab _setTabModel:];
-[UITab _tabBarItemImage];
-[UITab _tabBarItemSelectedImage];
-[UITab _tabModel];
-[UITab _tabPlacement];
-[UITab _updateLinkedTabBarItem];
-[UITab allowsHiding];
-[UITab hasVisiblePlacement];
-[UITab isHiddenByDefault];
-[UITab setAllowsHiding:];
-[UITab setHiddenByDefault:];
-[UITab setPreferredPlacement:];
```
