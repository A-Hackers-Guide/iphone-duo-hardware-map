# `SBSystemAction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`
- 9 instance variables, 14 properties, 18 instance methods, 1 class methods

## Instance variables

```
B _cameraCaptureAction;
B _shouldBePerformedWhenSuppressed;
B _shouldWakeScreenWhenPerformed;
B _canBePerformedInSetupMode;
B _hostBundleRequiresValidation;
@"WFConfiguredStaccatoAction" _configuredAction;
@"<SBSystemActionInstanceIdentifying>" _instanceIdentity;
@"NSString" _hostBundleIdentifier;
{SBSystemActionAnalyticsData="actionIdentifier"@"NSString""parameterValueIdentifier"@"NSString"} _analyticsData;
```

## Properties

```
@property (T@"CHSControlIdentity",R,N) controlIdentity;
@property (T@"WFConfiguredStaccatoAction",R,N,V_configuredAction) configuredAction;
@property (T@"<SBSystemActionInstanceIdentifying>",R,C,N,V_instanceIdentity) instanceIdentity;
@property (TB,R,N,GisCameraCaptureAction,V_cameraCaptureAction) cameraCaptureAction;
@property (TB,R,N,V_shouldBePerformedWhenSuppressed) shouldBePerformedWhenSuppressed;
@property (TB,R,N,V_shouldWakeScreenWhenPerformed) shouldWakeScreenWhenPerformed;
@property (TB,R,N,V_canBePerformedInSetupMode) canBePerformedInSetupMode;
@property (TB,R,N,V_hostBundleRequiresValidation) hostBundleRequiresValidation;
@property (T@"NSString",R,N,V_hostBundleIdentifier) hostBundleIdentifier;
@property (T{SBSystemActionAnalyticsData=@@},R,N,V_analyticsData) analyticsData;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSystemAction defaultSymbolFont];
```

## Instance methods

```
-[SBSystemAction analyticsData];
-[SBSystemAction appendDescriptionToFormatter:];
-[SBSystemAction isCameraCaptureAction];
-[SBSystemAction hostBundleIdentifier];
-[SBSystemAction hash];
-[SBSystemAction description];
-[SBSystemAction isEqual:];
-[SBSystemAction controlIdentity];
-[SBSystemAction instanceIdentity];
-[SBSystemAction shouldBePerformedWhenSuppressed];
-[SBSystemAction canBePerformedInSetupMode];
-[SBSystemAction configuredAction];
-[SBSystemAction controlAction];
-[SBSystemAction hostBundleRequiresValidation];
-[SBSystemAction initWithConfiguredAction:instanceIdentity:];
-[SBSystemAction newExecutor];
-[SBSystemAction newSimplePreviewElement];
-[SBSystemAction shouldWakeScreenWhenPerformed];
```
