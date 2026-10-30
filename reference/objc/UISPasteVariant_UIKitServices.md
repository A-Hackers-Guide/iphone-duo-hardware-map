# `UISPasteVariant`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UISSecureVariant`
- 6 instance variables, 10 properties, 8 instance methods, 4 class methods

## Instance variables

```
I _secureName;
: _selector;
@"NSString" _actionIdentifier;
@"NSString" _glyph;
@"NSString" _keyInput;
q _keyModifierFlags;
```

## Properties

```
@property (TI,R,N,V_secureName) secureName;
@property (T:,R,N,V_selector) selector;
@property (T@"NSString",R,N,V_actionIdentifier) actionIdentifier;
@property (T@"NSString",R,N,V_glyph) glyph;
@property (T@"NSString",R,N,V_keyInput) keyInput;
@property (Tq,R,N,V_keyModifierFlags) keyModifierFlags;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISPasteVariant variantForSecureName:];
+[UISPasteVariant allVariants];
+[UISPasteVariant variantForActionIdentifier:];
+[UISPasteVariant variantForSelector:];
```

## Instance methods

```
-[UISPasteVariant selector];
-[UISPasteVariant glyph];
-[UISPasteVariant actionIdentifier];
-[UISPasteVariant keyModifierFlags];
-[UISPasteVariant secureName];
-[UISPasteVariant initWithSecureName:selector:actionIdentifier:glpyh:keyInput:keyModifierFlags:];
-[UISPasteVariant localizedStringForLocalization:];
-[UISPasteVariant keyInput];
```
