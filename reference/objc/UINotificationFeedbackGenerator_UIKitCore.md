# `UINotificationFeedbackGenerator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIFeedbackGenerator`
- 0 instance variables, 1 properties, 14 instance methods, 1 class methods

## Properties

```
@property (T@"_UINotificationFeedbackGeneratorConfiguration",R,N,G_eventConfiguration) eventConfiguration;
```

## Class methods

```
+[UINotificationFeedbackGenerator _configurationClass];
```

## Instance methods

```
-[UINotificationFeedbackGenerator _stats_key];
-[UINotificationFeedbackGenerator _categoryForType:];
-[UINotificationFeedbackGenerator _playEventType:atLocation:];
-[UINotificationFeedbackGenerator _privateNotificationInterrupted:];
-[UINotificationFeedbackGenerator notificationOccurred:atLocation:];
-[UINotificationFeedbackGenerator _privateNotificationOccurred:atLocation:];
-[UINotificationFeedbackGenerator notificationOccurred:];
-[UINotificationFeedbackGenerator _stopEventType:];
-[UINotificationFeedbackGenerator _preparationTimeoutForStyle:];
-[UINotificationFeedbackGenerator _eventConfiguration];
-[UINotificationFeedbackGenerator _notificationOccurred:atLocation:];
-[UINotificationFeedbackGenerator _privateNotificationOccurred:];
-[UINotificationFeedbackGenerator _privateNotificationOccurred:atLocation:powerSourceID:];
-[UINotificationFeedbackGenerator _privateNotificationOccurred:atLocation:senderID:];
```
