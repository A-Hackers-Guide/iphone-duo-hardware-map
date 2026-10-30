# `_UIMainMenuSessionLocalCache`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"_UIMainMenuElementBookkeeping" _elementBookkeeping;
@"_UIMenuLeafValidator" _leafValidator;
@"NSMutableDictionary" _validatedMenuLeavesForIdentifiers;
@"UIResponder" _firstResponder;
@"NSMutableDictionary" _menuStates;
@"NSMutableDictionary" _deferredElementStates;
@"NSMutableDictionary" _commandStates;
@"NSMutableDictionary" _pendingDeferredElementRequestHandlers;
```

## Properties

```
@property (T@"_UIMainMenuElementBookkeeping",R,N,V_elementBookkeeping) elementBookkeeping;
@property (T@"_UIMenuLeafValidator",&,N,V_leafValidator) leafValidator;
@property (T@"NSMutableDictionary",R,N,V_validatedMenuLeavesForIdentifiers) validatedMenuLeavesForIdentifiers;
@property (T@"UIResponder",W,N,V_firstResponder) firstResponder;
@property (T@"NSMutableDictionary",&,N,V_menuStates) menuStates;
@property (T@"NSMutableDictionary",&,N,V_deferredElementStates) deferredElementStates;
@property (T@"NSMutableDictionary",&,N,V_commandStates) commandStates;
@property (T@"NSMutableDictionary",&,N,V_pendingDeferredElementRequestHandlers) pendingDeferredElementRequestHandlers;
```

## Instance methods

```
-[_UIMainMenuSessionLocalCache commandStates];
-[_UIMainMenuSessionLocalCache deferredElementStates];
-[_UIMainMenuSessionLocalCache elementBookkeeping];
-[_UIMainMenuSessionLocalCache firstResponder];
-[_UIMainMenuSessionLocalCache initWithBaseMenuBookkeeping:];
-[_UIMainMenuSessionLocalCache leafValidator];
-[_UIMainMenuSessionLocalCache menuStates];
-[_UIMainMenuSessionLocalCache pendingDeferredElementRequestHandlers];
-[_UIMainMenuSessionLocalCache setCommandStates:];
-[_UIMainMenuSessionLocalCache setDeferredElementStates:];
-[_UIMainMenuSessionLocalCache setFirstResponder:];
-[_UIMainMenuSessionLocalCache setLeafValidator:];
-[_UIMainMenuSessionLocalCache setMenuStates:];
-[_UIMainMenuSessionLocalCache setPendingDeferredElementRequestHandlers:];
-[_UIMainMenuSessionLocalCache validatedMenuLeavesForIdentifiers];
```
