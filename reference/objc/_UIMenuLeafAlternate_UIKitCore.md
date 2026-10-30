# `_UIMenuLeafAlternate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIMenuLeafAlternateOrCommandAlternate`, `NSSecureCoding`, `NSCopying`
- 2 instance variables, 9 properties, 13 instance methods, 2 class methods

## Instance variables

```
q _modifierFlags;
@"UIMenuElement<UIMenuLeaf>" _menuLeaf;
```

## Properties

```
@property (T@"_UIMenuLeafAlternate",R,N) leafAlternate;
@property (T@"UICommandAlternate",R,N) commandAlternate;
@property (Tq,R,N) modifierFlags;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,R,N,V_modifierFlags) modifierFlags;
@property (T@"UIMenuElement<UIMenuLeaf>",R,N,V_menuLeaf) menuLeaf;
```

## Class methods

```
+[_UIMenuLeafAlternate supportsSecureCoding];
+[_UIMenuLeafAlternate alternateWithModifierFlags:menuLeaf:];
```

## Instance methods

```
-[_UIMenuLeafAlternate initWithModifierFlags:menuLeaf:];
-[_UIMenuLeafAlternate _alternateWithMenuLeaf:];
-[_UIMenuLeafAlternate modifierFlags];
-[_UIMenuLeafAlternate menuLeaf];
-[_UIMenuLeafAlternate encodeWithCoder:];
-[_UIMenuLeafAlternate alternateLeafWithBaseLeaf:];
-[_UIMenuLeafAlternate hash];
-[_UIMenuLeafAlternate description];
-[_UIMenuLeafAlternate initWithCoder:];
-[_UIMenuLeafAlternate commandAlternate];
-[_UIMenuLeafAlternate leafAlternate];
-[_UIMenuLeafAlternate copyWithZone:];
-[_UIMenuLeafAlternate isEqual:];
```
