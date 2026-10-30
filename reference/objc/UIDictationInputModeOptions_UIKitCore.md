# `UIDictationInputModeOptions`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 8 instance methods, 2 class methods

## Instance variables

```
B _shouldStayInDictationInputModeIfAutoEndpointed;
B _shouldSupressShowingAlternativesAutomatically;
@"NSString" _invocationSource;
```

## Properties

```
@property (T@"NSString",C,N,V_invocationSource) invocationSource;
@property (TB,N,V_shouldStayInDictationInputModeIfAutoEndpointed) shouldStayInDictationInputModeIfAutoEndpointed;
@property (TB,N,V_shouldSupressShowingAlternativesAutomatically) shouldSupressShowingAlternativesAutomatically;
```

## Class methods

```
+[UIDictationInputModeOptions supportsSecureCoding];
+[UIDictationInputModeOptions dictationInputModeOptionsWithInvocationSource:];
```

## Instance methods

```
-[UIDictationInputModeOptions setInvocationSource:];
-[UIDictationInputModeOptions encodeWithCoder:];
-[UIDictationInputModeOptions initWithCoder:];
-[UIDictationInputModeOptions invocationSource];
-[UIDictationInputModeOptions setShouldStayInDictationInputModeIfAutoEndpointed:];
-[UIDictationInputModeOptions setShouldSupressShowingAlternativesAutomatically:];
-[UIDictationInputModeOptions shouldStayInDictationInputModeIfAutoEndpointed];
-[UIDictationInputModeOptions shouldSupressShowingAlternativesAutomatically];
```
