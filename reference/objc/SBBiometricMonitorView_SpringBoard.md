# `SBBiometricMonitorView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 6 instance variables, 3 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"UIView" _stateView;
@"UIView" _presenceView;
@"UIView" _poseView;
q _matchState;
q _presenceDetectState;
q _poseState;
```

## Properties

```
@property (Tq,N,V_matchState) matchState;
@property (Tq,N,V_presenceDetectState) presenceDetectState;
@property (Tq,N,V_poseState) poseState;
```

## Instance methods

```
-[SBBiometricMonitorView layoutSubviews];
-[SBBiometricMonitorView hitTest:withEvent:];
-[SBBiometricMonitorView initWithFrame:];
-[SBBiometricMonitorView matchState];
-[SBBiometricMonitorView poseState];
-[SBBiometricMonitorView presenceDetectState];
-[SBBiometricMonitorView setMatchState:];
-[SBBiometricMonitorView setPoseState:];
-[SBBiometricMonitorView setPresenceDetectState:];
```
