# `_UIMenuLeafKeyboardShortcut`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 6 instance variables, 4 properties, 17 instance methods, 2 class methods

## Instance variables

```
@"_UIMenuLeafKeyCombination" _localizedKeyCombination;
@"NSString" _lastLayout;
I _lastKeyboardType;
B _automaticLocalizationEnabled;
B _automaticMirroringEnabled;
@"_UIMenuLeafKeyCombination" _baseKeyCombination;
```

## Properties

```
@property (T@"_UIMenuLeafKeyCombination",R,N,V_baseKeyCombination) baseKeyCombination;
@property (T@"_UIMenuLeafKeyCombination",R,N) currentLocalizedKeyCombination;
@property (TB,N,GisAutomaticLocalizationEnabled,V_automaticLocalizationEnabled) automaticLocalizationEnabled;
@property (TB,N,GisAutomaticMirroringEnabled,V_automaticMirroringEnabled) automaticMirroringEnabled;
```

## Class methods

```
+[_UIMenuLeafKeyboardShortcut supportsSecureCoding];
+[_UIMenuLeafKeyboardShortcut shortcutWithBaseKeyCombination:];
```

## Instance methods

```
-[_UIMenuLeafKeyboardShortcut isAutomaticMirroringEnabled];
-[_UIMenuLeafKeyboardShortcut setAutomaticMirroringEnabled:];
-[_UIMenuLeafKeyboardShortcut shortcutAddingModifierFlags:];
-[_UIMenuLeafKeyboardShortcut currentLocalizedKeyCombination];
-[_UIMenuLeafKeyboardShortcut _clearLocalizedKeyCombination];
-[_UIMenuLeafKeyboardShortcut isAutomaticLocalizationEnabled];
-[_UIMenuLeafKeyboardShortcut setAutomaticLocalizationEnabled:];
-[_UIMenuLeafKeyboardShortcut initWithBaseKeyCombination:];
-[_UIMenuLeafKeyboardShortcut encodeWithCoder:];
-[_UIMenuLeafKeyboardShortcut _isKeyEquivalentOrKeyCodeSpecialKey];
-[_UIMenuLeafKeyboardShortcut _localizeWithGSKeyboard:automatically:force:forDefaultShortcut:action:];
-[_UIMenuLeafKeyboardShortcut hash];
-[_UIMenuLeafKeyboardShortcut baseKeyCombination];
-[_UIMenuLeafKeyboardShortcut description];
-[_UIMenuLeafKeyboardShortcut initWithCoder:];
-[_UIMenuLeafKeyboardShortcut copyWithZone:];
-[_UIMenuLeafKeyboardShortcut isEqual:];
```
