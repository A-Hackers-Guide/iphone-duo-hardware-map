# `_UICursorAccessoryViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `_UICursorAccessoryItemDataSource`
- 8 instance variables, 14 properties, 33 instance methods, 0 class methods

## Instance variables

```
B _visible;
@"<_UICursorAccessoryViewControllerDelegate>" _delegate;
@"NSArray" _selectionRects;
@"UITextRange" _selectedRange;
@"NSArray" _accessories;
@"_UICursorAccessoryHostView" _hostView;
@"NSDictionary" _accessoriesByIdentifier;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _cursorRect;
```

## Properties

```
@property (T@"_UICursorAccessoryHostView",&,N,V_hostView) hostView;
@property (T@"NSDictionary",&,N,V_accessoriesByIdentifier) accessoriesByIdentifier;
@property (T@"<_UICursorAccessoryViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_cursorRect) cursorRect;
@property (T@"NSArray",&,N,V_selectionRects) selectionRects;
@property (T@"UITextRange",&,N,V_selectedRange) selectedRange;
@property (T@"UIColor",&,N) accessoryTintColor;
@property (TB,N) touchFallbackEnabled;
@property (T@"NSArray",&,N,V_accessories) accessories;
@property (TB,N,GisVisible,V_visible) visible;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UICursorAccessoryViewController setSelectedRange:];
-[_UICursorAccessoryViewController selectedRange];
-[_UICursorAccessoryViewController hostView];
-[_UICursorAccessoryViewController setHostView:];
-[_UICursorAccessoryViewController _setSelectionRect:preferredPlacement:animated:];
-[_UICursorAccessoryViewController setVisible:animationStyle:];
-[_UICursorAccessoryViewController setVisible:];
-[_UICursorAccessoryViewController setVisible:animationStyle:completion:];
-[_UICursorAccessoryViewController init];
-[_UICursorAccessoryViewController isVisible];
-[_UICursorAccessoryViewController viewDidLoad];
-[_UICursorAccessoryViewController setTouchFallbackEnabled:];
-[_UICursorAccessoryViewController accessories];
-[_UICursorAccessoryViewController setAccessories:animated:];
-[_UICursorAccessoryViewController setCursorRect:];
-[_UICursorAccessoryViewController _canShowWhileLocked];
-[_UICursorAccessoryViewController setDelegate:];
-[_UICursorAccessoryViewController cursorRect];
-[_UICursorAccessoryViewController didTapToActivateAccessoryWithIdentifier:];
-[_UICursorAccessoryViewController hitTest:withEvent:fromView:];
-[_UICursorAccessoryViewController setSelectionRects:];
-[_UICursorAccessoryViewController loadView];
-[_UICursorAccessoryViewController selectionRects];
-[_UICursorAccessoryViewController setAccessories:];
-[_UICursorAccessoryViewController delegate];
-[_UICursorAccessoryViewController _contentForAccessory:];
-[_UICursorAccessoryViewController setAccessoriesByIdentifier:];
-[_UICursorAccessoryViewController accessoryTintColor];
-[_UICursorAccessoryViewController configureItemView:forAccessoryIdentifier:];
-[_UICursorAccessoryViewController touchFallbackEnabled];
-[_UICursorAccessoryViewController _updateSelectionRectAnimated:];
-[_UICursorAccessoryViewController accessoriesByIdentifier];
-[_UICursorAccessoryViewController setAccessoryTintColor:];
```
