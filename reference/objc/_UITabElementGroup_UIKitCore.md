# `_UITabElementGroup`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UITabElement`
- Protocols: `_UITabGroup`
- 7 instance variables, 15 properties, 40 instance methods, 0 class methods

## Instance variables

```
{?="didSelectElement"b1"didCustomizeDisplayOrder"b1} _delegateImplements;
B _allowsReordering;
@"<_UITabElementGroupDelegate>" _delegate;
@"_UITabElement" _selectedElement;
@"NSArray" _children;
@"NSString" __defaultChildIdentifier;
Q __sidebarAppearance;
```

## Properties

```
@property (T@"<_UITabElementGroupDelegate>",W,N,S_setDelegate:,V_delegate) _delegate;
@property (T@"NSString",&,N,S_setDefaultChildIdentifier:,V__defaultChildIdentifier) _defaultChildIdentifier;
@property (T@"_UITabElement",&,N,S_setSelectedElement:,V_selectedElement) _selectedElement;
@property (T@"NSArray",C,N,S_setChildren:,V_children) _children;
@property (TQ,N,S_setSidebarAppearance:,V__sidebarAppearance) _sidebarAppearance;
@property (T@"UITab",R,N) selectedChild;
@property (T@"NSArray",R,C,N) children;
@property (TB,N,V_allowsReordering) allowsReordering;
@property (TB,R,N,GisCollapsedByDefault) collapsedByDefault;
@property (TQ,R,N) sidebarAppearance;
@property (T@"NSArray",R,N) sidebarActions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITabElementGroup _setDelegate:];
-[_UITabElementGroup allowsReordering];
-[_UITabElementGroup initWithIdentifier:title:image:children:];
-[_UITabElementGroup _canReorderChild:];
-[_UITabElementGroup _selectElement:notifyingDelegate:notifyOnReselection:performBeforeNotifyingDelegate:];
-[_UITabElementGroup _sidebarAppearance];
-[_UITabElementGroup _setChildren:];
-[_UITabElementGroup setAllowsReordering:];
-[_UITabElementGroup _updateDescriptionWithBuilder:recursive:];
-[_UITabElementGroup _children];
-[_UITabElementGroup tabForIdentifier:];
-[_UITabElementGroup _isCustomizable];
-[_UITabElementGroup _delegate];
-[_UITabElementGroup _canBeReordered];
-[_UITabElementGroup setCollapsedByDefault:];
-[_UITabElementGroup _defaultChildIdentifier];
-[_UITabElementGroup _isGroup];
-[_UITabElementGroup _updateForManagingNavigationStackChange];
-[_UITabElementGroup _selectElement:notifyOnReselection:performBeforeNotifyingDelegate:];
-[_UITabElementGroup children];
-[_UITabElementGroup _setSelectedElement:];
-[_UITabElementGroup _filteredDisplayOrderIdentifiers];
-[_UITabElementGroup _setDefaultChildIdentifier:];
-[_UITabElementGroup _selectedElement];
-[_UITabElementGroup initWithIdentifier:title:image:];
-[_UITabElementGroup _tabForIdentifier:];
-[_UITabElementGroup isCollapsedByDefault];
-[_UITabElementGroup _setDisplayOrderIdentifiers:];
-[_UITabElementGroup _defaultChildElement];
-[_UITabElementGroup _updateManagingNavigationStackUsingTransition:];
-[_UITabElementGroup _defaultChildForSelection];
-[_UITabElementGroup sidebarAppearance];
-[_UITabElementGroup _selectElement:notifyingDelegate:notifyOnReselection:];
-[_UITabElementGroup _isSidebarDestination];
-[_UITabElementGroup _notifyObserversElementsChanged];
-[_UITabElementGroup sidebarActions];
-[_UITabElementGroup _didChangeTabModel:];
-[_UITabElementGroup selectedChild];
-[_UITabElementGroup _setSidebarAppearance:];
-[_UITabElementGroup _orderedChildrenForDisplayOrder:];
```
