# `UITableViewLabel`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UILabel`
- 5 instance variables, 2 properties, 17 instance methods, 0 class methods

## Instance variables

```
q _savedNumberOfLines;
d _firstParagraphFirstLineHeadIndent;
@"NSAttributedString" _shadowAttributedText;
B _usingDefaultFont;
@"UITableViewCell" _tableCell;
```

## Properties

```
@property (T@"UITableViewCell",W,N,V_tableCell) tableCell;
@property (TB,R,N,V_usingDefaultFont) usingDefaultFont;
```

## Instance methods

```
-[UITableViewLabel setAttributedText:];
-[UITableViewLabel initWithCoder:];
-[UITableViewLabel traitCollectionDidChange:];
-[UITableViewLabel setText:];
-[UITableViewLabel _disabledFontColor];
-[UITableViewLabel initWithFrame:];
-[UITableViewLabel setFont:];
-[UITableViewLabel _attributedStringHasParagraphStyleWithNonzeroFirstLineHeadIndent:];
-[UITableViewLabel _cleanupErrantFirstLineHeadIndent];
-[UITableViewLabel _clearNumberOfLines];
-[UITableViewLabel _restoreNumberOfLines];
-[UITableViewLabel _setDefaultFont:];
-[UITableViewLabel _setFirstParagraphFirstLineHeadIndent:];
-[UITableViewLabel _setNumberOfLinesForAXLayoutIfNecessary];
-[UITableViewLabel setTableCell:];
-[UITableViewLabel tableCell];
-[UITableViewLabel usingDefaultFont];
```
