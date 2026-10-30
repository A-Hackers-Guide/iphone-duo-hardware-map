# `UIWebFormDelegate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WebFormDelegate`
- 2 instance variables, 4 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"UIWebBrowserView" _webBrowserView;
@"_UIWebFormDelegateEditedFormsMap" _editedForms;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIWebFormDelegate dealloc];
-[UIWebFormDelegate textFieldDidEndEditing:inFrame:];
-[UIWebFormDelegate frame:sourceFrame:willSubmitForm:withValues:submissionListener:];
-[UIWebFormDelegate _clearEditedFormsInFrame:];
-[UIWebFormDelegate _didEditFormElement:inFrame:];
-[UIWebFormDelegate _shouldIgnoreFormTextChangesInFrame:];
-[UIWebFormDelegate acceptedAutoFillWord:];
-[UIWebFormDelegate dataSourceHasChangedForFrame:];
-[UIWebFormDelegate didFocusTextField:inFrame:];
-[UIWebFormDelegate formWasEdited];
-[UIWebFormDelegate hasCurrentSuggestions];
-[UIWebFormDelegate initWithWebBrowserView:];
-[UIWebFormDelegate suggestionsForString:inputIndex:];
-[UIWebFormDelegate textDidChangeInTextArea:inFrame:];
-[UIWebFormDelegate textDidChangeInTextField:inFrame:];
-[UIWebFormDelegate textField:doCommandBySelector:inFrame:];
-[UIWebFormDelegate textFieldDidBeginEditing:inFrame:];
-[UIWebFormDelegate willSendSubmitEventToForm:inFrame:withValues:];
```
