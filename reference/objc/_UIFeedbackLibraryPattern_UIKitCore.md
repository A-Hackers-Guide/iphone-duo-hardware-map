# `_UIFeedbackLibraryPattern`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedback`
- Protocols: `_UIFeedbackCoreHapticsPatternProviding`
- 4 instance variables, 8 properties, 11 instance methods, 3 class methods

## Instance variables

```
@"NSString" _libraryKey;
@"CHHapticPattern" _pattern;
B _highPriority;
q _forcedEnginePriority;
```

## Properties

```
@property (T@"NSString",R,N,V_libraryKey) libraryKey;
@property (Tq,N,V_forcedEnginePriority) forcedEnginePriority;
@property (T@"CHHapticPattern",R,N) pattern;
@property (TB,R,N,GisHighPriority,V_highPriority) highPriority;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIFeedbackLibraryPattern supportsSecureCoding];
+[_UIFeedbackLibraryPattern type];
+[_UIFeedbackLibraryPattern feedbackPatternWithLibraryKey:];
```

## Instance methods

```
-[_UIFeedbackLibraryPattern isHighPriority];
-[_UIFeedbackLibraryPattern _effectivePlayableFeedbackTypes];
-[_UIFeedbackLibraryPattern pattern];
-[_UIFeedbackLibraryPattern initWithDictionaryRepresentation:];
-[_UIFeedbackLibraryPattern copyWithZone:];
-[_UIFeedbackLibraryPattern isEqual:];
-[_UIFeedbackLibraryPattern dictionaryRepresentation];
-[_UIFeedbackLibraryPattern forcedEnginePriority];
-[_UIFeedbackLibraryPattern initWithLibraryKey:];
-[_UIFeedbackLibraryPattern libraryKey];
-[_UIFeedbackLibraryPattern setForcedEnginePriority:];
```
