# `SBWindowingModifierBase`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBChainableModifier`
- Protocols: `SBWindowingModifierContext`, `SBWindowingModifierQuery`, `SBWindowingModifierUpdate`
- 2 instance variables, 5 properties, 6 instance methods, 3 class methods

## Instance variables

```
B _hasPerformedLayoutViewModelsAsTemporaryChildAtLeastOnce;
B _staticTemporaryChildModifier;
```

## Properties

```
@property (TB,N,GisStaticTemporaryChildModifier,V_staticTemporaryChildModifier) staticTemporaryChildModifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBWindowingModifierBase contextProtocol];
+[SBWindowingModifierBase queryProtocol];
+[SBWindowingModifierBase updateProtocol];
```

## Instance methods

```
-[SBWindowingModifierBase handleEvent:];
-[SBWindowingModifierBase displayName];
-[SBWindowingModifierBase isStaticTemporaryChildModifier];
-[SBWindowingModifierBase isWindowingModifier];
-[SBWindowingModifierBase setStaticTemporaryChildModifier:];
-[SBWindowingModifierBase willPerformAsTemporaryChildModifier];
```
