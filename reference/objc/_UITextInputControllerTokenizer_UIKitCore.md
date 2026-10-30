# `_UITextInputControllerTokenizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextInputStringTokenizer`
- 8 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"UITextInputController" _textInput;
^{__CFStringTokenizer=} _tokenizer;
{?="location"q"length"q} _tokenizerRange;
i _tokenizerType;
B _tokenizerIsInvalid;
^{__CFStringTokenizer=} _wordTokenizer;
{?="location"q"length"q} _wordTokenizerRange;
B _wordTokenizerIsInvalid;
```

## Instance methods

```
-[_UITextInputControllerTokenizer _closestTokenSubrangeForPosition:granularity:downstream:];
-[_UITextInputControllerTokenizer dealloc];
-[_UITextInputControllerTokenizer _positionFromPosition:offset:affinity:];
-[_UITextInputControllerTokenizer _indexForTextPosition:];
-[_UITextInputControllerTokenizer invalidateTokenizer];
-[_UITextInputControllerTokenizer _isDownstreamForDirection:atPosition:];
-[_UITextInputControllerTokenizer initWithTextInputController:];
```
