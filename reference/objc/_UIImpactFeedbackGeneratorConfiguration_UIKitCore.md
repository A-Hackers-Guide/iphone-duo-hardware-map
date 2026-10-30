# `_UIImpactFeedbackGeneratorConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedbackGeneratorConfiguration`
- 4 instance variables, 4 properties, 14 instance methods, 6 class methods

## Instance variables

```
@"_UIFeedback<_UIFeedbackDiscretePlayable>" _feedback;
@? _feedbackUpdateBlock;
d _minimumInterval;
@"NSString" _hidFeedbackPatternName;
```

## Properties

```
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",&,N,V_feedback) feedback;
@property (T@?,C,N,V_feedbackUpdateBlock) feedbackUpdateBlock;
@property (Td,N,V_minimumInterval) minimumInterval;
@property (T@"NSString",&,N,V_hidFeedbackPatternName) hidFeedbackPatternName;
```

## Class methods

```
+[_UIImpactFeedbackGeneratorConfiguration rigidConfiguration];
+[_UIImpactFeedbackGeneratorConfiguration lightConfiguration];
+[_UIImpactFeedbackGeneratorConfiguration strongConfiguration];
+[_UIImpactFeedbackGeneratorConfiguration refreshConfiguration];
+[_UIImpactFeedbackGeneratorConfiguration defaultConfiguration];
+[_UIImpactFeedbackGeneratorConfiguration softConfiguration];
```

## Instance methods

```
-[_UIImpactFeedbackGeneratorConfiguration feedback];
-[_UIImpactFeedbackGeneratorConfiguration setFeedback:];
-[_UIImpactFeedbackGeneratorConfiguration feedbackKeyPaths];
-[_UIImpactFeedbackGeneratorConfiguration setFeedbackUpdateBlock:];
-[_UIImpactFeedbackGeneratorConfiguration _alternateFeedback:forDevice:senderID:];
-[_UIImpactFeedbackGeneratorConfiguration setHidFeedbackPatternName:];
-[_UIImpactFeedbackGeneratorConfiguration setMinimumInterval:];
-[_UIImpactFeedbackGeneratorConfiguration feedbackUpdateBlock];
-[_UIImpactFeedbackGeneratorConfiguration hidFeedbackPatternNameKeyPaths];
-[_UIImpactFeedbackGeneratorConfiguration hidFeedbackPatternName];
-[_UIImpactFeedbackGeneratorConfiguration requiredSupportLevel];
-[_UIImpactFeedbackGeneratorConfiguration copyWithZone:];
-[_UIImpactFeedbackGeneratorConfiguration isEqual:];
-[_UIImpactFeedbackGeneratorConfiguration minimumInterval];
```
