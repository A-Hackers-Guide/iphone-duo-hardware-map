# `UIImpactFeedbackGenerator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIFeedbackGenerator`
- 1 instance variables, 1 properties, 13 instance methods, 2 class methods

## Instance variables

```
q _style;
```

## Properties

```
@property (T@"_UIImpactFeedbackGeneratorConfiguration",R,N,G_impactConfiguration) impactConfiguration;
```

## Class methods

```
+[UIImpactFeedbackGenerator _configurationClass];
+[UIImpactFeedbackGenerator feedbackGeneratorWithStyle:forView:];
```

## Instance methods

```
-[UIImpactFeedbackGenerator _stats_key];
-[UIImpactFeedbackGenerator initWithStyle:view:];
-[UIImpactFeedbackGenerator _impactOccurredWithIntensity:];
-[UIImpactFeedbackGenerator initWithStyle:coordinateSpace:];
-[UIImpactFeedbackGenerator impactOccurredAtLocation:];
-[UIImpactFeedbackGenerator impactOccurredWithIntensity:atLocation:];
-[UIImpactFeedbackGenerator _ui_descriptionBuilder];
-[UIImpactFeedbackGenerator initWithStyle:];
-[UIImpactFeedbackGenerator impactOccurredWithIntensity:];
-[UIImpactFeedbackGenerator _styleString];
-[UIImpactFeedbackGenerator _impactConfiguration];
-[UIImpactFeedbackGenerator _impactOccurredWithIntensity:atLocation:];
-[UIImpactFeedbackGenerator impactOccurred];
```
