# `_UIFluidSliderFeedbackConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedbackGeneratorUserInteractionDrivenConfiguration`
- 6 instance variables, 6 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"_UIFeedback<_UIFeedbackDiscretePlayable>" _maxEdgeFeedback;
@"_UIFeedback<_UIFeedbackDiscretePlayable>" _detentFeedback;
@"_UIFeedback<_UIFeedbackDiscretePlayable>" _selectionFeedback;
@"_UIFeedback<_UIFeedbackDiscretePlayable>" _minEdgeFeedback;
@"NSString" _hidEdgeFeedbackPatternName;
@"NSString" _hidDetentFeedbackPatternName;
```

## Properties

```
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",R,N,V_maxEdgeFeedback) maxEdgeFeedback;
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",R,N,V_detentFeedback) detentFeedback;
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",R,N,V_selectionFeedback) selectionFeedback;
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",R,N,V_minEdgeFeedback) minEdgeFeedback;
@property (T@"NSString",&,N,V_hidEdgeFeedbackPatternName) hidEdgeFeedbackPatternName;
@property (T@"NSString",&,N,V_hidDetentFeedbackPatternName) hidDetentFeedbackPatternName;
```

## Class methods

```
+[_UIFluidSliderFeedbackConfiguration defaultConfiguration];
```

## Instance methods

```
-[_UIFluidSliderFeedbackConfiguration hidDetentFeedbackPatternName];
-[_UIFluidSliderFeedbackConfiguration detentFeedback];
-[_UIFluidSliderFeedbackConfiguration minEdgeFeedback];
-[_UIFluidSliderFeedbackConfiguration setHidDetentFeedbackPatternName:];
-[_UIFluidSliderFeedbackConfiguration selectionFeedback];
-[_UIFluidSliderFeedbackConfiguration _alternateFeedback:forDevice:senderID:];
-[_UIFluidSliderFeedbackConfiguration hidEdgeFeedbackPatternName];
-[_UIFluidSliderFeedbackConfiguration setHidEdgeFeedbackPatternName:];
-[_UIFluidSliderFeedbackConfiguration setmaxEdgeFeedback:];
-[_UIFluidSliderFeedbackConfiguration setselectionFeedback:];
-[_UIFluidSliderFeedbackConfiguration setminEdgeFeedback:];
-[_UIFluidSliderFeedbackConfiguration hidFeedbackPatternNameKeyPaths];
-[_UIFluidSliderFeedbackConfiguration setdetentFeedback:];
-[_UIFluidSliderFeedbackConfiguration maxEdgeFeedback];
```
