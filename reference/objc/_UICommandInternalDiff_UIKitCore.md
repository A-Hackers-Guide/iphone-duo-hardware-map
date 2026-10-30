# `_UICommandInternalDiff`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _menuDeletes;
@"NSMutableDictionary" _itemDeletes;
@"NSMutableDictionary" _inserts;
@"NSMutableDictionary" _replacements;
```

## Properties

```
@property (T@"NSSet",R,N,V_menuDeletes) menuDeletes;
@property (T@"NSDictionary",R,N,V_itemDeletes) itemDeletes;
@property (T@"NSDictionary",R,N,V_inserts) inserts;
@property (T@"NSDictionary",R,N,V_replacements) replacements;
```

## Instance methods

```
-[_UICommandInternalDiff replacements];
-[_UICommandInternalDiff inserts];
-[_UICommandInternalDiff _deletesForMenu:];
-[_UICommandInternalDiff _parentInsertsForMenu:];
-[_UICommandInternalDiff _replacementsForMenu:];
-[_UICommandInternalDiff deleteItem:inMenu:];
-[_UICommandInternalDiff deleteMenu:];
-[_UICommandInternalDiff insertAtStartElements:atEndElements:inMenu:];
-[_UICommandInternalDiff insertBeforeElements:afterElements:aroundElement:inMenu:];
-[_UICommandInternalDiff insertFallbackBeforeElements:fallbackAfterElements:inMenu:];
-[_UICommandInternalDiff itemDeletes];
-[_UICommandInternalDiff menuDeletes];
-[_UICommandInternalDiff replaceItem:inMenu:withElements:];
```
