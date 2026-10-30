# `_UITabModel`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UITabCustomizationStoreObserver`
- 10 instance variables, 13 properties, 41 instance methods, 0 class methods

## Instance variables

```
@"NSPointerArray" _observers;
{?="isBroadcasting"b1"ignoreSelectedLeafChanges"b1"notifyTabBarControllerOnLeafReselection"b1"allowUpdatesDuringBroadcast"b1"disallowsUpdates"b1"isPerformingBatchUpdates"b1} _flags;
B _editable;
B _editing;
@"_UITabCustomizationStore" _customizationStore;
@"UITabBarController" _tabBarController;
@"NSArray" _tabItems;
@"UITab" _selectedItem;
@"UITab" _selectedLeaf;
@"NSString" _persistenceIdentifier;
```

## Properties

```
@property (T@"UITabBarController",W,N,V_tabBarController) tabBarController;
@property (T@"NSArray",&,N,V_tabItems) tabItems;
@property (T@"UITab",R,N,V_selectedItem) selectedItem;
@property (T@"UITab",R,N,V_selectedLeaf) selectedLeaf;
@property (TB,R,N) isPerformingBatchUpdates;
@property (T@"NSString",&,N,V_persistenceIdentifier) persistenceIdentifier;
@property (T@"_UITabCustomizationStore",R,N,V_customizationStore) customizationStore;
@property (TB,N,GisEditable,V_editable) editable;
@property (TB,N,GisEditing,V_editing) editing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITabModel tabContentDidChange:];
-[_UITabModel selectedItem];
-[_UITabModel isEditable];
-[_UITabModel setSelectedItem:];
-[_UITabModel isTabHidden:];
-[_UITabModel tabItems];
-[_UITabModel customizabilityDidChangeForTab:];
-[_UITabModel _sendToObservers:allowUpdatesDuringBroadcast:];
-[_UITabModel resolvedPopoverPresentationControllerSourceItemForTab:];
-[_UITabModel removeObserver:];
-[_UITabModel _setSelectedItem:notifyDelegateOnReselection:];
-[_UITabModel selectTabInSidebar:notifyOnReselection:];
-[_UITabModel tabForIdentifier:];
-[_UITabModel tabBarController];
-[_UITabModel setPersistenceIdentifier:];
-[_UITabModel replaceItemAtIndex:withItem:];
-[_UITabModel addObserver:];
-[_UITabModel _updateSelectedLeaf];
-[_UITabModel elementsDidChangeForGroup:];
-[_UITabModel customizationStore];
-[_UITabModel selectTab:notifyOnReselection:];
-[_UITabModel setEditing:];
-[_UITabModel _updateSelectedLeafPerformBeforeNotifyingBlock:];
-[_UITabModel shouldSelectTab:];
-[_UITabModel performBatchUpdates:];
-[_UITabModel _selectTab:notifyObserversOnReselection:];
-[_UITabModel customizationStoreDidReset:];
-[_UITabModel setEditable:];
-[_UITabModel performWithUpdatesDisabled:];
-[_UITabModel persistenceIdentifier];
-[_UITabModel visibilityDidChangeForTab:editing:];
-[_UITabModel isPerformingBatchUpdates];
-[_UITabModel setTabBarController:];
-[_UITabModel favoriteOrderDidChange:];
-[_UITabModel selectedLeaf];
-[_UITabModel displayOrderIdentifiersDidChangeForGroup:];
-[_UITabModel isEditing];
-[_UITabModel _inferCurrentEditability];
-[_UITabModel setTabItems:];
-[_UITabModel setTabItems:inferSelection:];
-[_UITabModel selectedElementDidChangeForGroup:];
```
