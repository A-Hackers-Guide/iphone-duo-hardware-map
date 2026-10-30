# `BKSTouchDeliveryBackgroundObserver`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCSecureCoding`
- 3 instance variables, 7 properties, 9 instance methods, 1 class methods

## Instance variables

```
Q _token;
@"NSSet" _contexts;
d _timestamp;
```

## Properties

```
@property (TQ,N,V_token) token;
@property (T@"NSSet",C,N,V_contexts) contexts;
@property (Td,N,V_timestamp) timestamp;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSTouchDeliveryBackgroundObserver supportsBSXPCSecureCoding];
```

## Instance methods

```
-[BKSTouchDeliveryBackgroundObserver setTimestamp:];
-[BKSTouchDeliveryBackgroundObserver timestamp];
-[BKSTouchDeliveryBackgroundObserver contexts];
-[BKSTouchDeliveryBackgroundObserver setContexts:];
-[BKSTouchDeliveryBackgroundObserver description];
-[BKSTouchDeliveryBackgroundObserver token];
-[BKSTouchDeliveryBackgroundObserver encodeWithBSXPCCoder:];
-[BKSTouchDeliveryBackgroundObserver setToken:];
-[BKSTouchDeliveryBackgroundObserver initWithBSXPCCoder:];
```
