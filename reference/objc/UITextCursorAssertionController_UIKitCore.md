# `UITextCursorAssertionController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _assertions;
@"<UITextCursorAssertionControllerSubject>" _subject;
```

## Properties

```
@property (T@"<UITextCursorAssertionControllerSubject>",W,N,V_subject) subject;
```

## Instance methods

```
-[UITextCursorAssertionController setSubject:];
-[UITextCursorAssertionController activeInputModeAssertionWithReason:];
-[UITextCursorAssertionController _createAssertionWithReason:options:userInfo:];
-[UITextCursorAssertionController _endTrackingAssertion:];
-[UITextCursorAssertionController subject];
-[UITextCursorAssertionController debugDescription];
-[UITextCursorAssertionController _isNonBlinking];
-[UITextCursorAssertionController nonBlinkingAssertionWithReason:];
-[UITextCursorAssertionController nonBlinkingGhostAssertionWithReason:];
-[UITextCursorAssertionController dealloc];
-[UITextCursorAssertionController nonVisibleAssertionWithReason:];
-[UITextCursorAssertionController inputModeSelectorAssertionWithReason:userInfo:];
-[UITextCursorAssertionController capslockAssertionWithReason:];
-[UITextCursorAssertionController dictationIndicatorAssertionWithReason:userInfo:];
-[UITextCursorAssertionController _updateSubjectWithAssertionState];
-[UITextCursorAssertionController _beginTrackingAssertion:];
-[UITextCursorAssertionController deleteIndicatorAssertionWithReason:];
```
