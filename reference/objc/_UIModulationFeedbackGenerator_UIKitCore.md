# `_UIModulationFeedbackGenerator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIFeedbackGenerator`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
d _currentValue;
@"_UIFeedback<_UIFeedbackContinuousPlayable>" _playingContinuousFeedback;
```

## Properties

```
@property (T@"_UIModulationFeedbackGeneratorConfiguration",R,N,G_modulationConfiguration) modulationConfiguration;
@property (T@"_UIFeedback<_UIFeedbackContinuousPlayable>",&,N,V_playingContinuousFeedback) playingContinuousFeedback;
```

## Class methods

```
+[_UIModulationFeedbackGenerator _configurationClass];
```

## Instance methods

```
-[_UIModulationFeedbackGenerator _stats_key];
-[_UIModulationFeedbackGenerator deactivate];
-[_UIModulationFeedbackGenerator activateWithCompletionBlock:];
-[_UIModulationFeedbackGenerator playingContinuousFeedback];
-[_UIModulationFeedbackGenerator setPlayingContinuousFeedback:];
-[_UIModulationFeedbackGenerator _modulationConfiguration];
-[_UIModulationFeedbackGenerator activateWithInitialValue:completionBlock:];
-[_UIModulationFeedbackGenerator valueUpdated:];
```
