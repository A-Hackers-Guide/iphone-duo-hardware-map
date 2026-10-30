# `SBFluidDismissalState`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SiriUIFluidDismissalState`
- 6 instance variables, 14 properties, 12 instance methods, 0 class methods

## Instance variables

```
d _backgroundWeighting;
d _contentWeighting;
q _dismissalType;
q _transitionPhase;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _contentRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _homeGrabberContentRect;
```

## Properties

```
@property (Td,N) backgroundWeighting;
@property (Td,N) contentWeighting;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) contentRect;
@property (Tq,R,N) transitionPhase;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,N,V_backgroundWeighting) backgroundWeighting;
@property (Td,N,V_contentWeighting) contentWeighting;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_contentRect) contentRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_homeGrabberContentRect) homeGrabberContentRect;
@property (Tq,N,V_dismissalType) dismissalType;
@property (Tq,N,V_transitionPhase) transitionPhase;
```

## Instance methods

```
-[SBFluidDismissalState contentRect];
-[SBFluidDismissalState setContentRect:];
-[SBFluidDismissalState setDismissalType:];
-[SBFluidDismissalState transitionPhase];
-[SBFluidDismissalState setTransitionPhase:];
-[SBFluidDismissalState backgroundWeighting];
-[SBFluidDismissalState contentWeighting];
-[SBFluidDismissalState dismissalType];
-[SBFluidDismissalState homeGrabberContentRect];
-[SBFluidDismissalState setBackgroundWeighting:];
-[SBFluidDismissalState setContentWeighting:];
-[SBFluidDismissalState setHomeGrabberContentRect:];
```
