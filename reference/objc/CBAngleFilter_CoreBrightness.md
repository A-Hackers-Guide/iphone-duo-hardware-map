# `CBAngleFilter`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBCoexFilter`
- 4 instance variables, 6 properties, 6 instance methods, 0 class methods

## Instance variables

```
f _angleThreshold;
f _currentAngle;
@"<CBALSNodeProtocol>" _alsNode;
@"<CBCoexSource>" _source;
```

## Properties

```
@property (T@"<CBCoexSource>",R,N,V_source) source;
@property (TQ,R,N) coexState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBAngleFilter dealloc];
-[CBAngleFilter handleALSEvent:];
-[CBAngleFilter source];
-[CBAngleFilter coexState];
-[CBAngleFilter handleSourceEvent:];
-[CBAngleFilter initWithALS:andSource:andThreshold:];
```
