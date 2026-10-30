# `_UIPopoverGlassBackground`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 6 instance variables, 7 properties, 16 instance methods, 0 class methods

## Instance variables

```
$__lazy_storage_$_hostingView;
{CGRect={CGPoint=dd}{CGSize=dd}} contentViewFrame;
B usesMenuStyleGlass;
@"UIBezierPath" shapePath;
@"UITraitCollection" _traitCollectionForGlassContent;
? presentationController;
```

## Properties

```
@property (T@"UIView",N,&) contentView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,VcontentViewFrame) contentViewFrame;
@property (TB,N,VusesMenuStyleGlass) usesMenuStyleGlass;
@property (T@"UIBezierPath",N,&,VshapePath) shapePath;
@property (T@"UITraitCollection",N,&,V_traitCollectionForGlassContent) _traitCollectionForGlassContent;
@property (T@"UITraitCollection",N,R) traitCollectionForGlassContent;
@property (T@"UIPopoverPresentationController",N,W,VpresentationController) presentationController;
```

## Instance methods

```
-[_UIPopoverGlassBackground setContentView:];
-[_UIPopoverGlassBackground presentationController];
-[_UIPopoverGlassBackground contentView];
-[_UIPopoverGlassBackground setPresentationController:];
-[_UIPopoverGlassBackground initWithCoder:];
-[_UIPopoverGlassBackground initWithFrame:];
-[_UIPopoverGlassBackground _traitCollectionForGlassContent];
-[_UIPopoverGlassBackground setGlassContentTraitCollection:];
-[_UIPopoverGlassBackground contentViewFrame];
-[_UIPopoverGlassBackground setContentViewFrame:];
-[_UIPopoverGlassBackground setShapePath:];
-[_UIPopoverGlassBackground setUsesMenuStyleGlass:];
-[_UIPopoverGlassBackground set_traitCollectionForGlassContent:];
-[_UIPopoverGlassBackground shapePath];
-[_UIPopoverGlassBackground traitCollectionForGlassContent];
-[_UIPopoverGlassBackground usesMenuStyleGlass];
```
