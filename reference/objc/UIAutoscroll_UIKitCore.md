# `UIAutoscroll`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 8 properties, 20 instance methods, 0 class methods

## Instance variables

```
@ m_target;
{CGPoint="x"d"y"d} m_point;
@"UIView<UIAutoscrollContainer>" m_scrollContainer;
i m_directions;
d m_repeatInterval;
@"NSTimer" m_timer;
Q m_count;
B m_active;
B m_disabled;
@ _target;
```

## Properties

```
@property (T@,W,N,V_target) target;
@property (T@"UIView<UIAutoscrollContainer>",&,N,Vm_scrollContainer) scrollContainer;
@property (T{CGPoint=dd},N,Vm_point) point;
@property (Ti,N,Vm_directions) directions;
@property (Td,N,Vm_repeatInterval) repeatInterval;
@property (TQ,N,Vm_count) count;
@property (TB,N,Vm_active) active;
@property (TB,N,Vm_disabled) disabled;
```

## Instance methods

```
-[UIAutoscroll disabled];
-[UIAutoscroll active];
-[UIAutoscroll setCount:];
-[UIAutoscroll repeatInterval];
-[UIAutoscroll setRepeatInterval:];
-[UIAutoscroll dealloc];
-[UIAutoscroll count];
-[UIAutoscroll setActive:];
-[UIAutoscroll invalidate];
-[UIAutoscroll setTarget:];
-[UIAutoscroll point];
-[UIAutoscroll target];
-[UIAutoscroll timerFired:];
-[UIAutoscroll setDisabled:];
-[UIAutoscroll setPoint:];
-[UIAutoscroll scrollContainer];
-[UIAutoscroll directions];
-[UIAutoscroll setDirections:];
-[UIAutoscroll setScrollContainer:];
-[UIAutoscroll startAutoscroll:scrollContainer:point:directions:repeatInterval:];
```
