# `SBSystemApertureContextProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 9 instance methods, 0 class methods

## Properties

```
@property (TB,?,R,N,GisAffiliatedWithSessionMonitor) affiliatedWithSessionMonitor;
@property (T@"UIColor",?,R,N) keyColor;
@property (T@"FBScene",?,R,N) scene;
@property (TB,?,R,N) preventsSwipeToHide;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) preferredAvoidanceRect;
@property (Td,?,R,N) preferredAvoidanceCornerRadius;
@property (TB,?,R,N) inhibitsIndicatorMitosis;
@property (Td,?,R,N) preferredSystemClipPadding;
```

## Instance methods

```
-[SBSystemApertureContextProviding keyColor];
-[SBSystemApertureContextProviding inhibitsIndicatorMitosis];
-[SBSystemApertureContextProviding preferredAvoidanceCornerRadius];
-[SBSystemApertureContextProviding preferredAlertingDuration:];
-[SBSystemApertureContextProviding preferredSystemClipPadding];
-[SBSystemApertureContextProviding preferredAvoidanceRect];
-[SBSystemApertureContextProviding scene];
-[SBSystemApertureContextProviding isAffiliatedWithSessionMonitor];
-[SBSystemApertureContextProviding preventsSwipeToHide];
```
