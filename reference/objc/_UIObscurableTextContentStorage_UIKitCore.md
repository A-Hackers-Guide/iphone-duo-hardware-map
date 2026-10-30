# `_UIObscurableTextContentStorage`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSTextContentStorage`
- 4 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"_UICascadingTextStorage" _cascadingTextStorage;
@"NSAttributedString" _obscuredAttributedString;
B _obscured;
{_NSRange="location"Q"length"Q} _unobscuredRange;
```

## Properties

```
@property (T@"NSAttributedString",R,N) obscuredAttributedString;
@property (TB,N,GisObscured,V_obscured) obscured;
@property (T{_NSRange=QQ},N,V_unobscuredRange) unobscuredRange;
```

## Instance methods

```
-[_UIObscurableTextContentStorage setTextStorage:];
-[_UIObscurableTextContentStorage setUnobscuredRange:];
-[_UIObscurableTextContentStorage initWithTextStorage:];
-[_UIObscurableTextContentStorage attributedString];
-[_UIObscurableTextContentStorage obscuredAttributedString];
-[_UIObscurableTextContentStorage unobscuredRange];
-[_UIObscurableTextContentStorage _validateUnobscuredRange];
-[_UIObscurableTextContentStorage setObscured:];
-[_UIObscurableTextContentStorage processEditingForTextStorage:edited:range:changeInLength:invalidatedRange:];
-[_UIObscurableTextContentStorage isObscured];
-[_UIObscurableTextContentStorage _invalidateObscuredAttributedString];
```
