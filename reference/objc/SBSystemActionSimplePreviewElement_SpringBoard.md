# `SBSystemActionSimplePreviewElement`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBActivityProvidedContentElement`
- Protocols: `SBSystemApertureContextProviding`
- 2 instance variables, 12 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"UIColor" _keyColor;
@"SBSystemAction" _systemAction;
```

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
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemActionSimplePreviewElement keyColor];
-[SBSystemActionSimplePreviewElement isMinimalPresentationPossible];
-[SBSystemActionSimplePreviewElement shouldSuppressElementWhilePresentingAppWithBundleId:];
-[SBSystemActionSimplePreviewElement initWithSystemAction:];
-[SBSystemActionSimplePreviewElement initWithSystemAction:contentProvider:keyColor:];
```
