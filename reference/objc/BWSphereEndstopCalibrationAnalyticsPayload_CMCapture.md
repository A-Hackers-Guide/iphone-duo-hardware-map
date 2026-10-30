# `BWSphereEndstopCalibrationAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 13 instance variables, 17 properties, 31 instance methods, 0 class methods

## Instance variables

```
q _magneticFieldMagnitude;
@"NSString" _portType;
I _calibrationStatus;
i _sphereXPosEndstop;
i _sphereXNegEndstop;
i _sphereYPosEndstop;
i _sphereYNegEndstop;
i _deltaSphereXPosEndstop;
i _deltaSphereXNegEndstop;
i _deltaSphereYPosEndstop;
i _deltaSphereYNegEndstop;
i _sphereXStroke;
i _sphereYStroke;
```

## Properties

```
@property (Tq,N,V_magneticFieldMagnitude) magneticFieldMagnitude;
@property (T@"NSString",&,N,V_portType) portType;
@property (TI,N,V_calibrationStatus) calibrationStatus;
@property (Ti,N,V_sphereXPosEndstop) sphereXPosEndstop;
@property (Ti,N,V_sphereXNegEndstop) sphereXNegEndstop;
@property (Ti,N,V_sphereYPosEndstop) sphereYPosEndstop;
@property (Ti,N,V_sphereYNegEndstop) sphereYNegEndstop;
@property (Ti,N,V_deltaSphereXPosEndstop) deltaSphereXPosEndstop;
@property (Ti,N,V_deltaSphereXNegEndstop) deltaSphereXNegEndstop;
@property (Ti,N,V_deltaSphereYPosEndstop) deltaSphereYPosEndstop;
@property (Ti,N,V_deltaSphereYNegEndstop) deltaSphereYNegEndstop;
@property (Ti,N,V_sphereXStroke) sphereXStroke;
@property (Ti,N,V_sphereYStroke) sphereYStroke;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWSphereEndstopCalibrationAnalyticsPayload portType];
-[BWSphereEndstopCalibrationAnalyticsPayload eventDictionary];
-[BWSphereEndstopCalibrationAnalyticsPayload init];
-[BWSphereEndstopCalibrationAnalyticsPayload dealloc];
-[BWSphereEndstopCalibrationAnalyticsPayload reset];
-[BWSphereEndstopCalibrationAnalyticsPayload setPortType:];
-[BWSphereEndstopCalibrationAnalyticsPayload eventName];
-[BWSphereEndstopCalibrationAnalyticsPayload calibrationStatus];
-[BWSphereEndstopCalibrationAnalyticsPayload setCalibrationStatus:];
-[BWSphereEndstopCalibrationAnalyticsPayload deltaSphereXNegEndstop];
-[BWSphereEndstopCalibrationAnalyticsPayload deltaSphereXPosEndstop];
-[BWSphereEndstopCalibrationAnalyticsPayload deltaSphereYNegEndstop];
-[BWSphereEndstopCalibrationAnalyticsPayload deltaSphereYPosEndstop];
-[BWSphereEndstopCalibrationAnalyticsPayload magneticFieldMagnitude];
-[BWSphereEndstopCalibrationAnalyticsPayload setDeltaSphereXNegEndstop:];
-[BWSphereEndstopCalibrationAnalyticsPayload setDeltaSphereXPosEndstop:];
-[BWSphereEndstopCalibrationAnalyticsPayload setDeltaSphereYNegEndstop:];
-[BWSphereEndstopCalibrationAnalyticsPayload setDeltaSphereYPosEndstop:];
-[BWSphereEndstopCalibrationAnalyticsPayload setMagneticFieldMagnitude:];
-[BWSphereEndstopCalibrationAnalyticsPayload setSphereXNegEndstop:];
-[BWSphereEndstopCalibrationAnalyticsPayload setSphereXPosEndstop:];
-[BWSphereEndstopCalibrationAnalyticsPayload setSphereXStroke:];
-[BWSphereEndstopCalibrationAnalyticsPayload setSphereYNegEndstop:];
-[BWSphereEndstopCalibrationAnalyticsPayload setSphereYPosEndstop:];
-[BWSphereEndstopCalibrationAnalyticsPayload setSphereYStroke:];
-[BWSphereEndstopCalibrationAnalyticsPayload sphereXNegEndstop];
-[BWSphereEndstopCalibrationAnalyticsPayload sphereXPosEndstop];
-[BWSphereEndstopCalibrationAnalyticsPayload sphereXStroke];
-[BWSphereEndstopCalibrationAnalyticsPayload sphereYNegEndstop];
-[BWSphereEndstopCalibrationAnalyticsPayload sphereYPosEndstop];
-[BWSphereEndstopCalibrationAnalyticsPayload sphereYStroke];
```
