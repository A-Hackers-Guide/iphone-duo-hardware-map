# `PLHealthKitAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 2 instance variables, 2 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"PLXPCListenerOperatorComposition" _queryHandler;
@"PLXPCListenerOperatorComposition" _cloudSyncHandler;
```

## Properties

```
@property (T@"PLXPCListenerOperatorComposition",&,V_queryHandler) queryHandler;
@property (T@"PLXPCListenerOperatorComposition",&,V_cloudSyncHandler) cloudSyncHandler;
```

## Class methods

```
+[PLHealthKitAgent entryEventPointDefinitions];
+[PLHealthKitAgent load];
```

## Instance methods

```
-[PLHealthKitAgent initOperatorDependancies];
-[PLHealthKitAgent queryHandler];
-[PLHealthKitAgent setQueryHandler:];
-[PLHealthKitAgent cloudSyncHandler];
-[PLHealthKitAgent setCloudSyncHandler:];
```
