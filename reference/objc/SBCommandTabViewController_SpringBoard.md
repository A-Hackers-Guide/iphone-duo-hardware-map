# `SBCommandTabViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBIconViewDelegate`
- 21 instance variables, 5 properties, 26 instance methods, 1 class methods

## Instance variables

```
@"NSMutableOrderedSet" _recentDisplayItems;
Q _selectedIndex;
@"SBIconController" _iconController;
@"SBIconModel" _iconModel;
@"NSMutableArray" _iconViews;
@"UIView" _blurredBackgroundView;
@"UIView" _selectionSquareView;
@"SBIconView" _selectedIconView;
@"UILabel" _selectedIconLabel;
@"NSLayoutConstraint" _selectionXLayoutConstraint;
@"NSLayoutConstraint" _selectedLabelXConstraint;
@"NSLayoutConstraint" _selectedLabelBottomConstraint;
@"UIStackView" _stackView;
@"SBIconView" _homeIconView;
@"UIPanGestureRecognizer" _panGestureRecognizer;
@"UITapGestureRecognizer" _tapDismissGestureRecognizer;
@"UIHoverGestureRecognizer" _hoverGestureRecognizer;
{CGPoint="x"d"y"d} _lastHoverLocation;
B _isTouchDown;
B _isIconSelected;
@"<SBCommandTabViewControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBCommandTabViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBCommandTabViewController canActivateWithRecentDisplayItems:];
```

## Instance methods

```
-[SBCommandTabViewController iconTouchBegan:];
-[SBCommandTabViewController icon:touchEnded:];
-[SBCommandTabViewController next];
-[SBCommandTabViewController previous];
-[SBCommandTabViewController iconTapped:];
-[SBCommandTabViewController dealloc];
-[SBCommandTabViewController viewDidLoad];
-[SBCommandTabViewController setDelegate:];
-[SBCommandTabViewController iconViewDisplaysAccessories:];
-[SBCommandTabViewController delegate];
-[SBCommandTabViewController _updateForUserInterfaceStyle];
-[SBCommandTabViewController iconViewCanBeginDrags:];
-[SBCommandTabViewController canBecomeFirstResponder];
-[SBCommandTabViewController _moveSelectionSquareToIconAtIndex:];
-[SBCommandTabViewController _configureGridLayoutConfiguration:];
-[SBCommandTabViewController _handleCommandTab:];
-[SBCommandTabViewController _handleShiftCommandTab:];
-[SBCommandTabViewController _handleTapDismissGesture:];
-[SBCommandTabViewController _handleUIGesture:];
-[SBCommandTabViewController _updateIconSelectionPositionAndLabelText];
-[SBCommandTabViewController iconModelDidChange:];
-[SBCommandTabViewController indexOfDisplayItem:];
-[SBCommandTabViewController initWithRecentDisplayItems:iconController:];
-[SBCommandTabViewController removeDisplayItem:];
-[SBCommandTabViewController selectedApplicationDisplayItem];
-[SBCommandTabViewController showCommandTabBar];
```
