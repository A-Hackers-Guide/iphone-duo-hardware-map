# `UIPasscodeField`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UITextFieldDelegate`
- 10 instance variables, 4 properties, 26 instance methods, 2 class methods

## Instance variables

```
@"NSMutableString" _value;
@"NSMutableArray" _entryFields;
@"NSMutableArray" _entryBackgrounds;
@"UIButton" _okButton;
B _opaqueBackground;
B _centerHorizontally;
q _keyboardType;
q _keyboardAppearance;
i _emptyContentReturnKeyType;
@ _delegate;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIPasscodeField defaultHeight];
+[UIPasscodeField textFieldClass];
```

## Instance methods

```
-[UIPasscodeField stringValue];
-[UIPasscodeField setKeyboardType:];
-[UIPasscodeField isFirstResponder];
-[UIPasscodeField setStringValue:];
-[UIPasscodeField dealloc];
-[UIPasscodeField becomeFirstResponder];
-[UIPasscodeField appendString:];
-[UIPasscodeField _textDidChange];
-[UIPasscodeField setDelegate:];
-[UIPasscodeField canBecomeFirstResponder];
-[UIPasscodeField initWithFrame:];
-[UIPasscodeField _updateFields];
-[UIPasscodeField deleteLastCharacter];
-[UIPasscodeField hitTest:forEvent:];
-[UIPasscodeField numberOfEntryFields];
-[UIPasscodeField okButtonClicked:];
-[UIPasscodeField setKeyboardType:appearance:];
-[UIPasscodeField setKeyboardType:appearance:emptyContentReturnKeyType:];
-[UIPasscodeField setNumberOfEntryFields:];
-[UIPasscodeField setNumberOfEntryFields:opaqueBackground:];
-[UIPasscodeField setShowsOKButton:];
-[UIPasscodeField setTextCentersHorizontally:];
-[UIPasscodeField showsOKButton];
-[UIPasscodeField textField:shouldInsertText:replacingRange:];
-[UIPasscodeField textFieldDidResignFirstResponder:];
-[UIPasscodeField textFieldShouldStartEditing:];
```
