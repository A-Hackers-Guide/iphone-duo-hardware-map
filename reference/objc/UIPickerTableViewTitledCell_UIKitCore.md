# `UIPickerTableViewTitledCell`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPickerTableViewCell`
- 3 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"UILabel" _titleLabel;
B _isAttributed;
@"UIColor" _textColor;
```

## Properties

```
@property (T@"NSString",&,N) title;
@property (T@"NSAttributedString",&,N) attributedTitle;
@property (T@"UILabel",R,N,V_titleLabel) _titleLabel;
@property (TB,R,N,V_isAttributed) _isAttributed;
```

## Instance methods

```
-[UIPickerTableViewTitledCell _canBeReusedInPickerView];
-[UIPickerTableViewTitledCell setAttributedTitle:];
-[UIPickerTableViewTitledCell _setIsCenterCell:shouldModifyAlphaOfView:];
-[UIPickerTableViewTitledCell title];
-[UIPickerTableViewTitledCell prepareForReuse];
-[UIPickerTableViewTitledCell attributedTitle];
-[UIPickerTableViewTitledCell setTitle:];
-[UIPickerTableViewTitledCell _isAttributed];
-[UIPickerTableViewTitledCell _titleLabel];
-[UIPickerTableViewTitledCell initWithStyle:reuseIdentifier:textColor:forceTextAlignmentCentered:];
```
