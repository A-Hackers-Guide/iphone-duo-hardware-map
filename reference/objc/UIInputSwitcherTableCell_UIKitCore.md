# `UIInputSwitcherTableCell`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewCell`
- 5 instance variables, 6 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _usesDarkTheme;
B _usesStraightLeftEdge;
B _first;
B _last;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _interactiveInsets;
```

## Properties

```
@property (T@"UIInputSwitcherTableCellBackgroundView",&,D,N) backgroundView;
@property (TB,N,V_usesDarkTheme) usesDarkTheme;
@property (TB,N,V_usesStraightLeftEdge) usesStraightLeftEdge;
@property (TB,N,GisFirst,V_first) first;
@property (TB,N,GisLast,V_last) last;
@property (T{UIEdgeInsets=dddd},N,V_interactiveInsets) interactiveInsets;
```

## Class methods

```
+[UIInputSwitcherTableCell reuseIdentifier];
```

## Instance methods

```
-[UIInputSwitcherTableCell layoutSubviews];
-[UIInputSwitcherTableCell setFirst:];
-[UIInputSwitcherTableCell initWithStyle:reuseIdentifier:];
-[UIInputSwitcherTableCell setSelected:animated:];
-[UIInputSwitcherTableCell isFirst];
-[UIInputSwitcherTableCell _updateRoundedCorners];
-[UIInputSwitcherTableCell interactiveInsets];
-[UIInputSwitcherTableCell isLast];
-[UIInputSwitcherTableCell setInteractiveInsets:];
-[UIInputSwitcherTableCell setLast:];
-[UIInputSwitcherTableCell setUsesDarkTheme:];
-[UIInputSwitcherTableCell setUsesStraightLeftEdge:];
-[UIInputSwitcherTableCell updateSelectionWithPoint:];
-[UIInputSwitcherTableCell usesDarkTheme];
-[UIInputSwitcherTableCell usesStraightLeftEdge];
```
