# `_UIClickPresentationFeedbackGeneratorConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedbackGeneratorUserInteractionDrivenConfiguration`
- 0 instance variables, 6 properties, 11 instance methods, 1 class methods

## Properties

```
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",R,N) previewedPattern;
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",R,N) poppedPattern;
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",R,N) draggedPattern;
@property (T@"NSString",R,N) hidPreviewedPatternName;
@property (T@"NSString",R,N) hidPoppedPatternName;
@property (T@"NSString",R,N) hidDraggedPatternName;
```

## Class methods

```
+[_UIClickPresentationFeedbackGeneratorConfiguration defaultConfiguration];
```

## Instance methods

```
-[_UIClickPresentationFeedbackGeneratorConfiguration previewedPattern];
-[_UIClickPresentationFeedbackGeneratorConfiguration feedbackKeyPaths];
-[_UIClickPresentationFeedbackGeneratorConfiguration requiredPeripheralSupportLevel];
-[_UIClickPresentationFeedbackGeneratorConfiguration _alternateFeedback:forDevice:senderID:];
-[_UIClickPresentationFeedbackGeneratorConfiguration hidPreviewedPatternName];
-[_UIClickPresentationFeedbackGeneratorConfiguration hidDraggedPatternName];
-[_UIClickPresentationFeedbackGeneratorConfiguration hidPoppedPatternName];
-[_UIClickPresentationFeedbackGeneratorConfiguration hidFeedbackPatternNameKeyPaths];
-[_UIClickPresentationFeedbackGeneratorConfiguration draggedPattern];
-[_UIClickPresentationFeedbackGeneratorConfiguration requiredSupportLevel];
-[_UIClickPresentationFeedbackGeneratorConfiguration poppedPattern];
```
