# `SRFaceMetricsPacketV5`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRFaceMetricsPacket`
- 4 instance variables, 21 properties, 18 instance methods, 1 class methods

## Instance variables

```
^{?=I[16C]IQQQdQd{?=[3[3f]][3f]}[3f][3f]ffff[3f]{?=fffffffffffffffffffffffffffffffffffffffffffffffffff}{?={?=fffffff}{?=ffffffff}}} _packet;
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
+[SRFaceMetricsPacketV5 packetWithHAFacialMetricsPacket:];
```

## Instance methods

```
-[SRFaceMetricsPacketV5 sessionIdentifier];
-[SRFaceMetricsPacketV5 rotation];
-[SRFaceMetricsPacketV5 dealloc];
-[SRFaceMetricsPacketV5 version];
-[SRFaceMetricsPacketV5 context];
-[SRFaceMetricsPacketV5 translation];
-[SRFaceMetricsPacketV5 gaze];
-[SRFaceMetricsPacketV5 trackingData];
-[SRFaceMetricsPacketV5 geometryLeftEye];
-[SRFaceMetricsPacketV5 blendshapes];
-[SRFaceMetricsPacketV5 faceIdentifier];
-[SRFaceMetricsPacketV5 geometryRightEye];
-[SRFaceMetricsPacketV5 leftEyePitch];
-[SRFaceMetricsPacketV5 leftEyeYaw];
-[SRFaceMetricsPacketV5 partialFaceExpressions];
-[SRFaceMetricsPacketV5 rightEyePitch];
-[SRFaceMetricsPacketV5 rightEyeYaw];
-[SRFaceMetricsPacketV5 wholeFaceExpressions];
```
