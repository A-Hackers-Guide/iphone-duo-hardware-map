# `_UIInputViewControllerState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 16 instance methods, 2 class methods

## Instance variables

```
B _needsInputModeSwitchKey;
@"TIDocumentState" _documentState;
@"TITextInputTraits" _textInputTraits;
@"UITextInputMode" _documentInputMode;
@"NSUUID" _documentIdentifier;
```

## Properties

```
@property (T@"TIDocumentState",&,N,V_documentState) documentState;
@property (T@"TITextInputTraits",&,N,V_textInputTraits) textInputTraits;
@property (T@"UITextInputMode",&,N,V_documentInputMode) documentInputMode;
@property (T@"NSUUID",C,N,V_documentIdentifier) documentIdentifier;
@property (TB,N,V_needsInputModeSwitchKey) needsInputModeSwitchKey;
```

## Class methods

```
+[_UIInputViewControllerState supportsSecureCoding];
+[_UIInputViewControllerState stateForKeyboardState:];
```

## Instance methods

```
-[_UIInputViewControllerState setDocumentState:];
-[_UIInputViewControllerState documentState];
-[_UIInputViewControllerState documentInputMode];
-[_UIInputViewControllerState textInputTraits];
-[_UIInputViewControllerState setTextInputTraits:];
-[_UIInputViewControllerState documentIdentifier];
-[_UIInputViewControllerState encodeWithCoder:];
-[_UIInputViewControllerState needsInputModeSwitchKey];
-[_UIInputViewControllerState description];
-[_UIInputViewControllerState initWithCoder:];
-[_UIInputViewControllerState setDocumentIdentifier:];
-[_UIInputViewControllerState copyWithZone:];
-[_UIInputViewControllerState setDocumentInputMode:];
-[_UIInputViewControllerState isEqual:];
-[_UIInputViewControllerState createDocumentStateIfNecessary];
-[_UIInputViewControllerState setNeedsInputModeSwitchKey:];
```
