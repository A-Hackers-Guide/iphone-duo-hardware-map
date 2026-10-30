# `_UIMainMenuCommandState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _performable;
@"UIMenuElement<_UIMenuLeaf>" _validatedMenuLeaf;
@"_UIMenuLeafKeyCombination" _localizedKeyCombination;
```

## Properties

```
@property (T@"UIMenuElement<_UIMenuLeaf>",R,N,V_validatedMenuLeaf) _validatedMenuLeaf;
@property (T@"_UIMenuLeafKeyCombination",R,N,V_localizedKeyCombination) _localizedKeyCombination;
@property (TB,R,N,G_isPerformable,V_performable) _performable;
```

## Class methods

```
+[_UIMainMenuCommandState supportsSecureCoding];
```

## Instance methods

```
-[_UIMainMenuCommandState encodeWithCoder:];
-[_UIMainMenuCommandState hash];
-[_UIMainMenuCommandState description];
-[_UIMainMenuCommandState initWithCoder:];
-[_UIMainMenuCommandState isEqual:];
-[_UIMainMenuCommandState _initWithValidatedMenuLeaf:localizedKeyCombination:isPerformable:];
-[_UIMainMenuCommandState _isPerformable];
-[_UIMainMenuCommandState _localizedKeyCombination];
-[_UIMainMenuCommandState _resolvedAttributedTitleWithSecureVariant:];
-[_UIMainMenuCommandState _resolvedImageWithSecureVariant:];
-[_UIMainMenuCommandState _resolvedSelectedImageWithSecureVariant:];
-[_UIMainMenuCommandState _resolvedTitleWithSecureVariant:];
-[_UIMainMenuCommandState _validatedMenuLeaf];
```
