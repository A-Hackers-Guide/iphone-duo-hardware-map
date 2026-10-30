# `BWAutoFocusROIAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 6 instance variables, 10 properties, 17 instance methods, 0 class methods

## Instance variables

```
i _focusRegionType;
i _luxLevel;
f _subjectDistance;
@"NSString" _portType;
@"NSDictionary" _focusRegion;
@"NSString" _clientApplicationID;
```

## Properties

```
@property (T@"NSString",&,N,V_portType) portType;
@property (Ti,N,V_focusRegionType) focusRegionType;
@property (T@"NSDictionary",&,N,V_focusRegion) focusRegion;
@property (Ti,N,V_luxLevel) luxLevel;
@property (Tf,N,V_subjectDistance) subjectDistance;
@property (T@"NSString",C,N,V_clientApplicationID) clientApplicationID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWAutoFocusROIAnalyticsPayload portType];
-[BWAutoFocusROIAnalyticsPayload focusRegionType];
-[BWAutoFocusROIAnalyticsPayload eventDictionary];
-[BWAutoFocusROIAnalyticsPayload init];
-[BWAutoFocusROIAnalyticsPayload dealloc];
-[BWAutoFocusROIAnalyticsPayload reset];
-[BWAutoFocusROIAnalyticsPayload setClientApplicationID:];
-[BWAutoFocusROIAnalyticsPayload setPortType:];
-[BWAutoFocusROIAnalyticsPayload eventName];
-[BWAutoFocusROIAnalyticsPayload luxLevel];
-[BWAutoFocusROIAnalyticsPayload setLuxLevel:];
-[BWAutoFocusROIAnalyticsPayload clientApplicationID];
-[BWAutoFocusROIAnalyticsPayload subjectDistance];
-[BWAutoFocusROIAnalyticsPayload setFocusRegion:];
-[BWAutoFocusROIAnalyticsPayload focusRegion];
-[BWAutoFocusROIAnalyticsPayload setFocusRegionType:];
-[BWAutoFocusROIAnalyticsPayload setSubjectDistance:];
```
