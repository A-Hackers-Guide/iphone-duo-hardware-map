# `UISDictationVariant`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UISSecureVariant`
- 3 instance variables, 7 properties, 5 instance methods, 3 class methods

## Instance variables

```
I _secureName;
: _selector;
@"NSString" _glyph;
```

## Properties

```
@property (TI,R,N,V_secureName) secureName;
@property (T:,R,N,V_selector) selector;
@property (T@"NSString",R,N,V_glyph) glyph;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISDictationVariant variantForSecureName:];
+[UISDictationVariant allVariants];
+[UISDictationVariant variantForSelector:];
```

## Instance methods

```
-[UISDictationVariant selector];
-[UISDictationVariant glyph];
-[UISDictationVariant secureName];
-[UISDictationVariant localizedStringForLocalization:];
-[UISDictationVariant initWithSecureName:selector:glyph:];
```
