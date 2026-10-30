# `SRFaceMetricsPacketV3`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRFaceMetricsPacket`
- 4 instance variables, 21 properties, 18 instance methods, 1 class methods

## Instance variables

```
^{?=IIIQdQd{?=[3[3f]][3f]}[3f]{?=fffffffffffffffffffffffffffffffffffffffffffffffffff}{?={?=fffffff}{?=ffffffff}}} _packet;
@"NSUUID" _faceIdentifier;
@"NSString" _sessionIdentifier;
Q _context;
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
+[SRFaceMetricsPacketV3 packetWithHAFacialMetricsPacket:];
```

## Instance methods

```
-[SRFaceMetricsPacketV3 sessionIdentifier];
-[SRFaceMetricsPacketV3 rotation];
-[SRFaceMetricsPacketV3 dealloc];
-[SRFaceMetricsPacketV3 version];
-[SRFaceMetricsPacketV3 context];
-[SRFaceMetricsPacketV3 translation];
-[SRFaceMetricsPacketV3 gaze];
-[SRFaceMetricsPacketV3 trackingData];
-[SRFaceMetricsPacketV3 geometryLeftEye];
-[SRFaceMetricsPacketV3 blendshapes];
-[SRFaceMetricsPacketV3 faceIdentifier];
-[SRFaceMetricsPacketV3 geometryRightEye];
-[SRFaceMetricsPacketV3 leftEyePitch];
-[SRFaceMetricsPacketV3 leftEyeYaw];
-[SRFaceMetricsPacketV3 partialFaceExpressions];
-[SRFaceMetricsPacketV3 rightEyePitch];
-[SRFaceMetricsPacketV3 rightEyeYaw];
-[SRFaceMetricsPacketV3 wholeFaceExpressions];
```
