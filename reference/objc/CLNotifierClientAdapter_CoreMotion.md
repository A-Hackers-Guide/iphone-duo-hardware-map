# `CLNotifierClientAdapter`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CLNotifierServiceClientProtocol`
- 2 instance variables, 5 properties, 7 instance methods, 2 class methods

## Instance variables

```
^{CLNotifierClientBase=^^?} _client;
B _valid;
```

## Properties

```
@property (TB,N,V_valid) valid;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CLNotifierClientAdapter becameFatallyBlocked:index:];
+[CLNotifierClientAdapter performSyncOnSilo:invoker:];
```

## Instance methods

```
-[CLNotifierClientAdapter valid];
-[CLNotifierClientAdapter debugDescription];
-[CLNotifierClientAdapter initWithClient:];
-[CLNotifierClientAdapter init];
-[CLNotifierClientAdapter setValid:];
-[CLNotifierClientAdapter invalidate];
-[CLNotifierClientAdapter onNotification:withData:];
```
