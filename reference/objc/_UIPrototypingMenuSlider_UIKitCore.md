# `_UIPrototypingMenuSlider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UISlider`
- 6 instance variables, 6 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _didBringKnobToFront;
d _stepSize;
@"UIView" _knobView;
@"UIImageView" _knobBGView;
@"_UIPortalView" _knobPortal;
@"UILabel" _currentValueLabel;
```

## Properties

```
@property (T@"UIView",&,N,V_knobView) knobView;
@property (T@"UIImageView",&,N,V_knobBGView) knobBGView;
@property (T@"_UIPortalView",&,N,V_knobPortal) knobPortal;
@property (T@"UILabel",&,N,V_currentValueLabel) currentValueLabel;
@property (Td,N,V_stepSize) stepSize;
@property (T{CGPoint=dd},R,N) knobCenter;
```

## Instance methods

```
-[_UIPrototypingMenuSlider touchesEnded:withEvent:];
-[_UIPrototypingMenuSlider setValue:animated:];
-[_UIPrototypingMenuSlider touchesCancelled:withEvent:];
-[_UIPrototypingMenuSlider increment];
-[_UIPrototypingMenuSlider value];
-[_UIPrototypingMenuSlider layoutSubviews];
-[_UIPrototypingMenuSlider touchesBegan:withEvent:];
-[_UIPrototypingMenuSlider knobView];
-[_UIPrototypingMenuSlider setKnobView:];
-[_UIPrototypingMenuSlider thumbRectForBounds:trackRect:value:];
-[_UIPrototypingMenuSlider decrement];
-[_UIPrototypingMenuSlider initWithFrame:];
-[_UIPrototypingMenuSlider _setKnobViewProminent:animated:];
-[_UIPrototypingMenuSlider _thumbHitEdgeInsets];
-[_UIPrototypingMenuSlider currentValueLabel];
-[_UIPrototypingMenuSlider knobBGView];
-[_UIPrototypingMenuSlider knobCenter];
-[_UIPrototypingMenuSlider knobPortal];
-[_UIPrototypingMenuSlider setCurrentValueLabel:];
-[_UIPrototypingMenuSlider setKnobBGView:];
-[_UIPrototypingMenuSlider setKnobPortal:];
-[_UIPrototypingMenuSlider setStepSize:];
-[_UIPrototypingMenuSlider stepSize];
```
