# `_UIFeedbackHapticFilePattern`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedback`
- Protocols: `_UIFeedbackFilePlayable_Internal`, `_UIFeedbackDiscretePlayable`
- 2 instance variables, 6 properties, 8 instance methods, 3 class methods

## Instance variables

```
B _highPriority;
@"NSURL" _fileURL;
```

## Properties

```
@property (T@"NSURL",R,N,V_fileURL) fileURL;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N,GisHighPriority,V_highPriority) highPriority;
```

## Class methods

```
+[_UIFeedbackHapticFilePattern supportsSecureCoding];
+[_UIFeedbackHapticFilePattern type];
+[_UIFeedbackHapticFilePattern feedbackPatternFromFile:];
```

## Instance methods

```
-[_UIFeedbackHapticFilePattern isHighPriority];
-[_UIFeedbackHapticFilePattern _effectivePlayableFeedbackTypes];
-[_UIFeedbackHapticFilePattern initWithDictionaryRepresentation:];
-[_UIFeedbackHapticFilePattern fileURL];
-[_UIFeedbackHapticFilePattern initWithFileURL:];
-[_UIFeedbackHapticFilePattern copyWithZone:];
-[_UIFeedbackHapticFilePattern isEqual:];
-[_UIFeedbackHapticFilePattern dictionaryRepresentation];
```
