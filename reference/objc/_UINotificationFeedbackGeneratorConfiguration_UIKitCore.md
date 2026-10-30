# `_UINotificationFeedbackGeneratorConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedbackGeneratorConfiguration`
- 2 instance variables, 2 properties, 8 instance methods, 3 class methods

## Instance variables

```
B _includePrivateEvents;
@"NSDictionary" _feedbacks;
```

## Properties

```
@property (TB,N,V_includePrivateEvents) includePrivateEvents;
@property (T@"NSDictionary",&,N,V_feedbacks) feedbacks;
```

## Class methods

```
+[_UINotificationFeedbackGeneratorConfiguration privateConfiguration];
+[_UINotificationFeedbackGeneratorConfiguration privateConfigurationForTypes:];
+[_UINotificationFeedbackGeneratorConfiguration defaultConfiguration];
```

## Instance methods

```
-[_UINotificationFeedbackGeneratorConfiguration feedbacks];
-[_UINotificationFeedbackGeneratorConfiguration setFeedbacks:];
-[_UINotificationFeedbackGeneratorConfiguration feedbackKeyPaths];
-[_UINotificationFeedbackGeneratorConfiguration setIncludePrivateEvents:];
-[_UINotificationFeedbackGeneratorConfiguration defaultEnabled];
-[_UINotificationFeedbackGeneratorConfiguration includePrivateEvents];
-[_UINotificationFeedbackGeneratorConfiguration copyWithZone:];
-[_UINotificationFeedbackGeneratorConfiguration isEqual:];
```
