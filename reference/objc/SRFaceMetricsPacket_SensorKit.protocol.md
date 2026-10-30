# `SRFaceMetricsPacket` (protocol)

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 17 properties, 17 instance methods, 0 class methods

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
```

## Instance methods

```
-[SRFaceMetricsPacket sessionIdentifier];
-[SRFaceMetricsPacket rotation];
-[SRFaceMetricsPacket version];
-[SRFaceMetricsPacket context];
-[SRFaceMetricsPacket translation];
-[SRFaceMetricsPacket gaze];
-[SRFaceMetricsPacket trackingData];
-[SRFaceMetricsPacket geometryLeftEye];
-[SRFaceMetricsPacket blendshapes];
-[SRFaceMetricsPacket faceIdentifier];
-[SRFaceMetricsPacket geometryRightEye];
-[SRFaceMetricsPacket leftEyePitch];
-[SRFaceMetricsPacket leftEyeYaw];
-[SRFaceMetricsPacket partialFaceExpressions];
-[SRFaceMetricsPacket rightEyePitch];
-[SRFaceMetricsPacket rightEyeYaw];
-[SRFaceMetricsPacket wholeFaceExpressions];
```
