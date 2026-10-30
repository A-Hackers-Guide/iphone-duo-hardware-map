# `SRFaceMetricsPacketV0`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRFaceMetricsPacket`
- 2 instance variables, 21 properties, 18 instance methods, 1 class methods

## Instance variables

```
^{?=II[501f]{?=[3[3f]][3f]}[3f]{?=fffffffffffffffffffffffffffffffffffffffffffffffffff}{?={?=ffffffffff}{?=ffffffff}}} _packet;
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
+[SRFaceMetricsPacketV0 packetWithHAFacialMetricsPacket:];
```

## Instance methods

```
-[SRFaceMetricsPacketV0 sessionIdentifier];
-[SRFaceMetricsPacketV0 rotation];
-[SRFaceMetricsPacketV0 dealloc];
-[SRFaceMetricsPacketV0 version];
-[SRFaceMetricsPacketV0 context];
-[SRFaceMetricsPacketV0 translation];
-[SRFaceMetricsPacketV0 gaze];
-[SRFaceMetricsPacketV0 trackingData];
-[SRFaceMetricsPacketV0 geometryLeftEye];
-[SRFaceMetricsPacketV0 blendshapes];
-[SRFaceMetricsPacketV0 faceIdentifier];
-[SRFaceMetricsPacketV0 geometryRightEye];
-[SRFaceMetricsPacketV0 leftEyePitch];
-[SRFaceMetricsPacketV0 leftEyeYaw];
-[SRFaceMetricsPacketV0 partialFaceExpressions];
-[SRFaceMetricsPacketV0 rightEyePitch];
-[SRFaceMetricsPacketV0 rightEyeYaw];
-[SRFaceMetricsPacketV0 wholeFaceExpressions];
```
