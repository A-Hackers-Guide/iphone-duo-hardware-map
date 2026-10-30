# `STUIStatusBarDisplayable` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 7 instance methods, 0 class methods

## Properties

```
@property (TB,?,R,N) wantsCrossfade;
@property (TB,?,R,N) prefersBaselineAlignment;
@property (TB,?,R,N) prefersCenterVerticalAlignment;
@property (Tq,?,R,N) overriddenVerticalAlignment;
@property (T{CGSize=dd},?,R,N) contentBoundingSize;
@property (T@"UIAccessibilityHUDItem",?,R,N) accessibilityHUDRepresentation;
```

## Instance methods

```
-[STUIStatusBarDisplayable prefersBaselineAlignment];
-[STUIStatusBarDisplayable accessibilityHUDRepresentation];
-[STUIStatusBarDisplayable applyStyleAttributes:];
-[STUIStatusBarDisplayable overriddenVerticalAlignment];
-[STUIStatusBarDisplayable wantsCrossfade];
-[STUIStatusBarDisplayable prefersCenterVerticalAlignment];
-[STUIStatusBarDisplayable contentBoundingSize];
```
