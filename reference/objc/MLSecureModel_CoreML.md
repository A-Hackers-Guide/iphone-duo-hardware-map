# `MLSecureModel`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModel`
- Protocols: `MLModeling`, `NSSecureCoding`
- 2 instance variables, 13 properties, 12 instance methods, 5 class methods

## Instance variables

```
@"NSXPCConnection" _connectionToModelSecurityService;
@"NSObject<CoreMLModelSecurityProtocol>" _secureModelProxy;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_connectionToModelSecurityService) connectionToModelSecurityService;
@property (T@"NSObject<CoreMLModelSecurityProtocol>",&,N,V_secureModelProxy) secureModelProxy;
@property (T@"MLModelDescription",R,N) modelDescription;
@property (T@"MLModelConfiguration",R,N) configuration;
@property (TB,R,N) supportsConcurrentSubmissions;
@property (TQ,R,N) predictionTypeForKTrace;
@property (TB,R,N) recordsPredictionEvent;
@property (TQ,R,N) signpostID;
@property (T@"MLModelMetadata",R) metadata;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLSecureModel supportsSecureCoding];
+[MLSecureModel modelWithContentsOfURL:configuration:decryptCredential:error:];
+[MLSecureModel modelWithContentsOfURL:decryptCredential:error:];
+[MLSecureModel sandboxExtensionPathsForModelURL:];
+[MLSecureModel sandboxExtensionTokenForModelURL:];
```

## Instance methods

```
-[MLSecureModel predictionsFromBatch:options:error:];
-[MLSecureModel parameterValueForKey:error:];
-[MLSecureModel predictionFromFeatures:error:];
-[MLSecureModel dealloc];
-[MLSecureModel predictionsFromBatch:error:];
-[MLSecureModel encodeWithCoder:];
-[MLSecureModel initWithCoder:];
-[MLSecureModel predictionFromFeatures:options:error:];
-[MLSecureModel connectionToModelSecurityService];
-[MLSecureModel secureModelProxy];
-[MLSecureModel setConnectionToModelSecurityService:];
-[MLSecureModel setSecureModelProxy:];
```
