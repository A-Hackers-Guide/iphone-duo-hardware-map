# `SBSwitcherLayoutCalculationsCacheValidityToken`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
Q _appLayoutsGenCount;
Q _continuousExposeIdentifiersGenCount;
q _switcherInterfaceOrientation;
Q _modifierEventGenCount;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _containerViewBounds;
```

## Properties

```
@property (TQ,N,V_appLayoutsGenCount) appLayoutsGenCount;
@property (TQ,N,V_continuousExposeIdentifiersGenCount) continuousExposeIdentifiersGenCount;
@property (Tq,N,V_switcherInterfaceOrientation) switcherInterfaceOrientation;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_containerViewBounds) containerViewBounds;
@property (TQ,N,V_modifierEventGenCount) modifierEventGenCount;
```

## Instance methods

```
-[SBSwitcherLayoutCalculationsCacheValidityToken switcherInterfaceOrientation];
-[SBSwitcherLayoutCalculationsCacheValidityToken containerViewBounds];
-[SBSwitcherLayoutCalculationsCacheValidityToken isEqual:];
-[SBSwitcherLayoutCalculationsCacheValidityToken appLayoutsGenCount];
-[SBSwitcherLayoutCalculationsCacheValidityToken continuousExposeIdentifiersGenCount];
-[SBSwitcherLayoutCalculationsCacheValidityToken initWithAppLayoutsGenCount:continuousExposeIdentifiersGenCount:switcherInterfaceOrientation:containerViewBounds:modifierEventGenCount:];
-[SBSwitcherLayoutCalculationsCacheValidityToken modifierEventGenCount];
-[SBSwitcherLayoutCalculationsCacheValidityToken setAppLayoutsGenCount:];
-[SBSwitcherLayoutCalculationsCacheValidityToken setContainerViewBounds:];
-[SBSwitcherLayoutCalculationsCacheValidityToken setContinuousExposeIdentifiersGenCount:];
-[SBSwitcherLayoutCalculationsCacheValidityToken setModifierEventGenCount:];
-[SBSwitcherLayoutCalculationsCacheValidityToken setSwitcherInterfaceOrientation:];
```
