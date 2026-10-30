# `_UITextSelectionRangeAdjustmentContainerView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 14 instance variables, 16 properties, 38 instance methods, 0 class methods

## Instance variables

```
B _selectionGrabbersAreConcreteImpl;
B _vertical;
B _portalsLollipopDotsToContainerWindow;
B _selectionGrabbersHidden;
B _hostsGrabbersInClientViews;
B _hitTestsGrabbersInContainer;
d _shapeScale;
@"NSArray" _selectionGrabbers;
@"UIView" _leadingGrabberHostView;
@"UIView" _trailingGrabberHostView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _startEdge;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _endEdge;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _leadingGrabberHitRegion;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _trailingGrabberHitRegion;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_startEdge) startEdge;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_endEdge) endEdge;
@property (TB,N,GisVertical,V_vertical) vertical;
@property (Td,N,V_shapeScale) shapeScale;
@property (TB,N,V_portalsLollipopDotsToContainerWindow) portalsLollipopDotsToContainerWindow;
@property (TB,N,GareSelectionGrabbersHidden,V_selectionGrabbersHidden) selectionGrabbersHidden;
@property (TB,R,N,GareSelectionGrabbersConcreteImpl) selectionGrabbersAreConcreteImpl;
@property (T@"NSArray",&,N,V_selectionGrabbers) selectionGrabbers;
@property (T@"UIView<UITextSelectionHandleView>",R,N) leadingLollipopView;
@property (T@"UIView<UITextSelectionHandleView>",R,N) trailingLollipopView;
@property (T@"UIView",W,N,V_leadingGrabberHostView) leadingGrabberHostView;
@property (T@"UIView",W,N,V_trailingGrabberHostView) trailingGrabberHostView;
@property (TB,N,V_hostsGrabbersInClientViews) hostsGrabbersInClientViews;
@property (TB,N,V_hitTestsGrabbersInContainer) hitTestsGrabbersInContainer;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_leadingGrabberHitRegion) leadingGrabberHitRegion;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_trailingGrabberHitRegion) trailingGrabberHitRegion;
```

## Instance methods

```
-[_UITextSelectionRangeAdjustmentContainerView textInputView];
-[_UITextSelectionRangeAdjustmentContainerView setHidden:];
-[_UITextSelectionRangeAdjustmentContainerView isVertical];
-[_UITextSelectionRangeAdjustmentContainerView layoutSubviews];
-[_UITextSelectionRangeAdjustmentContainerView hitTest:withEvent:];
-[_UITextSelectionRangeAdjustmentContainerView accessibilityIdentifier];
-[_UITextSelectionRangeAdjustmentContainerView initWithFrame:];
-[_UITextSelectionRangeAdjustmentContainerView setHitTestsGrabbersInContainer:];
-[_UITextSelectionRangeAdjustmentContainerView endEdge];
-[_UITextSelectionRangeAdjustmentContainerView _getBounds:position:fromPreferredFrame:];
-[_UITextSelectionRangeAdjustmentContainerView _layoutGrabber:forEdge:host:trailing:];
-[_UITextSelectionRangeAdjustmentContainerView _setPortalsLollipopDotsToContainerWindow:];
-[_UITextSelectionRangeAdjustmentContainerView areSelectionGrabbersConcreteImpl];
-[_UITextSelectionRangeAdjustmentContainerView areSelectionGrabbersHidden];
-[_UITextSelectionRangeAdjustmentContainerView hitTestsGrabbersInContainer];
-[_UITextSelectionRangeAdjustmentContainerView hostsGrabbersInClientViews];
-[_UITextSelectionRangeAdjustmentContainerView leadingGrabberHitRegion];
-[_UITextSelectionRangeAdjustmentContainerView leadingGrabberHostView];
-[_UITextSelectionRangeAdjustmentContainerView leadingLollipopView];
-[_UITextSelectionRangeAdjustmentContainerView portalsLollipopDotsToContainerWindow];
-[_UITextSelectionRangeAdjustmentContainerView selectionGrabbers];
-[_UITextSelectionRangeAdjustmentContainerView setEndEdge:];
-[_UITextSelectionRangeAdjustmentContainerView setHostsGrabbersInClientViews:];
-[_UITextSelectionRangeAdjustmentContainerView setLeadingGrabberHitRegion:];
-[_UITextSelectionRangeAdjustmentContainerView setLeadingGrabberHostView:];
-[_UITextSelectionRangeAdjustmentContainerView setPortalsLollipopDotsToContainerWindow:];
-[_UITextSelectionRangeAdjustmentContainerView setSelectionGrabbers:];
-[_UITextSelectionRangeAdjustmentContainerView setSelectionGrabbersHidden:];
-[_UITextSelectionRangeAdjustmentContainerView setShapeScale:];
-[_UITextSelectionRangeAdjustmentContainerView setStartEdge:];
-[_UITextSelectionRangeAdjustmentContainerView setTrailingGrabberHitRegion:];
-[_UITextSelectionRangeAdjustmentContainerView setTrailingGrabberHostView:];
-[_UITextSelectionRangeAdjustmentContainerView setVertical:];
-[_UITextSelectionRangeAdjustmentContainerView shapeScale];
-[_UITextSelectionRangeAdjustmentContainerView startEdge];
-[_UITextSelectionRangeAdjustmentContainerView trailingGrabberHitRegion];
-[_UITextSelectionRangeAdjustmentContainerView trailingGrabberHostView];
-[_UITextSelectionRangeAdjustmentContainerView trailingLollipopView];
```
