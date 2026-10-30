# `UIDocumentPasswordView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UITextFieldDelegate`
- 3 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"UIDocumentPasswordField" _passwordTextField;
@"UILabel" _label;
@"NSObject<UIDocumentPasswordViewDelegate>" passwordDelegate;
```

## Properties

```
@property (T@"NSObject<UIDocumentPasswordViewDelegate>",N,VpasswordDelegate) passwordDelegate;
@property (T@"UITextField",R,N,V_passwordTextField) passwordField;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIDocumentPasswordView _canDrawContent];
-[UIDocumentPasswordView dealloc];
-[UIDocumentPasswordView drawRect:];
-[UIDocumentPasswordView textFieldDidBeginEditing:];
-[UIDocumentPasswordView layoutSubviews];
-[UIDocumentPasswordView textFieldDidEndEditing:];
-[UIDocumentPasswordView _labelTextColor];
-[UIDocumentPasswordView _textFieldWidth];
-[UIDocumentPasswordView _labelFont];
-[UIDocumentPasswordView _labelHorizontalOffset];
-[UIDocumentPasswordView _passwordEntered:];
-[UIDocumentPasswordView initWithDocumentName:];
-[UIDocumentPasswordView passwordDelegate];
-[UIDocumentPasswordView passwordField];
-[UIDocumentPasswordView setPasswordDelegate:];
```
