# `SBPrototypeBasicAlertElement`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SAElement`, `SAAlertBehavior`, `SAUIElementViewProviding`
- 3 instance variables, 14 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"_SBPrototypeBasicAlertElementCompoundView" _minimalCompoundView;
@"UIView" _leadingView;
@"UIView" _trailingView;
```

## Properties

```
@property (T@"<SAElementHosting>",?,W,N) elementHost;
@property (T@"NSString",R,C,N) clientIdentifier;
@property (T@"NSString",R,C,N) elementIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SAAlertHosting>",?,W,N) alertHost;
@property (T@"UIView",R,N,V_leadingView) leadingView;
@property (T@"UIView",R,N,V_trailingView) trailingView;
@property (T@"UIView",R,N) minimalView;
@property (T@"UIView",?,R,N) detachedMinimalView;
@property (T@"<SAElement>",R,W,N) element;
@property (TQ,?,N) layoutAxis;
```

## Instance methods

```
-[SBPrototypeBasicAlertElement minimalView];
-[SBPrototypeBasicAlertElement trailingView];
-[SBPrototypeBasicAlertElement leadingView];
-[SBPrototypeBasicAlertElement clientIdentifier];
-[SBPrototypeBasicAlertElement element];
-[SBPrototypeBasicAlertElement elementIdentifier];
-[SBPrototypeBasicAlertElement viewProvider];
-[SBPrototypeBasicAlertElement layoutAxis];
-[SBPrototypeBasicAlertElement handleElementViewEvent:];
-[SBPrototypeBasicAlertElement _canShowWhileLocked];
-[SBPrototypeBasicAlertElement setLayoutAxis:];
-[SBPrototypeBasicAlertElement hasAlertBehavior];
```
