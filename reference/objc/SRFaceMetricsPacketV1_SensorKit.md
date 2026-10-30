# `SRFaceMetricsPacketV1`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRFaceMetricsPacket`
- 2 instance variables, 21 properties, 18 instance methods, 1 class methods

## Instance variables

```
^{?=III[501f]{?=[3[3f]][3f]}[3f]{?=fffffffffffffffffffffffffffffffffffffffffffffffffff}{?={?=ffffffffff}{?=ffffffff}}} _packet;
@"NSUUID" _faceIdentifier;
```

## Properties

```
@property (T@"NSString",R,N) version;
@property (TQ,R,N) context;
@property (T@"NSString",R,C,N) sessionIdentifier;
@property (T@"NSArray",R,&,N) wholeFaceExpressions;
@property (T@"NSArray",R,&,N) partialFaceExpressions;
@property (T@"NSUUID",R,&,N) faceIdentifier;
@property (T@"NSArray",R,&,N) rotation;
@property (T@"NSArray",R,&,N) translation;
@property (T@"NSArray",R,&,N) gaze;
@property (T@"NSData",R,&,N) blendshapes;
@property (T@"NSArray",R,&,N) geometryLeftEye;
@property (T@"NSArray",R,&,N) geometryRightEye;
@property (Tf,R,N) leftEyePitch;
@property (Tf,R,N) rightEyePitch;
@property (Tf,R,N) leftEyeYaw;
@property (Tf,R,N) rightEyeYaw;
@property (T@"NSDictionary",R,&,N) trackingData;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRFaceMetricsPacketV1 packetWithHAFacialMetricsPacket:];
```

## Instance methods

```
-[SRFaceMetricsPacketV1 sessionIdentifier];
-[SRFaceMetricsPacketV1 rotation];
-[SRFaceMetricsPacketV1 dealloc];
-[SRFaceMetricsPacketV1 version];
-[SRFaceMetricsPacketV1 context];
-[SRFaceMetricsPacketV1 translation];
-[SRFaceMetricsPacketV1 gaze];
-[SRFaceMetricsPacketV1 trackingData];
-[SRFaceMetricsPacketV1 geometryLeftEye];
-[SRFaceMetricsPacketV1 blendshapes];
-[SRFaceMetricsPacketV1 faceIdentifier];
-[SRFaceMetricsPacketV1 geometryRightEye];
-[SRFaceMetricsPacketV1 leftEyePitch];
-[SRFaceMetricsPacketV1 leftEyeYaw];
-[SRFaceMetricsPacketV1 partialFaceExpressions];
-[SRFaceMetricsPacketV1 rightEyePitch];
-[SRFaceMetricsPacketV1 rightEyeYaw];
-[SRFaceMetricsPacketV1 wholeFaceExpressions];
```
