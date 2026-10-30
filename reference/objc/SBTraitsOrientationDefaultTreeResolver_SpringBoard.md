# `SBTraitsOrientationDefaultTreeResolver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTraitsOrientationStageComponent`
- Protocols: `TRAPreferencesStageResolving`
- 3 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"TRASettingsValidator" _settingsValidator;
@"NSMutableDictionary" _mapResolverCache;
@? _deviceToInterfaceOrientationConversionBlock;
```

## Properties

```
@property (T@?,C,N,V_deviceToInterfaceOrientationConversionBlock) deviceToInterfaceOrientationConversionBlock;
@property (T@"NSNumber",R,N) componentOrder;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBTraitsOrientationDefaultTreeResolver _mapResolverForTargetOrientation:currentOrientation:];
-[SBTraitsOrientationDefaultTreeResolver _node:validatesNewSettings:];
-[SBTraitsOrientationDefaultTreeResolver _targetOrientationForResolutionInfo:validatedInputs:rawInputs:participant:parent:];
-[SBTraitsOrientationDefaultTreeResolver deviceToInterfaceOrientationConversionBlock];
-[SBTraitsOrientationDefaultTreeResolver initWithComponentOrder:];
-[SBTraitsOrientationDefaultTreeResolver resolveStagePreferencesWithContext:preferencesTree:];
-[SBTraitsOrientationDefaultTreeResolver setDeviceToInterfaceOrientationConversionBlock:];
```
