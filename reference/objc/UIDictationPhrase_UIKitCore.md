# `UIDictationPhrase`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 9 instance methods, 3 class methods

## Instance variables

```
@"NSString" _text;
@"NSArray" _alternativeInterpretations;
q _style;
```

## Properties

```
@property (Tq,N,V_style) style;
@property (T@"NSString",R,N,V_text) text;
@property (T@"NSArray",R,N,V_alternativeInterpretations) alternativeInterpretations;
```

## Class methods

```
+[UIDictationPhrase supportsSecureCoding];
+[UIDictationPhrase phraseWithText:alternativeInterpretations:];
+[UIDictationPhrase phraseWithText:alternativeInterpretations:style:];
```

## Instance methods

```
-[UIDictationPhrase text];
-[UIDictationPhrase style];
-[UIDictationPhrase setStyle:];
-[UIDictationPhrase encodeWithCoder:];
-[UIDictationPhrase description];
-[UIDictationPhrase initWithCoder:];
-[UIDictationPhrase isEqual:];
-[UIDictationPhrase alternativeInterpretations];
-[UIDictationPhrase initWithText:alternativeInterpretations:style:];
```
