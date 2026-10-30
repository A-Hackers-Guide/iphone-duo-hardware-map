# `_UICursorAccessory`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 22 instance methods, 1 class methods

## Instance variables

```
B _interactive;
B _large;
@"NSString" _identifier;
@"NSString" _groupIdentifier;
d _preferredWidth;
Q _style;
```

## Properties

```
@property (T@"NSString",C,N,V_identifier) identifier;
@property (T@"NSString",C,N,V_groupIdentifier) groupIdentifier;
@property (Td,N,V_preferredWidth) preferredWidth;
@property (TB,N,GisInteractive,V_interactive) interactive;
@property (TB,N,GisLarge,V_large) large;
@property (TQ,N,V_style) style;
```

## Class methods

```
+[_UICursorAccessory supportsSecureCoding];
```

## Instance methods

```
-[_UICursorAccessory groupIdentifier];
-[_UICursorAccessory identifier];
-[_UICursorAccessory isInteractive];
-[_UICursorAccessory style];
-[_UICursorAccessory setStyle:];
-[_UICursorAccessory setIdentifier:];
-[_UICursorAccessory preferredWidth];
-[_UICursorAccessory setPreferredWidth:];
-[_UICursorAccessory encodeWithCoder:];
-[_UICursorAccessory hash];
-[_UICursorAccessory description];
-[_UICursorAccessory initWithCoder:];
-[_UICursorAccessory setLarge:];
-[_UICursorAccessory descriptionBuilder];
-[_UICursorAccessory isEqual:];
-[_UICursorAccessory setInteractive:];
-[_UICursorAccessory setGroupIdentifier:];
-[_UICursorAccessory isLarge];
-[_UICursorAccessory _deleteCursorAccessory];
-[_UICursorAccessory _dictationCursorAccessory];
-[_UICursorAccessory _inputModeCursorAccessory];
-[_UICursorAccessory _modifierKeyCursorAccessory];
```
