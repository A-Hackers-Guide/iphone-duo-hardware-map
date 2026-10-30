# `UIKeyEvent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 24 instance methods, 3 class methods

## Instance variables

```
B _keyRepeating;
i _inputFlags;
@"NSString" _characters;
@"NSString" _charactersIgnoringModifiers;
q _type;
q _keyCode;
d _timestamp;
q _modifierFlags;
@"NSString" _inputManagerHint;
@"WebEvent" _webEvent;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (T@"NSString",C,N,V_characters) characters;
@property (T@"NSString",C,N,V_charactersIgnoringModifiers) charactersIgnoringModifiers;
@property (TB,N,GisKeyRepeating,V_keyRepeating) keyRepeating;
@property (Tq,N,V_keyCode) keyCode;
@property (Td,N,V_timestamp) timestamp;
@property (Tq,N,V_modifierFlags) modifierFlags;
@property (Ti,N,V_inputFlags) inputFlags;
@property (T@"NSString",&,N,V_inputManagerHint) inputManagerHint;
@property (T@"WebEvent",&,N,V_webEvent) webEvent;
```

## Class methods

```
+[UIKeyEvent modifierFlagsFromWebFlags:];
+[UIKeyEvent stringFromKeyEventType:];
+[UIKeyEvent typeFromWebEventType:];
```

## Instance methods

```
-[UIKeyEvent characters];
-[UIKeyEvent setTimestamp:];
-[UIKeyEvent setInputManagerHint:];
-[UIKeyEvent setCharacters:];
-[UIKeyEvent timestamp];
-[UIKeyEvent modifierFlags];
-[UIKeyEvent setModifierFlags:];
-[UIKeyEvent keyCode];
-[UIKeyEvent setType:];
-[UIKeyEvent type];
-[UIKeyEvent setKeyCode:];
-[UIKeyEvent description];
-[UIKeyEvent inputManagerHint];
-[UIKeyEvent charactersIgnoringModifiers];
-[UIKeyEvent copyWithZone:];
-[UIKeyEvent setCharactersIgnoringModifiers:];
-[UIKeyEvent copyWithUpdatedKeyEventType:];
-[UIKeyEvent initWithWebEvent:];
-[UIKeyEvent inputFlags];
-[UIKeyEvent isKeyRepeating];
-[UIKeyEvent setInputFlags:];
-[UIKeyEvent setKeyRepeating:];
-[UIKeyEvent setWebEvent:];
-[UIKeyEvent webEvent];
```
