# `SBResizeMorphSideRecord`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"UIView" _installView;
@"UIView" _underlyingContentView;
Q _anchorEdge;
@"SBContinuousFoldResizeMorphOverlayView" _overlay;
q _sideState;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
```

## Properties

```
@property (T@"UIView",W,N,V_installView) installView;
@property (T@"UIView",W,N,V_underlyingContentView) underlyingContentView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_frame) frame;
@property (TQ,N,V_anchorEdge) anchorEdge;
@property (T@"SBContinuousFoldResizeMorphOverlayView",&,N,V_overlay) overlay;
@property (Tq,N,V_sideState) sideState;
```

## Instance methods

```
-[SBResizeMorphSideRecord setOverlay:];
-[SBResizeMorphSideRecord overlay];
-[SBResizeMorphSideRecord setFrame:];
-[SBResizeMorphSideRecord frame];
-[SBResizeMorphSideRecord underlyingContentView];
-[SBResizeMorphSideRecord installView];
-[SBResizeMorphSideRecord anchorEdge];
-[SBResizeMorphSideRecord setAnchorEdge:];
-[SBResizeMorphSideRecord setInstallView:];
-[SBResizeMorphSideRecord setSideState:];
-[SBResizeMorphSideRecord setUnderlyingContentView:];
-[SBResizeMorphSideRecord sideState];
```
