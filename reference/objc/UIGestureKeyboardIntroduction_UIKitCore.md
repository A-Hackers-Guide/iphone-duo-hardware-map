# `UIGestureKeyboardIntroduction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"UIKeyboardLayoutStar" m_layout;
@"UIView" m_view;
@"UIKBKeyView" m_firstKeyView;
@"UIKBKeyView" m_secondKeyView;
@? m_completionBlock;
d m_start;
@"NSTimer" m_gestureKeyboardInfoTimer;
{CGPoint="x"d"y"d} m_initPoint;
B m_isInTransition;
B m_hasPeeked;
Q m_insertedTextLength;
```

## Instance methods

```
-[UIGestureKeyboardIntroduction showGestureKeyboardIntroduction];
-[UIGestureKeyboardIntroduction dismissGestureKeyboardIntroduction];
-[UIGestureKeyboardIntroduction dismissGestureKeyboardIntroduction:];
-[UIGestureKeyboardIntroduction initWithLayoutStar:completion:];
-[UIGestureKeyboardIntroduction insertText:forKey:];
-[UIGestureKeyboardIntroduction playGestureKeyboardIntroduction:];
-[UIGestureKeyboardIntroduction tryGestureKeyboardFromView:withEvent:];
```
