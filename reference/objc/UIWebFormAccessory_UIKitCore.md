# `UIWebFormAccessory`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInputView`
- 15 instance variables, 6 properties, 32 instance methods, 1 class methods

## Instance variables

```
@"UIToolbar" _leftToolbar;
@"UIToolbar" _rightToolbar;
@"UIBarButtonItem" _doneButton;
@"UIBarButtonItem" _flexibleSpaceItem;
@"UIBarButtonItem" _previousItem;
@"UIBarButtonItem" _nextItem;
@"UIBarButtonItem" _nextPreviousSpacer;
@"UIBarButtonItem" _autofillSpacer;
@"UIBarButtonItemGroup" _buttonGroupAutoFill;
@"UIBarButtonItemGroup" _buttonGroupNavigation;
B _usesUCB;
@"UISegmentedControl" _tab;
@"UIBarButtonItem" _autofill;
@"UIBarButtonItem" _clearButton;
@"<UIWebFormAccessoryDelegate>" delegate;
```

## Properties

```
@property (T@"UISegmentedControl",&,N,V_tab) _tab;
@property (T@"UIBarButtonItem",&,N,V_autofill) _autofill;
@property (T@"UIBarButtonItem",&,N,V_clearButton) _clearButton;
@property (T@"<UIWebFormAccessoryDelegate>",W,N,Vdelegate) delegate;
@property (TB,N,GisNextEnabled) nextEnabled;
@property (TB,N,GisPreviousEnabled) previousEnabled;
```

## Class methods

```
+[UIWebFormAccessory toolbarWithItems:];
```

## Instance methods

```
-[UIWebFormAccessory done:];
-[UIWebFormAccessory _setRenderConfig:];
-[UIWebFormAccessory dealloc];
-[UIWebFormAccessory layoutSubviews];
-[UIWebFormAccessory _tab];
-[UIWebFormAccessory setDelegate:];
-[UIWebFormAccessory _orientationDidChange:];
-[UIWebFormAccessory delegate];
-[UIWebFormAccessory _clearButton];
-[UIWebFormAccessory clear:];
-[UIWebFormAccessory _autoFillButton];
-[UIWebFormAccessory setNextEnabled:];
-[UIWebFormAccessory _applyTreatmentToAutoFillLabel];
-[UIWebFormAccessory _autofill];
-[UIWebFormAccessory _nextTapped:];
-[UIWebFormAccessory _previousTapped:];
-[UIWebFormAccessory _refreshAutofillPresentation];
-[UIWebFormAccessory _updateFrame];
-[UIWebFormAccessory autoFill:];
-[UIWebFormAccessory hideAutoFillButton];
-[UIWebFormAccessory initForUCB:];
-[UIWebFormAccessory initWithInputAssistantItem:];
-[UIWebFormAccessory isNextEnabled];
-[UIWebFormAccessory isPreviousEnabled];
-[UIWebFormAccessory setClearVisible:];
-[UIWebFormAccessory setNextPreviousItemsVisible:];
-[UIWebFormAccessory setPreviousEnabled:];
-[UIWebFormAccessory set_autofill:];
-[UIWebFormAccessory set_clearButton:];
-[UIWebFormAccessory set_tab:];
-[UIWebFormAccessory showAutoFillButton];
-[UIWebFormAccessory showAutoFillButtonWithTitle:];
```
