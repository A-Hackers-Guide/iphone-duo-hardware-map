# `_UIDragFeedbackGeneratorConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedbackGeneratorUserInteractionDrivenConfiguration`
- 5 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"_UIFeedback<_UIFeedbackContinuousPlayable>" _interactionProgressingFeedback;
@"_UIFeedback<_UIFeedbackDiscretePlayable>" _interactionUpdatedFeedback;
@"_UIFeedback<_UIFeedbackDiscretePlayable>" _targetUpdatedFeedback;
d _progressingFeedbackDelay;
@"NSString" _hidTargetUpdatedFeedbackPatternName;
```

## Properties

```
@property (T@"_UIFeedback<_UIFeedbackContinuousPlayable>",&,N,V_interactionProgressingFeedback) interactionProgressingFeedback;
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",&,N,V_interactionUpdatedFeedback) interactionUpdatedFeedback;
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",&,N,V_targetUpdatedFeedback) targetUpdatedFeedback;
@property (T@"NSString",&,N,V_hidTargetUpdatedFeedbackPatternName) hidTargetUpdatedFeedbackPatternName;
@property (Td,N,V_progressingFeedbackDelay) progressingFeedbackDelay;
```

## Class methods

```
+[_UIDragFeedbackGeneratorConfiguration defaultConfiguration];
```

## Instance methods

```
-[_UIDragFeedbackGeneratorConfiguration feedbackKeyPaths];
-[_UIDragFeedbackGeneratorConfiguration requiredPeripheralSupportLevel];
-[_UIDragFeedbackGeneratorConfiguration _alternateFeedback:forDevice:senderID:];
-[_UIDragFeedbackGeneratorConfiguration hidFeedbackPatternNameKeyPaths];
-[_UIDragFeedbackGeneratorConfiguration requiredSupportLevel];
-[_UIDragFeedbackGeneratorConfiguration copyWithZone:];
-[_UIDragFeedbackGeneratorConfiguration isEqual:];
-[_UIDragFeedbackGeneratorConfiguration hidTargetUpdatedFeedbackPatternName];
-[_UIDragFeedbackGeneratorConfiguration interactionProgressingFeedback];
-[_UIDragFeedbackGeneratorConfiguration interactionUpdatedFeedback];
-[_UIDragFeedbackGeneratorConfiguration progressingFeedbackDelay];
-[_UIDragFeedbackGeneratorConfiguration setHidTargetUpdatedFeedbackPatternName:];
-[_UIDragFeedbackGeneratorConfiguration setInteractionProgressingFeedback:];
-[_UIDragFeedbackGeneratorConfiguration setInteractionUpdatedFeedback:];
-[_UIDragFeedbackGeneratorConfiguration setProgressingFeedbackDelay:];
-[_UIDragFeedbackGeneratorConfiguration setTargetUpdatedFeedback:];
-[_UIDragFeedbackGeneratorConfiguration targetUpdatedFeedback];
```
