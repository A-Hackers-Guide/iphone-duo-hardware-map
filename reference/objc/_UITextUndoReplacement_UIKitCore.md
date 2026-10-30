# `_UITextUndoReplacement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSAttributedString" _attributedString;
{_NSRange="location"Q"length"Q} _affectedRange;
{_NSRange="location"Q"length"Q} _replacementTextRange;
```

## Properties

```
@property (T@"NSAttributedString",C,N,V_attributedString) attributedString;
@property (T{_NSRange=QQ},R,N,V_affectedRange) affectedRange;
@property (T{_NSRange=QQ},R,N,V_replacementTextRange) replacementTextRange;
```

## Instance methods

```
-[_UITextUndoReplacement setAttributedString:];
-[_UITextUndoReplacement attributedString];
-[_UITextUndoReplacement description];
-[_UITextUndoReplacement affectedRange];
-[_UITextUndoReplacement initWithAttributedString:affectedRange:replacementTextRange:];
-[_UITextUndoReplacement replacementTextRange];
```
