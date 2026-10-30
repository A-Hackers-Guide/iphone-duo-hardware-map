# `_UIPhysicalKeyTranslationMap`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 14 instance methods, 2 class methods

## Instance variables

```
I _keyCode;
I _keyAction;
@"NSMapTable" _translationMap;
q _originalModifiers;
```

## Properties

```
@property (T@"NSMapTable",R,N,V_translationMap) translationMap;
@property (TI,R,V_keyCode) keyCode;
@property (TI,R,V_keyAction) keyAction;
@property (Tq,R,V_originalModifiers) originalModifiers;
```

## Class methods

```
+[_UIPhysicalKeyTranslationMap supportsSecureCoding];
+[_UIPhysicalKeyTranslationMap enumerateAllCombinationsOfModifiers:staticModifiers:usingBlock:];
```

## Instance methods

```
-[_UIPhysicalKeyTranslationMap originalModifiers];
-[_UIPhysicalKeyTranslationMap areModifiers:minimalExcessOfMask:matching:translator:matchedModifierSubset:betterMatchFound:];
-[_UIPhysicalKeyTranslationMap setKeyTranslation:modifiers:];
-[_UIPhysicalKeyTranslationMap keyAction];
-[_UIPhysicalKeyTranslationMap populateAllCombinationsOfModifiers:translator:];
-[_UIPhysicalKeyTranslationMap keyCode];
-[_UIPhysicalKeyTranslationMap keyTranslationWithModifiers:translator:];
-[_UIPhysicalKeyTranslationMap encodeWithCoder:];
-[_UIPhysicalKeyTranslationMap initWithKeyCode:action:modifiers:];
-[_UIPhysicalKeyTranslationMap initWithCoder:];
-[_UIPhysicalKeyTranslationMap copyWithZone:];
-[_UIPhysicalKeyTranslationMap keyTranslation:withModifiers:];
-[_UIPhysicalKeyTranslationMap allTranslations];
-[_UIPhysicalKeyTranslationMap translationMap];
```
