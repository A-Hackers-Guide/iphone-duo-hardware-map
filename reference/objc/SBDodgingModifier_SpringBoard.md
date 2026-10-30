# `SBDodgingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBChainableModifier`
- Protocols: `SBDodgingQueryProviding`, `SBDodgingContextProviding`
- 0 instance variables, 4 properties, 8 instance methods, 3 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBDodgingModifier contextProtocol];
+[SBDodgingModifier newEventResponse];
+[SBDodgingModifier queryProtocol];
```

## Instance methods

```
-[SBDodgingModifier _handleEvent:];
-[SBDodgingModifier loggingCategory];
-[SBDodgingModifier handleRemovalEvent:];
-[SBDodgingModifier handleAnimationCompletionEvent:];
-[SBDodgingModifier handleCustomEvent:];
-[SBDodgingModifier handleInsertionEvent:];
-[SBDodgingModifier handlePreferenceChangeEvent:];
-[SBDodgingModifier handleRotationEvent:];
```
