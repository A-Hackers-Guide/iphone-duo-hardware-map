# `UITableViewCellEditingData`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 1 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"UITableViewCell" _cell;
q _editingStyle;
@"UITableViewCellEditControl" _editControl;
@"UITableViewCellReorderControl" _reorderControl;
@"UIView" _reorderSeparatorView;
{?="addedEditControlAsSubview"b1"addedReorderControlAsSubview"b1"addedReorderSeparatorViewAsSubview"b1} _flags;
```

## Properties

```
@property (TB,R,N) wantsMaskingWhileAnimatingDisabled;
```

## Instance methods

```
-[UITableViewCellEditingData dealloc];
-[UITableViewCellEditingData reorderControl:];
-[UITableViewCellEditingData editControl:];
-[UITableViewCellEditingData initWithTableViewCell:editingStyle:];
-[UITableViewCellEditingData reorderSeparatorView:];
-[UITableViewCellEditingData wantsMaskingWhileAnimatingDisabled];
```
