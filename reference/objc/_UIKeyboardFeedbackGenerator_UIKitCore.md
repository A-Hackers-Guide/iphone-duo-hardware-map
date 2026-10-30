# `_UIKeyboardFeedbackGenerator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIFeedbackGenerator`
- Protocols: `_UIKBFeedbackGenerating`
- 1 instance variables, 6 properties, 11 instance methods, 1 class methods

## Instance variables

```
d _lastTypedKeyTimestamp;
```

## Properties

```
@property (T@"_UIKeyboardFeedbackGeneratorConfiguration",R,N,G_keyboardConfiguration) keyboardConfiguration;
@property (Td,N,G_lastTypedKeyTimestamp,S_setLastTypedKeyTimestamp:,V_lastTypedKeyTimestamp) lastTypedKeyTimestamp;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIKeyboardFeedbackGenerator _configurationClass];
```

## Instance methods

```
-[_UIKeyboardFeedbackGenerator _stats_key];
-[_UIKeyboardFeedbackGenerator actionOccurred:textLength:atLocation:];
-[_UIKeyboardFeedbackGenerator _playFeedbackForActionType:withCustomization:];
-[_UIKeyboardFeedbackGenerator _lastTypedKeyTimestamp];
-[_UIKeyboardFeedbackGenerator _keyboardConfiguration];
-[_UIKeyboardFeedbackGenerator scaleVolumeSlow:fast:timeSpan:];
-[_UIKeyboardFeedbackGenerator _setLastTypedKeyTimestamp:];
-[_UIKeyboardFeedbackGenerator actionOccurred:];
-[_UIKeyboardFeedbackGenerator _feedbackWithUpdatedVolume:];
-[_UIKeyboardFeedbackGenerator _autoDeactivationTimeout];
-[_UIKeyboardFeedbackGenerator actionOccurred:atLocation:];
```
