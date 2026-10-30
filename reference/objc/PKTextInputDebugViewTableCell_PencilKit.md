# `PKTextInputDebugViewTableCell`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewCell`
- 8 instance variables, 8 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _showDetailsButton;
@"NSString" _titleText;
@"NSAttributedString" _valueAttributedText;
@"NSString" _statusKey;
@"<PKTextInputDebugViewTableCellDelegate>" _delegate;
@"UILabel" __titleLabel;
@"UILabel" __valueLabel;
@"UIButton" __detailsButton;
```

## Properties

```
@property (T@"UILabel",&,N,V__titleLabel) _titleLabel;
@property (T@"UILabel",&,N,V__valueLabel) _valueLabel;
@property (T@"UIButton",&,N,V__detailsButton) _detailsButton;
@property (T@"NSString",C,N,V_titleText) titleText;
@property (T@"NSAttributedString",C,N,V_valueAttributedText) valueAttributedText;
@property (TB,N,V_showDetailsButton) showDetailsButton;
@property (T@"NSString",C,N,V_statusKey) statusKey;
@property (T@"<PKTextInputDebugViewTableCellDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[PKTextInputDebugViewTableCell setTitleText:];
-[PKTextInputDebugViewTableCell titleText];
-[PKTextInputDebugViewTableCell setDelegate:];
-[PKTextInputDebugViewTableCell _updateLabels];
-[PKTextInputDebugViewTableCell delegate];
-[PKTextInputDebugViewTableCell initWithStyle:reuseIdentifier:];
-[PKTextInputDebugViewTableCell _titleLabel];
-[PKTextInputDebugViewTableCell set_valueLabel:];
-[PKTextInputDebugViewTableCell set_titleLabel:];
-[PKTextInputDebugViewTableCell _valueLabel];
-[PKTextInputDebugViewTableCell _detailsButton];
-[PKTextInputDebugViewTableCell _handleDetailsButton:];
-[PKTextInputDebugViewTableCell _setupContentViewsIfNeeded];
-[PKTextInputDebugViewTableCell setShowDetailsButton:];
-[PKTextInputDebugViewTableCell setStatusKey:];
-[PKTextInputDebugViewTableCell setValueAttributedText:];
-[PKTextInputDebugViewTableCell set_detailsButton:];
-[PKTextInputDebugViewTableCell showDetailsButton];
-[PKTextInputDebugViewTableCell statusKey];
-[PKTextInputDebugViewTableCell valueAttributedText];
```
