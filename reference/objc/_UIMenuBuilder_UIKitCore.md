# `_UIMenuBuilder`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `UIMenuBuilder`
- 5 instance variables, 7 properties, 45 instance methods, 0 class methods

## Instance variables

```
@"UIMenuSystem" _system;
q _changeCountStorage;
q _actualChangeCountStorage;
_currentBookkeeping;
_cachedKeyboardShortcutLeaves;
```

## Properties

```
@property (T@"UIMenuSystem",N,R) system;
@property (T@"UIMenuSystem",N,&,V_system) _system;
@property (Tq,N,R) _changeCount;
@property (Tq,N,V_changeCountStorage) _changeCountStorage;
@property (Tq,N,R) _actualChangeCount;
@property (Tq,N,V_actualChangeCountStorage) _actualChangeCountStorage;
@property (T@"NSArray",N,R) _keyCommands;
```

## Instance methods

```
-[_UIMenuBuilder insertElements:afterActionForIdentifier:];
-[_UIMenuBuilder removeCommandForAction:propertyList:];
-[_UIMenuBuilder _isInternallyConsistent];
-[_UIMenuBuilder set_actualChangeCountStorage:];
-[_UIMenuBuilder init];
-[_UIMenuBuilder insertElements:beforeActionForIdentifier:];
-[_UIMenuBuilder set_changeCountStorage:];
-[_UIMenuBuilder insertChildMenu:atStartOfMenuForIdentifier:];
-[_UIMenuBuilder replaceCommandForAction:propertyList:withElements:];
-[_UIMenuBuilder _setNeedsRecacheKeyboardShortcutLeaves];
-[_UIMenuBuilder commandForAction:propertyList:];
-[_UIMenuBuilder _changeCount];
-[_UIMenuBuilder insertElements:atStartOfMenuForIdentifier:];
-[_UIMenuBuilder _actualChangeCountStorage];
-[_UIMenuBuilder replaceChildrenOfMenuForIdentifier:fromChildrenBlock:];
-[_UIMenuBuilder menuForIdentifier:];
-[_UIMenuBuilder _commandFor:];
-[_UIMenuBuilder insertElements:afterMenuForIdentifier:];
-[_UIMenuBuilder insertSiblingMenu:beforeMenuForIdentifier:];
-[_UIMenuBuilder initWithRootMenu:];
-[_UIMenuBuilder _changeCountStorage];
-[_UIMenuBuilder insertChildMenu:atEndOfMenuForIdentifier:];
-[_UIMenuBuilder _actualChangeCount];
-[_UIMenuBuilder initWithSystem:rootMenu:];
-[_UIMenuBuilder insertElements:beforeCommandForAction:propertyList:];
-[_UIMenuBuilder _system];
-[_UIMenuBuilder set_system:];
-[_UIMenuBuilder replaceMenuForIdentifier:withElements:];
-[_UIMenuBuilder insertElements:atEndOfMenuForIdentifier:];
-[_UIMenuBuilder _patchInternalDiff:];
-[_UIMenuBuilder _firstValidMenuWithinIdentifiers:];
-[_UIMenuBuilder replaceActionForIdentifier:withElements:];
-[_UIMenuBuilder copyWithZone:];
-[_UIMenuBuilder insertSiblingMenu:afterMenuForIdentifier:];
-[_UIMenuBuilder _parentOfMenuForIdentifier:commandForIdentifier:];
-[_UIMenuBuilder removeMenuForIdentifier:];
-[_UIMenuBuilder _internalDiffForDiffv1:];
-[_UIMenuBuilder _patch:];
-[_UIMenuBuilder insertElements:afterCommandForAction:propertyList:];
-[_UIMenuBuilder replaceMenuForIdentifier:withMenu:];
-[_UIMenuBuilder actionForIdentifier:];
-[_UIMenuBuilder insertElements:beforeMenuForIdentifier:];
-[_UIMenuBuilder _keyCommands];
-[_UIMenuBuilder removeActionForIdentifier:];
-[_UIMenuBuilder system];
```
