# `UIAlertView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 18 instance variables, 15 properties, 73 instance methods, 3 class methods

## Instance variables

```
@"UIAlertController" _alertController;
@"_UIAlertControllerShimPresenter" _presenter;
@ _retainedSelf;
@"NSMutableArray" _actions;
q _cancelIndex;
q _defaultButtonIndex;
q _firstOtherButtonIndex;
@"NSString" _message;
@"NSString" _subtitle;
q _alertViewStyle;
B _hasPreparedAlertActions;
B _isPresented;
B _alertControllerShouldDismiss;
B _handlingAlertActionShouldDismiss;
B _dismissingAlertController;
@ _delegate;
@ _context;
@"UIViewController" _externalViewControllerForPresentation;
```

## Properties

```
@property (T@,&,N,V_context) context;
@property (Tq,N) defaultButtonIndex;
@property (Tq,N) numberOfRows;
@property (T@"NSString",&,N) subtitle;
@property (T@"UIViewController",&,N,G_externalViewControllerForPresentation,S_setExternalViewControllerForPresentation:,V_externalViewControllerForPresentation) externalViewControllerForPresentation;
@property (T@"NSString",&,N) bodyText;
@property (TB,N) groupsTextFields;
@property (T@,W,N,V_delegate) delegate;
@property (T@"NSString",C,N) title;
@property (T@"NSString",C,N) message;
@property (Tq,R,N) numberOfButtons;
@property (Tq,N) cancelButtonIndex;
@property (Tq,R,N) firstOtherButtonIndex;
@property (TB,R,N,GisVisible) visible;
@property (Tq,N) alertViewStyle;
```

## Class methods

```
+[UIAlertView _alertViewForSessionWithRemoteViewController:];
+[UIAlertView _alertViewForWindow:];
+[UIAlertView _remoteAlertViewWithBlock:];
```

## Instance methods

```
-[UIAlertView _isAnimating];
-[UIAlertView dismissAnimated:];
-[UIAlertView tableView];
-[UIAlertView keyboard];
-[UIAlertView textFieldAtIndex:];
-[UIAlertView setMessage:];
-[UIAlertView dismiss];
-[UIAlertView subtitle];
-[UIAlertView message];
-[UIAlertView titleLabel];
-[UIAlertView backgroundSize];
-[UIAlertView _setAccessoryView:];
-[UIAlertView dealloc];
-[UIAlertView textField];
-[UIAlertView isVisible];
-[UIAlertView window];
-[UIAlertView setSubtitle:];
-[UIAlertView setDelegate:];
-[UIAlertView bodyText];
-[UIAlertView setContext:];
-[UIAlertView title];
-[UIAlertView delegate];
-[UIAlertView show];
-[UIAlertView initWithCoder:];
-[UIAlertView setTitle:];
-[UIAlertView layout];
-[UIAlertView buttonCount];
-[UIAlertView _alertController];
-[UIAlertView numberOfRows];
-[UIAlertView context];
-[UIAlertView initWithFrame:];
-[UIAlertView numberOfButtons];
-[UIAlertView _updateButtonTitle:buttonIndex:];
-[UIAlertView addButtonWithTitle:buttonClass:];
-[UIAlertView _addButtonWithTitle:];
-[UIAlertView _addTextFieldWithValue:label:];
-[UIAlertView _dismissForTappedIndex:];
-[UIAlertView _externalViewControllerForPresentation];
-[UIAlertView _maximumNumberOfTextFieldsForCurrentStyle];
-[UIAlertView _performPresentationDismissalWithClickedButtonIndex:animated:];
-[UIAlertView _prepareAlertActions];
-[UIAlertView _prepareToDismissForTappedIndex:];
-[UIAlertView _preparedAlertActionAtIndex:];
-[UIAlertView _setExternalViewControllerForPresentation:];
-[UIAlertView _setFirstOtherButtonIndex:];
-[UIAlertView _setIsPresented:];
-[UIAlertView _showAnimated:];
-[UIAlertView _textDidChangeInTextField:];
-[UIAlertView _titleLabel];
-[UIAlertView _updateFirstOtherButtonEnabledState];
-[UIAlertView _updateMessageAndSubtitle];
-[UIAlertView addButtonWithTitle:];
-[UIAlertView addButtonWithTitle:label:];
-[UIAlertView addTextFieldWithValue:label:];
-[UIAlertView alertViewStyle];
-[UIAlertView buttonTitleAtIndex:];
-[UIAlertView cancelButtonIndex];
-[UIAlertView defaultButtonIndex];
-[UIAlertView dismissWithClickedButtonIndex:animated:];
-[UIAlertView firstOtherButtonIndex];
-[UIAlertView groupsTextFields];
-[UIAlertView initWithTitle:buttons:defaultButtonIndex:delegate:context:];
-[UIAlertView initWithTitle:message:delegate:cancelButtonTitle:];
-[UIAlertView initWithTitle:message:delegate:cancelButtonTitle:otherButtonTitles:];
-[UIAlertView initWithTitle:message:delegate:defaultButton:cancelButton:otherButtons:];
-[UIAlertView setAlertViewStyle:];
-[UIAlertView setBodyText:];
-[UIAlertView setCancelButtonIndex:];
-[UIAlertView setDefaultButtonIndex:];
-[UIAlertView setGroupsTextFields:];
-[UIAlertView setNumberOfRows:];
-[UIAlertView setTableShouldShowMinimumContent:];
-[UIAlertView textFieldCount];
```
