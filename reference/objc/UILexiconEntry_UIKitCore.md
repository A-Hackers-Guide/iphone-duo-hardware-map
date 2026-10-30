# `UILexiconEntry`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSString" _userInput;
@"NSString" _documentText;
^{CGImage=} _focusedSecureLabel;
^{CGImage=} _unfocusedSecureLabel;
Q _slotID;
```

## Properties

```
@property (T^{CGImage=},R,N,V_focusedSecureLabel) focusedSecureLabel;
@property (T^{CGImage=},R,N,V_unfocusedSecureLabel) unfocusedSecureLabel;
@property (TQ,R,N,V_slotID) slotID;
@property (T@"NSString",R,N,V_documentText) documentText;
@property (T@"NSString",R,N,V_userInput) userInput;
```

## Class methods

```
+[UILexiconEntry _entryWithTILexiconEntry:];
```

## Instance methods

```
-[UILexiconEntry userInput];
-[UILexiconEntry dealloc];
-[UILexiconEntry documentText];
-[UILexiconEntry slotID];
-[UILexiconEntry copyWithZone:];
-[UILexiconEntry isEqual:];
-[UILexiconEntry focusedSecureLabel];
-[UILexiconEntry unfocusedSecureLabel];
```
