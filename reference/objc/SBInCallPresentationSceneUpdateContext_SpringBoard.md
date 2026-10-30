# `SBInCallPresentationSceneUpdateContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSString" _analyticsSource;
q _executionTarget;
@? _completionHandler;
@? _postSceneUpdateHandler;
@? _transitionRequestBuilderBlock;
@? _validatorHandler;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _referenceFrame;
```

## Properties

```
@property (T@"NSString",C,N,V_analyticsSource) analyticsSource;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_referenceFrame) referenceFrame;
@property (Tq,N,V_executionTarget) executionTarget;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (T@?,C,N,V_postSceneUpdateHandler) postSceneUpdateHandler;
@property (T@?,C,N,V_transitionRequestBuilderBlock) transitionRequestBuilderBlock;
@property (T@?,C,N,V_validatorHandler) validatorHandler;
```

## Instance methods

```
-[SBInCallPresentationSceneUpdateContext setCompletionHandler:];
-[SBInCallPresentationSceneUpdateContext completionHandler];
-[SBInCallPresentationSceneUpdateContext referenceFrame];
-[SBInCallPresentationSceneUpdateContext executionTarget];
-[SBInCallPresentationSceneUpdateContext setReferenceFrame:];
-[SBInCallPresentationSceneUpdateContext analyticsSource];
-[SBInCallPresentationSceneUpdateContext setAnalyticsSource:];
-[SBInCallPresentationSceneUpdateContext initWithReferenceFrame:analyticsSource:transitionRequestBuilderBlock:];
-[SBInCallPresentationSceneUpdateContext postSceneUpdateHandler];
-[SBInCallPresentationSceneUpdateContext setExecutionTarget:];
-[SBInCallPresentationSceneUpdateContext setPostSceneUpdateHandler:];
-[SBInCallPresentationSceneUpdateContext setTransitionRequestBuilderBlock:];
-[SBInCallPresentationSceneUpdateContext setValidatorHandler:];
-[SBInCallPresentationSceneUpdateContext transitionRequestBuilderBlock];
-[SBInCallPresentationSceneUpdateContext validatorHandler];
```
