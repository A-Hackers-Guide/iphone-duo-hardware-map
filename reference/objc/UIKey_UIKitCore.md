# `UIKey`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSCoding`
- 4 instance variables, 6 properties, 22 instance methods, 0 class methods

## Instance variables

```
q _modifierFlags;
q _keyCode;
@"NSString" _unmodifiedInput;
@"NSString" _modifiedInput;
```

## Properties

```
@property (T@"NSString",&,N,S_setUnmodifiedInput:,V_unmodifiedInput) unmodifiedInput;
@property (T@"NSString",&,N,S_setModifiedInput:,V_modifiedInput) modifiedInput;
@property (Tq,N,S_setModifierFlags:,V_modifierFlags) modifierFlags;
@property (Tq,N,S_setKeyCode:,V_keyCode) keyCode;
@property (T@"NSString",R,N) characters;
@property (T@"NSString",R,N) charactersIgnoringModifiers;
```

## Instance methods

```
-[UIKey characters];
-[UIKey modiferFlagsWithoutCapsLockOrNumberPad];
-[UIKey _setModifiedInput:];
-[UIKey _initWithKey:];
-[UIKey _setUnmodifiedInput:];
-[UIKey modifiedInput];
-[UIKey modifierFlags];
-[UIKey equalsKeyCode:modifiers:];
-[UIKey modifiersEqual:];
-[UIKey keyCode];
-[UIKey encodeWithCoder:];
-[UIKey hash];
-[UIKey description];
-[UIKey initWithCoder:];
-[UIKey _setModifierFlags:];
-[UIKey initWithKeyboardEvent:];
-[UIKey unmodifiedKeyCodeEquals:];
-[UIKey _setKeyCode:];
-[UIKey charactersIgnoringModifiers];
-[UIKey copyWithZone:];
-[UIKey isEqual:];
-[UIKey unmodifiedInput];
```
