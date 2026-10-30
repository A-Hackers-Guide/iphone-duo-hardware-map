# `UIDictationSerializableResults`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 11 instance variables, 11 properties, 43 instance methods, 1 class methods

## Instance variables

```
B _fromKeyboard;
B _showMultilingualAlternatives;
B _lowConfidenceAboutLanguageDetection;
B _useServerCapitalization;
B _addTrailingSpace;
B _allowsAlternatives;
B _isFinalResult;
@"NSArray" _phrases;
@"NSArray" _multilingualAlternatives;
^{__CFString=} _transform;
@"NSIndexPath" _indexPathOfInterpretations;
```

## Properties

```
@property (T@"NSArray",C,N,V_phrases) phrases;
@property (T@"NSArray",C,N,V_multilingualAlternatives) multilingualAlternatives;
@property (TB,N,V_fromKeyboard) fromKeyboard;
@property (TB,N,V_showMultilingualAlternatives) showMultilingualAlternatives;
@property (TB,N,V_lowConfidenceAboutLanguageDetection) lowConfidenceAboutLanguageDetection;
@property (T^{__CFString=},N,V_transform) transform;
@property (TB,N,V_useServerCapitalization) useServerCapitalization;
@property (TB,N,V_addTrailingSpace) addTrailingSpace;
@property (T@"NSIndexPath",&,N,V_indexPathOfInterpretations) indexPathOfInterpretations;
@property (TB,R,N,V_allowsAlternatives) allowsAlternatives;
@property (TB,N,V_isFinalResult) isFinalResult;
```

## Class methods

```
+[UIDictationSerializableResults supportsSecureCoding];
```

## Instance methods

```
-[UIDictationSerializableResults text];
-[UIDictationSerializableResults init];
-[UIDictationSerializableResults dealloc];
-[UIDictationSerializableResults setTransform:];
-[UIDictationSerializableResults lowConfidenceAboutLanguageDetection];
-[UIDictationSerializableResults transform];
-[UIDictationSerializableResults setLowConfidenceAboutLanguageDetection:];
-[UIDictationSerializableResults encodeWithCoder:];
-[UIDictationSerializableResults description];
-[UIDictationSerializableResults initWithCoder:];
-[UIDictationSerializableResults copyWithZone:];
-[UIDictationSerializableResults phrases];
-[UIDictationSerializableResults addTrailingSpace];
-[UIDictationSerializableResults allowsAlternatives];
-[UIDictationSerializableResults bestResults];
-[UIDictationSerializableResults bestText];
-[UIDictationSerializableResults bestTextArray];
-[UIDictationSerializableResults bestTextArrayForAlternatives:];
-[UIDictationSerializableResults bestTextForMultilingualAlternatives];
-[UIDictationSerializableResults dictationPhraseArray];
-[UIDictationSerializableResults fromKeyboard];
-[UIDictationSerializableResults indexPathOfInterpretations];
-[UIDictationSerializableResults initWithArrayOfArrayOfStrings:];
-[UIDictationSerializableResults initWithDetectedPhrases:multilingualAlternatives:];
-[UIDictationSerializableResults initWithPhrases:];
-[UIDictationSerializableResults isFinalResult];
-[UIDictationSerializableResults multilingualAlternatives];
-[UIDictationSerializableResults multilingualResultsByLanguageCode];
-[UIDictationSerializableResults secondBestText];
-[UIDictationSerializableResults secondBestTextArray];
-[UIDictationSerializableResults setAddTrailingSpace:];
-[UIDictationSerializableResults setFromKeyboard:];
-[UIDictationSerializableResults setIndexPathOfInterpretations:];
-[UIDictationSerializableResults setIsFinalResult:];
-[UIDictationSerializableResults setMultilingualAlternatives:];
-[UIDictationSerializableResults setPhrases:];
-[UIDictationSerializableResults setShowMultilingualAlternatives:];
-[UIDictationSerializableResults setUseServerCapitalization:];
-[UIDictationSerializableResults showMultilingualAlternatives];
-[UIDictationSerializableResults singleLineResult];
-[UIDictationSerializableResults textArray];
-[UIDictationSerializableResults textArrayForAlternatives:];
-[UIDictationSerializableResults useServerCapitalization];
```
