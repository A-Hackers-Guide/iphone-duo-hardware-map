# `_UITabCustomizationStore`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 12 properties, 37 instance methods, 3 class methods

## Instance variables

```
B _ignoringUpdates;
@"NSString" _persistenceIdentifier;
@"NSMutableSet" _excludedItems;
@"NSSet" _allGroupIdentifiers;
@"NSMutableSet" _collapsedGroupIdentifiers;
d _preferredSidebarWidth;
q _preferredSidebarVisibility;
@"NSPointerArray" _observers;
@"NSMutableOrderedSet" _includedItems;
@"NSMutableSet" _hiddenItems;
@"NSMutableSet" _visibleItems;
@"NSMutableDictionary" _displayOrdersByIdentifier;
```

## Properties

```
@property (T@"NSPointerArray",R,N,V_observers) observers;
@property (T@"NSMutableOrderedSet",R,N,V_includedItems) includedItems;
@property (T@"NSMutableSet",&,N,V_excludedItems) excludedItems;
@property (T@"NSMutableSet",R,N,V_hiddenItems) hiddenItems;
@property (T@"NSMutableSet",R,N,V_visibleItems) visibleItems;
@property (T@"NSMutableDictionary",R,N,V_displayOrdersByIdentifier) displayOrdersByIdentifier;
@property (T@"NSMutableSet",&,N,V_collapsedGroupIdentifiers) collapsedGroupIdentifiers;
@property (T@"NSSet",&,N,V_allGroupIdentifiers) allGroupIdentifiers;
@property (T@"NSString",R,C,N,V_persistenceIdentifier) persistenceIdentifier;
@property (TB,R,N) hasFavoriteOrderCustomization;
@property (Td,N,V_preferredSidebarWidth) preferredSidebarWidth;
@property (Tq,N,V_preferredSidebarVisibility) preferredSidebarVisibility;
```

## Class methods

```
+[_UITabCustomizationStore _dataForKey:persistenceIdentifier:];
+[_UITabCustomizationStore _saveData:forKey:persistenceIdentifier:];
+[_UITabCustomizationStore customizationStoreWithPersistenceIdentifier:];
```

## Instance methods

```
-[_UITabCustomizationStore removeObserver:];
-[_UITabCustomizationStore reset];
-[_UITabCustomizationStore visibleItems];
-[_UITabCustomizationStore addObserver:];
-[_UITabCustomizationStore allGroupIdentifiers];
-[_UITabCustomizationStore persistenceIdentifier];
-[_UITabCustomizationStore observers];
-[_UITabCustomizationStore hiddenItems];
-[_UITabCustomizationStore _initWithPersistenceIdentifier:];
-[_UITabCustomizationStore _indexOfObserver:];
-[_UITabCustomizationStore _notifyForContentReset];
-[_UITabCustomizationStore _notifyForFavoriteOrderChange];
-[_UITabCustomizationStore _saveCustomization];
-[_UITabCustomizationStore _saveCustomizationForTab:recursive:];
-[_UITabCustomizationStore _saveSidebarState];
-[_UITabCustomizationStore collapsedGroupIdentifiers];
-[_UITabCustomizationStore displayOrderIdentifiersForGroupWithIdentifier:];
-[_UITabCustomizationStore displayOrdersByIdentifier];
-[_UITabCustomizationStore excludedItems];
-[_UITabCustomizationStore favoriteOrderContainsTab:];
-[_UITabCustomizationStore favoriteOrderForDefaultIdentifiers:];
-[_UITabCustomizationStore hasFavoriteOrderCustomization];
-[_UITabCustomizationStore hasModelCustomizations];
-[_UITabCustomizationStore includedItems];
-[_UITabCustomizationStore isHiddenForTabIdentifier:isCustomized:];
-[_UITabCustomizationStore performWithoutSavingCustomization:];
-[_UITabCustomizationStore preferredSidebarVisibility];
-[_UITabCustomizationStore preferredSidebarWidth];
-[_UITabCustomizationStore saveCustomizationForTabs:];
-[_UITabCustomizationStore saveFavoriteOrderCustomization:defaultIdentifiers:excludedIdentifiers:];
-[_UITabCustomizationStore setAllGroupIdentifiers:];
-[_UITabCustomizationStore setCollapsedGroupIdentifiers:];
-[_UITabCustomizationStore setCollapsedGroupIdentifiers:availableIdentifiers:];
-[_UITabCustomizationStore setExcludedItems:];
-[_UITabCustomizationStore setPreferredSidebarVisibility:];
-[_UITabCustomizationStore setPreferredSidebarWidth:];
-[_UITabCustomizationStore updateCustomizationForTab:];
```
