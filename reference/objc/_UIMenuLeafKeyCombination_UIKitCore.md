# `_UIMenuLeafKeyCombination`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 4 instance variables, 4 properties, 17 instance methods, 3 class methods

## Instance variables

```
B _hasDisplayKeyEquivalentOverride;
q _modifierFlags;
@"NSString" _keyEquivalent;
@"NSIndexSet" _keyCodes;
```

## Properties

```
@property (Tq,R,N,V_modifierFlags) modifierFlags;
@property (T@"NSString",R,N,V_keyEquivalent) keyEquivalent;
@property (T@"NSIndexSet",R,N,V_keyCodes) keyCodes;
@property (T@"NSString",R,N) displayKeyEquivalentOverride;
```

## Class methods

```
+[_UIMenuLeafKeyCombination supportsSecureCoding];
+[_UIMenuLeafKeyCombination combinationWithModifierFlags:keyEquivalent:keyCodes:];
+[_UIMenuLeafKeyCombination combinationWithModifierFlags:keyEquivalent:];
```

## Instance methods

```
-[_UIMenuLeafKeyCombination combinationAddingModifierFlags:];
-[_UIMenuLeafKeyCombination _readableStringForKeyEquivalentUsingWords:forHUD:isSingleCharacterOrKeySymbol:];
-[_UIMenuLeafKeyCombination _setDisplayKeyEquivalentOverride:];
-[_UIMenuLeafKeyCombination keyCodes];
-[_UIMenuLeafKeyCombination modifierFlags];
-[_UIMenuLeafKeyCombination initWithModifierFlags:keyEquivalent:keyCodes:displayKeyEquivalentOverride:];
-[_UIMenuLeafKeyCombination _keyEquivalentStringFromKeyEquivalentOrKeyCodes];
-[_UIMenuLeafKeyCombination _currentGSKeyboard];
-[_UIMenuLeafKeyCombination displayKeyEquivalentOverride];
-[_UIMenuLeafKeyCombination _readableStringForModifierFlagsUsingWords:forHUD:];
-[_UIMenuLeafKeyCombination keyEquivalent];
-[_UIMenuLeafKeyCombination encodeWithCoder:];
-[_UIMenuLeafKeyCombination hash];
-[_UIMenuLeafKeyCombination description];
-[_UIMenuLeafKeyCombination initWithCoder:];
-[_UIMenuLeafKeyCombination copyWithZone:];
-[_UIMenuLeafKeyCombination isEqual:];
```
