# `UICommandAlternate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIMenuLeafAlternateOrCommandAlternate`, `NSCopying`, `NSSecureCoding`
- 4 instance variables, 11 properties, 14 instance methods, 2 class methods

## Instance variables

```
@"NSString" _title;
: _action;
q _modifierFlags;
@ _sender;
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
@property (T@,R,N,V_sender) sender;
@property (T@"NSString",R,N,V_title) title;
@property (T:,R,N,V_action) action;
@property (Tq,R,N,V_modifierFlags) modifierFlags;
```

## Class methods

```
+[UICommandAlternate supportsSecureCoding];
+[UICommandAlternate alternateWithTitle:action:modifierFlags:];
```

## Instance methods

```
-[UICommandAlternate modifierFlags];
-[UICommandAlternate action];
-[UICommandAlternate sender];
-[UICommandAlternate title];
-[UICommandAlternate encodeWithCoder:];
-[UICommandAlternate hash];
-[UICommandAlternate initWithCoder:];
-[UICommandAlternate commandAlternate];
-[UICommandAlternate leafAlternate];
-[UICommandAlternate copyWithZone:];
-[UICommandAlternate isEqual:];
-[UICommandAlternate _resolvedTargetFromFirstTarget:sender:];
-[UICommandAlternate initWithModifierFlags:];
-[UICommandAlternate initWithTitle:action:modifierFlags:];
```
