# `UIDictationConnectionOptions`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 18 properties, 36 instance methods, 0 class methods

## Instance variables

```
B _secureInput;
B _useAutomaticEndpointing;
B _acceptsDictationSearchResults;
B _autoPunctuation;
B _shouldRecognizeCommands;
Q _version;
Q _activationType;
@"NSString" _languageCode;
@"NSString" _regionCode;
@"NSString" _fieldIdentifier;
@"NSString" _activationIdentifier;
@"NSString" _layoutIdentifier;
q _keyboardType;
q _returnKeyType;
@"NSString" _prefixText;
@"NSString" _selectedText;
@"NSString" _postfixText;
@ _turnIdentifier;
```

## Properties

```
@property (TQ,N,V_version) version;
@property (TQ,N,V_activationType) activationType;
@property (T@"NSString",C,N,V_languageCode) languageCode;
@property (T@"NSString",C,N,V_regionCode) regionCode;
@property (T@"NSString",C,N,V_fieldIdentifier) fieldIdentifier;
@property (T@"NSString",C,N,V_activationIdentifier) activationIdentifier;
@property (T@"NSString",C,N,V_layoutIdentifier) layoutIdentifier;
@property (Tq,N,V_keyboardType) keyboardType;
@property (Tq,N,V_returnKeyType) returnKeyType;
@property (TB,N,V_secureInput) secureInput;
@property (TB,N,V_useAutomaticEndpointing) useAutomaticEndpointing;
@property (TB,N,V_acceptsDictationSearchResults) acceptsDictationSearchResults;
@property (T@"NSString",C,N,V_prefixText) prefixText;
@property (T@"NSString",C,N,V_selectedText) selectedText;
@property (T@"NSString",C,N,V_postfixText) postfixText;
@property (T@,C,N,V_turnIdentifier) turnIdentifier;
@property (TB,N,V_autoPunctuation) autoPunctuation;
@property (TB,N,V_shouldRecognizeCommands) shouldRecognizeCommands;
```

## Instance methods

```
-[UIDictationConnectionOptions regionCode];
-[UIDictationConnectionOptions setKeyboardType:];
-[UIDictationConnectionOptions setReturnKeyType:];
-[UIDictationConnectionOptions setActivationIdentifier:];
-[UIDictationConnectionOptions setRegionCode:];
-[UIDictationConnectionOptions setSelectedText:];
-[UIDictationConnectionOptions selectedText];
-[UIDictationConnectionOptions activationIdentifier];
-[UIDictationConnectionOptions keyboardType];
-[UIDictationConnectionOptions setPrefixText:];
-[UIDictationConnectionOptions version];
-[UIDictationConnectionOptions acceptsDictationSearchResults];
-[UIDictationConnectionOptions languageCode];
-[UIDictationConnectionOptions activationType];
-[UIDictationConnectionOptions setUseAutomaticEndpointing:];
-[UIDictationConnectionOptions setTurnIdentifier:];
-[UIDictationConnectionOptions setVersion:];
-[UIDictationConnectionOptions setActivationType:];
-[UIDictationConnectionOptions prefixText];
-[UIDictationConnectionOptions turnIdentifier];
-[UIDictationConnectionOptions setAcceptsDictationSearchResults:];
-[UIDictationConnectionOptions useAutomaticEndpointing];
-[UIDictationConnectionOptions returnKeyType];
-[UIDictationConnectionOptions setLanguageCode:];
-[UIDictationConnectionOptions autoPunctuation];
-[UIDictationConnectionOptions fieldIdentifier];
-[UIDictationConnectionOptions setSecureInput:];
-[UIDictationConnectionOptions setPostfixText:];
-[UIDictationConnectionOptions layoutIdentifier];
-[UIDictationConnectionOptions postfixText];
-[UIDictationConnectionOptions secureInput];
-[UIDictationConnectionOptions setAutoPunctuation:];
-[UIDictationConnectionOptions setFieldIdentifier:];
-[UIDictationConnectionOptions setLayoutIdentifier:];
-[UIDictationConnectionOptions setShouldRecognizeCommands:];
-[UIDictationConnectionOptions shouldRecognizeCommands];
```
