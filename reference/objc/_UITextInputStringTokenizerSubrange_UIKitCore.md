# `_UITextInputStringTokenizerSubrange`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSString" _substring;
@"UITextPosition" _basePosition;
q _indexOfBase;
{_NSRange="location"Q"length"Q} _relevantRange;
```

## Properties

```
@property (T@"NSString",R,N,V_substring) substring;
@property (T@"UITextPosition",R,N,V_basePosition) basePosition;
@property (Tq,N,V_indexOfBase) indexOfBase;
@property (T{_NSRange=QQ},N,V_relevantRange) relevantRange;
```

## Class methods

```
+[_UITextInputStringTokenizerSubrange subrangeWithSubstring:basePosition:];
```

## Instance methods

```
-[_UITextInputStringTokenizerSubrange substring];
-[_UITextInputStringTokenizerSubrange relevantRange];
-[_UITextInputStringTokenizerSubrange indexOfBase];
-[_UITextInputStringTokenizerSubrange setRelevantRange:];
-[_UITextInputStringTokenizerSubrange basePosition];
-[_UITextInputStringTokenizerSubrange description];
-[_UITextInputStringTokenizerSubrange setIndexOfBase:];
```
