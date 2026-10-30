# `SBMenuBarActivationView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `STUIStatusBarDisplayable`
- 3 instance variables, 11 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"UILabel" _applicationNameLabel;
@"STUIStatusBarStyleAttributes" _currentStyleAttributes;
@"NSString" _applicationDisplayName;
```

## Properties

```
@property (T@"NSString",C,N,V_applicationDisplayName) applicationDisplayName;
@property (TB,?,R,N) wantsCrossfade;
@property (TB,?,R,N) prefersBaselineAlignment;
@property (TB,?,R,N) prefersCenterVerticalAlignment;
@property (Tq,?,R,N) overriddenVerticalAlignment;
@property (T{CGSize=dd},?,R,N) contentBoundingSize;
@property (T@"UIAccessibilityHUDItem",?,R,N) accessibilityHUDRepresentation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBMenuBarActivationView applyStyleAttributes:];
-[SBMenuBarActivationView applicationDisplayName];
-[SBMenuBarActivationView setApplicationDisplayName:];
-[SBMenuBarActivationView initWithApplicationDisplayName:];
-[SBMenuBarActivationView _updateLabelFromStyleAttributesWithApplicationNameChange:];
```
