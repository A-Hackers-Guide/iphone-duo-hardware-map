# `BWSphereInteractionCalibrationAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 7 instance variables, 11 properties, 19 instance methods, 0 class methods

## Instance variables

```
q _magneticFieldMagnitude;
@"NSString" _portType;
I _calibrationStatus;
i _sphereNeutralPositionError;
i _sphereNeutralPosition;
i _sphereMacroPositionError;
i _sphereMacroPosition;
```

## Properties

```
@property (Tq,N,V_magneticFieldMagnitude) magneticFieldMagnitude;
@property (T@"NSString",&,N,V_portType) portType;
@property (TI,N,V_calibrationStatus) calibrationStatus;
@property (Ti,N,V_sphereNeutralPositionError) sphereNeutralPositionError;
@property (Ti,N,V_sphereNeutralPosition) sphereNeutralPosition;
@property (Ti,N,V_sphereMacroPositionError) sphereMacroPositionError;
@property (Ti,N,V_sphereMacroPosition) sphereMacroPosition;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWSphereInteractionCalibrationAnalyticsPayload portType];
-[BWSphereInteractionCalibrationAnalyticsPayload eventDictionary];
-[BWSphereInteractionCalibrationAnalyticsPayload init];
-[BWSphereInteractionCalibrationAnalyticsPayload dealloc];
-[BWSphereInteractionCalibrationAnalyticsPayload reset];
-[BWSphereInteractionCalibrationAnalyticsPayload setPortType:];
-[BWSphereInteractionCalibrationAnalyticsPayload eventName];
-[BWSphereInteractionCalibrationAnalyticsPayload calibrationStatus];
-[BWSphereInteractionCalibrationAnalyticsPayload setCalibrationStatus:];
-[BWSphereInteractionCalibrationAnalyticsPayload magneticFieldMagnitude];
-[BWSphereInteractionCalibrationAnalyticsPayload setMagneticFieldMagnitude:];
-[BWSphereInteractionCalibrationAnalyticsPayload setSphereMacroPosition:];
-[BWSphereInteractionCalibrationAnalyticsPayload setSphereMacroPositionError:];
-[BWSphereInteractionCalibrationAnalyticsPayload setSphereNeutralPosition:];
-[BWSphereInteractionCalibrationAnalyticsPayload setSphereNeutralPositionError:];
-[BWSphereInteractionCalibrationAnalyticsPayload sphereMacroPosition];
-[BWSphereInteractionCalibrationAnalyticsPayload sphereMacroPositionError];
-[BWSphereInteractionCalibrationAnalyticsPayload sphereNeutralPosition];
-[BWSphereInteractionCalibrationAnalyticsPayload sphereNeutralPositionError];
```
