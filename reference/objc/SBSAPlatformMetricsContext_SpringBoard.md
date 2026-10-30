# `SBSAPlatformMetricsContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `NSCopying`, `SBSABlockMutating`
- 1 instance variables, 18 properties, 50 instance methods, 3 class methods

## Instance variables

```
@"NSMutableDictionary" _backingDictionary;
```

## Properties

```
@property (Td,N,S_setMaximumCornerRadius:) maximumCornerRadius;
@property (Td,N,S_setCustomLayoutSquareCornerRadius:) customLayoutSquareCornerRadius;
@property (Td,N,S_setCustomLayoutSquareLargeCornerRadius:) customLayoutSquareLargeCornerRadius;
@property (Td,N,S_setCustomLayoutOvalCornerRadius:) customLayoutOvalCornerRadius;
@property (Td,N,S_setCustomLayoutTallRectCornerRadius:) customLayoutTallRectCornerRadius;
@property (Td,N,S_setMinimumEdgePadding:) minimumEdgePadding;
@property (T@"NSArray",C,N,S_setInertContainerFrames:) inertContainerFrames;
@property (Td,N,S_setDisplayCornerRadius:) displayCornerRadius;
@property (Td,N,S_setMinimumContainerDimension:) minimumContainerDimension;
@property (Td,N,S_setDisplayCornerRadiusIgnoringZoom:) displayCornerRadiusIgnoringZoom;
@property (TQ,N,S_setSensorVariant:) sensorVariant;
@property (Td,N,S_setCornerCircleSensorAttachedPillExtensionPadding:) cornerCircleSensorAttachedPillExtensionPadding;
@property (T{UIEdgeInsets=dddd},R,N) screenEdgeInsets;
@property (T{UIEdgeInsets=dddd},R,N) landscapeScreenEdgeInsets;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSAPlatformMetricsContext initialize];
+[SBSAPlatformMetricsContext instanceWithBlock:];
+[SBSAPlatformMetricsContext mutatorClass];
```

## Instance methods

```
-[SBSAPlatformMetricsContext init];
-[SBSAPlatformMetricsContext displayCornerRadiusIgnoringZoom];
-[SBSAPlatformMetricsContext hash];
-[SBSAPlatformMetricsContext description];
-[SBSAPlatformMetricsContext copyWithZone:];
-[SBSAPlatformMetricsContext isEqual:];
-[SBSAPlatformMetricsContext cornerCircleSensorAttachedPillExtensionPadding];
-[SBSAPlatformMetricsContext copyWithBlock:];
-[SBSAPlatformMetricsContext displayCornerRadius];
-[SBSAPlatformMetricsContext membersForCoder];
-[SBSAPlatformMetricsContext initWithPlatformMetricsContext:];
-[SBSAPlatformMetricsContext _setCornerCircleSensorAttachedPillExtensionPadding:];
-[SBSAPlatformMetricsContext _setCustomLayoutOvalCornerRadius:];
-[SBSAPlatformMetricsContext _setCustomLayoutSquareCornerRadius:];
-[SBSAPlatformMetricsContext _setCustomLayoutSquareLargeCornerRadius:];
-[SBSAPlatformMetricsContext _setCustomLayoutTallRectCornerRadius:];
-[SBSAPlatformMetricsContext _setDisplayCornerRadius:];
-[SBSAPlatformMetricsContext _setDisplayCornerRadiusIgnoringZoom:];
-[SBSAPlatformMetricsContext _setInertContainerFrames:];
-[SBSAPlatformMetricsContext _setLandscapeScreenEdgeInsets:];
-[SBSAPlatformMetricsContext _setMaximumCornerRadius:];
-[SBSAPlatformMetricsContext _setMinimumContainerDimension:];
-[SBSAPlatformMetricsContext _setMinimumEdgePadding:];
-[SBSAPlatformMetricsContext _setScreenEdgeInsets:];
-[SBSAPlatformMetricsContext _setSensorVariant:];
-[SBSAPlatformMetricsContext copyBySettingCornerCircleSensorAttachedPillExtensionPadding:];
-[SBSAPlatformMetricsContext copyBySettingCustomLayoutOvalCornerRadius:];
-[SBSAPlatformMetricsContext copyBySettingCustomLayoutSquareCornerRadius:];
-[SBSAPlatformMetricsContext copyBySettingCustomLayoutSquareLargeCornerRadius:];
-[SBSAPlatformMetricsContext copyBySettingCustomLayoutTallRectCornerRadius:];
-[SBSAPlatformMetricsContext copyBySettingDisplayCornerRadius:];
-[SBSAPlatformMetricsContext copyBySettingDisplayCornerRadiusIgnoringZoom:];
-[SBSAPlatformMetricsContext copyBySettingInertContainerFrames:];
-[SBSAPlatformMetricsContext copyBySettingLandscapeScreenEdgeInsets:];
-[SBSAPlatformMetricsContext copyBySettingMaximumCornerRadius:];
-[SBSAPlatformMetricsContext copyBySettingMinimumContainerDimension:];
-[SBSAPlatformMetricsContext copyBySettingMinimumEdgePadding:];
-[SBSAPlatformMetricsContext copyBySettingScreenEdgeInsets:];
-[SBSAPlatformMetricsContext copyBySettingSensorVariant:];
-[SBSAPlatformMetricsContext customLayoutOvalCornerRadius];
-[SBSAPlatformMetricsContext customLayoutSquareCornerRadius];
-[SBSAPlatformMetricsContext customLayoutSquareLargeCornerRadius];
-[SBSAPlatformMetricsContext customLayoutTallRectCornerRadius];
-[SBSAPlatformMetricsContext inertContainerFrames];
-[SBSAPlatformMetricsContext landscapeScreenEdgeInsets];
-[SBSAPlatformMetricsContext maximumCornerRadius];
-[SBSAPlatformMetricsContext minimumContainerDimension];
-[SBSAPlatformMetricsContext minimumEdgePadding];
-[SBSAPlatformMetricsContext screenEdgeInsets];
-[SBSAPlatformMetricsContext sensorVariant];
```
