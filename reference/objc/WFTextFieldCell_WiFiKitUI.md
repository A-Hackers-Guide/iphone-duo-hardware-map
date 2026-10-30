# `WFTextFieldCell`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewCell`
- Protocols: `UITextFieldDelegate`
- 12 instance variables, 16 properties, 41 instance methods, 0 class methods

## Instance variables

```
B _editable;
B _hideLabel;
@"UILabel" _label;
@"UITextField" _textField;
@? _textChangeHandler;
@? _returnKeyHandler;
@"NSLayoutConstraint" _trailingMarginConstraint;
@"NSLayoutConstraint" _labelWidthConstraint;
@"UIStackView" _stackView;
@"NSLayoutConstraint" _stackViewTopConstraint;
@"NSLayoutConstraint" _stackViewBottomConstraint;
@"NSLayoutConstraint" _stackViewLeadingConstraint;
```

## Properties

```
@property (T@"NSLayoutConstraint",W,N,V_trailingMarginConstraint) trailingMarginConstraint;
@property (T@"NSLayoutConstraint",W,N,V_labelWidthConstraint) labelWidthConstraint;
@property (T@"UIStackView",W,N,V_stackView) stackView;
@property (T@"NSLayoutConstraint",W,N,V_stackViewTopConstraint) stackViewTopConstraint;
@property (T@"NSLayoutConstraint",W,N,V_stackViewBottomConstraint) stackViewBottomConstraint;
@property (T@"NSLayoutConstraint",W,N,V_stackViewLeadingConstraint) stackViewLeadingConstraint;
@property (T@"UILabel",&,N,V_label) label;
@property (T@"UITextField",W,N,V_textField) textField;
@property (T@?,C,N,V_textChangeHandler) textChangeHandler;
@property (T@?,C,N,V_returnKeyHandler) returnKeyHandler;
@property (TB,N,V_editable) editable;
@property (TB,N,V_hideLabel) hideLabel;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WFTextFieldCell label];
-[WFTextFieldCell setLabel:];
-[WFTextFieldCell dealloc];
-[WFTextFieldCell textField];
-[WFTextFieldCell becomeFirstResponder];
-[WFTextFieldCell setEditing:animated:];
-[WFTextFieldCell textFieldShouldBeginEditing:];
-[WFTextFieldCell copy:];
-[WFTextFieldCell prepareForReuse];
-[WFTextFieldCell setEditable:];
-[WFTextFieldCell stackView];
-[WFTextFieldCell setTrailingMarginConstraint:];
-[WFTextFieldCell setStackView:];
-[WFTextFieldCell traitCollectionDidChange:];
-[WFTextFieldCell canBecomeFirstResponder];
-[WFTextFieldCell setSelected:animated:];
-[WFTextFieldCell trailingMarginConstraint];
-[WFTextFieldCell canPerformAction:withSender:];
-[WFTextFieldCell awakeFromNib];
-[WFTextFieldCell editable];
-[WFTextFieldCell setAccessoryType:];
-[WFTextFieldCell setTextField:];
-[WFTextFieldCell textFieldDidChange:];
-[WFTextFieldCell setStackViewLeadingConstraint:];
-[WFTextFieldCell stackViewLeadingConstraint];
-[WFTextFieldCell _verticalPadding];
-[WFTextFieldCell hideLabel];
-[WFTextFieldCell returnKeyHandler];
-[WFTextFieldCell setReturnKeyHandler:];
-[WFTextFieldCell setStackViewBottomConstraint:];
-[WFTextFieldCell setStackViewTopConstraint:];
-[WFTextFieldCell stackViewBottomConstraint];
-[WFTextFieldCell stackViewTopConstraint];
-[WFTextFieldCell setTextChangeHandler:];
-[WFTextFieldCell textChangeHandler];
-[WFTextFieldCell _adjustStackViewPadding];
-[WFTextFieldCell _updateStackViewForTraitCollection];
-[WFTextFieldCell labelWidthConstraint];
-[WFTextFieldCell setHideLabel:];
-[WFTextFieldCell setLabelWidthConstraint:];
-[WFTextFieldCell textFieldDidEndEditingExit:];
```
