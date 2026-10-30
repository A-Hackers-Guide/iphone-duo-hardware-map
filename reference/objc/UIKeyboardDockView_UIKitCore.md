# `UIKeyboardDockView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIViewRepresentingKeyboardLayout`
- 6 instance variables, 6 properties, 26 instance methods, 3 class methods

## Instance variables

```
@"<UIKeyboardDockViewDelegate>" _delegate;
@"UIKeyboardDockItem" _leftDockItem;
@"UIKeyboardDockItem" _rightDockItem;
@"UIKeyboardDockItem" _centerDockItem;
@"UIKeyboardModeSwitcherView" _keyboardModeSwitcherView;
q _currentLayoutType;
```

## Properties

```
@property (T@"<UIKeyboardDockViewDelegate>",W,N,V_delegate) delegate;
@property (T@"UIKeyboardDockItem",&,N,V_leftDockItem) leftDockItem;
@property (T@"UIKeyboardDockItem",&,N,V_rightDockItem) rightDockItem;
@property (T@"UIKeyboardDockItem",&,N,V_centerDockItem) centerDockItem;
@property (T@"UIKeyboardModeSwitcherView",&,N,V_keyboardModeSwitcherView) keyboardModeSwitcherView;
@property (Tq,N,V_currentLayoutType) currentLayoutType;
```

## Class methods

```
+[UIKeyboardDockView _currentInterfaceOrientation];
+[UIKeyboardDockView _itemFramesForBoundingSize:];
+[UIKeyboardDockView dockViewHomeGestureExclusionZones];
```

## Instance methods

```
-[UIKeyboardDockView updateLayoutItemType];
-[UIKeyboardDockView _dockItemButtonWasTapped:withEvent:];
-[UIKeyboardDockView keyboardModeSwitcherView];
-[UIKeyboardDockView insetsForDockItems];
-[UIKeyboardDockView setCenterDockItem:];
-[UIKeyboardDockView setRightDockItem:];
-[UIKeyboardDockView dealloc];
-[UIKeyboardDockView setCurrentLayoutType:];
-[UIKeyboardDockView layoutSubviews];
-[UIKeyboardDockView setKeyboardModeSwitcherView:];
-[UIKeyboardDockView _configureDockItem:];
-[UIKeyboardDockView _currentDockItems];
-[UIKeyboardDockView centerDockItem];
-[UIKeyboardDockView _didReceiveHandBiasChangeNotification:];
-[UIKeyboardDockView setDelegate:];
-[UIKeyboardDockView rightDockItem];
-[UIKeyboardDockView currentLayoutType];
-[UIKeyboardDockView delegate];
-[UIKeyboardDockView shouldIgnoreTouchAtPoint:];
-[UIKeyboardDockView _keyboardLayoutView];
-[UIKeyboardDockView setLeftDockItem:];
-[UIKeyboardDockView pointInside:withEvent:];
-[UIKeyboardDockView _dockItemWithButton:];
-[UIKeyboardDockView _keyboardLongPressInteractionRegions];
-[UIKeyboardDockView initWithFrame:];
-[UIKeyboardDockView leftDockItem];
```
