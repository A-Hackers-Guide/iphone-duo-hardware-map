# `BWFusionTrackerObservable`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FTObservable`
- 7 instance variables, 11 properties, 9 instance methods, 0 class methods

## Instance variables

```
{?="value"q"timescale"i"flags"I"epoch"q} _lastDetectionTimestamp;
@"NSDictionary" _metadata;
f _confidence;
q _objectKind;
Q _identifier;
{?="value"q"timescale"i"flags"I"epoch"q} _frameTimestamp;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _box;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_box) box;
@property (Tq,R,N,V_objectKind) objectKind;
@property (Tf,R,N,V_confidence) confidence;
@property (T{?=qiIq},R,N,V_frameTimestamp) frameTimestamp;
@property (T{?=qiIq},R,N) lastDetectionTimestamp;
@property (T@"NSDictionary",R,N) metadata;
@property (TQ,R,N,V_identifier) identifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWFusionTrackerObservable identifier];
-[BWFusionTrackerObservable dealloc];
-[BWFusionTrackerObservable metadata];
-[BWFusionTrackerObservable frameTimestamp];
-[BWFusionTrackerObservable confidence];
-[BWFusionTrackerObservable box];
-[BWFusionTrackerObservable initWithKind:box:confidence:timestamp:identifier:metadata:];
-[BWFusionTrackerObservable lastDetectionTimestamp];
-[BWFusionTrackerObservable objectKind];
```
