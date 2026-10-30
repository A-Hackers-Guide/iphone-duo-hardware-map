# `SBSystemActionPreviewSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
d _minimumPreviewInterval;
d _additionalUrgencyInterval;
```

## Properties

```
@property (Td,N,V_minimumPreviewInterval) minimumPreviewInterval;
@property (Td,N,V_additionalUrgencyInterval) additionalUrgencyInterval;
```

## Class methods

```
+[SBSystemActionPreviewSettings settingsControllerModule];
```

## Instance methods

```
-[SBSystemActionPreviewSettings setDefaultValues];
-[SBSystemActionPreviewSettings additionalUrgencyInterval];
-[SBSystemActionPreviewSettings minimumPreviewInterval];
-[SBSystemActionPreviewSettings setAdditionalUrgencyInterval:];
-[SBSystemActionPreviewSettings setMinimumPreviewInterval:];
```
