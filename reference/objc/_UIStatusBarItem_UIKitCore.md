# `_UIStatusBarItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 21 instance methods, 8 class methods

## Instance variables

```
B _needsUpdate;
@"_UIStatusBarIdentifier" _identifier;
@"NSMutableDictionary" _displayItems;
@"_UIStatusBar" _statusBar;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_displayItems) displayItems;
@property (T@"_UIStatusBar",R,W,V_statusBar) statusBar;
@property (T@"_UIStatusBarIdentifier",R,N,V_identifier) identifier;
@property (T@"NSSet",R,N) dependentEntryKeys;
@property (TB,R,N,V_needsUpdate) needsUpdate;
```

## Class methods

```
+[_UIStatusBarItem identifier];
+[_UIStatusBarItem createItemForIdentifier:statusBar:];
+[_UIStatusBarItem defaultDisplayIdentifier];
+[_UIStatusBarItem displayItemIdentifierFromIdentifier:string:];
+[_UIStatusBarItem displayItemIdentifierFromString:];
+[_UIStatusBarItem itemClassForIdentifier:];
+[_UIStatusBarItem itemIdentifierForDisplayItemIdentifier:];
+[_UIStatusBarItem itemIdentifierFromString:];
```

## Instance methods

```
-[_UIStatusBarItem statusBar];
-[_UIStatusBarItem needsUpdate];
-[_UIStatusBarItem applyStyleAttributes:toDisplayItem:];
-[_UIStatusBarItem initWithIdentifier:statusBar:];
-[_UIStatusBarItem displayItems];
-[_UIStatusBarItem viewForIdentifier:];
-[_UIStatusBarItem identifier];
-[_UIStatusBarItem additionAnimationForDisplayItemWithIdentifier:];
-[_UIStatusBarItem createDisplayItemForIdentifier:];
-[_UIStatusBarItem canEnableDisplayItem:fromData:];
-[_UIStatusBarItem setDisplayItems:];
-[_UIStatusBarItem removalAnimationForDisplayItemWithIdentifier:];
-[_UIStatusBarItem dependentEntryKeys];
-[_UIStatusBarItem description];
-[_UIStatusBarItem applyUpdate:toDisplayItem:];
-[_UIStatusBarItem setNeedsUpdate];
-[_UIStatusBarItem prepareAnimation:forDisplayItem:];
-[_UIStatusBarItem overriddenStyleAttributesForData:identifier:];
-[_UIStatusBarItem _applyUpdate:toDisplayItem:];
-[_UIStatusBarItem displayItemForIdentifier:];
-[_UIStatusBarItem updatedDisplayItemsWithData:];
```
