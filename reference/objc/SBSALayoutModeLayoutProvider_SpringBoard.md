# `SBSALayoutModeLayoutProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSABasePreferencesProvider`
- Protocols: `SBSAElementLayoutModeSupporting`
- 2 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
B _performedInitialLayoutIfNecessary;
q _supportedElementLayoutMode;
```

## Properties

```
@property (Tq,R,N,V_supportedElementLayoutMode) supportedElementLayoutMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSALayoutModeLayoutProvider defaultTransitionSettings];
-[SBSALayoutModeLayoutProvider description];
-[SBSALayoutModeLayoutProvider initWithLayoutMode:];
-[SBSALayoutModeLayoutProvider _updateElementDescription:forProminentPillWithElementContext:context:prominentPillContentWidth:containerBounds:];
-[SBSALayoutModeLayoutProvider preferencesFromContext:];
-[SBSALayoutModeLayoutProvider supportedElementLayoutMode];
```
