# `SBSADefaultsContextMutator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"SBSADefaultsContext" _mutatable;
```

## Properties

```
@property (T@"SBSADefaultsContext",R,N,V_mutatable) mutatable;
@property (TB,N) suppressDynamicIslandCompletely;
@property (TB,N) alwaysShowSystemApertureOnClonedDisplays;
@property (TB,N) alwaysShowSystemApertureInSnapshots;
@property (TB,N) alwaysRenderSystemApertureFillOnGPU;
@property (TB,N) neverRenderSystemApertureFillOnGPU;
@property (TB,N) enableSystemApertureStateCollection;
```

## Instance methods

```
-[SBSADefaultsContextMutator description];
-[SBSADefaultsContextMutator suppressDynamicIslandCompletely];
-[SBSADefaultsContextMutator alwaysRenderSystemApertureFillOnGPU];
-[SBSADefaultsContextMutator alwaysShowSystemApertureInSnapshots];
-[SBSADefaultsContextMutator alwaysShowSystemApertureOnClonedDisplays];
-[SBSADefaultsContextMutator enableSystemApertureStateCollection];
-[SBSADefaultsContextMutator initWithDefaultsContext:];
-[SBSADefaultsContextMutator mutatable];
-[SBSADefaultsContextMutator neverRenderSystemApertureFillOnGPU];
-[SBSADefaultsContextMutator setAlwaysRenderSystemApertureFillOnGPU:];
-[SBSADefaultsContextMutator setAlwaysShowSystemApertureInSnapshots:];
-[SBSADefaultsContextMutator setAlwaysShowSystemApertureOnClonedDisplays:];
-[SBSADefaultsContextMutator setEnableSystemApertureStateCollection:];
-[SBSADefaultsContextMutator setNeverRenderSystemApertureFillOnGPU:];
-[SBSADefaultsContextMutator setSuppressDynamicIslandCompletely:];
```
