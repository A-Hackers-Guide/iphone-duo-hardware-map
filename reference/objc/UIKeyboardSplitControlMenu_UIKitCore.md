# `UIKeyboardSplitControlMenu`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardMenuView`
- Protocols: `_UIInputSwitcherSplitMenu`
- 3 instance variables, 1 properties, 13 instance methods, 2 class methods

## Instance variables

```
{CGSize="width"d"height"d} m_preferredSize;
@"NSArray" _items;
@? _finishSplitTransitionBlock;
```

## Properties

```
@property (T@?,C,N,V_finishSplitTransitionBlock) finishSplitTransitionBlock;
```

## Class methods

```
+[UIKeyboardSplitControlMenu sharedInstance];
+[UIKeyboardSplitControlMenu activeInstance];
```

## Instance methods

```
-[UIKeyboardSplitControlMenu numberOfItems];
-[UIKeyboardSplitControlMenu actionForItem:];
-[UIKeyboardSplitControlMenu initWithFrame:];
-[UIKeyboardSplitControlMenu preferredSize];
-[UIKeyboardSplitControlMenu defaultSelectedIndex];
-[UIKeyboardSplitControlMenu didFinishSplitTransition];
-[UIKeyboardSplitControlMenu didSelectItemAtIndex:];
-[UIKeyboardSplitControlMenu finishSplitTransitionBlock];
-[UIKeyboardSplitControlMenu setFinishSplitTransitionBlock:];
-[UIKeyboardSplitControlMenu setSplitAndUndocked:];
-[UIKeyboardSplitControlMenu titleForItemAtIndex:];
-[UIKeyboardSplitControlMenu usesDeviceLanguageForItemAtIndex:];
-[UIKeyboardSplitControlMenu visibleItemForIndex:];
```
