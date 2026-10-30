# `SBPortalView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 2 instance variables, 8 properties, 17 instance methods, 1 class methods

## Instance variables

```
B _passesTouchesThrough;
@"UIView" _sourceView;
```

## Properties

```
@property (T@"UIView",W,N,V_sourceView) sourceView;
@property (TB,D,N) hidesSourceView;
@property (TB,D,N) matchesAlpha;
@property (TB,D,N) matchesTransform;
@property (TB,D,N) matchesPosition;
@property (TB,D,N) allowsBackdropGroups;
@property (TB,N,V_passesTouchesThrough) passesTouchesThrough;
@property (T@"CAPortalLayer",R,D,N) portalLayer;
```

## Class methods

```
+[SBPortalView layerClass];
```

## Instance methods

```
-[SBPortalView matchesTransform];
-[SBPortalView setMatchesTransform:];
-[SBPortalView hidesSourceView];
-[SBPortalView portalLayer];
-[SBPortalView hitTest:withEvent:];
-[SBPortalView setMatchesAlpha:];
-[SBPortalView setPassesTouchesThrough:];
-[SBPortalView matchesPosition];
-[SBPortalView passesTouchesThrough];
-[SBPortalView setSourceView:];
-[SBPortalView setHidesSourceView:];
-[SBPortalView allowsBackdropGroups];
-[SBPortalView description];
-[SBPortalView setMatchesPosition:];
-[SBPortalView setAllowsBackdropGroups:];
-[SBPortalView matchesAlpha];
-[SBPortalView sourceView];
```
