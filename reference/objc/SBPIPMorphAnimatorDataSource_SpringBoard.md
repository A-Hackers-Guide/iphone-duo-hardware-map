# `SBPIPMorphAnimatorDataSource`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBViewMorphAnimatorDataSource`
- 5 instance variables, 8 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _morphAnimatorToPegasusInitialFrame;
@"SBPIPController" _pipController;
@"PGPictureInPictureController" _pegasusController;
@"SBPIPMorphAnimatorController" _morphAnimatorController;
@"SBPIPContentViewLayoutSettings" _contentViewLayoutSettings;
```

## Properties

```
@property (T@"SBPIPController",&,N,V_pipController) pipController;
@property (T@"PGPictureInPictureController",&,N,V_pegasusController) pegasusController;
@property (T@"SBPIPMorphAnimatorController",W,N,V_morphAnimatorController) morphAnimatorController;
@property (T@"SBPIPContentViewLayoutSettings",&,N,V_contentViewLayoutSettings) contentViewLayoutSettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBPIPMorphAnimatorDataSource pipController];
-[SBPIPMorphAnimatorDataSource setPipController:];
-[SBPIPMorphAnimatorDataSource _appLayoutBoundingBoxForAnimator:];
-[SBPIPMorphAnimatorDataSource _isSingleAppModeEnabledForAnimator:];
-[SBPIPMorphAnimatorDataSource contentViewLayoutSettings];
-[SBPIPMorphAnimatorDataSource initWithMorphAnimatorController:pipController:pegasusController:contentViewLayoutSettings:];
-[SBPIPMorphAnimatorDataSource morphAnimatorController];
-[SBPIPMorphAnimatorDataSource pegasusController];
-[SBPIPMorphAnimatorDataSource setContentViewLayoutSettings:];
-[SBPIPMorphAnimatorDataSource setMorphAnimatorController:];
-[SBPIPMorphAnimatorDataSource setPegasusController:];
-[SBPIPMorphAnimatorDataSource shouldProvideSourceClippingFrameInFixedCoordinateSpace:];
-[SBPIPMorphAnimatorDataSource sourceBlackCurtainCornerRadiusForAnimator:];
-[SBPIPMorphAnimatorDataSource sourceContentContainerFrameForAnimator:];
-[SBPIPMorphAnimatorDataSource sourceContentFrameForAnimator:];
-[SBPIPMorphAnimatorDataSource sourceCornerRadiusForAnimator:];
-[SBPIPMorphAnimatorDataSource sourceSubviewFrame:inScreenSpaceForAnimator:];
-[SBPIPMorphAnimatorDataSource targetFinalCornerRadiusForAnimator:];
-[SBPIPMorphAnimatorDataSource targetFinalFrameForAnimator:];
```
