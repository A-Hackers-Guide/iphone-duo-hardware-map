# `_UITextAttributeDefaults`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UITextAttributeDefaults`, `NSCopying`
- 1 instance variables, 9 properties, 15 instance methods, 3 class methods

## Instance variables

```
@"_UIMutableTextAttributeDictionary" _attributes;
```

## Properties

```
@property (T@"UIColor",&,N,S_setTextColor:) _textColor;
@property (T@"UIFont",&,N,S_setFont:) _font;
@property (T@"NSParagraphStyle",&,N,S_setParagraphStyle:) _paragraphStyle;
@property (T@"NSShadow",&,N,S_setShadow:) _shadow;
@property (T@"_UITextAttributeDictionary",R,C,N) _attributes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UITextAttributeDefaults _unspecifiedDefaults];
+[_UITextAttributeDefaults _defaultsForUserInterfaceIdiom:];
+[_UITextAttributeDefaults _getFontSizesForUserInterfaceIdiom:labelFontSize:buttonFontSize:systemFontSize:smallSystemFontSize:];
```

## Instance methods

```
-[_UITextAttributeDefaults _font];
-[_UITextAttributeDefaults _setFont:];
-[_UITextAttributeDefaults _setTextColor:];
-[_UITextAttributeDefaults _attributes];
-[_UITextAttributeDefaults _textColor];
-[_UITextAttributeDefaults _initWithFallback:];
-[_UITextAttributeDefaults _setShadow:];
-[_UITextAttributeDefaults _init];
-[_UITextAttributeDefaults _paragraphStyle];
-[_UITextAttributeDefaults _setParagraphStyle:];
-[_UITextAttributeDefaults _shadow];
-[_UITextAttributeDefaults hash];
-[_UITextAttributeDefaults description];
-[_UITextAttributeDefaults copyWithZone:];
-[_UITextAttributeDefaults isEqual:];
```
