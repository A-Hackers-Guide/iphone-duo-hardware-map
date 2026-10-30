# `UISelectionFeedbackGenerator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIFeedbackGenerator`
- 1 instance variables, 2 properties, 14 instance methods, 1 class methods

## Instance variables

```
d _lastSelectionChangeTime;
```

## Properties

```
@property (Td,N,V_lastSelectionChangeTime) lastSelectionChangeTime;
@property (T@"_UISelectionFeedbackGeneratorConfiguration",R,N,G_selectionConfiguration) selectionConfiguration;
```

## Class methods

```
+[UISelectionFeedbackGenerator _configurationClass];
```

## Instance methods

```
-[UISelectionFeedbackGenerator userInteractionStartedAtLocation:];
-[UISelectionFeedbackGenerator _stats_key];
-[UISelectionFeedbackGenerator userInteractionCancelledAtLocation:];
-[UISelectionFeedbackGenerator userInteractionStarted];
-[UISelectionFeedbackGenerator userInteractionEnded];
-[UISelectionFeedbackGenerator userInteractionEndedAtLocation:];
-[UISelectionFeedbackGenerator userInteractionCancelled];
-[UISelectionFeedbackGenerator selectionChanged];
-[UISelectionFeedbackGenerator selectionChangedAtLocation:];
-[UISelectionFeedbackGenerator setLastSelectionChangeTime:];
-[UISelectionFeedbackGenerator _deactivated];
-[UISelectionFeedbackGenerator lastSelectionChangeTime];
-[UISelectionFeedbackGenerator _selectionConfiguration];
-[UISelectionFeedbackGenerator _selectionChangedAtLocation:];
```
