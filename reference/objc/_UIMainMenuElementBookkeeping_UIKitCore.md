# `_UIMainMenuElementBookkeeping`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _menusForIdentifiers;
@"NSMutableDictionary" _deferredElementsForIdentifiers;
@"NSMutableDictionary" _commandsForIdentifiers;
@"NSMutableDictionary" _parentIdentifiersForIdentifiers;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V_menusForIdentifiers) menusForIdentifiers;
@property (T@"NSMutableDictionary",R,N,V_deferredElementsForIdentifiers) deferredElementsForIdentifiers;
@property (T@"NSMutableDictionary",R,N,V_commandsForIdentifiers) commandsForIdentifiers;
@property (T@"NSMutableDictionary",R,N,V_parentIdentifiersForIdentifiers) parentIdentifiersForIdentifiers;
```

## Instance methods

```
-[_UIMainMenuElementBookkeeping init];
-[_UIMainMenuElementBookkeeping hash];
-[_UIMainMenuElementBookkeeping description];
-[_UIMainMenuElementBookkeeping copyWithZone:];
-[_UIMainMenuElementBookkeeping isEqual:];
-[_UIMainMenuElementBookkeeping removeAllObjects];
-[_UIMainMenuElementBookkeeping parentIdentifiersForIdentifiers];
-[_UIMainMenuElementBookkeeping _initWithMenusForIdentifiers:deferredElementsForIdentifiers:commandsForIdentifiers:parentIdentifiersForIdentifiers:];
-[_UIMainMenuElementBookkeeping commandsForIdentifiers];
-[_UIMainMenuElementBookkeeping deferredElementsForIdentifiers];
-[_UIMainMenuElementBookkeeping menusForIdentifiers];
```
