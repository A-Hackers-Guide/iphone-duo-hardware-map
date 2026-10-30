# `UITextInputStringTokenizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITextInputTokenizer`
- 1 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"UIResponder<UITextInput>" _textInput;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UITextInputStringTokenizer _closestTokenSubrangeForPosition:granularity:downstream:];
-[UITextInputStringTokenizer _distanceForTokenizerWithGranularity:];
-[UITextInputStringTokenizer isPosition:withinTextUnit:inDirection:];
-[UITextInputStringTokenizer isPosition:atBoundary:inDirection:];
-[UITextInputStringTokenizer positionFromPosition:toBoundary:inDirection:];
-[UITextInputStringTokenizer _positionFromPosition:offset:affinity:];
-[UITextInputStringTokenizer _indexForTextPosition:];
-[UITextInputStringTokenizer initWithTextInput:];
-[UITextInputStringTokenizer _isDownstreamForDirection:atPosition:];
-[UITextInputStringTokenizer rangeEnclosingPosition:withGranularity:inDirection:];
```
