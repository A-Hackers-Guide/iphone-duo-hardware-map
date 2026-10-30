# `UIKeyboardDockItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 12 properties, 23 instance methods, 2 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSString" _title;
@"UIImage" _image;
@"UIAction" _customAction;
@"UITouch" _lastTouchUp;
@"UIKeyboardDockItemButton" _button;
@"UIPanGestureRecognizer" _panGestureRecognizer;
@"UILongPressGestureRecognizer" _longPressGestureRecognizer;
{CGPoint="x"d"y"d} _touchDownPoint;
```

## Properties

```
@property (T@"UIKeyboardDockItemButton",&,N,V_button) button;
@property (T{CGPoint=dd},N,V_touchDownPoint) touchDownPoint;
@property (T@"UIPanGestureRecognizer",&,N,V_panGestureRecognizer) panGestureRecognizer;
@property (T@"UILongPressGestureRecognizer",&,N,V_longPressGestureRecognizer) longPressGestureRecognizer;
@property (TB,N) active;
@property (TB,N) enabled;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (T@"NSString",R,N,V_title) title;
@property (T@"UIImage",R,N,V_image) image;
@property (T@"UIKeyboardDockItemButton",R,N) view;
@property (T@"UIAction",&,N,V_customAction) customAction;
@property (T@"UITouch",&,N,V_lastTouchUp) lastTouchUp;
```

## Class methods

```
+[UIKeyboardDockItem _darkStyleGlyphColor];
+[UIKeyboardDockItem _standardGlyphColor];
```

## Instance methods

```
-[UIKeyboardDockItem panGestureRecognizer];
-[UIKeyboardDockItem active];
-[UIKeyboardDockItem lastTouchUp];
-[UIKeyboardDockItem setPanGestureRecognizer:];
-[UIKeyboardDockItem longPressGestureRecognizer];
-[UIKeyboardDockItem enabled];
-[UIKeyboardDockItem identifier];
-[UIKeyboardDockItem setButton:];
-[UIKeyboardDockItem setLastTouchUp:];
-[UIKeyboardDockItem initWithTitle:image:identifier:];
-[UIKeyboardDockItem setTitle:image:];
-[UIKeyboardDockItem button];
-[UIKeyboardDockItem setActive:];
-[UIKeyboardDockItem setTouchDownPoint:];
-[UIKeyboardDockItem customAction];
-[UIKeyboardDockItem view];
-[UIKeyboardDockItem touchDownPoint];
-[UIKeyboardDockItem title];
-[UIKeyboardDockItem setEnabled:];
-[UIKeyboardDockItem setLongPressGestureRecognizer:];
-[UIKeyboardDockItem image];
-[UIKeyboardDockItem isEqual:];
-[UIKeyboardDockItem setCustomAction:];
```
