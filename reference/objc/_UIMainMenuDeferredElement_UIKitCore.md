# `_UIMainMenuDeferredElement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIMainMenuElement`, `NSSecureCoding`
- 3 instance variables, 7 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"UIDeferredMenuElement" _uiDeferredMenuElement;
@"NSArray" _localProvidedElements;
@"_UIMainMenuDeferredElementIdentifier" _identifier;
```

## Properties

```
@property (T@"UIDeferredMenuElement",R,N,V_uiDeferredMenuElement) _uiDeferredMenuElement;
@property (T@"NSArray",&,N,V_localProvidedElements) _localProvidedElements;
@property (T@"_UIMainMenuDeferredElementIdentifier",R,N,V_identifier) identifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIMainMenuDeferredElement supportsSecureCoding];
```

## Instance methods

```
-[_UIMainMenuDeferredElement identifier];
-[_UIMainMenuDeferredElement encodeWithCoder:];
-[_UIMainMenuDeferredElement hash];
-[_UIMainMenuDeferredElement description];
-[_UIMainMenuDeferredElement initWithCoder:];
-[_UIMainMenuDeferredElement isEqual:];
-[_UIMainMenuDeferredElement _initWithUIDeferredMenuElement:];
-[_UIMainMenuDeferredElement _initWithIdentifier:uiDeferredMenuElement:];
-[_UIMainMenuDeferredElement _localProvidedElements];
-[_UIMainMenuDeferredElement _uiDeferredMenuElement];
-[_UIMainMenuDeferredElement set_localProvidedElements:];
-[_UIMainMenuDeferredElement uiDeferredMenuElementForProvider:];
```
