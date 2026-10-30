# `UITextDocumentProxy` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `UIKeyInput`
- 0 instance variables, 5 properties, 8 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,N) documentContextBeforeInput;
@property (T@"NSString",R,N) documentContextAfterInput;
@property (T@"NSString",R,N) selectedText;
@property (T@"UITextInputMode",R,N) documentInputMode;
@property (T@"NSUUID",R,C,N) documentIdentifier;
```

## Instance methods

```
-[UITextDocumentProxy documentInputMode];
-[UITextDocumentProxy unmarkText];
-[UITextDocumentProxy documentContextBeforeInput];
-[UITextDocumentProxy selectedText];
-[UITextDocumentProxy documentIdentifier];
-[UITextDocumentProxy adjustTextPositionByCharacterOffset:];
-[UITextDocumentProxy documentContextAfterInput];
-[UITextDocumentProxy setMarkedText:selectedRange:];
```
