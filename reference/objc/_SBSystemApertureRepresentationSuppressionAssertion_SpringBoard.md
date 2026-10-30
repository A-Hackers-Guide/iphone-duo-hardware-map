# `_SBSystemApertureRepresentationSuppressionAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 3 instance variables, 10 properties, 11 instance methods, 0 class methods

## Instance variables

```
@? _invalidationBlock;
Q _reason;
B __valid;
```

## Properties

```
@property (TB,R,N) suppressForCoverSheetVisible;
@property (TB,R,N) suppressForLiquidDetectionVisible;
@property (TB,R,N) suppressForProximityReaderVisible;
@property (TB,R,N) suppressForSystemChromeSuppression;
@property (TB,R,N) suppressForCompanionSceneVisible;
@property (TB,N,G_isValid,S_setValid:,V__valid) _valid;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBSystemApertureRepresentationSuppressionAssertion _isValid];
-[_SBSystemApertureRepresentationSuppressionAssertion dealloc];
-[_SBSystemApertureRepresentationSuppressionAssertion invalidate];
-[_SBSystemApertureRepresentationSuppressionAssertion description];
-[_SBSystemApertureRepresentationSuppressionAssertion initWithReason:invalidationBlock:];
-[_SBSystemApertureRepresentationSuppressionAssertion _setValid:];
-[_SBSystemApertureRepresentationSuppressionAssertion suppressForCompanionSceneVisible];
-[_SBSystemApertureRepresentationSuppressionAssertion suppressForCoverSheetVisible];
-[_SBSystemApertureRepresentationSuppressionAssertion suppressForLiquidDetectionVisible];
-[_SBSystemApertureRepresentationSuppressionAssertion suppressForProximityReaderVisible];
-[_SBSystemApertureRepresentationSuppressionAssertion suppressForSystemChromeSuppression];
```
