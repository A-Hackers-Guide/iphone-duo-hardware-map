# `_UIKBFeedbackGeneratorIntensitySettings`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 5 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
d _min;
d _max;
d _randomInPercentage;
d _intervalWeight;
d _decayInterval;
```

## Properties

```
@property (Td,N,V_min) min;
@property (Td,N,V_max) max;
@property (Td,N,V_randomInPercentage) randomInPercentage;
@property (Td,N,V_intervalWeight) intervalWeight;
@property (Td,N,V_decayInterval) decayInterval;
```

## Class methods

```
+[_UIKBFeedbackGeneratorIntensitySettings settingsControllerModule];
```

## Instance methods

```
-[_UIKBFeedbackGeneratorIntensitySettings min];
-[_UIKBFeedbackGeneratorIntensitySettings setDefaultValues];
-[_UIKBFeedbackGeneratorIntensitySettings max];
-[_UIKBFeedbackGeneratorIntensitySettings setMax:];
-[_UIKBFeedbackGeneratorIntensitySettings setMin:];
-[_UIKBFeedbackGeneratorIntensitySettings decayInterval];
-[_UIKBFeedbackGeneratorIntensitySettings intervalWeight];
-[_UIKBFeedbackGeneratorIntensitySettings randomInPercentage];
-[_UIKBFeedbackGeneratorIntensitySettings setDecayInterval:];
-[_UIKBFeedbackGeneratorIntensitySettings setIntervalWeight:];
-[_UIKBFeedbackGeneratorIntensitySettings setRandomInPercentage:];
```
