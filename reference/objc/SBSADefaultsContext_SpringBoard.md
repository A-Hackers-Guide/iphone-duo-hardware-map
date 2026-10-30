# `SBSADefaultsContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `NSCopying`, `SBSABlockMutating`
- 6 instance variables, 10 properties, 24 instance methods, 3 class methods

## Instance variables

```
B _suppressDynamicIslandCompletely;
B _alwaysShowSystemApertureOnClonedDisplays;
B _alwaysShowSystemApertureInSnapshots;
B _alwaysRenderSystemApertureFillOnGPU;
B _neverRenderSystemApertureFillOnGPU;
B _enableSystemApertureStateCollection;
```

## Properties

```
@property (TB,N,S_setSuppressDynamicIslandCompletely:,V_suppressDynamicIslandCompletely) suppressDynamicIslandCompletely;
@property (TB,N,S_setAlwaysShowSystemApertureOnClonedDisplays:,V_alwaysShowSystemApertureOnClonedDisplays) alwaysShowSystemApertureOnClonedDisplays;
@property (TB,N,S_setAlwaysShowSystemApertureInSnapshots:,V_alwaysShowSystemApertureInSnapshots) alwaysShowSystemApertureInSnapshots;
@property (TB,N,S_setAlwaysRenderSystemApertureFillOnGPU:,V_alwaysRenderSystemApertureFillOnGPU) alwaysRenderSystemApertureFillOnGPU;
@property (TB,N,S_setNeverRenderSystemApertureFillOnGPU:,V_neverRenderSystemApertureFillOnGPU) neverRenderSystemApertureFillOnGPU;
@property (TB,N,S_setEnableSystemApertureStateCollection:,V_enableSystemApertureStateCollection) enableSystemApertureStateCollection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSADefaultsContext initialize];
+[SBSADefaultsContext instanceWithBlock:];
+[SBSADefaultsContext mutatorClass];
```

## Instance methods

```
-[SBSADefaultsContext hash];
-[SBSADefaultsContext copyWithZone:];
-[SBSADefaultsContext isEqual:];
-[SBSADefaultsContext copyWithBlock:];
-[SBSADefaultsContext membersForCoder];
-[SBSADefaultsContext suppressDynamicIslandCompletely];
-[SBSADefaultsContext _setAlwaysRenderSystemApertureFillOnGPU:];
-[SBSADefaultsContext _setAlwaysShowSystemApertureInSnapshots:];
-[SBSADefaultsContext _setAlwaysShowSystemApertureOnClonedDisplays:];
-[SBSADefaultsContext _setEnableSystemApertureStateCollection:];
-[SBSADefaultsContext _setNeverRenderSystemApertureFillOnGPU:];
-[SBSADefaultsContext _setSuppressDynamicIslandCompletely:];
-[SBSADefaultsContext alwaysRenderSystemApertureFillOnGPU];
-[SBSADefaultsContext alwaysShowSystemApertureInSnapshots];
-[SBSADefaultsContext alwaysShowSystemApertureOnClonedDisplays];
-[SBSADefaultsContext copyBySettingAlwaysRenderSystemApertureFillOnGPU:];
-[SBSADefaultsContext copyBySettingAlwaysShowSystemApertureInSnapshots:];
-[SBSADefaultsContext copyBySettingAlwaysShowSystemApertureOnClonedDisplays:];
-[SBSADefaultsContext copyBySettingEnableSystemApertureStateCollection:];
-[SBSADefaultsContext copyBySettingNeverRenderSystemApertureFillOnGPU:];
-[SBSADefaultsContext copyBySettingSuppressDynamicIslandCompletely:];
-[SBSADefaultsContext enableSystemApertureStateCollection];
-[SBSADefaultsContext initWithDefaultsContext:];
-[SBSADefaultsContext neverRenderSystemApertureFillOnGPU];
```
