# `_UIModulationFeedbackGeneratorConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedbackGeneratorConfiguration`
- 2 instance variables, 2 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"_UIFeedback<_UIFeedbackContinuousPlayable>" _feedback;
@? _feedbackUpdateBlock;
```

## Properties

```
@property (T@"_UIFeedback<_UIFeedbackContinuousPlayable>",&,N,V_feedback) feedback;
@property (T@?,C,N,V_feedbackUpdateBlock) feedbackUpdateBlock;
```

## Class methods

```
+[_UIModulationFeedbackGeneratorConfiguration sliderConfiguration];
+[_UIModulationFeedbackGeneratorConfiguration defaultConfiguration];
```

## Instance methods

```
-[_UIModulationFeedbackGeneratorConfiguration feedback];
-[_UIModulationFeedbackGeneratorConfiguration setFeedback:];
-[_UIModulationFeedbackGeneratorConfiguration feedbackKeyPaths];
-[_UIModulationFeedbackGeneratorConfiguration setFeedbackUpdateBlock:];
-[_UIModulationFeedbackGeneratorConfiguration feedbackUpdateBlock];
-[_UIModulationFeedbackGeneratorConfiguration requiredSupportLevel];
-[_UIModulationFeedbackGeneratorConfiguration copyWithZone:];
```
