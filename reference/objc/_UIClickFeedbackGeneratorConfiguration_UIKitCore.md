# `_UIClickFeedbackGeneratorConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedbackGeneratorUserInteractionDrivenConfiguration`
- 4 instance variables, 6 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"_UIFeedback<_UIFeedbackDiscretePlayable>" _clickDownFeedback;
@"_UIFeedback<_UIFeedbackDiscretePlayable>" _clickDownAudioFeedback;
@"_UIFeedback<_UIFeedbackDiscretePlayable>" _clickUpFeedback;
@"_UIFeedback<_UIFeedbackDiscretePlayable>" _clickUpAudioFeedback;
```

## Properties

```
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",R,N) clickDownPattern;
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",R,N) clickUpPattern;
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",&,N,V_clickDownFeedback) clickDownFeedback;
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",&,N,V_clickDownAudioFeedback) clickDownAudioFeedback;
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",&,N,V_clickUpFeedback) clickUpFeedback;
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",&,N,V_clickUpAudioFeedback) clickUpAudioFeedback;
```

## Class methods

```
+[_UIClickFeedbackGeneratorConfiguration defaultConfiguration];
```

## Instance methods

```
-[_UIClickFeedbackGeneratorConfiguration feedbackKeyPaths];
-[_UIClickFeedbackGeneratorConfiguration requiredSupportLevel];
-[_UIClickFeedbackGeneratorConfiguration clickUpFeedback];
-[_UIClickFeedbackGeneratorConfiguration clickDownAudioFeedback];
-[_UIClickFeedbackGeneratorConfiguration clickDownFeedback];
-[_UIClickFeedbackGeneratorConfiguration clickDownPattern];
-[_UIClickFeedbackGeneratorConfiguration clickUpAudioFeedback];
-[_UIClickFeedbackGeneratorConfiguration clickUpPattern];
-[_UIClickFeedbackGeneratorConfiguration setClickDownAudioFeedback:];
-[_UIClickFeedbackGeneratorConfiguration setClickDownFeedback:];
-[_UIClickFeedbackGeneratorConfiguration setClickUpAudioFeedback:];
-[_UIClickFeedbackGeneratorConfiguration setClickUpFeedback:];
-[_UIClickFeedbackGeneratorConfiguration setclickDownFeedback:];
```
