# `UISwipeActionsConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
B _performsFirstActionWithFullSwipe;
B _autosizesButtons;
@"NSArray" _actions;
q __swipeActionsStyle;
d __roundedStyleCornerRadius;
```

## Properties

```
@property (TB,N,G_autosizesButtons,S_setAutosizesButtons:,V_autosizesButtons) autosizesButtons;
@property (Tq,N,G_swipeActionsStyle,S_setSwipeActionsStyle:,V__swipeActionsStyle) _swipeActionsStyle;
@property (Td,N,G_roundedStyleCornerRadius,S_setRoundedStyleCornerRadius:,V__roundedStyleCornerRadius) _roundedStyleCornerRadius;
@property (T@"NSArray",R,C,N,V_actions) actions;
@property (TB,N,V_performsFirstActionWithFullSwipe) performsFirstActionWithFullSwipe;
```

## Class methods

```
+[UISwipeActionsConfiguration configurationWithActions:];
```

## Instance methods

```
-[UISwipeActionsConfiguration init];
-[UISwipeActionsConfiguration actions];
-[UISwipeActionsConfiguration description];
-[UISwipeActionsConfiguration _autosizesButtons];
-[UISwipeActionsConfiguration _roundedStyleCornerRadius];
-[UISwipeActionsConfiguration _setAutosizesButtons:];
-[UISwipeActionsConfiguration _setRoundedStyleCornerRadius:];
-[UISwipeActionsConfiguration _setSwipeActionsStyle:];
-[UISwipeActionsConfiguration _swipeActionsStyle];
-[UISwipeActionsConfiguration performsFirstActionWithFullSwipe];
-[UISwipeActionsConfiguration setPerformsFirstActionWithFullSwipe:];
```
