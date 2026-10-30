# `SBAppResizeGrabberView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `MTLumaDodgePillBackgroundLuminanceObserver`, `UIPointerInteractionDelegate`
- 5 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
Q _corner;
d _cornerRadius;
@"UIView" _pillViewContainerView;
@"MTLumaDodgePillView" _pillView;
@"UIBezierPath" _grabberPath;
```

## Properties

```
@property (Td,N) cornerRadius;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAppResizeGrabberView pointerInteraction:styleForRegion:];
-[SBAppResizeGrabberView layoutSubviews];
-[SBAppResizeGrabberView setCornerRadius:];
-[SBAppResizeGrabberView lumaDodgePillDidDetectBackgroundLuminanceChange:];
-[SBAppResizeGrabberView cornerRadius];
-[SBAppResizeGrabberView pointerInteraction:regionForRequest:defaultRegion:];
-[SBAppResizeGrabberView initWithCorner:];
-[SBAppResizeGrabberView _grabberCurve];
-[SBAppResizeGrabberView _grabberPathForLength:curve:];
-[SBAppResizeGrabberView _pillViewContainerViewFrame];
-[SBAppResizeGrabberView _pillViewContainerViewOffset];
-[SBAppResizeGrabberView _pointerRegionRect];
-[SBAppResizeGrabberView _updateGrabberPathAnimated:];
-[SBAppResizeGrabberView frameInContentRect:];
-[SBAppResizeGrabberView initWithCorner:cornerRadius:];
```
