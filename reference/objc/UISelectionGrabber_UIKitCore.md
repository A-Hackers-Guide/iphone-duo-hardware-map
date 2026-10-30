# `UISelectionGrabber`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 6 instance variables, 6 properties, 44 instance methods, 2 class methods

## Instance variables

```
d m_screenScale;
@"UISelectionGrabberDot" m_dotView;
B m_isDotted;
B m_animating;
q m_orientation;
@"UISelectionGrabberCustomPath" _customPath;
```

## Properties

```
@property (T@"CAShapeLayer",R,N) shapeLayer;
@property (T@"UITextRangeView",R,N) hostView;
@property (TB,N,Vm_isDotted) isDotted;
@property (TB,N,Vm_animating) animating;
@property (Tq,N,Vm_orientation) orientation;
@property (T@"UISelectionGrabberCustomPath",&,N,V_customPath) customPath;
```

## Class methods

```
+[UISelectionGrabber layerClass];
+[UISelectionGrabber _grabberDot];
```

## Instance methods

```
-[UISelectionGrabber setOrientation:];
-[UISelectionGrabber hostView];
-[UISelectionGrabber animating];
-[UISelectionGrabber shapeLayer];
-[UISelectionGrabber _dynamicUserInterfaceTraitDidChange];
-[UISelectionGrabber setHidden:];
-[UISelectionGrabber isScrolling];
-[UISelectionGrabber fillColor];
-[UISelectionGrabber orientation];
-[UISelectionGrabber isVertical];
-[UISelectionGrabber dealloc];
-[UISelectionGrabber drawRect:];
-[UISelectionGrabber setCenter:];
-[UISelectionGrabber setBounds:];
-[UISelectionGrabber willMoveToWindow:];
-[UISelectionGrabber removeFromSuperview];
-[UISelectionGrabber isRotating];
-[UISelectionGrabber setFrame:];
-[UISelectionGrabber didMoveToSuperview];
-[UISelectionGrabber setAnimating:];
-[UISelectionGrabber initWithFrame:];
-[UISelectionGrabber animateGrabberInWithCompletion:];
-[UISelectionGrabber _defaultDotWidth];
-[UISelectionGrabber _dotView];
-[UISelectionGrabber animateGrabberOutWithCompletion:];
-[UISelectionGrabber autoscrolled];
-[UISelectionGrabber bezierPathFromCustomPath:];
-[UISelectionGrabber clipDot:];
-[UISelectionGrabber customPath];
-[UISelectionGrabber dotIsVisibleInDocument:];
-[UISelectionGrabber inputViewIsChanging];
-[UISelectionGrabber isDotted];
-[UISelectionGrabber isPointedDown];
-[UISelectionGrabber isPointedLeft];
-[UISelectionGrabber isPointedRight];
-[UISelectionGrabber isPointedUp];
-[UISelectionGrabber isScaling];
-[UISelectionGrabber redrawDotForScale:];
-[UISelectionGrabber scroller:fullyContainSelectionRect:];
-[UISelectionGrabber setCustomPath:];
-[UISelectionGrabber setIsDotted:];
-[UISelectionGrabber transitionDot:completion:];
-[UISelectionGrabber updateDot];
-[UISelectionGrabber updatePathForBoundsChangeIfNecessary];
```
