# `_UITextCursorBlinkAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIViewMultiLayerDelegate`, `_UITextCursorAnimation`
- 3 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"CAKeyframeAnimation" _caretBlinkAnimation;
B _enabled;
@"UIView" _cursorShapeView;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,W,N,V_cursorShapeView) cursorShapeView;
@property (TB,N,GisEnabled,V_enabled) enabled;
```

## Instance methods

```
-[_UITextCursorBlinkAnimation reset];
-[_UITextCursorBlinkAnimation cursorShapeDidChange];
-[_UITextCursorBlinkAnimation isEnabled];
-[_UITextCursorBlinkAnimation _outermostLayerDidChange:];
-[_UITextCursorBlinkAnimation setEnabled:];
-[_UITextCursorBlinkAnimation initWithCursorShapeView:];
-[_UITextCursorBlinkAnimation cursorShapeView];
```
