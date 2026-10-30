# `UIKeyboardPathEffectView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 7 instance variables, 7 properties, 29 instance methods, 0 class methods

## Instance variables

```
B _increasedContrastEnabled;
B _done;
@"UIKBHandwritingQuadCurvePointFIFO" _pointInterpolator;
d _startTime;
@"NSMutableArray" _paths;
@"NSMutableIndexSet" _pointDecayQueue;
@"CADisplayLink" _pointDecayDisplayLink;
```

## Properties

```
@property (T@"UIKBHandwritingQuadCurvePointFIFO",&,N,V_pointInterpolator) pointInterpolator;
@property (Td,N,V_startTime) startTime;
@property (T@"NSMutableArray",&,N,V_paths) paths;
@property (TB,N,V_increasedContrastEnabled) increasedContrastEnabled;
@property (TB,N,V_done) done;
@property (T@"NSMutableIndexSet",&,N,V_pointDecayQueue) pointDecayQueue;
@property (T@"CADisplayLink",&,N,V_pointDecayDisplayLink) pointDecayDisplayLink;
```

## Instance methods

```
-[UIKeyboardPathEffectView _displayLinkFired:];
-[UIKeyboardPathEffectView setPaths:];
-[UIKeyboardPathEffectView _addDrawingPoint:force:sentinel:];
-[UIKeyboardPathEffectView didMoveToWindow];
-[UIKeyboardPathEffectView setDone:];
-[UIKeyboardPathEffectView addPoint:force:timestamp:];
-[UIKeyboardPathEffectView setIncreasedContrastEnabled:];
-[UIKeyboardPathEffectView done];
-[UIKeyboardPathEffectView startTime];
-[UIKeyboardPathEffectView drawRect:];
-[UIKeyboardPathEffectView increasedContrastEnabled];
-[UIKeyboardPathEffectView reset];
-[UIKeyboardPathEffectView setPointDecayDisplayLink:];
-[UIKeyboardPathEffectView pointDecayQueue];
-[UIKeyboardPathEffectView _pushNewPath];
-[UIKeyboardPathEffectView setStartTime:];
-[UIKeyboardPathEffectView keyboardAppearance];
-[UIKeyboardPathEffectView paths];
-[UIKeyboardPathEffectView setPointInterpolator:];
-[UIKeyboardPathEffectView buildOut];
-[UIKeyboardPathEffectView accessibilityValueChanged:];
-[UIKeyboardPathEffectView pointDecayDisplayLink];
-[UIKeyboardPathEffectView setPointDecayQueue:];
-[UIKeyboardPathEffectView _currentThemeSettings];
-[UIKeyboardPathEffectView _currentPath];
-[UIKeyboardPathEffectView initWithFrame:];
-[UIKeyboardPathEffectView textEffectsVisibilityLevel];
-[UIKeyboardPathEffectView _clearPointInterpolators];
-[UIKeyboardPathEffectView pointInterpolator];
```
