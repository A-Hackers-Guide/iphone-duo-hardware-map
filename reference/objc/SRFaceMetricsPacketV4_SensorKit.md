# `SRFaceMetricsPacketV4`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRFaceMetricsPacket`
- 4 instance variables, 21 properties, 18 instance methods, 1 class methods

## Instance variables

```
^{?=IIIQQQdQd{?=[3[3f]][3f]}[3f][3f]ffff[3f]{?=fffffffffffffffffffffffffffffffffffffffffffffffffff}{?={?=fffffff}{?=ffffffff}}} _packet;
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
+[SRFaceMetricsPacketV4 packetWithHAFacialMetricsPacket:];
```

## Instance methods

```
-[SRFaceMetricsPacketV4 sessionIdentifier];
-[SRFaceMetricsPacketV4 rotation];
-[SRFaceMetricsPacketV4 dealloc];
-[SRFaceMetricsPacketV4 version];
-[SRFaceMetricsPacketV4 context];
-[SRFaceMetricsPacketV4 translation];
-[SRFaceMetricsPacketV4 gaze];
-[SRFaceMetricsPacketV4 trackingData];
-[SRFaceMetricsPacketV4 geometryLeftEye];
-[SRFaceMetricsPacketV4 blendshapes];
-[SRFaceMetricsPacketV4 faceIdentifier];
-[SRFaceMetricsPacketV4 geometryRightEye];
-[SRFaceMetricsPacketV4 leftEyePitch];
-[SRFaceMetricsPacketV4 leftEyeYaw];
-[SRFaceMetricsPacketV4 partialFaceExpressions];
-[SRFaceMetricsPacketV4 rightEyePitch];
-[SRFaceMetricsPacketV4 rightEyeYaw];
-[SRFaceMetricsPacketV4 wholeFaceExpressions];
```
