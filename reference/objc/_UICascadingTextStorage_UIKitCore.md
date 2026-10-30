# `_UICascadingTextStorage`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSConcreteTextStorage`
- 2 instance variables, 10 properties, 33 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _defaultAttributes;
@"<_UITextAttributeDefaults>" _defaults;
```

## Properties

```
@property (T@"UIFont",&,N) font;
@property (T@"UIColor",&,N) textColor;
@property (T@"UIColor",&,N) shadowColor;
@property (T{CGSize=dd},N) shadowOffset;
@property (Tq,N) textAlignment;
@property (Tq,N) lineBreakMode;
@property (Td,N) shadowBlur;
@property (T@"NSDictionary",C,N) defaultAttributes;
@property (Tq,N) defaultBaseWritingDirection;
@property (T@"<_UITextAttributeDefaults>",&,N,S_setDefaults:,V_defaults) _defaults;
```

## Class methods

```
+[_UICascadingTextStorage defaultFont];
```

## Instance methods

```
-[_UICascadingTextStorage setDefaultAttributes:];
-[_UICascadingTextStorage defaultAttributes];
-[_UICascadingTextStorage setShadowBlur:];
-[_UICascadingTextStorage shadowBlur];
-[_UICascadingTextStorage setTextAlignment:];
-[_UICascadingTextStorage _shouldSetOriginalFontAttribute];
-[_UICascadingTextStorage attributesAtIndex:longestEffectiveRange:inRange:];
-[_UICascadingTextStorage textAlignment];
-[_UICascadingTextStorage attribute:atIndex:effectiveRange:];
-[_UICascadingTextStorage _defaults];
-[_UICascadingTextStorage setShadowOffset:];
-[_UICascadingTextStorage textColor];
-[_UICascadingTextStorage init];
-[_UICascadingTextStorage attributesAtIndex:effectiveRange:];
-[_UICascadingTextStorage attribute:atIndex:longestEffectiveRange:inRange:];
-[_UICascadingTextStorage setDefaultBaseWritingDirection:];
-[_UICascadingTextStorage setTextColor:];
-[_UICascadingTextStorage shadowColor];
-[_UICascadingTextStorage _ui_resolvedTextAlignment];
-[_UICascadingTextStorage _setShadow:];
-[_UICascadingTextStorage _restoreOriginalFontAttribute];
-[_UICascadingTextStorage defaultBaseWritingDirection];
-[_UICascadingTextStorage _shadow];
-[_UICascadingTextStorage initWithDefaults:];
-[_UICascadingTextStorage setShadowColor:];
-[_UICascadingTextStorage font];
-[_UICascadingTextStorage _setDefaults:];
-[_UICascadingTextStorage _defaultAttributes];
-[_UICascadingTextStorage setLineBreakMode:];
-[_UICascadingTextStorage shadowOffset];
-[_UICascadingTextStorage lineBreakMode];
-[_UICascadingTextStorage resolvedWritingDirectionForBaseWritingDirection:];
-[_UICascadingTextStorage setFont:];
```
