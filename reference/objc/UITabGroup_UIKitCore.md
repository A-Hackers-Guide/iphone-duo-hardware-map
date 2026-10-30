# `UITabGroup`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITab`
- Protocols: `_UITabGroup`
- 13 instance variables, 15 properties, 50 instance methods, 0 class methods

## Instance variables

```
@"<UITraitChangeRegistration>" _sizeClassTraitRegistration;
B _isUpdatingManagedNavigationController;
B _allowsReordering;
B _isSidebarDestination;
B _collapsedByDefault;
@"NSArray" _displayOrder;
@"UITab" _selectedChild;
@"NSString" _defaultChildIdentifier;
@"NSArray" _children;
@"NSArray" _displayOrderIdentifiers;
@"UINavigationController" _managingNavigationController;
@"NSArray" _sidebarActions;
Q _sidebarAppearance;
```

## Properties

```
@property (T@"UITab",&,N,V_selectedChild) selectedChild;
@property (T@"NSString",C,N,V_defaultChildIdentifier) defaultChildIdentifier;
@property (T@"NSArray",C,N,V_children) children;
@property (TB,N,V_allowsReordering) allowsReordering;
@property (T@"NSArray",C,N,V_displayOrderIdentifiers) displayOrderIdentifiers;
@property (T@"NSArray",R,N,V_displayOrder) displayOrder;
@property (T@"UINavigationController",&,N,V_managingNavigationController) managingNavigationController;
@property (T@"NSArray",C,N,V_sidebarActions) sidebarActions;
@property (TQ,N,V_sidebarAppearance) sidebarAppearance;
@property (TB,N,V_isSidebarDestination) isSidebarDestination;
@property (TB,N,GisCollapsedByDefault,V_collapsedByDefault) collapsedByDefault;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UITabGroup _displayedViewController];
-[UITabGroup setChildren:];
-[UITabGroup _existingDisplayedViewController];
-[UITabGroup setDefaultChildIdentifier:];
-[UITabGroup managingTabGroup];
-[UITabGroup allowsReordering];
-[UITabGroup _registerManagingNavigationTraitsIfNeeded];
-[UITabGroup defaultChildIdentifier];
-[UITabGroup _selectedTabHierarchy];
-[UITabGroup _canReorderChild:];
-[UITabGroup initWithTitle:image:identifier:viewControllerProvider:];
-[UITabGroup setSidebarActions:];
-[UITabGroup initWithTitle:image:identifier:children:viewControllerProvider:];
-[UITabGroup _validateSelectedElement];
-[UITabGroup setAllowsReordering:];
-[UITabGroup _updateDescriptionWithBuilder:recursive:];
-[UITabGroup tabForIdentifier:];
-[UITabGroup isSidebarDestination];
-[UITabGroup _updateManagingNavigationStackUsingTransition:isExplicit:];
-[UITabGroup _isCustomizable];
-[UITabGroup setIsSidebarDestination:];
-[UITabGroup _canBeReordered];
-[UITabGroup setSelectedChild:];
-[UITabGroup setCollapsedByDefault:];
-[UITabGroup _isGroup];
-[UITabGroup _updateForManagingNavigationStackChange];
-[UITabGroup _updateManagingNavigationStackFromTraitUpdate];
-[UITabGroup _selectElement:notifyOnReselection:performBeforeNotifyingDelegate:];
-[UITabGroup children];
-[UITabGroup setManagingNavigationController:];
-[UITabGroup _filteredDisplayOrderIdentifiers];
-[UITabGroup setDisplayOrderIdentifiers:];
-[UITabGroup displayOrder];
-[UITabGroup _elementsDidChange];
-[UITabGroup isCollapsedByDefault];
-[UITabGroup _setDisplayOrderIdentifiers:];
-[UITabGroup _selectedElementDidChange];
-[UITabGroup _invalidateDisplayOrder];
-[UITabGroup _updateManagingNavigationStackUsingTransition:];
-[UITabGroup setSidebarAppearance:];
-[UITabGroup _defaultChildForSelection];
-[UITabGroup sidebarAppearance];
-[UITabGroup _isSidebarDestination];
-[UITabGroup sidebarActions];
-[UITabGroup _didChangeTabModel:];
-[UITabGroup selectedChild];
-[UITabGroup _performWithoutUpdatingManagingNavigationController:];
-[UITabGroup displayOrderIdentifiers];
-[UITabGroup managingNavigationController];
-[UITabGroup _orderedChildrenForDisplayOrder:];
```
